#!/usr/bin/env python3
"""
EATHESEN V3000-Ω | 8000KICKS LIVE FACTORY INJECTOR
Chức năng: Kích hoạt ma trận Siphon và TIÊM TRỰC TIẾP 100% vào Landing Page 8000Kicks
"""
import os
import re
from datetime import datetime, timezone

def run_all_siphons():
    print("[V3000-8000KICKS] Khởi chạy chuỗi module quan trắc ngầm...")
    os.system("python3 Traffic-Siphon.py")
    os.system("python3 Affiliate-Network-Siphon.py")
    os.system("python3 SEO-Shield-Siphon.py")
    os.system("python3 Social-Preview-Siphon.py")
    os.system("python3 Google-Siphon.py")
    os.system("python3 Bing-Siphon.py")

def inject_production_html():
    index_path = os.path.join("..", "index.html")
    if not os.path.exists(index_path):
        index_path = "index.html"
        
    if not os.path.exists(index_path):
        print("[ERROR] Không tìm thấy file index.html của 8000Kicks!")
        return

    print(f"[V3000-INJECTOR] Đại phẫu và tiêm dữ liệu vào: {index_path}")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. THỪA HƯỞNG TỪ SEO-SHIELD: Bơm từ khóa giày gai dầu chống nước
    seo_tags = """
    <meta name="keywords" content="8000Kicks, giày gai dầu, giày chống nước, waterproof hemp shoes, sustainable footwear, Donabico Global Media">
    <meta name="description" content="Khám phá dòng giày làm từ sợi gai dầu tự nhiên chống nước 100% của 8000Kicks tại phân khu Donabico.">"""
    if "<head>" in html and "8000Kicks" not in html:
        html = html.replace("<head>", f"<head>{seo_tags}")

    # 2. THỪA HƯỞNG TỪ SOCIAL-PREVIEW: Tối ưu OpenGraph hiển thị link mạng xã hội
    og_tags = """
    <meta property="og:title" content="8000Kicks - Giày Gai Dầu Chống Nước Đầu Tiên Trên Thế Giới">
    <meta property="og:image" content="https://donabico-global-media.github.io/8000kicks/assets/hemp-shoes-banner.jpg">"""
    if "<head>" in html and "og:title" not in html:
        html = html.replace("<head>", f"<head>{og_tags}")

    # 3. THỪA HƯỞNG TỪ TRAFFIC-SIPHON: Tiêm thanh trạng thái Donabico Global Media System
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    status_banner = f"""
    <div id="dnbc-adtech-banner" style="background: linear-gradient(90deg, #11998e, #38ef7d); color: #000; text-align: center; font-family: sans-serif; font-size: 11px; padding: 6px; font-weight: bold; border-bottom: 2px solid #fff;">
        🛡️ DONABICO GLOBAL MEDIA SYSTEM | 8000KICKS NODE ACTIVE AT {current_time}
    </div>"""
    html = re.sub(r'<div id="dnbc-adtech-banner">.*?</div>', '', html, flags=re.DOTALL)
    if "<body>" in html:
        html = html.replace("<body>", f"<body>\n    {status_banner}")

    # 4. THỪA HƯỞNG TỪ AFFILIATE-NETWORK: Cố định tuyến link phân phối trực tiếp
    # Tự động thay thế toàn bộ link giữ chỗ thành link affiliate đích của bạn
    target_aff_url = "https://donabico-global-media.github.io/shop/8000kicks.html"
    html = re.sub(r'href="[^"]*placeholder_affiliate_link[^"]*"', f'href="{target_aff_url}"', html)

    # 5. THỪA HƯỞNG TỪ AI-CACHE-SIPHON: Nén dung lượng HTML cực hạn
    compressed_html = "\n".join([line.strip() for line in html.split("\n") if line.strip()])

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(compressed_html)
    print("[SUCCESS] Lộ trình tiêm dữ liệu trực tiếp 100% vào 8000Kicks hoàn tất!")

if __name__ == "__main__":
    run_all_siphons()
    inject_production_html()
