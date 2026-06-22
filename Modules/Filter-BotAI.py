import os
from bs4 import BeautifulSoup

def run():
    print("[+] Filter-BotAI: Đang thiết lập Hệ thống lọc Click ảo & Chặn Bot AI...")
    file_path = "index.html"
    if not os.path.exists(file_path):
        print("[-] Không tìm thấy index.html")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # NHÚNG LỚP KHIÊN REAL-TIME BOT FILTER SHIELD
    filter_script_id = "dnbc-anti-bot-shield"
    existing_filter = soup.find("script", id=filter_script_id)
    if existing_filter:
        existing_filter.decompose()

    filter_script_tag = soup.new_tag("script", id=filter_script_id)
    filter_script_tag.string = """
        (function() {
            let isRealUser = false;

            // 1. Gắn các trình lắng nghe hành vi vật lý thực tế của con người
            function verifyHuman() {
                isRealUser = true;
                // Người dùng thật tương tác -> Gỡ bỏ các trình lắng nghe để tiết kiệm tài nguyên
                window.removeEventListener('mousemove', verifyHuman);
                window.removeEventListener('touchstart', verifyHuman);
                window.removeEventListener('keydown', verifyHuman);
                window.removeEventListener('scroll', verifyHuman);
                console.log("[Shield Pass] Xác minh thực thể: Người dùng thật.");
            }

            window.addEventListener('mousemove', verifyHuman);
            window.addEventListener('touchstart', verifyHuman);
            window.addEventListener('keydown', verifyHuman);
            window.addEventListener('scroll', verifyHuman);

            // 2. Chặn tương tác nút bấm nếu phát hiện hành vi tự động hoặc Bot AI lọt lưới
            document.addEventListener('click', function(event) {
                const target = event.target.closest('a[data-dnbc-lock="true"]');
                if (target) {
                    const ua = navigator.userAgent.toLowerCase();
                    // Danh sách chữ ký nhận diện các hệ thống cào dữ liệu và Bot AI phổ biến
                    const botKeywords = [
                        'bot', 'spider', 'crawl', 'headless', 'puppeteer', 'selenium', 
                        'chatgpt', 'openai', 'claudebot', 'googlebot', 'bingbot', 'bytesspider'
                    ];
                    
                    const isBotUA = botKeywords.some(keyword => ua.includes(keyword));
                    
                    // Nếu là Bot UA hoặc click được kích hoạt tự động (không có hành vi di chuyển/chạm)
                    if (!isRealUser || isBotUA || event.isTrusted === false) {
                        event.preventDefault();
                        event.stopPropagation();
                        console.log("[Shield Blocked] Chặn thành công 01 Click ảo từ hệ thống tự động/Bot AI.");
                        alert("Access Denied: Automated interaction detected.");
                        return false;
                    }
                }
            }, true); // Sử dụng chế độ Capture để chặn trước khi sự kiện truyền đi
        })();
    """
    
    if soup.head:
        soup.head.append(filter_script_tag)
    else:
        soup.append(filter_script_tag)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("[===] Filter-BotAI: Đã triển khai Khiên bảo mật chống Click ảo thành công.")

if __name__ == "__main__":
    run()
