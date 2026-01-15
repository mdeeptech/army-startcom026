import streamlit as st
import feedparser
import urllib.parse
from datetime import datetime

# --- SYSTEM CONFIGURATION ---
st.set_page_config(page_title="STRATCOM TACTICAL NODE", layout="wide")

# 1. LIVE MILITARY CLOCK (DTG)
# Updates every time the page refreshes
now = datetime.now()
dtg = now.strftime('%d%H%M %b %y').upper()

# --- CSS: ARMY TACTICAL THEME ---
st.markdown("""
    <style>
    .stApp { background-color: #05070a; color: #00ff41; font-family: 'Courier New', monospace; }
    .intel-unit { 
        border: 1px solid #1f2937; border-left: 8px solid #00ff41; 
        padding: 20px; margin-bottom: 15px; background: #0d1117;
        border-radius: 4px;
    }
    .flash-alert { border-left-color: #ff3131 !important; background: #1a0a0a !important; }
    .priority-label { font-weight: bold; font-size: 0.9em; margin-bottom: 5px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🛡️ STRATCOM : INDIA OSINT NODE")
    st.write(f"**STATUS:** OPERATIONAL | **SENSORS:** LIVE | **WINDOW:** ROLLING 24H")
with col2:
    st.metric("SYSTEM DTG", f"{dtg}L")

st.divider()

# --- REFLEXIVE SEARCH (THE TARGETING VECTOR) ---
# This is the "reflex" - the user inputs a target, and the system hunts.
target_vector = st.text_input("🎯 ENTER SECTOR / UNIT / ASSET (e.g., LAC, S-400, Ladakh, DRDO)", placeholder="AWAITING TARGET SELECTION...")

if target_vector:
    # 2. TEMPORAL LOGIC: "when:1d" forces the search to only show the last 24 hours.
    # If tomorrow is the 14th, this will show the 14th's news.
    search_query = f"{target_vector} defense india when:1d"
    encoded = urllib.parse.quote(search_query)
    url = f"https://news.google.com/rss/search?q={encoded}&hl=en-IN&gl=IN&ceid=IN:en"
    
    with st.spinner(f"RE-TASKING SENSORS TO {target_vector.upper()}..."):
        feed = feedparser.parse(url)
    
    if not feed.entries:
        st.warning(f"NO NEW INTEL RECORDED FOR '{target_vector.upper()}' IN THE LAST 24-HOUR CYCLE.")
    else:
        st.subheader(f"📍 INTSUM (Intelligence Summary): {target_vector.upper()}")
        
        # 3. ARMY STYLE PRESENTATION
        for entry in feed.entries[:12]:
            # Automated Triage: Detect "FLASH" alerts
            is_flash = any(word in entry.title.lower() for word in ["clash", "strike", "missile", "border", "alert", "attack"])
            alert_class = "flash-alert" if is_flash else ""
            priority = "🚨 FLASH" if is_flash else "📡 ROUTINE"
            color = "#ff3131" if is_flash else "#00ff41"

            # Render the Intel Unit (No permanent storage, just UI display)
            st.markdown(f"""
                <div class="intel-unit {alert_class}">
                    <span class="priority-label" style="color: {color};">{priority}</span>
                    <h3 style="margin: 5px 0; color: #ffffff;">{entry.title}</h3>
                    <div style="font-size: 0.8em; color: #8b949e;">
                        SOURCE: {entry.source.get('title', 'EXTERNAL')} | 
                        PUBLISHED: {entry.published}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"OPEN INTEL SOURCE", entry.link)
else:
    st.info("SYSTEM READY. ENTER A TARGET VECTOR TO INITIALIZE SCAN.")