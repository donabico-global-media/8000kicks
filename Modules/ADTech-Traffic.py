import os
from bs4 import BeautifulSoup

def run():
    print("[+] ADTech-Traffic: Kích hoạt Module cấu hình luồng Paid Traffic...")
    file_path = "index.html"
    if not os.path.exists(file_path): return

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # Tích hợp tập lệnh nhận diện thẻ UTM Source (Ví dụ: ?utm_source=taboola)
    traffic_script_id = "dnbc-paid-traffic-monitor"
    existing_script = soup.find("script", id=traffic_script_id)
    if existing_script: existing_script.decompose()

    traffic_script_tag = soup.new_tag("script", id=traffic_script_id)
    traffic_script_tag.string = """
        function parseAdTechTraffic() {
            const urlParams = new URLSearchParams(window.location.search);
            const source = urlParams.get('utm_source');
            if (source) {
                console.log(`[ADTech Active] Hứng luồng Traffic thành công từ nguồn: ${source}`);
                // Bạn có thể tùy biến giao diện hoặc đẩy event tracking riêng về GA/GTM tại đây
            }
        }
        window.addEventListener('DOMContentLoaded', parseAdTechTraffic);
    """
    
    if soup.head: soup.head.append(traffic_script_tag)
    else: soup.append(traffic_script_tag)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("[===] ADTech-Traffic: Đồng bộ hạ tầng Paid Traffic thành công. Hệ thống đã sẵn sàng đón luồng truy cập.")

if __name__ == "__main__":
    run()
