# PROJECT_STATE

## Discord Server: Ai Hoán Giải Cục

**Guild ID:** `1501877785197674737`  
**Bot:** Hệ Thống Nghịch Thiên Cải Mệnh

---

## ✅ Đã xong

- 6 categories + 17 forum channels
- 6 roles (Phàm Nhân → Nội Điện)
- Carl-bot (auto-role + reaction role)
- Permissions đã set
- Welcome + rules đã đăng

---

## 📁 Cấu trúc

```
Root (Private)
├── PublicInfo/     ← Công khai (1 file)
├── docs/           ← Private
├── scripts/        ← Private
└── human2agent.md ← Communication
```

---

## 🚀 Chạy scripts

```bash
export $(cat .env | xargs)
uv run --no-project scripts/<script>.py
```

---

## ⚙️ Scripts có sẵn

| Script | Chức năng |
|--------|-----------|
| `set_role_hierarchy.py` | Sắp xếp Carl-bot |
| `set_permissions.py` | Set permissions |
| `set_role_colors.py` | Set màu roles |
| `post_content.py` | Đăng nội quy/welcome |

---

## 🔧 Env

- `DISCORD_TOKEN` - từ `.env`
- `DISCORD_GUILD_ID` = `1501877785197674737`