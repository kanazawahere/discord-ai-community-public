# Ai Hoán Giải Cục - Discord Server

Discord server tu-tiên-themed cho cộng đồng học AI/Claude tại Việt Nam.

## 🌟 Ý tưởng

Server hoạt động như **thư viện tri thức sống**:
- Agent = Linh Thể
- Theme = Dị Giới
- Ưu tiên lưu trữ thay vì xóa

## 📚 Cấu trúc

| Cấp Bậc | Khu Vực | Yêu cầu |
|---------|---------|---------|
| 🩶 Phàm Nhân | Cổng Nhập Môn | Default |
| 🌱 Khai Linh | Nhập Môn Tu Hành | React 🌱 |
| ⚔️ Luyện Khí | Claude Code Pháp Môn | Tự nâng cấp |
| 🌀 Kết Giới | Đồng Tu & API, MCP Kết Giới | Tự nâng cấp |
| ☁️ Thiên Cơ | Vân Hải Tiên Cung | Tự nâng cấp |
| 👁️ Nội Điện | Linh Trí Học Cung | Admin |

## 🔧 Scripts

| Script | Mô tả |
|--------|-------|
| `scripts/set_role_hierarchy.py` | Sắp xếp role hierarchy |
| `scripts/set_permissions.py` | Set permissions cho categories |
| `scripts/set_role_colors.py` | Set màu + hoist roles |
| `scripts/post_content.py` | Đăng nội quy & welcome |

Chạy: `uv run --no-project scripts/<script>.py`

## 🔐 Private

- `.env` - Bot token
- `discord-mcp/` - MCP server config

## 📄 License

MIT
