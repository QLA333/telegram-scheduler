import os
import time
import urllib.parse
import urllib.request
import json

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_IDS = os.environ.get("TELEGRAM_CHAT_IDS", "")
MESSAGE = os.environ.get("TELEGRAM_MESSAGE", "Xin chào! Đây là tin nhắn tự động.")
PARSE_MODE = os.environ.get("TELEGRAM_PARSE_MODE", "HTML")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    if PARSE_MODE:
        data["parse_mode"] = PARSE_MODE
    data_encoded = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=data_encoded)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode())
            return res
    except Exception as e:
        print(f"Error sending to {chat_id}: {e}")
        return None

def main():
    if not BOT_TOKEN:
        print("Missing TELEGRAM_BOT_TOKEN")
        return
    if not CHAT_IDS:
        print("Missing TELEGRAM_CHAT_IDS")
        return
    ids = [c.strip() for c in CHAT_IDS.split(",") if c.strip()]
    for cid in ids:
        print("Sending to", cid)
        res = send_message(cid, MESSAGE)
        print("Result:", res)
        time.sleep(0.3)
    print("Done.")

if __name__ == "__main__":
    main()
