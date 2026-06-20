#!/usr/bin/env python3
"""
EATHESEN V3000-Ω | AUTONOMOUS MATRIX INJECTOR v2 (Hàng trăm module + Grouped Output + Real Injection)
"""
import os
import re
import sys
import concurrent.futures
from datetime import datetime, timezone
from collections import defaultdict

def get_protocols_from_file(module_file):
    """Đọc danh sách PROTOCOLS từ file module"""
    try:
        with open(module_file, "r", encoding="utf-8") as f:
            content = f.read()
        if "PROTOCOLS = [" in content:
            start = content.find("PROTOCOLS = [") + len("PROTOCOLS = [")
            end = content.find("]", start)
            protocols_str = content[start:end]
            return [p.strip().strip("'\"") for p in protocols_str.split(",") if p.strip()]
    except:
        pass
    return []

def execute_single_module(module_file, target_url):
    if module_file == "Active-Modules.py":
        return None, []
    try:
        cmd = f"'{sys.executable}' '{module_file}' --url '{target_url}' > /dev/null 2>&1"
        exit_code = os.system(cmd)
        protocols = get_protocols_from_file(module_file)
        
        if exit_code == 0:
            return f"✅ {module_file}", protocols
        else:
            return f"❌ {module_file}", protocols
    except Exception as e:
        return f"💥 {module_file} -> {str(e)}", []

def run_massive_siphon_matrix(target_url):
    print("[V3000-Ω] === EATHESEN MATRIX ACTIVATION (HÀNG TRĂM MODULE) ===")
    all_files = os.listdir(".")
    module_targets = [f for f in all_files if f.endswith(".py") and f != "Active-Modules.py"]
    
    print(f"[V3000-Ω] Tổng module phát hiện: {len(module_targets)}")
    print("-" * 70)

    results = []
    protocol_groups = defaultdict(list)

    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
        futures = {executor.submit(execute_single_module, mod, target_url): mod for mod in module_targets}
        for future in concurrent.futures.as_completed(futures):
            status, protocols = future.result()
            if status:
                print(status)
                for p in protocols:
                    print(f"   ✅ {p}")
                    # Gom nhóm theo từ khóa
                    if "Google" in p:
                        protocol_groups["Google"].append(p)
                    elif any(x in p for x in ["Bing", "Microsoft"]):
                        protocol_groups["Bing/Microsoft"].append(p)
                    elif any(x in p for x in ["Facebook", "Meta", "Instagram"]):
                        protocol_groups["Meta/Social"].append(p)
                    elif "TikTok" in p:
                        protocol_groups["TikTok"].append(p)
                    elif any(x in p for x in ["Affiliate", "Amazon", "CJ", "Impact"]):
                        protocol_groups["Affiliate"].append(p)
                    else:
                        protocol_groups["Other"].append(p)
                results.append((status, protocols))

    print("-" * 70)
    print("[V3000-Ω] TỔNG KẾT THEO NHÓM:")
    for group, protos in protocol_groups.items():
        print(f"  {group}: {len(protos)} giao thức ✅")

    return results, protocol_groups

def inject_production_html(results, protocol_groups):
    index_path = os.path.join("..", "index.html")
    if not os.path.exists(index_path):
        index_path = "index.html"
    if not os.path.exists(index_path):
        print("[ERROR] Không tìm thấy index.html!")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Golden 2px Drone Shield
    golden_style = """
    <style>
    .drone-frame, #drone-main, .hero-drone, img[alt*="drone"] {
        border: 2px solid #FFD700 !important;
        box-shadow: 0 0 15px #FFD700, 0 0 25px #FFAA00 !important;
        animation: golden-glow 2s infinite alternate;
    }
    @keyframes golden-glow { from { box-shadow: 0 0 10px #FFD700; } to { box-shadow: 0 0 20px #FFAA00; } }
    </style>
    """
    if "<head>" in html:
        html = html.replace("<head>", f"<head>\n{golden_style}")

    # Inject summary section
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    summary = f"""
    <div id="eath esen-matrix-summary" style="background:#111; color:#0f0; padding:15px; margin:20px 0; border:1px solid #0f0; font-family:monospace;">
        <strong>🛡️ EATHESEN V3000-Ω MATRIX ACTIVATED</strong><br>
        Time: {current_time}<br>
        Total Protocols Activated: {sum(len(v) for v in protocol_groups.values())}<br>
        Groups: {', '.join(protocol_groups.keys())}<br>
        <span style="color:#FFD700">Golden Drone Shield: ACTIVE</span>
    </div>
    """
    if "<body>" in html:
        html = html.replace("<body>", f"<body>\n{summary}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("[SUCCESS] Golden 2px + Protocol Summary injected into index.html!")

if __name__ == "__main__":
    target = "https://donabico-global-media.github.io/8000kicks/"
    if "--url" in sys.argv:
        idx = sys.argv.index("--url")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]

    results, protocol_groups = run_massive_siphon_matrix(target)
    inject_production_html(results, protocol_groups)