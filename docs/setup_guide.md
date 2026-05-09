# Discord MCP – Hướng dẫn lấy Bot Token & Guild ID

Hướng dẫn từng bước để có 2 giá trị cần điền vào `discord-mcp/.env` và `claude_desktop_config.json`:

- `DISCORD_BOT_TOKEN`
- `DISCORD_GUILD_ID`

---

## Phần 1 – Tạo Discord Bot và lấy Token

### Bước 1. Tạo Application

1. Mở https://discord.com/developers/applications
2. Đăng nhập bằng tài khoản Discord của bạn.
3. Bấm **New Application** (góc trên bên phải).
4. Đặt tên (ví dụ: `SoKHCN AI Bot`) → tick **Terms of Service** → bấm **Create**.

### Bước 2. Tạo Bot User

1. Trong sidebar bên trái của Application, chọn **Bot**.
2. Bấm **Add Bot** → xác nhận **Yes, do it!**.
3. (Tùy chọn) Đặt tên/avatar cho bot.

### Bước 3. Lấy Bot Token

> ⚠️ Token là mật khẩu của bot. **Không** share, **không** commit lên git.

1. Trong tab **Bot**, ở khu vực **Token**:
   - Bấm **Reset Token** (hoặc **Copy** nếu có).
   - Nhập mật khẩu Discord / mã 2FA nếu được hỏi.
2. **Copy token ngay lập tức** – Discord chỉ cho xem **một lần** duy nhất.
3. Dán vào file `discord-mcp/.env`:
   ```
   DISCORD_BOT_TOKEN=<token_vừa_copy>
   ```
4. Nếu lỡ mất token → quay lại bấm **Reset Token** để cấp token mới (token cũ sẽ bị vô hiệu).

### Bước 4. Bật Privileged Intents (BẮT BUỘC)

Vẫn ở tab **Bot**, kéo xuống mục **Privileged Gateway Intents**, bật **cả 2** công tắc sau:

| Intent                     | Vì sao cần                                                      |
|----------------------------|-----------------------------------------------------------------|
| **Server Members Intent**  | Để liệt kê thành viên, quản lý role, các thao tác liên quan member |
| **Message Content Intent** | Để đọc nội dung tin nhắn (không chỉ metadata)                   |

Bấm **Save Changes** ở dưới cùng.

### Bước 5. Tạo link mời Bot vào server

1. Sidebar → **OAuth2** → **URL Generator**.
2. **Scopes**: tick `bot` và `applications.commands`.
3. **Bot Permissions**: chọn **Administrator** cho đầy đủ chức năng (hoặc chọn riêng các quyền liệt kê trong README của discord-mcp nếu muốn tối thiểu).
4. Copy URL ở cuối trang → mở trên trình duyệt.
5. Chọn server muốn thêm bot (cần quyền **Manage Server**) → **Authorize** → giải CAPTCHA nếu có.
6. Bot sẽ xuất hiện trong member list của server (hiển thị **offline** là bình thường – MCP server dùng REST API chứ không giữ kết nối Gateway liên tục).

---

## Phần 2 – Lấy Server (Guild) ID

1. Mở Discord (desktop hoặc web).
2. Bấm icon ⚙️ **User Settings** (gần tên user, góc dưới trái).
3. Vào **App Settings → Advanced**.
4. Bật công tắc **Developer Mode**.
5. Đóng Settings.
6. Trong server list bên trái, **chuột phải** vào tên server → **Copy Server ID**.
7. Dán vào `discord-mcp/.env`:
   ```
   DISCORD_GUILD_ID=<id_vừa_copy>
   ```

---

## Phần 3 – Kiểm tra setup

1. File `discord-mcp/.env` đã có **cả 2** giá trị (không để trống).
2. File `claude_desktop_config.json` cũng có cả 2 giá trị tương ứng (xem hướng dẫn merge ở bên dưới).
3. Khởi động lại Claude Desktop hoàn toàn (thoát từ system tray, không chỉ đóng cửa sổ).
4. Mở chat mới trong Claude Desktop → thử yêu cầu:
   - "List channels in my Discord server"
   - "Send a test message to channel <id>"

### Nếu báo lỗi

- **401 Unauthorized** → token sai hoặc đã bị reset → reset lại và copy lại.
- **403 Forbidden** → bot thiếu quyền → kiểm tra role của bot trong server.
- **Bot offline** → đây là **bình thường**, MCP server chỉ kết nối khi Claude gọi.
- **Không đọc được nội dung message** → chưa bật **Message Content Intent**.
- **Không list được member** → chưa bật **Server Members Intent**.

---

## Tham khảo

- README gốc: `discord-mcp/README.md`
- Repo: https://github.com/glittercowboy/discord-mcp
- Discord Developer Portal: https://discord.com/developers/applications
