import urllib.request
import urllib.parse
import sys
import time

def blast_google_infrastructure(target_url):
    search_ping = f"https://www.google.com/ping?sitemap={urllib.parse.quote(target_url)}"
    try:
        req = urllib.request.Request(search_ping, headers={'User-Agent': 'DONABICO-ENGINE-V5000'})
        with urllib.request.urlopen(req, timeout=15) as response:
            pass
    except Exception:
        pass

    time.sleep(2)

    google_display_bots = {
        "Google_Mediapartners_AdSense": "Mediapartners-Google",
        "Google_AdsBot_LandingPage": "AdsBot-Google (+http://www.google.com/adsbot.html)",
        "Google_AdsBot_Mobile": "AdsBot-Google-Mobile",
        "Google_AdSense_Explicit": "Google-Adwords-Instant (+http://www.google.com/adsbot.html)"
    }
    
    for bot_name, user_agent in google_display_bots.items():
        try:
            req = urllib.request.Request(target_url, headers={'User-Agent': user_agent, 'X-Siphon-Source': 'DONABICO-GLOBAL-MEDIA'})
            with urllib.request.urlopen(req, timeout=15) as response:
                print(f"[GOOGLE DISPLAY] Node {bot_name} - Ingestion Status: {response.status}")
        except Exception:
            pass
        time.sleep(1.5)

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://donabico-global-media.github.io/8000kicks/"
    blast_google_infrastructure(url)
  
