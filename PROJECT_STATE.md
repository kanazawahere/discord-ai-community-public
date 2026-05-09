# Discord AI Community Bot — Project State

**One-liner**: Discord server tu-tiên-themed cho cộng đồng học AI/Claude, hoạt động như thư viện tri thức sống.
**Target user**: Người Việt học AI fluency, Claude Code, MCP — beginner đến intermediate.
**Môi trường chạy**: Discord platform; bot management qua Carl-bot dashboard + Python scripts (uv) chạy local trên Windows.
**Server**: Ai Hoán Giải Cục — Guild ID `1501877785197674737`
**Bot**: Hệ Thống Nghịch Thiên Cải Mệnh — User ID `1501929197860552957`

---

## Stack

- **Discord** (web app) — platform
- **Carl-bot** (đã invite, Administrator) — auto-role, reaction-role, moderation. Free, thay thế MEE6 hoàn toàn.
- **Python 3.12+** qua **`uv`** (user pref, KHÔNG pip) — script ad-hoc tạo/quản channels
- **Node.js** qua **`fnm`** (user pref, KHÔNG nvm) — chạy MCP server qua `npx`
- **`@ncodelife/discord-mcp-server@0.1.1`** (npm) — MCP cho **Claude Desktop** (KHÔNG chạy được trong Cowork)
- **Discord API v10** — `https://discord.com/api/v10`. Bot token CHỈ dùng được từ HTTP client thường (không phải browser).

---

## Structure

```
C:\Users\BeTin\Dropbox\SoKHCN\Discord_Ai_Community_Bot\   ← shared (multi-agent collab)
└── PROJECT_STATE.md                                       ← file này, source of truth

C:\Users\BeTin\Documents\Claude\Projects\Discord AI Community Bot\   ← project workspace
├── create_channels.py                  ← Legacy: tạo 1 text channel
├── create_full_structure.py            ← v2: tạo full 6 cat + 17 forum channels (script reference)
├── claude_desktop_config.discord.json  ← MCP config snippet (chứa bot token, KHÔNG commit)
├── install_discord_mcp.ps1             ← PowerShell: merge config vào claude_desktop_config.json
└── (chưa có .gitignore + .env — cần tạo)
```

**Discord Server structure (đã setup)**:
```
Ai Hoán Giải Cục/
├── 📜 Cổng Nhập Môn        ← public, ai cũng vào
│   ├── # rules
│   ├── # welcome
│   └── # chọn-danh-tính    ← reaction-role: 🌱 → role Khai Linh
├── 🌱 Nhập Môn Tu Hành     ← cần Khai Linh
│   ├── claude-101-khai-linh-nhập-môn
│   ├── ai-fluency-foundations-linh-trí-căn-cơ
│   └── ai-capabilities-limitations-thiên-cơ-giới-hạn
├── ⚔️ Claude Code Pháp Môn  ← cần Luyện Khí
│   ├── claude-code-101-kim-văn-nhập-môn
│   ├── claude-code-in-action-kim-văn-thực-chiến
│   ├── intro-agent-skills-linh-khế-bí-thuật
│   └── intro-subagents-phân-thần-thuật
├── 🔮 Đồng Tu & API        ← cần Kết Giới
│   ├── intro-claude-cowork-đồng-tu-pháp
│   └── building-claude-api-linh-mạch-api
├── 🌀 MCP Kết Giới         ← cần Kết Giới
│   ├── intro-mcp-kết-giới-nhập-môn
│   └── mcp-advanced-kết-giới-huyền-cơ
├── ☁️ Vân Hải Tiên Cung    ← cần Thiên Cơ
│   ├── claude-bedrock-vân-hải-đạo-đài
│   └── claude-vertex-thiên-cung-vertex
└── 📖 Linh Trí Học Cung    ← cần Nội Điện
    ├── ai-fluency-educators-đạo-sư-tu-hành
    ├── ai-fluency-students-học-cung-tu-hành
    ├── ai-fluency-nonprofits-thiện-tâm-đạo
    └── teaching-ai-fluency-truyền-đạo-sư
```

**Roles (6 tiers, cao → thấp)**:
- 👁️ Nội Điện (admin tier)
- ☁️ Thiên Cơ
- 🌀 Kết Giới
- ⚔️ Luyện Khí
- 🌱 Khai Linh (entry tier — sau react)
- 🩶 Phàm Nhân (default cho người mới join)

---

## Server Architecture

### Theme
- **Agent = Linh Thể**
- **Theme = Dị Giới**
- Server hoạt động như **hệ thống tri thức** thay vì chat room hỗn loạn.

