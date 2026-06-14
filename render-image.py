#!/usr/bin/env python3
import argparse

def generate_final_html(brand_name, affiliate_link, images):
    # Nội dung HTML giống như trên (đã được rút gọn để dễ đọc)
    # Bạn có thể paste toàn bộ nội dung index.html ở trên vào đây và thay thế biến
    html = open("index.html").read()  # Đọc template
    html = html.replace("{{BRAND_NAME}}", brand_name)
    html = html.replace("{{AFFILIATE_LINK}}", affiliate_link)
    html = html.replace("{{IMAGE_1}}", images[0])
    html = html.replace("{{IMAGE_2}}", images[1])
    html = html.replace("{{IMAGE_3}}", images[2])
    html = html.replace("{{IMAGE_4}}", images[3])
    return html

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--affiliate_link", required=True)
    parser.add_argument("--image1", required=True)
    parser.add_argument("--image2", required=True)
    parser.add_argument("--image3", required=True)
    parser.add_argument("--image4", required=True)
    args = parser.parse_args()

    brand_name = "8000Kicks"
    images = [args.image1, args.image2, args.image3, args.image4]

    final_html = generate_final_html(brand_name, args.affiliate_link, images)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("✅ Đã cập nhật index.html thành công!")
