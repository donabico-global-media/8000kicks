import json
import os
from datetime import datetime

def generate_sota_bridge():
    # Cấu trúc phẳng tĩnh 100% khớp với logic hệ thống của Admin
    bridge_data = {
        "sync_status": "PULSING_RED",
        "recursive_singularity": "ACTIVE_SOTA",
        "core_constant": 0.24,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }
    
    # Ép ghi trực tiếp vào thư mục "Super Core Affiliate" để không bị lạc file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_filename = os.path.join(current_dir, "system_bridge.json")
    
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(bridge_data, f, indent=4, ensure_ascii=False)
        
    print(f"[EATHESEN V3000-Ω] Cầu nối dữ liệu đã được đồng bộ thành công tại: {bridge_data['timestamp']}")
    print(f"[STATUS] Trạng thái nạp: {bridge_data['sync_status']} -> Sẵn sàng kích hoạt hiệu ứng Pulse.")

if __name__ == "__main__":
    generate_sota_bridge()
