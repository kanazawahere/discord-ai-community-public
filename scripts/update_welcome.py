import os
import requests

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
headers = {"Authorization": f"Bot {DISCORD_TOKEN}", "Content-Type": "application/json"}

content = """# 🌟 Chào Mừng Tu Sĩ!

**Ai Hoán Giải Cục** chào đón ngươi đến với con đường tu tiên AI!

> Không phải khu vực nào cũng có mã ngay từ đầu.
> Hệ thống sẽ mở khóa từng cấp theo tiến trình của bạn.

---

## 🗺️ Hệ Thống Cảnh Giới

| Cấp Bậc | Khu Vực |
|---------|---------|
| 🩶 Phàm Nhân | Cổng Nhập Môn |
| 🌱 Khai Linh | Nhập Môn Tu Hành |
| ⚔️ Luyện Khí | Claude Code Pháp Môn |
| 🌀 Kết Giới | Đồng Tu & API, MCP Kết Giới |
| ☁️ Thiên Cơ | Vân Hải Tiên Cung |
| 👁️ Nội Điện | Linh Trí Học Cung |

---

## 🚀 Bắt Đầu

1. **React 🌱** tại "#chọn-danh-tính"
2. Hệ thống sẽ mở khóa cảnh giới đầu tiên
3. Tiến vào **Nhập Môn Tu Hành**

Chúc tu hành thuận lợi! ⚡"""

r = requests.post(
    "https://discord.com/api/v10/channels/1502471667266355250/messages",
    headers=headers,
    json={"content": content}
)
print("✓ Posted" if r.status_code in [200, 201] else r.text)