# Hướng Dẫn Sử Dụng - Me (Private)

## 🎯 Mục Đích

Repository này chứa:
- Bot token và secrets
- MCP server configs
- Private notes của mentor
- Scripts chạy trên máy local

## 📁 Cấu Trúc

```
.
├── .env                    ← Bot token (KHÔNG commit)
├── discord-mcp/            ← MCP server (KHÔNG commit)
├── .claude/                ← Claude settings (KHÔNG commit)
├── scripts/                ← Python scripts (CÓ thể commit)
│   ├── set_role_hierarchy.py
│   ├── set_permissions.py
│   ├── set_role_colors.py
│   └── post_content.py
└── docs/                   ← Documentation
```

## 🚀 Cách Chạy Scripts

### 1. Set up môi trường

```bash
# Install uv (nếu chưa có)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Load token từ .env
export $(cat .env | xargs)
```

### 2. Chạy script

```bash
uv run --no-project scripts/<script_name>.py
```

## 📝 Scripts Có Sẵn

| Script | Chức năng |
|--------|-----------|
| `set_role_hierarchy.py` | Sắp xếp Carl-bot lên trên |
| `set_permissions.py` | Set permissions cho 5 forum categories |
| `set_role_colors.py` | Set màu + hoist cho roles |
| `post_content.py` | Đăng nội quy và welcome message |

## 🔧 Cập Nhật Bot Token

1. Vào https://discord.com/developers/applications
2. Chọn bot → Bot → Reset Token
3. Cập nhật `.env`:
   ```
   DISCORD_TOKEN=<token_mới>
   ```

## 🔄 Git Workflow

```bash
# Me (private) - push all
git push origin main

# Con (public) - chỉ public files
git push public main
```

## ⚠️ Lưu Ý

- KHÔNG bao giờ commit `.env`, `discord-mcp/`, `.claude/`
- Scripts trong `scripts/` có thể push lên public nếu không chứa secrets
- PROJECT_STATE.md là source of truth - cập nhật thường xuyên