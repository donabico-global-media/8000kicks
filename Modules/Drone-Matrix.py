import os
import re
from bs4 import BeautifulSoup

def run():
    print("[+] Drone-Matrix: Kích hoạt chế độ tự trị cấu trúc...")
    file_path = "index.html"
    if not os.path.exists(file_path): return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "name:" in content or "on:" in content:
        content = re.sub(r"^[\s\S]*?(?=(<!DOCTYPE html>|<html))", "", content)
        
    soup = BeautifulSoup(content, "html.parser")
    
    # Ép khung di động mượt mà
    if soup.head and not soup.find("meta", attrs={"name": "viewport"}):
        meta = soup.new_tag("meta", content="width=device-width, initial-scale=1.0")
        meta.attrs["name"] = "viewport"
        soup.head.append(meta)

    # Khóa cứng CSS hệ thống
    style_tag = soup.find("style", id="dnbc-core-font-lock")
    if not style_tag:
        style_tag = soup.new_tag("style", id="dnbc-core-font-lock")
        if soup.head: soup.head.append(style_tag)
        else: soup.append(style_tag)
    style_tag.string = "html, body, p, div, span, a, h1, h2, h3, h4, h5, h6, table, td, th { font-family: 'Times New Roman', Times, serif !important; } body { border: 4px solid #00ff66 !important; box-sizing: border-box; padding: 0 8px; }"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("[===] Drone-Matrix: Hoàn tất thiết lập cấu trúc tự trị.")

if __name__ == "__main__":
    run()
