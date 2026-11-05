"""Ftriyana AI Client — DeepSeek primary, Gemini fallback."""
import json
from pathlib import Path
import requests

CONFIG = Path(__file__).parent.parent / "config" / "ai_config.json"


def load_config():
    if CONFIG.exists():
        return json.load(open(CONFIG))
    return {"gemini": {"enabled": False}, "deepseek": {"enabled": False}, "primary": "deepseek"}


def _call_gemini(prompt, cfg):
    key = cfg["gemini"].get("api_key", "")
    if not key:
        return None, "Gemini key missing"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{cfg['gemini'].get('model','gemini-1.5-flash')}:generateContent?key={key}"
    try:
        r = requests.post(url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=60)
        if r.status_code == 200:
            return r.json()["candidates"][0]["content"]["parts"][0]["text"], None
        return None, f"Gemini HTTP {r.status_code}"
    except Exception as e:
        return None, f"Gemini: {e}"


def _call_deepseek(prompt, cfg):
    key = cfg["deepseek"].get("api_key", "")
    if not key:
        return None, "DeepSeek key missing"
    url = f"{cfg['deepseek'].get('base_url','https://api.deepseek.com')}/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    body = {"model": cfg["deepseek"].get("model", "deepseek-chat"),
            "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
    try:
        r = requests.post(url, headers=headers, json=body, timeout=60)
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"], None
        return None, f"DeepSeek HTTP {r.status_code}: {r.text[:200]}"
    except Exception as e:
        return None, f"DeepSeek: {e}"


def ask(prompt):
    cfg = load_config()
    primary = cfg.get("primary", "deepseek")
    if primary == "deepseek" and cfg["deepseek"].get("enabled"):
        r, e = _call_deepseek(prompt, cfg)
        if r: return r, "deepseek"
        if cfg["gemini"].get("enabled"):
            r2, e2 = _call_gemini(prompt, cfg)
            if r2: return r2, "gemini (fallback)"
            return f"[AI Error] DeepSeek: {e} | Gemini: {e2}", "none"
        return f"[AI Error] DeepSeek: {e}", "none"
    if cfg["gemini"].get("enabled"):
        r, e = _call_gemini(prompt, cfg)
        if r: return r, "gemini"
        if cfg["deepseek"].get("enabled"):
            r2, e2 = _call_deepseek(prompt, cfg)
            if r2: return r2, "deepseek (fallback)"
            return f"[AI Error] Gemini: {e} | DeepSeek: {e2}", "none"
        return f"[AI Error] Gemini: {e}", "none"
    return "[AI Disabled] Add API keys in config/ai_config.json (see README)", "none"
