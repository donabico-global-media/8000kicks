import os
from bs4 import BeautifulSoup

def run():
    print("[+] Push-To-Google-Ads: Kiểm tra mã hóa tracking an toàn...")
    file_path = "index.html"
    if not os.path.exists(file_path): return

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    gateway_comment = "=== DNBC ADTECH GATEWAY - ETHICAL TRACKING MATRIX ==="
    if gateway_comment not in str(soup) and soup.head:
        soup.head.append(soup.new_string(f"\n\n"))
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("[===] Push-To-Google-Ads: Cổng truyền tải dữ liệu sạch đã online.")

if __name__ == "__main__":
    run()
