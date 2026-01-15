import feedparser
import urllib.parse
from datetime import datetime

# --- TACTICAL CONFIGURATION ---
# These are the "Permanent Watchlist" items the Army always needs to monitor
CORE_TARGETS = [
    "Indian Army LAC Ladakh",
    "Line of Control (LoC) ceasefire",
    "DRDO missile test 2026",
    "Indian Navy submarine project",
    "Agniveer recruitment 2026"
]

def run_24h_recon():
    """
    Executes a global search for the CORE_TARGETS limited to the last 24 hours.
    This mimics a 'Morning Briefing' collection.
    """
    dtg = datetime.now().strftime('%d%H%M %b %y').upper()
    print(f"[*] INITIALIZING RECONNAISSANCE | DTG: {dtg}L")
    print("-" * 50)

    for target in CORE_TARGETS:
        # 'when:1d' ensures we never fetch 'yesterday's war'
        search_query = f"{target} when:1d"
        encoded = urllib.parse.quote(search_query)
        url = f"https://news.google.com/rss/search?q={encoded}&hl=en-IN&gl=IN&ceid=IN:en"
        
        feed = feedparser.parse(url)
        
        print(f"\n[+] SECTOR: {target.upper()}")
        
        if not feed.entries:
            print("    [!] NO NEW ACTIVITY DETECTED IN LAST 24H.")
        else:
            # Displaying the top 3 critical units for the terminal log
            for entry in feed.entries[:3]:
                # Priority Logic
                is_flash = any(word in entry.title.lower() for word in ["clash", "strike", "failed", "missile", "alert"])
                status = "🚨 FLASH" if is_flash else "📡 ROUTINE"
                
                print(f"    [{status}] {entry.title}")
                print(f"    LINK: {entry.link}\n")

if __name__ == "__main__":
    try:
        run_24h_recon()
        print("-" * 50)
        print("[*] RECONNAISSANCE COMPLETE. SYSTEM IDLE.")
    except Exception as e:
        print(f"[!] SYSTEM CRITICAL ERROR: {e}")