### Thuật ngữ (DUY NHẤT)
| Tiếng Anh | Tiếng Việt |
|-----------|------------|
| Channel   | Kênh       |
| Post      | Bài viết   |
| Comment   | Bình luận  |

**KHÔNG dùng**: Thread, Forum, Topic, Discussion, Subthread

### Phân tầng nội dung

**Kênh hoạt động** — Dành cho nội dung còn đang active hoặc còn giá trị hiện tại.

**Khu lưu trữ** — 📦 Ký Ức Dị Giới → Kho Tri Thức
- Lưu các bài viết không còn active nhưng vẫn có giá trị tham khảo

### Workflow
```
Bài còn active → Hết thời sự nhưng còn giá trị → Chuyển vào Kho Tri Thức
```

### Nguyên tắc
- **Ưu tiên lưu trữ** thay vì xóa
- Khi chuyển bài vào lưu trữ:
  - Bình luận đi theo
  - File đi theo
  - Lịch sử được giữ nguyên
- **Mục tiêu**: giữ context, bảo tồn tri thức, biến server thành **thư viện sống**

---

## Rules

### Naming
- **Channel slug**: `english-slug-tiếng-việt` — bilingual, dấu `-` phân cách. Discord auto lowercase, replace space → `-`. Unicode tiếng Việt OK (max 100 chars).
- **Category**: `<emoji> <Tên tiếng Việt>` (emoji ở category giữ nguyên, ở channel slug bị strip).
- **Role**: `<emoji> <Tên>` — emoji đầu để member list đẹp.
- **Python**: `uv run --no-project script.py`. snake_case. KHÔNG hardcode token, đọc từ env hoặc `claude_desktop_config.discord.json`.

### Architecture
- **Channel type**: TẤT CẢ channel nội dung là **Forum** (type 15), KHÔNG dùng Text. Lý do: Forum tự enforce thread-only, không cho chat tự do.
- **Welcome channels** (rules, welcome, chọn-danh-tính) là **Text** (type 0).
- **Permission model (hướng B — "thấy nhưng không vào được")**: View Channel ALLOW cho @everyone (hiện trong sidebar), Read Message History + Send Messages + Create Threads DENY. Role tương ứng được ALLOW các permission đó cho category của họ.
- **Bot role hierarchy**: Carl-bot phải ở TRÊN role nó manage. Khi mới invite, Carl-bot có thể nằm dưới custom role → cần kéo lên.

### Bảo mật
- Bot token KHÔNG hardcode trong file commit lên git public. Đọc từ env (`DISCORD_TOKEN`) hoặc file ngoài git.
- Đã reset 1 lần do lộ. Token mới ở `claude_desktop_config.discord.json`. Cần move sang `.env` + add `.gitignore`.

---

## Current State

### Server core
- [x] Bot `Hệ Thống Nghịch Thiên Cải Mệnh` (Administrator)
- [x] Carl-bot invite (Administrator)
- [x] Kick MEE6
- [x] Xoá voice channel `Chung`
- [x] Xoá category `Kênh Chat` + `# thao-luan` mặc định
- [x] Xoá category `Kênh đàm thoại`

### Categories & channels
- [x] 6 categories tu tiên + 1 Cổng Nhập Môn (= 7 total)
- [x] 17 forum channels với tên song ngữ Anh-Việt
- [x] 3 text channels trong Cổng (rules, welcome, chọn-danh-tính)
- [x] Kéo `📜 Cổng Nhập Môn` lên đầu sidebar

### Roles & Carl-bot
- [x] 6 roles: Phàm Nhân, Khai Linh, Luyện Khí, Kết Giới, Thiên Cơ, Nội Điện
- [x] Carl-bot Auto-Role: assign `🩶 Phàm Nhân` cho member mới join (Sticky roles bật)
- [x] Carl-bot Reaction Role trong `# chọn-danh-tính`: 🌱 → Khai Linh
- [x] Sắp xếp role hierarchy — Carl-bot phải ở trên các custom role
- [x] Set màu cho roles (default xám)
- [x] Hoist (display separately) cho Khai Linh trở lên

### Permissions
- [x] @everyone DENY content trên 5 forum categories
- [x] 🌱 Khai Linh ALLOW content trên `🌱 Nhập Môn Tu Hành`
- [x] Permissions cho 4 role/category còn lại (Luyện Khí, Kết Giới, Thiên Cơ, Nội Điện)
- [ ] 📜 Cổng Nhập Môn full ALLOW @everyone

### Content
- [x] Đăng nội quy `# rules`
- [x] Đăng welcome message `# welcome` (embed format)

