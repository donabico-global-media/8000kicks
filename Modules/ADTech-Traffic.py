import os
import sys
from bs4 import BeautifulSoup

def run():
    sys.stdout.write("[+] ADTech-Traffic: Đang khởi tạo bộ lõi Agentic Siphon cho hạ tầng GitHub Pages...\n")
    
    # Định cấu hình tệp tĩnh đích trên kho lưu trữ GitHub
    file_path = "landing_pages.html"
    if not os.path.exists(file_path) and os.path.exists("index.html"):
        file_path = "index.html"
    
    if not os.path.exists(file_path):
        sys.stderr.write("[-] Thất bại: Không tìm thấy tệp tin cấu hình tĩnh trên Repository.\n")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        # 1. KHỬ CÁC THÀNH PHẦN CŨ TRÁNH ĐÈ MÃ TRONG CHU KỲ WORKFLOW
        traffic_script_id = "dnbc-paid-traffic-monitor"
        existing_script = soup.find("script", id=traffic_script_id)
        if existing_script: 
            existing_script.decompose()

        existing_schema = soup.find("script", type="application/ld+json")
        if existing_schema:
            existing_schema.decompose()

        # 2. CẤY DỮ LIỆU CẤU TRÚC JSON-LD (SEO AUTO-PILOT ĐỂ HÚT TRAFFIC MIỄN PHÍ VỀ GITHUB PAGES)
        schema_tag = soup.new_tag("script", type="application/ld+json")
        schema_tag.string = """
        {
          "@context": "https://schema.org",
          "@type": "TechArticle",
          "headline": "AeroControl V5-Agricultural Intelligence Platform",
          "description": "Real-Time Multispectral Mapping & NDVI Analysis. Autonomous Static Operations.",
          "proficiencyLevel": "Expert",
          "publisher": {
            "@type": "Organization",
            "name": "DONABICO GLOBAL MEDIA SYSTEM",
            "url": "https://donabicomedia.net"
          }
        }
        """
        if soup.head:
            soup.head.append(schema_tag)

        # 3. NHÚNG KỊCH BẢN XỬ LÝ CLIENT-SIDE (BẪY DỮ LIỆU TRÊN TRÌNH DUYỆT KHÁCH HÀNG)
        traffic_script_tag = soup.new_tag("script", id=traffic_script_id)
        traffic_script_tag.string = """
        (function() {
            try {
                const urlParams = new URLSearchParams(window.location.search);
                const source = urlParams.get('utm_source');
                const p_aid = urlParams.get('aid') || urlParams.get('clickid');
                
                // Phân luồng nguồn ngay trên trình duyệt của khách
                if (source) {
                    localStorage.setItem('dnbc_last_paid_source', source);
                    document.body.setAttribute('data-traffic-origin', source.toLowerCase());
                    if (source.toLowerCase() === 'mgid') {
                        document.body.setAttribute('data-traffic-tier', 'high-ticket');
                    }
                } else {
                    localStorage.setItem('dnbc_traffic_type', 'organic-free');
                    document.body.setAttribute('data-traffic-origin', 'organic');
                }
                
                // Cơ chế bẫy đối tượng: Gửi định danh về mạng ADS để tích lũy tệp Retargeting miễn phí
                if (p_aid) {
                    let pool = JSON.parse(localStorage.getItem('dnbc_audience_pool')) || [];
                    if (!pool.includes(p_aid)) {
                        pool.push(p_aid);
                        localStorage.setItem('dnbc_audience_pool', JSON.stringify(pool));
                    }
                    
                    // Tạo phần tử ảnh ẩn để đẩy dữ liệu khứ hồi về hệ thống đối tác quảng cáo
                    const imgPixel = new Image();
                    imgPixel.src = `https://partners.propellerads.com/audiences?aid=${encodeURIComponent(p_aid)}`;
                    imgPixel.style.display = 'none';
                    document.body.appendChild(imgPixel);
                }
            } catch (err) {
                console.log("[-] GitHub Pages traffic core bypassed.");
            }
        })();
        """
        
        if soup.head:
            soup.head.append(traffic_script_tag)
        else:
            soup.append(traffic_script_tag)

        # GHI ĐÈ ĐỂ GITHUB WORKFLOW THỰC HIỆN COMMIT VÀ TRIỂN KHAI LÊN GITHUB PAGES
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
        sys.stdout.write(f"[===] ADTech-Traffic: Đã chuẩn hóa tệp tĩnh cho hạ tầng GitHub Pages tại {file_path}.\n")

    except Exception as e:
        sys.stderr.write(f"[-] Lỗi xử lý cấu trúc tệp trên Git: {str(e)}\n")

if __name__ == "__main__":
    run()
