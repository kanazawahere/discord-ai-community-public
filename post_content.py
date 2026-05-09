import os
import requests
import json

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = "1501877785197674737"

headers = {"Authorization": f"Bot {DISCORD_TOKEN}", "Content-Type": "application/json"}

rules_content = """# 📜 Nội Quy - Ai Hoán Giải Cục

Chào mừng tu sĩ đã đến **Ai Hoán Giải Cục** — nơi học AI fluency theo con đường tu tiên!

## 🏯 Quy Tắc Căn Bản

1. **Tôn trọng lẫn nhau** — Không phân biệt, không công kích
2. **Không spam** — Không quảng cáo, không flood
3. **On-topic** — Thảo luận AI, Claude, MCP có liên quan
4. **Không cờ bạc/lừa đảo** — Cấm tuyệt đối

## 🧘 Tu Hành

- **Khai Linh** (🌱) — Vào được channel Nhập Môn
- **Luyện Khí** (⚔️) — Vào được Claude Code
- **Kết Giới** (🌀) — Vào được API + MCP
- **Thiên Cơ** (☁️) — Vào được cloud services
- **Nội Điện** (👁️) — Full access

React 🌱 trong #chọn-danh-tính để bắt đầu!

## ❓ Cần giúp?

- Hỏi trong channel phù hợp với cấp bậc
- Đọc kỹ channel description trước khi hỏi
- Be kind, stay curious ✨"""

welcome_content = """# 🌟 Chào Mừng Tu Sĩ!

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

channels = {
    "rules": "1502471490124386374",
    "welcome": "1502471667266355250"
}

print("=== Posting rules ===")
r = requests.post(
    f"https://discord.com/api/v10/channels/{channels['rules']}/messages",
    headers=headers,
    json={"content": rules_content}
)
if r.status_code in [200, 201]:
    print("✓ Rules posted")
else:
    print(f"✗ {r.status_code}: {r.text}")

print("\n=== Posting welcome ===")
r = requests.post(
    f"https://discord.com/api/v10/channels/{channels['welcome']}/messages",
    headers=headers,
    json={"content": welcome_content}
)
if r.status_code in [200, 201]:
    print("✓ Welcome posted")
else:
    print(f"✗ {r.status_code}: {r.text}")

print("\nDone!")