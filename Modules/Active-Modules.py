import json
import os
from datetime import datetime

def activate_all_modules():
    # 1. Định vị các đường dẫn cốt lõi
    current_dir = os.path.dirname(os.path.abspath(__file__)) # Thư mục Modules/
    root_dir = os.path.dirname(current_dir)                 # Thư mục gốc dự án
    
    # Đường dẫn đến file bridge tổng của toàn bộ ma trận hệ thống
    core_bridge_path = os.path.join(root_dir, "Super Core Affiliate", "system_bridge.json")
    
    # 2. Quét vô hạn/tự động cấu trúc thư mục con bên trong Modules/
    detected_modules = {}
    print("[+] KÍCH HOẠT NEURAL SIPHON PROTOCOL - QUÉT MODULES...")
    
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        # Nếu là thư mục con (ví dụ: Modules/Anti_Bot, Modules/SEO_Siphon...)
        if os.path.isdir(item_path) and not item.startswith(".") and not item.startswith("__"):
            
            # Cấu hình mặc định cho mỗi Module tìm thấy
            module_config = {
                "status": "ACTIVE_SOTA",
                "mode": "HYPER_INTELLIGENCE_2026",
                "last_pulse": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
            }
            
            # Nếu bên trong Module con có file config riêng (json), nạp bổ sung vào hệ thống
            config_file = os.path.join(item_path, "config.json")
            if os.path.exists(config_file):
                try:
                    with open(config_file, "r", encoding="utf-8") as f:
                        custom_data = json.load(f)
                        module_config.update(custom_data)
                except Exception:
                    pass
                    
            detected_modules[item] = module_config
            print(f" |-- [ONLINE] Module: {item} -> Đã đồng bộ luồng tín hiệu.")

    # 3. Nạp và chuyển tải dữ liệu trực tiếp sang cho Super Core
    base_bridge_data = {}
    if os.path.exists(core_bridge_path):
        try:
            with open(core_bridge_path, "r", encoding="utf-8") as f:
                base_bridge_data = json.load(f)
        except Exception:
            pass

    # Hợp nhất (Merge) danh sách Module hoạt động vào lõi dữ liệu của Super Core
    base_bridge_data["active_modules_matrix"] = detected_modules
    base_bridge_data["modules_sync_timestamp"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Lưu lại file system_bridge.json tạm thời để Workflow trung chuyển ra ngoài
    os.makedirs(os.path.dirname(core_bridge_path), exist_ok=True)
    with open(core_bridge_path, "w", encoding="utf-8") as f:
        json.dump(base_bridge_data, f, indent=4, ensure_ascii=False)
        
    print(f"[SUCCESS] Đã đồng bộ tín hiệu vô hạn của {len(detected_modules)} Modules về Super Core Affiliate.")

if __name__ == "__main__":
    activate_all_modules()
    
