import os
import sys
import subprocess

# Đường dẫn bộ Core mới tại Kho 8000kicks
LOCAL_CORE_PATH = "Super-Core-Affiliate/Super-Core-Affiliate.py"

def run_local_core():
    print(f"[INTERNAL-BRIDGE] 📡 Đang khởi động Core nội tại tại 8000kicks...")
    
    # Kiểm tra sự tồn tại của bộ Core
    if not os.path.exists(LOCAL_CORE_PATH):
        print(f"[❌ ERROR] Không tìm thấy bộ Core tại: {LOCAL_CORE_PATH}")
        return False
    
    try:
        # Gọi trực tiếp bộ Core nội bộ, không dùng API ngoại vi
        print(f"[🚀 EXECUTE] Kích hoạt tiến trình: {LOCAL_CORE_PATH}")
        subprocess.run([sys.executable, LOCAL_CORE_PATH], check=True)
        print("[✅ SUCCESS] Bộ Core 8000kicks đã hoàn tất nhiệm vụ.")
        return True
    except Exception as e:
        print(f"[❌ CRITICAL ERROR] Lỗi khi chạy Core nội bộ: {e}")
        return False

if __name__ == "__main__":
    run_local_core()
    
