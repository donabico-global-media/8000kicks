#!/usr/bin/env python3
"""
EATHESEN V3000-Ω | AUTONOMOUS MATRIX INJECTOR + GOLDEN 2PX DRONE SHIELD
Tự động quét hàng ngàn modules, hiển thị danh sách + tích xanh, tiêm viền vàng 2px khi kích hoạt thành công.
"""
import os
import re
import sys
import concurrent.futures
from datetime import datetime, timezone

def execute_single_module(module_file, target_url):
    if module_file == "Active-Modules.py":
        return None
    try:
        cmd = f"'{sys.executable}' '{module_file}' --url '{target_url}' > /dev/null 2>&1"
        exit_code = os.system(cmd)
        if exit_code == 0:
            return f"✅ {module_file} -> Success"
        else:
            return f"❌ {module_file} -> Failed (Code {exit_code})"
    except Exception as e:
        return f"💥 {module_file} -> Error: {str(e)}"

def run_massive_siphon_matrix(target_url):
    print("[V3000-Ω] === DANH SÁCH MODULE ĐANG HOẠT ĐỘNG ===")
    all_files = os.listdir(".")
    module_targets = [f for f in all_files if f.endswith(".py") and f != "Active-Modules.py"]
    
    print(f"[V3000-Ω] Tổng module tìm thấy: {len(module_targets)}")
    print("Danh sách module:")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(execute_single_module, mod, target_url): mod for mod in module_targets}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                print(res)          # In rõ ràng từng dòng ✅ / ❌
                results.append(res)
    
    print("[V3000-Ω] Hoàn thành quét ma trận. Tổng module thành công:", len([r for r in results if "Success" in r]))

def inject_production_html():
    index_path = os.path.join("..", "index.html")
    if not os.path.exists(index_path):
        index_path = "index.html"
    if not os.path.exists(index_path):
        print("[ERROR] Không tìm thấy index.html!")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # === VIỀN VÀNG 2PX (Golden Drone Shield) ===
    golden_style = """
    <style>
    .drone-frame, #drone-main, .hero-drone, img[alt*="drone"], .drone-container {
        border: 2px solid #FFD700 !important;
        box-shadow: 0 0 15px #FFD700, 0 0 25px #FFAA00 !important;
        animation: golden-glow 2s infinite alternate;
    }
    @keyframes golden-glow { 
        from { box-shadow: 0 0 10px #FFD700; } 
        to { box-shadow: 0 0 20px #FFAA00; } 
    }
    </style>
    """
    if "<head>" in html:
        html = html.replace("<head>", f"<head>\n{golden_style}")

    # Banner thông báo + Affiliate
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    status_banner = f'<div id="dnbc-adtech-banner" style="background: linear-gradient(90deg, #FFD700, #FFAA00); color: #000; text-align: center; font-weight: bold; padding: 8px;">🛡️ EATHESEN V3000-Ω MATRIX + GOLDEN DRONE SHIELD ACTIVE AT {current_time}</div>'
    if "<body>" in html:
        html = html.replace("<body>", f"<body>\n    {status_banner}")

    # Affiliate mapping
    target_aff = "https://donabico-global-media.github.io/shop/8000kicks.html"
    html = re.sub(r'href="[^"]*placeholder[^"]*"', f'href="{target_aff}"', html)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("[SUCCESS] Golden 2px Drone Shield + Matrix Injection completed!")

if __name__ == "__main__":
    target = "https://donabico-global-media.github.io/8000kicks/"
    if "--url" in sys.argv:
        idx = sys.argv.index("--url")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]

    run_massive_siphon_matrix(target)
    inject_production_html()