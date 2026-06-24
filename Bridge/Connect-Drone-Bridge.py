import os
import sys
import time
import requests
from datetime import datetime

KHO_4_REPO = "donabico-global-media/KHO-4-DRONE-LANDING-PAGE-CONTROL-CENTER"
KHO_4_DISPATCH_ENDPOINT = f"https://api.github.com/repos/{KHO_4_REPO}/dispatches"
TARGET_MESH_CONTROLLER = "Protocol/Connet Affiliate Drone/Drone_Mesh_Controller.py"
NODE_SOURCE_NAME = "8000kicks"

def establish_mesh_connection():
    print(f"[MESH-BRIDGE] 📡 Đang khởi động cổng kết nối nội bộ...")
    bridge_token = os.getenv("BRIDGE_TOKEN")
    
    if not bridge_token:
        print("[❌ MESH-BRIDGE ERROR] Trống 'BRIDGE_TOKEN'. Khởi động bộ nhớ đệm vệ tinh.")
        return False

    payload = {
        "event_type": "LAUNCH_DRONE_MESH_CONNECT",
        "client_payload": {
            "satellite_node": NODE_SOURCE_NAME,
            "timestamp": datetime.utcnow().isoformat(),
            "telemetry": {"status": "HEALTHY", "bridge_version": "V3000-OMEGA"}
        }
    }

    headers = {
        "Authorization": f"token {bridge_token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    for attempt in range(3):
        try:
            print(f"[📡 TRANSMIT] Đang phát xung tín hiệu về Tổng trạm Kho 4 (Lần thử {attempt + 1})...")
            response = requests.post(KHO_4_DISPATCH_ENDPOINT, json=payload, headers=headers, timeout=15)
            if response.status_code in (200, 204):
                print("✅ [MESH-BRIDGE] THÔNG TUYẾN THÀNH CÔNG TRỰC TIẾP VỚI DRONE MESH CONTROLLER!")
                return True
            else:
                print(f"[⚠️ MESH-BRIDGE] Tổng trạm phản hồi trạng thái: {response.status_code}")
        except Exception as e:
            print(f"[❌ MESH-BRIDGE LỖI] Nghẽn mạch: {e}")
        time.sleep(1)
        
    print("[⚠️ SELF-HEALING] Kích hoạt cơ chế bảo lưu lưu lượng tàng hình cục bộ.")
    return False

if __name__ == "__main__":
    establish_mesh_connection()
    
