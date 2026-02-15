#!/usr/bin/env python3
import re
import html
from urllib.request import Request, urlopen

def fetch_title(url, timeout=6):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; CSOH-bot/1.0)'} )
        with urlopen(req, timeout=timeout) as r:
            # read a reasonable chunk
            raw = r.read(131072)
            try:
                text = raw.decode('utf-8', errors='replace')
            except Exception:
                text = raw.decode('latin-1', errors='replace')
            print(f"First 1000 chars of response:")
            print(text[:1000])
            print("\n" + "="*50 + "\n")
            m = re.search(r'<title[^>]*>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
            if m:
                t = html.unescape(m.group(1)).strip()
                # collapse whitespace
                t = re.sub(r'\s+', ' ', t)
                print(f"Extracted title: {t}")
                return t
            else:
                print("No title tag found")
    except Exception as e:
        print(f"Error: {e}")
        return None
    return None

# Test with first URL
url = "https://www.theregister.com/2017/09/19/viacom_exposure_in_aws3_bucket_blunder/"
print(f"Fetching: {url}\n")
title = fetch_title(url)
print(f"\nFinal title: {title}")