### Local files
- [x] `create_full_structure.py` (script tạo full structure)
- [x] `claude_desktop_config.discord.json` (MCP config)
- [x] `install_discord_mcp.ps1` (PowerShell installer)
- [x] `.gitignore` — CHƯA CÓ, RỦI RO commit lộ token
- [x] `.env` — chưa tạo, token vẫn ở JSON config

---

## Landmines (đọc kỹ trước khi làm)

### Discord API quirks
1. **Error 40333 "internal network error"**: Discord chặn bot token khi gọi API từ browser User-Agent. Bot token CHỈ dùng được từ HTTP client thường (Python `urllib`/`requests`, Node `axios`). Cả `fetch()` và `XMLHttpRequest` từ browser đều bị block ở guild operations endpoint, kể cả khi token hợp lệ. Endpoint `/users/@me` thì pass.
2. **Sandbox task block discord.com**: Cowork task sandbox trả `403 Tunnel Forbidden` cho mọi HTTPS request đến discord.com. Phải chạy script ngoài sandbox (máy user qua `uv run`).
3. **CORS không phải vấn đề** vì page đã ở discord.com origin. Anti-abuse detection ở Discord side mới là blocker.

### Forum channels
4. **KHÔNG convert được Text → Forum**: Discord không cho đổi loại channel sau khi tạo. Phải DELETE rồi recreate với `type: 15`.
5. **Forum permissions khác text**: "Send Messages and Create Posts" = quyền tạo post mới. "Send Messages in Threads and Posts" = quyền reply trong thread. Hai permission khác nhau.
6. **Forum channel có "Get Started" panel** chỉ moderator thấy. Có 5 setup tasks. Member không thấy panel này.

### UI automation gotchas
7. **Modal animation timing**: Sau khi click "Create Category"/"Create Channel", PHẢI wait ≥3-5s trước khi type.
8. **Emoji surrogate pairs**: `🩶` (gray heart, U+1FA76). KHÔNG phải `🫥`.
9. **Triple-click không clear input ổn định**: Dùng JS `inputElement.value = newValue` + `dispatchEvent(new Event('input', {bubbles:true}))`.
10. **Save Changes click qua coordinate đôi khi fail**: Workaround = dùng JS `Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Save Changes').click()`.
11. **Channel sidebar virtualized**: Channel ngoài viewport không tồn tại trong DOM. Cần `scrollIntoView()` trước khi find/click gear icon.
12. **Right-click context menu render lazy**: Sau right-click phải wait 1-2s trước khi find menu item.

### Channel naming
13. **Unicode tiếng Việt support trong slug**: `khai-linh-nhập-môn` hợp lệ. Max 100 chars.
14. **Emoji trong category name OK, trong channel slug bị strip**.

### Permissions
15. **Discord không có true "preview-only" mode**. Workaround: View Channel ALLOW + Read Message History DENY (~20 toggle/category).
16. **"Private Category" toggle ẩn HẲN category** khỏi @everyone. Đừng dùng cho hướng B.
17. **Permission inherit chain**: server > category > channel. Role ALLOW thắng DENY cùng level.

### Bot specifics
18. **Carl-bot role hierarchy**: Phải kéo Carl-bot role lên trên TẤT CẢ custom role nó cần manage.
19. **discord-mcp-server**: CHỈ chạy được trong **Claude Desktop**. KHÔNG chạy trong Cowork.

### Local environment
20. **Path Claude Desktop config trên Windows**: `%APPDATA%\Claude\claude_desktop_config.json`.
21. **`uv run --no-project`**: Dùng cho script standalone không có `pyproject.toml`.

### Token security
22. **Bot token format**: `<base64 user id>.<timestamp>.<HMAC>`. Lộ phần nào = lộ token.
23. **Token cũ đã commit code public** → reset là bắt buộc. Token mới đang ở `claude_desktop_config.discord.json`.
24. **Reset token**: Discord Developer Portal → Bot → Reset Token.

---

## Next steps (suggested order)

1. **Sắp role hierarchy**: Kéo Carl-bot role lên trên Khai Linh, Luyện Khí, v.v. trong Server Settings → Roles.
2. **Set permissions** trên 5 forum categories: @everyone DENY content (Hướng B: thấy nhưng không vào được). Dùng Python script (`uv`) để set hàng loạt.
3. **Set permissions Khai Linh** trên `🌱 Nhập Môn Tu Hành`: ALLOW content.
4. **Set màu + hoist** cho roles Khai Linh trở lên.
5. **Đăng nội quy** trong `# rules`.
6. **Đăng welcome message** trong `# welcome`.
7. **Move token ra `.env`** + thêm vào `.gitignore`.

---

*File này là source of truth chung cho mọi AI agent. Paste vào đầu chat để agent hiểu context ngay.*
