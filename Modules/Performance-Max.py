import os
import re
from bs4 import BeautifulSoup

def run():
    print("[+] Performance-Max: Đang quét sâu thanh lọc thông tin ảo...")
    file_path = "index.html"
    
    if not os.path.exists(file_path):
        print("[-] Không tìm thấy file index.html để quét.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # BỘ LỌC TRUNG THỰC: Tiêu diệt triệt để mọi thông tin áp lực/đếm ngược giả
    fake_patterns = [
        r"Only \d+ pairs left.*", 
        r"Chỉ còn \d+ đôi trong kho.*",
        r"Giảm giá \d+% trong \d+ phút.*",
        r"Flash sale.*",
        r"Khuyến mãi trực tiếp tại kho hàng.*"
    ]

    purge_count = 0
    # Sử dụng string=True thay cho text=True để tối ưu theo chuẩn BeautifulSoup mới
    for element in soup.find_all(string=True):
        text_value = element.strip()
        for pattern in fake_patterns:
            if re.search(pattern, text_value, re.IGNORECASE):
                element.replace_with("")
                purge_count += 1
                break

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"[===] Performance-Max: Đã dọn sạch {purge_count} vùng text lừa dối. Nội dung đạt chuẩn minh bạch 100%.")

if __name__ == "__main__":
    run()
