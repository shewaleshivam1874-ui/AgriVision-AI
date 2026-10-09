# Lightweight Gemini key validator — non-destructive and generic
import os
import sys
import json
import traceback

def load_key():
    if len(sys.argv) > 1:
        return sys.argv[1].strip()
    env = os.environ.get("GEMINI_API_KEY")
    if env:
        return env.strip()
    # fallback to .env file in repo root
    try:
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("GEMINI_API_KEY="):
                    return line.split("=",1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return None

def attempt_sdk_check(key):
    # Try using the installed GenAI SDK in a tolerant way
    try:
        import google.genai as genai
    except Exception:
        try:
            import google_genai as genai  # alternative import name (defensive)
        except Exception:
            return False, "SDK not importable"

    try:
        # prefer a very small, safe request; adapt to whichever helper exists
        client = None
        if hasattr(genai, "Client"):
            client = genai.Client(api_key=key) if "api_key" in genai.Client.__init__.__code__.co_varnames else genai.Client()
            if hasattr(client, "responses") and getattr(client, "responses"):
                r = client.responses.create(model="gemini-3.8-flash", input="Please respond with the single word OK")
                text = str(r)
                ok = "OK" in text or "ok" in text
                return ok, ("response" if ok else f"unexpected: {text[:200]}")
        # fallback: try models.generate_content if available
        if hasattr(genai, "models") and hasattr(genai.models, "generate_content"):
            res = genai.models.generate_content(model="gemini-3.8-flash", contents=["OK?"])
            text = json.dumps(res, default=str)
            return True, f"got {len(text)} bytes"
    except Exception as exc:
        return False, f"SDK call failed: {exc.__class__.__name__}: {str(exc)[:200]}"
    return False, "No supported client-method found"

def main():
    key = load_key()
    if not key:
        print("No GEMINI_API_KEY provided (env, .env, or arg).")
        sys.exit(2)
    ok, info = attempt_sdk_check(key)
    if ok:
        print("OK: key appears valid —", info)
        sys.exit(0)
    else:
        print("INVALID:", info)
        sys.exit(3)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(4)