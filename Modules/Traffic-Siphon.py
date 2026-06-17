import argparse
import json
import urllib.request
import os
from datetime import datetime, timezone

def main():
    # File luôn nằm cố định trong Modules
    report_path = os.path.join("Modules", "traffic_report.json")
    
    # URL đích
    target_url = "https://donabico-global-media.github.io/8000kicks/"
    
    # Đọc dữ liệu cũ
    history = []
    if os.path.exists(report_path):
        with open(report_path, "r") as f:
            try: history = json.load(f)
            except: history = []

    # Kiểm tra
    try:
        with urllib.request.urlopen(target_url, timeout=10) as response:
            status = response.status
    except Exception as e:
        status = 500

    # Ghi log mới
    history.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "url": target_url,
        "status": status
    })
    
    with open(report_path, "w") as f:
        json.dump(history, f, indent=4)

if __name__ == "__main__":
    main()
    
