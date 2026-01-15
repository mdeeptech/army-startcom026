@echo off
echo Starting Army Monitor...
echo.
python monitor.py
echo.
echo ========================================
echo Monitor finished. Check army_updates.csv
echo ========================================
pause
```

---

## 📁 File 5: `README.txt`
```
╔════════════════════════════════════════════════════════════╗
║     ARMY AWARENESS WEB MONITORING TOOL (OSINT)            ║
║     Legal RSS Feed Monitor for Defence Updates            ║
╚════════════════════════════════════════════════════════════╝

📋 QUICK START (3 Steps)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Double-click: setup.bat  (installs requirements)
2. Double-click: run.bat    (runs the monitor)
3. Open: army_updates.csv   (see results)

Done! That's it!


📂 FILES IN THIS FOLDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
monitor.py         → Main Python script
config.json        → Settings (feeds, keywords)
setup.bat          → One-time setup (installs Python packages)
run.bat            → Run the monitor (double-click this)
army_updates.csv   → Results saved here (auto-created)
README.txt         → This file


⚙️ WHAT IT DOES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Monitors official government RSS feeds
✓ Filters defence/security news using keywords
✓ Saves results with timestamp to CSV
✓ Shows updates in terminal
✓ 100% legal (uses public RSS feeds only)


🔧 CUSTOMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Edit config.json to:
  • Add more RSS feeds
  • Change keywords
  • Adjust timeout
  • Change output filename


📅 SCHEDULE DAILY RUNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Windows Task Scheduler:
1. Open "Task Scheduler" (search in Start)
2. Create Basic Task → Name it "Army Monitor"
3. Trigger: Daily at 8:00 AM
4. Action: Start a program
   Program: C:\army_monitor\run.bat
5. Done!


❌ COMMON PROBLEMS & FIXES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Problem: "Python not recognized"
Fix: Install Python from python.org
     ✓ Check "Add Python to PATH" during install

Problem: "Module not found"
Fix: Run setup.bat again

Problem: "Connection error"
Fix: Check internet connection
     Check firewall settings

Problem: "Permission denied" when saving CSV
Fix: Close Excel if army_updates.csv is open

Problem: "No results found"
Fix: This is normal if no defence news today
     Try editing keywords in config.json


🌐 DATA SOURCES (RSS Feeds)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ PIB Defence (Press Information Bureau)
✓ Ministry of External Affairs (MEA)
✓ The Hindu (National News)

All sources are official and legal to monitor.


⚖️ LEGAL & ETHICAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Uses official RSS feeds (public data)
✓ No web scraping
✓ No authentication bypass
✓ Respects rate limits
✓ Legal for personal/professional use

Do NOT:
✗ Share classified information
✗ Use for commercial purposes without permission
✗ Overwhelm servers with requests


📧 SUPPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For help, check:
- Python docs: docs.python.org
- RSS feeds: pib.gov.in (RSS section)


═══════════════════════════════════════════════════════════
Version 1.0 | Python 3.x Required | Windows Compatible
═══════════════════════════════════════════════════════════
```

---

## 📊 COMPLETE FOLDER STRUCTURE
```
C:\army_monitor\
│
├── 📄 monitor.py          (Main Python script)
├── 📄 config.json         (Configuration file)
├── 📄 setup.bat           (One-time setup)
├── 📄 run.bat             (Quick run script)
├── 📄 README.txt          (Instructions)
└── 📄 army_updates.csv    (Auto-created output)