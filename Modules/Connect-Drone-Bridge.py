import requests
import time
import sys
import os
from datetime import datetime

# Config
CONTROL_CENTER_REPO = "donabico-global-media/KHO-4-DRONE-LANDING-PAGE-CONTROL-CENTER"
DRONE_CORE_ENDPOINT = "https://api.github.com/repos/" + CONTROL_CENTER_REPO + "/dispatches"
TARGET_URL = "https://donabico-global-media.github.io/8000kicks/"
MAX_RETRIES = 5
BACKOFF_FACTOR = 2

def send_heartbeat(status="alive", details=None):
    """Gửi heartbeat về Engine Drone Core"""
    payload = {
        "event_type": "DRONE_BRIDGE_HEARTBEAT",
        "client_payload": {
            "repo": "8000kicks",
            "status": status,
            "timestamp": datetime.utcnow().isoformat(),
            "target_url": TARGET_URL,
            "modules_active": [f for f in os.listdir("Modules") if f.endswith(".py")],
            "details": details or {}
        }
    }
    
    for attempt in range(MAX_RETRIES):
        try:
            # Thay YOUR_TEMP_TOKEN bằng token thực tế từ payload hoặc secret
            headers = {
                "Authorization": "token YOUR_GITHUB_PAT_OR_TEMP_TOKEN",
                "Accept": "application/vnd.github.v3+json",
                "Content-Type": "application/json"
            }
            response = requests.post(DRONE_CORE_ENDPOINT, json=payload, headers=headers, timeout=15)
            if response.status_code in (200, 204):
                print(f"[BRIDGE] Heartbeat sent successfully at {datetime.utcnow()}")
                return True
        except Exception as e:
            print(f"[BRIDGE] Attempt {attempt+1} failed: {e}")
        
        time.sleep(BACKOFF_FACTOR ** attempt)
    
    print("[BRIDGE] All heartbeat attempts failed")
    return False

def ensure_connection():
    """Đảm bảo kết nối thông tuyến 24/7"""
    print(f"[DRONE-BRIDGE] Starting connection check at {datetime.utcnow()}")
    
    # Kiểm tra các module siphon khác
    for module in ["Google_Siphon.py", "Bing_Siphon.py", "AI_Cache_Siphon.py"]:
        if os.path.exists(f"Modules/{module}"):
            print(f"[BRIDGE] Detected active module: {module}")
    
    # Gửi heartbeat
    success = send_heartbeat("connected", {"bridge_version": "V3000-Ω-Bridge-001"})
    
    if success:
        print("[DRONE-BRIDGE] ✅ Thông tuyến ổn định với Engine Drone Core")
    else:
        print("[DRONE-BRIDGE] ⚠️ Kết nối gián đoạn - sẽ retry ở cycle sau")

if __name__ == "__main__":
    ensure_connection()
    # Chạy liên tục nếu muốn (nhưng workflow sẽ gọi từng lần)
    # while True: ensure_connection(); time.sleep(300)  # 5 phút/lần
