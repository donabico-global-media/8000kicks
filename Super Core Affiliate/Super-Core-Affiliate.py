import json
import os

def super_intelligent_core():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    m_bridge = os.path.join(root_dir, "Modules-Bridge.json")
    p_bridge = os.path.join(root_dir, "Protocols-Bridge.json")
    
    print("[CORE] ĐANG CHẠY MODE: SUPER_SMART_INTELLIGENT ✅")
    
    # Đọc ma trận Modules
    with open(m_bridge, "r") as f: m_data = json.load(f)
    # Đọc ma trận Protocols
    with open(p_bridge, "r") as f: p_data = json.load(f)
    
    # Logic điều phối chéo giữa Modules & Protocols
    print(f"[CORE] Sync Modules: {len(m_data['active_modules_matrix'])} | Sync Protocols: {len(p_data['active_protocols_matrix'])}")
    
    # Thực thi lệnh điều phối dựa trên trạng thái đồng bộ
    if m_data['sync_status'] == "PULSING_GREEN" and p_data['sync_status'] == "PULSING_GREEN":
        print("[CORE] Hệ thống ổn định. Bắt đầu tối ưu hóa Siphon Traffic...")
    
if __name__ == "__main__":
    super_intelligent_core()
