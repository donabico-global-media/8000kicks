#!/usr/bin/env python3
"""Bing-Siphon.py (GitHub Optimized v4 - Flawless Green Mode)"""

import argparse
import concurrent.futures
import random
import time
import urllib.request
import urllib.error
from typing import Dict

MICROSOFT_BOTS = [
    {"name": "BingBot_Standard", "ua": "Mozilla/5.0 (compatible; bingbot/2.0)"},
    {"name": "BingPreview_Mobile", "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 BingPreview/1.0b"},
    {"name": "MSN_AdBot", "ua": "MSNBot-Media/1.1"},
]

def get_headers(bot: Dict) -> Dict:
    return {"User-Agent": bot["ua"], "Accept": "text/html,application/xhtml+xml"}

def siphon_with_retry(target_url: str, bot: Dict, max_retries: int = 3) -> Dict:
    result = {"bot": bot["name"], "status": None, "error": None}
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(target_url, headers=get_headers(bot))
            with urllib.request.urlopen(req, timeout=25) as resp:
                result["status"] = resp.status
                return result
        except urllib.error.HTTPError as e:
            result["status"] = e.code
            if e.code in (404, 403): break
            time.sleep(random.uniform(2, 4) * attempt)
        except Exception as e:
            result["error"] = str(e)[:80]
            if attempt < max_retries: time.sleep(random.uniform(2, 4) * attempt)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True)
    args = parser.parse_args()

    print(f"[V3000-Ω] Bing-Siphon | Target: {args.url}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(siphon_with_retry, args.url, bot): bot for bot in MICROSOFT_BOTS}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            icon = "✅" if res["status"] == 200 else "❌"
            print(f"  {icon} [{res['bot']}] status={res['status']}")
            time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    main()
