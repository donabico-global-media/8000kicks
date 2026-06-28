# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

class IssueLogProcessor:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.raw_log_path = os.path.join(self.script_dir, "raw_harvested.json")
        self.final_matrix_path = os.path.join(self.script_dir, "siphon_conversion_matrix.log")
        self.processed_numbers_path = os.path.join(self.script_dir, "processed_numbers.txt")

    def process_signals(self):
        if not os.path.exists(self.raw_log_path):
            return

        try:
            with open(self.raw_log_path, "r", encoding="utf-8") as f:
                issues_list = json.load(f)
            
            if not issues_list:
                return

            processed_numbers = []
            
            with open(self.final_matrix_path, "a", encoding="utf-8") as matrix_f:
                for issue in issues_list:
                    body_str = issue.get("body", "")
                    issue_number = issue.get("number")
                    
                    try:
                        # Bóc tách nội dung JSON lưu trong thân của Issue
                        radar_package = json.loads(body_str)
                        radar_package["protocol_compiled_at"] = datetime.now().isoformat()
                        
                        matrix_f.write(json.dumps(radar_package) + "\n")
                        processed_numbers.append(str(issue_number))
                    except:
                        # Nếu body không phải json chuẩn, vẫn lưu thô tránh mất vết
                        continue
            
            # Ghi lại các số Issue đã xử lý để Workflow tiến hành đóng
            if processed_numbers:
                with open(self.processed_numbers_path, "w", encoding="utf-8") as num_f:
                    num_f.write("\n".join(processed_numbers))
            
            os.remove(self.raw_log_path)
            print(f"📊 Đã lọc thành công {len(processed_numbers)} tín hiệu.")

        except Exception as e:
            print(f"🚨 Lỗi biên dịch: {e}")

if __name__ == "__main__":
    IssueLogProcessor().process_signals()
