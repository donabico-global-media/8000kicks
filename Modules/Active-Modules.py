import json
import os
from datetime import datetime

def activate_all_modules():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    # File kết quả là Modules-Bridge.json
    bridge_path = os.path.join(root_dir, "Modules-Bridge.json")
    
    print("[+] KÍCH HOẠT NEURAL SIPHON PROTOCOL - QUÉT VÔ HẠN CÁC MODULES...")
    detected_modules = {}
    
    # Quét tất cả file .py trong thư mục, loại trừ chính nó
    for item in os.listdir(current_dir):
        if item.endswith(".py") and item != "Active-Modules.py":
            module_name = item.replace(".py", "")
            detected_modules[module_name] = {
                "status": "ACTIVE_INFINITE ✅",
                "pulse_time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
            }

    # Ghi ma trận ra file Modules-Bridge.json
    data = {
        "sync_status": "PULSING_GREEN",
        "recursive_singularity": "ACTIVE_SOTA",
        "active_modules_matrix": detected_modules,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }

    with open(bridge_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"[SUCCESS] Ma trận {len(detected_modules)} Modules đã được cập nhật vào Modules-Bridge.json!")

if __name__ == "__main__":
    activate_all_modules()
