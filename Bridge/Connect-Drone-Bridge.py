import os
import sys
import subprocess

# Đường dẫn chính xác tới tệp Core
LOCAL_CORE_PATH = "Super Core Affiliate/Super-Core-Affiliate.py"

def run_local_core():
    print("[INTERNAL-BRIDGE] Đang kích hoạt Core 8000kicks...")
    if not os.path.exists(LOCAL_CORE_PATH):
        print(f"[❌ ERROR] Không thấy tệp: {LOCAL_CORE_PATH}")
        return
    subprocess.run([sys.executable, LOCAL_CORE_PATH], check=True)
    print("[✅ SUCCESS] Core nội bộ vận hành hoàn tất.")

if __name__ == "__main__":
    run_local_core()
    
