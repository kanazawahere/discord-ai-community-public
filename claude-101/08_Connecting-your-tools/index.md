---
title: "Connecting your tools"
parent: Claude 101
nav_order: 8
---

# Connecting your tools

Explain what connectors are and why they matter for your work with Claude
Navigate the connectors directory and set up your first connection
Use connected tools effectively in your conversations with Claude
What are connectors?
Key takeaways
Connectors transform Claude from an assistant into an informed collaborator
by giving Claude access to the same tools, data, and context that you use every day. Instead of starting every conversation from scratch, Claude can work directly with your actual information.
Connectors allow Claude to read information and perform actions on your behalf.
Depending on the connector and permissions you grant, Claude can search your files, retrieve documents, analyze data, create new content, update records, and execute tasks across your connected applications—all from within your conversation.
The Model Context Protocol (MCP) powers connectors.
Think of MCP like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a single, consistent interface. This open standard means developers can build connectors for any tool, and those connectors work seamlessly with Claude.
There are two types of connectors: web connectors and desktop extensions.
Web connectors link Claude to cloud services like Google Drive, Notion, Slack, and Asana. Desktop extensions run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications.
Finding and connecting tools
Anthropic maintains a directory of recommended connectors at claude.ai/directory. The directory is organized into two tabs:
Web:
Cloud services and applications (Gmail, Notion, Slack, Asana, Linear, Stripe, and many more)
Desktop extensions:
Local tools that run on your computer through the Claude Desktop app
To browse available connectors, you can also click the
+
button in the lower left of the chat window, then select
Connectors
.
Setting up a web connector
Here's how to connect a cloud service:
Find the connector:
Navigate to claude.ai/directory, or click
+
>
Connectors
in any chat
Click Connect:
Select the connector you want to add
Authenticate:
You'll be redirected to the service's login page. Sign in with your existing credentials
Grant permissions:
Review the specific permissions Claude is requesting, then authorize access
Test the connection:
Return to Claude and try a simple request, like "Can you access my [tool name]?"
Once connected, Claude can search, read, and in some cases take actions within that service—depending on the permissions you've granted.
Desktop extensions
Desktop extensions require the Claude Desktop app rather than the web interface. These extensions let Claude interact with local applications, your file system, and native features on macOS or Windows.
Some desktop extensions include:
Local file access for reading and organizing documents
Browser control for automated web tasks
Native application integration (like Figma for design work)
To install a desktop extension:
Download and install the
Claude Desktop app
Open the app and navigate to Settings > Extensions
Browse available extensions and click Install
Follow any additional setup steps specific to that extension
Using connectors in your work
Once you've connected your tools, Claude considers them when responding to your requests. Here are some practical ways to use connected tools:
Project management (Asana, Linear, Jira)
"What are my highest priority tasks due this week?"
"Create a new task for reviewing the Q4 budget proposal"
"Summarize the status of our product launch project"
Communication (Slack, Gmail)
"Find the email thread where we discussed the vendor contract"
"Draft a reply to the latest message in the #marketing channel"
"What did the team decide about the timeline in yesterday's discussion?"
Documentation (Notion, Google Drive, Confluence)
"Search our documentation for our brand voice guidelines"
"Summarize the meeting notes from last week's product review"
"What does our style guide say about using contractions?"
Business tools (Stripe, PayPal, Salesforce)
"Show me revenue trends for the past quarter"
"What's the status of the Acme Corp opportunity?"
"List recent transactions over $1,000"
Security and permissions
When you connect Claude to external services, you're granting it access to read—and sometimes modify—data within those services. Here are some important considerations:
Scoped access:
Permissions are specific to what the connector needs and you can toggle individual permissions on and off within each application's menu.
Claude sees what you see:
Claude can only access data
you
have access to. Connecting your work email doesn't give Claude access to your CEO's inbox—only your own.
Revocable at any time:
You can disconnect a service through Claude's settings or through the third-party service's security settings. Just as with Skills, you can also find or build custom connectors. Exercise the same caution — only install connectors from trusted sources.
Lesson reflection
Before moving on, consider:
Which of your daily work tools would be most valuable to connect to Claude?
What tasks currently require you to copy and paste information that connectors could handle automatically?
Are there workflows where combining data from multiple connected sources would save you significant time?
What's next
In the next lesson, you'll learn about Enterprise Search—a specialized feature for Claude for Work users that connects Claude to your organization's knowledge sources with custom prompts optimized for your company's context.
For more information on connectors and the Model Context Protocol, visit the
Anthropic Help Center
or explore the connector directory at claude.ai/directory.
Feedback
As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work and any feedback you may have. Share your feedback
here
.
Acknowledgments and license
Copyright 2025 Anthropic. All rights reserved.

## Câu hỏi ôn tập

- Which of your daily work tools would be most valuable to connect to Claude?
- What tasks currently require you to copy and paste information that connectors could handle automatically?
- Are there workflows where combining data from multiple connected sources would save you significant time?



## Tóm tắt

Nguồn tài liệu này hướng dẫn cách sử dụng **Connectors**, một hệ thống đột phá giúp biến Claude từ một trợ lý thông thường thành một **cộng tác viên am hiểu dữ liệu thực tế** của người dùng. Dựa trên tiêu chuẩn **Model Context Protocol (MCP)**, công cụ này cho phép AI truy cập trực tiếp vào các nền tảng đám mây như Google Drive, Slack hoặc các tệp tin cục bộ trên máy tính để thực hiện tra cứu và xử lý tác vụ. Văn bản phân loại rõ ràng giữa **trình kết nối web và tiện ích mở rộng máy để bàn**, đồng thời cung cấp lộ trình chi tiết từ khâu thiết lập, cấp quyền bảo mật đến việc ứng dụng vào quản lý dự án và giao tiếp chuyên nghiệp. Mục tiêu cốt lõi của tài liệu là giúp người dùng tối ưu hóa quy trình làm việc bằng cách thiết lập một **giao diện thống nhất**, nơi Claude có thể thay mặt họ tương tác với dữ liệu mà không cần sao chép thủ công.

**Từ khóa:** `Kết nối công cụ` · `Model Context Protocol` · `Ứng dụng tích hợp` · `Quyền truy cập` · `Tự động hóa công việc`




## Câu hỏi kiểm tra

<div class="quiz-vn" id="quiz-08_Connecting-your-tools"><div class="quiz-tabs"><button class="qtab active" data-level="easy" onclick="qTab(this,'quiz-08_Connecting-your-tools')">🟢 Cơ bản (10)</button><button class="qtab " data-level="medium" onclick="qTab(this,'quiz-08_Connecting-your-tools')">🟡 Nâng cao (10)</button><button class="qtab " data-level="hard" onclick="qTab(this,'quiz-08_Connecting-your-tools')">🔴 Thử thách (10)</button></div><div class="quiz-panel" data-level="easy" ><div class="qitem" data-correct="Cung cấp các hướng dẫn phát triển API và thực hành triển khai doanh nghiệp.">
<p class="qtext"><strong>1.</strong> Mục tiêu chính của Anthropic Academy là gì?</p>
<div class="qchoices"><label data-choice="Cung cấp các trò chơi giải trí liên quan đến AI."><input type="radio" name="quiz-08_Connecting-your-tools-easy-0" value="0"> Cung cấp các trò chơi giải trí liên quan đến AI.</label><label data-choice="Cung cấp các hướng dẫn phát triển API và thực hành triển khai doanh nghiệp."><input type="radio" name="quiz-08_Connecting-your-tools-easy-0" value="1"> Cung cấp các hướng dẫn phát triển API và thực hành triển khai doanh nghiệp.</label><label data-choice="Bán phần cứng máy tính để chạy mô hình ngôn ngữ."><input type="radio" name="quiz-08_Connecting-your-tools-easy-0" value="2"> Bán phần cứng máy tính để chạy mô hình ngôn ngữ.</label><label data-choice="Thay thế hoàn toàn các trường đại học truyền thống."><input type="radio" name="quiz-08_Connecting-your-tools-easy-0" value="3"> Thay thế hoàn toàn các trường đại học truyền thống.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Học viện được thiết kế để giúp người dùng nắm vững các nguồn lực của Anthropic, từ phát triển kỹ thuật đến triển khai thực tế.</div>
</div><div class="qitem" data-correct="Cổng kết nối USB-C cho AI.">
<p class="qtext"><strong>2.</strong> Giao thức Model Context Protocol (MCP) được ví với công nghệ nào để giúp người dùng dễ hình dung?</p>
<div class="qchoices"><label data-choice="Kết nối Bluetooth không dây."><input type="radio" name="quiz-08_Connecting-your-tools-easy-1" value="0"> Kết nối Bluetooth không dây.</label><label data-choice="Cổng kết nối USB-C cho AI."><input type="radio" name="quiz-08_Connecting-your-tools-easy-1" value="1"> Cổng kết nối USB-C cho AI.</label><label data-choice="Hệ điều hành Windows."><input type="radio" name="quiz-08_Connecting-your-tools-easy-1" value="2"> Hệ điều hành Windows.</label><label data-choice="Đĩa mềm lưu trữ dữ liệu."><input type="radio" name="quiz-08_Connecting-your-tools-easy-1" value="3"> Đĩa mềm lưu trữ dữ liệu.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">MCP được coi là một tiêu chuẩn chung cho phép Claude kết nối mượt mà với nhiều ứng dụng khác nhau qua một giao diện nhất quán.</div>
</div><div class="qitem" data-correct="Quyền hạn của chính người dùng đó trong dịch vụ được kết nối.">
<p class="qtext"><strong>3.</strong> Khi sử dụng trình kết nối (connectors), Claude kế thừa quyền hạn truy cập dữ liệu từ đâu?</p>
<div class="qchoices"><label data-choice="Quyền hạn của quản trị viên cao nhất trong tổ chức."><input type="radio" name="quiz-08_Connecting-your-tools-easy-2" value="0"> Quyền hạn của quản trị viên cao nhất trong tổ chức.</label><label data-choice="Quyền hạn mặc định của Anthropic đối với mọi ứng dụng."><input type="radio" name="quiz-08_Connecting-your-tools-easy-2" value="1"> Quyền hạn mặc định của Anthropic đối với mọi ứng dụng.</label><label data-choice="Quyền hạn của chính người dùng đó trong dịch vụ được kết nối."><input type="radio" name="quiz-08_Connecting-your-tools-easy-2" value="2"> Quyền hạn của chính người dùng đó trong dịch vụ được kết nối.</label><label data-choice="Claude có toàn quyền truy cập không giới hạn để tối ưu hóa kết quả."><input type="radio" name="quiz-08_Connecting-your-tools-easy-2" value="3"> Claude có toàn quyền truy cập không giới hạn để tối ưu hóa kết quả.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude chỉ có thể tiếp cận những tệp, kênh hoặc hồ sơ mà cá nhân đó được phép truy cập trong hệ thống nguồn.</div>
</div><div class="qitem" data-correct="Trình kết nối Web liên kết với dịch vụ đám mây, còn Desktop chạy cục bộ trên máy tính của bạn.">
<p class="qtext"><strong>4.</strong> Sự khác biệt cơ bản giữa trình kết nối Web (Web connectors) và tiện ích mở rộng máy tính (Desktop extensions) là gì?</p>
<div class="qchoices"><label data-choice="Trình kết nối Web chỉ dành cho người dùng trả phí, còn Desktop dành cho tất cả mọi người."><input type="radio" name="quiz-08_Connecting-your-tools-easy-3" value="0"> Trình kết nối Web chỉ dành cho người dùng trả phí, còn Desktop dành cho tất cả mọi người.</label><label data-choice="Trình kết nối Web liên kết với dịch vụ đám mây, còn Desktop chạy cục bộ trên máy tính của bạn."><input type="radio" name="quiz-08_Connecting-your-tools-easy-3" value="1"> Trình kết nối Web liên kết với dịch vụ đám mây, còn Desktop chạy cục bộ trên máy tính của bạn.</label><label data-choice="Trình kết nối Web nhanh hơn tiện ích Desktop gấp 10 lần."><input type="radio" name="quiz-08_Connecting-your-tools-easy-3" value="2"> Trình kết nối Web nhanh hơn tiện ích Desktop gấp 10 lần.</label><label data-choice="Không có sự khác biệt nào, chúng là hai tên gọi cho cùng một thứ."><input type="radio" name="quiz-08_Connecting-your-tools-easy-3" value="3"> Không có sự khác biệt nào, chúng là hai tên gọi cho cùng một thứ.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Trình kết nối Web dành cho các dịch vụ như Slack hay Google Drive, trong khi Desktop extension tương tác với tệp và ứng dụng cài đặt tại chỗ.</div>
</div><div class="qitem" data-correct="Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner).">
<p class="qtext"><strong>5.</strong> Trong gói Team và Enterprise, ai là người có quyền bật trình kết nối cho toàn bộ tổ chức?</p>
<div class="qchoices"><label data-choice="Bất kỳ nhân viên nào trong công ty."><input type="radio" name="quiz-08_Connecting-your-tools-easy-4" value="0"> Bất kỳ nhân viên nào trong công ty.</label><label data-choice="Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner)."><input type="radio" name="quiz-08_Connecting-your-tools-easy-4" value="1"> Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner).</label><label data-choice="Đội ngũ hỗ trợ kỹ thuật của Anthropic."><input type="radio" name="quiz-08_Connecting-your-tools-easy-4" value="2"> Đội ngũ hỗ trợ kỹ thuật của Anthropic.</label><label data-choice="Mô hình Claude tự động quyết định dựa trên nhu cầu công việc."><input type="radio" name="quiz-08_Connecting-your-tools-easy-4" value="3"> Mô hình Claude tự động quyết định dựa trên nhu cầu công việc.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Chỉ những người có quyền quản trị tổ chức mới có thể phê duyệt và bật các trình kết nối để các thành viên khác sử dụng.</div>
</div><div class="qitem" data-correct="Chỉ 1 trình kết nối tùy chỉnh duy nhất.">
<p class="qtext"><strong>6.</strong> Người dùng gói Miễn phí (Free) được phép thêm tối đa bao nhiêu trình kết nối tùy chỉnh (custom connectors)?</p>
<div class="qchoices"><label data-choice="Không giới hạn số lượng."><input type="radio" name="quiz-08_Connecting-your-tools-easy-5" value="0"> Không giới hạn số lượng.</label><label data-choice="Tối đa 5 trình kết nối."><input type="radio" name="quiz-08_Connecting-your-tools-easy-5" value="1"> Tối đa 5 trình kết nối.</label><label data-choice="Chỉ 1 trình kết nối tùy chỉnh duy nhất."><input type="radio" name="quiz-08_Connecting-your-tools-easy-5" value="2"> Chỉ 1 trình kết nối tùy chỉnh duy nhất.</label><label data-choice="Người dùng miễn phí không được sử dụng tính năng này."><input type="radio" name="quiz-08_Connecting-your-tools-easy-5" value="3"> Người dùng miễn phí không được sử dụng tính năng này.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu hướng dẫn nêu rõ người dùng miễn phí bị giới hạn ở một trình kết nối tùy chỉnh sử dụng remote MCP.</div>
</div><div class="qitem" data-correct="Ứng dụng Claude Desktop phải đang chạy và máy tính không được ngủ.">
<p class="qtext"><strong>7.</strong> Điều gì PHẢI xảy ra để Claude Cowork có thể hoàn thành các tác vụ trên máy tính?</p>
<div class="qchoices"><label data-choice="Máy tính phải đang ở chế độ ngủ (Sleep) để tiết kiệm năng lượng."><input type="radio" name="quiz-08_Connecting-your-tools-easy-6" value="0"> Máy tính phải đang ở chế độ ngủ (Sleep) để tiết kiệm năng lượng.</label><label data-choice="Ứng dụng Claude Desktop phải đang chạy và máy tính không được ngủ."><input type="radio" name="quiz-08_Connecting-your-tools-easy-6" value="1"> Ứng dụng Claude Desktop phải đang chạy và máy tính không được ngủ.</label><label data-choice="Người dùng phải liên tục gõ phím để duy trì phiên làm việc."><input type="radio" name="quiz-08_Connecting-your-tools-easy-6" value="2"> Người dùng phải liên tục gõ phím để duy trì phiên làm việc.</label><label data-choice="Chỉ cần điện thoại có kết nối mạng là đủ."><input type="radio" name="quiz-08_Connecting-your-tools-easy-6" value="3"> Chỉ cần điện thoại có kết nối mạng là đủ.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Để duy trì kết nối và thực hiện các thao tác cục bộ, ứng dụng nền phải hoạt động liên tục trên thiết bị.</div>
</div><div class="qitem" data-correct="Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính.">
<p class="qtext"><strong>8.</strong> Tính năng &#x27;Remote Control&#x27; trên ứng dụng di động có tác dụng gì?</p>
<div class="qchoices"><label data-choice="Dùng điện thoại để điều khiển TV thông minh."><input type="radio" name="quiz-08_Connecting-your-tools-easy-7" value="0"> Dùng điện thoại để điều khiển TV thông minh.</label><label data-choice="Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính."><input type="radio" name="quiz-08_Connecting-your-tools-easy-7" value="1"> Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính.</label><label data-choice="Theo dõi vị trí GPS của máy tính xách tay."><input type="radio" name="quiz-08_Connecting-your-tools-easy-7" value="2"> Theo dõi vị trí GPS của máy tính xách tay.</label><label data-choice="Thay thế hoàn toàn bàn phím máy tính bằng màn hình cảm ứng."><input type="radio" name="quiz-08_Connecting-your-tools-easy-7" value="3"> Thay thế hoàn toàn bàn phím máy tính bằng màn hình cảm ứng.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Nó cho phép người dùng bắt đầu các nhiệm vụ lập trình từ xa và truy cập vào môi trường phát triển cục bộ thông qua di động.</div>
</div><div class="qitem" data-correct="Hội thoại, dự án, trí nhớ và tùy chọn sẽ đồng bộ trên web, máy tính và di động khi đăng nhập.">
<p class="qtext"><strong>9.</strong> Câu nào sau đây mô tả đúng nhất về việc đồng bộ hóa tài khoản Claude?</p>
<div class="qchoices"><label data-choice="Các cuộc hội thoại và tùy chọn chỉ lưu cục bộ trên từng thiết bị riêng biệt."><input type="radio" name="quiz-08_Connecting-your-tools-easy-8" value="0"> Các cuộc hội thoại và tùy chọn chỉ lưu cục bộ trên từng thiết bị riêng biệt.</label><label data-choice="Mọi thứ trừ các dự án đều được đồng bộ hóa."><input type="radio" name="quiz-08_Connecting-your-tools-easy-8" value="1"> Mọi thứ trừ các dự án đều được đồng bộ hóa.</label><label data-choice="Hội thoại, dự án, trí nhớ và tùy chọn sẽ đồng bộ trên web, máy tính và di động khi đăng nhập."><input type="radio" name="quiz-08_Connecting-your-tools-easy-8" value="2"> Hội thoại, dự án, trí nhớ và tùy chọn sẽ đồng bộ trên web, máy tính và di động khi đăng nhập.</label><label data-choice="Chỉ những tài khoản Enterprise mới có tính năng đồng bộ hóa."><input type="radio" name="quiz-08_Connecting-your-tools-easy-8" value="3"> Chỉ những tài khoản Enterprise mới có tính năng đồng bộ hóa.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude được thiết kế để mang lại trải nghiệm nhất quán, cho phép bạn bắt đầu ở một nơi và kết thúc ở một nơi khác.</div>
</div><div class="qitem" data-correct="Do máy chủ MCP nằm sau tường lửa hoặc trong mạng riêng không thể truy cập từ internet công cộng.">
<p class="qtext"><strong>10.</strong> Khi một trình kết nối tùy chỉnh không thể kết nối hoặc bị hết thời gian chờ (timeout), nguyên nhân phổ biến nhất là gì?</p>
<div class="qchoices"><label data-choice="Do người dùng gõ sai tên trình kết nối."><input type="radio" name="quiz-08_Connecting-your-tools-easy-9" value="0"> Do người dùng gõ sai tên trình kết nối.</label><label data-choice="Do máy chủ MCP nằm sau tường lửa hoặc trong mạng riêng không thể truy cập từ internet công cộng."><input type="radio" name="quiz-08_Connecting-your-tools-easy-9" value="1"> Do máy chủ MCP nằm sau tường lửa hoặc trong mạng riêng không thể truy cập từ internet công cộng.</label><label data-choice="Do Claude không hỗ trợ tiếng Việt trong trình kết nối tùy chỉnh."><input type="radio" name="quiz-08_Connecting-your-tools-easy-9" value="2"> Do Claude không hỗ trợ tiếng Việt trong trình kết nối tùy chỉnh.</label><label data-choice="Do người dùng chưa cài đặt ứng dụng di động."><input type="radio" name="quiz-08_Connecting-your-tools-easy-9" value="3"> Do người dùng chưa cài đặt ứng dụng di động.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Vì các trình kết nối tùy chỉnh chạy từ đám mây của Anthropic, chúng cần có khả năng kết nối tới máy chủ của bạn qua internet.</div>
</div></div><div class="quiz-panel" data-level="medium" style="display:none"><div class="qitem" data-correct="Mythos">
<p class="qtext"><strong>1.</strong> Mô hình nào của Claude hiện đang được giới thiệu dưới dạng bản xem trước (preview) trong danh mục sản phẩm của Anthropic?</p>
<div class="qchoices"><label data-choice="Opus"><input type="radio" name="quiz-08_Connecting-your-tools-medium-0" value="0"> Opus</label><label data-choice="Mythos"><input type="radio" name="quiz-08_Connecting-your-tools-medium-0" value="1"> Mythos</label><label data-choice="Sonnet"><input type="radio" name="quiz-08_Connecting-your-tools-medium-0" value="2"> Sonnet</label><label data-choice="Haiku"><input type="radio" name="quiz-08_Connecting-your-tools-medium-0" value="3"> Haiku</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Mythos được liệt kê cụ thể là phiên bản xem trước (preview) trong danh sách các mô hình của Anthropic.</div>
</div><div class="qitem" data-correct="Model Context Protocol (MCP)">
<p class="qtext"><strong>2.</strong> Giao thức nào được Anthropic ví như &#x27;USB-C cho AI&#x27;, cho phép Claude kết nối đồng nhất với nhiều ứng dụng khác nhau?</p>
<div class="qchoices"><label data-choice="API Framework"><input type="radio" name="quiz-08_Connecting-your-tools-medium-1" value="0"> API Framework</label><label data-choice="Model Context Protocol (MCP)"><input type="radio" name="quiz-08_Connecting-your-tools-medium-1" value="1"> Model Context Protocol (MCP)</label><label data-choice="Claude Connect"><input type="radio" name="quiz-08_Connecting-your-tools-medium-1" value="2"> Claude Connect</label><label data-choice="Anthropic Link"><input type="radio" name="quiz-08_Connecting-your-tools-medium-1" value="3"> Anthropic Link</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu mô tả MCP là một tiêu chuẩn mở cho phép các trình kết nối hoạt động liền mạch với Claude giống như cách USB-C hoạt động.</div>
</div><div class="qitem" data-correct="Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner)">
<p class="qtext"><strong>3.</strong> Trong các gói Team và Enterprise, ai là người có quyền hạn cao nhất để bật các trình kết nối (connectors) cho toàn bộ tổ chức?</p>
<div class="qchoices"><label data-choice="Mọi thành viên trong nhóm"><input type="radio" name="quiz-08_Connecting-your-tools-medium-2" value="0"> Mọi thành viên trong nhóm</label><label data-choice="Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner)"><input type="radio" name="quiz-08_Connecting-your-tools-medium-2" value="1"> Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner)</label><label data-choice="Bộ phận hỗ trợ của Anthropic"><input type="radio" name="quiz-08_Connecting-your-tools-medium-2" value="2"> Bộ phận hỗ trợ của Anthropic</label><label data-choice="Chuyên gia CNTT (IT Professional)"><input type="radio" name="quiz-08_Connecting-your-tools-medium-2" value="3"> Chuyên gia CNTT (IT Professional)</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu quy định rằng quản trị viên cấp cao nhất phải bật trình kết nối ở cấp tổ chức trước khi các thành viên khác có thể sử dụng.</div>
</div><div class="qitem" data-correct="Web Connectors kết nối với dịch vụ đám mây, còn Desktop Extensions truy cập các tệp cục bộ">
<p class="qtext"><strong>4.</strong> Điểm khác biệt chính giữa &#x27;Web Connectors&#x27; và &#x27;Desktop Extensions&#x27; là gì?</p>
<div class="qchoices"><label data-choice="Web Connectors yêu cầu trả phí, còn Desktop Extensions thì miễn phí"><input type="radio" name="quiz-08_Connecting-your-tools-medium-3" value="0"> Web Connectors yêu cầu trả phí, còn Desktop Extensions thì miễn phí</label><label data-choice="Web Connectors kết nối với dịch vụ đám mây, còn Desktop Extensions truy cập các tệp cục bộ"><input type="radio" name="quiz-08_Connecting-your-tools-medium-3" value="1"> Web Connectors kết nối với dịch vụ đám mây, còn Desktop Extensions truy cập các tệp cục bộ</label><label data-choice="Desktop Extensions có thể dùng được trên trình duyệt web"><input type="radio" name="quiz-08_Connecting-your-tools-medium-3" value="2"> Desktop Extensions có thể dùng được trên trình duyệt web</label><label data-choice="Web Connectors chỉ dành cho lập trình viên"><input type="radio" name="quiz-08_Connecting-your-tools-medium-3" value="3"> Web Connectors chỉ dành cho lập trình viên</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Web Connectors liên kết với các dịch vụ như Slack/Drive, trong khi Desktop Extensions chạy cục bộ trên máy tính để truy cập hệ thống tệp.</div>
</div><div class="qitem" data-correct="Máy tính phải đang chạy ứng dụng Desktop và không được ở chế độ ngủ">
<p class="qtext"><strong>5.</strong> Điều kiện cần thiết để tính năng &#x27;Claude Cowork&#x27; có thể hoàn thành các tác vụ đã được giao là gì?</p>
<div class="qchoices"><label data-choice="Máy tính phải đang chạy ứng dụng Desktop và không được ở chế độ ngủ"><input type="radio" name="quiz-08_Connecting-your-tools-medium-4" value="0"> Máy tính phải đang chạy ứng dụng Desktop và không được ở chế độ ngủ</label><label data-choice="Người dùng phải liên tục quan sát màn hình"><input type="radio" name="quiz-08_Connecting-your-tools-medium-4" value="1"> Người dùng phải liên tục quan sát màn hình</label><label data-choice="Chỉ cần ứng dụng di động đang mở"><input type="radio" name="quiz-08_Connecting-your-tools-medium-4" value="2"> Chỉ cần ứng dụng di động đang mở</label><label data-choice="Cần có kết nối Bluetooth giữa điện thoại và máy tính"><input type="radio" name="quiz-08_Connecting-your-tools-medium-4" value="3"> Cần có kết nối Bluetooth giữa điện thoại và máy tính</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu nêu rõ ứng dụng Desktop cần được mở để Claude hoàn thành công việc; nếu máy tính ngủ, Claude không thể làm việc.</div>
</div><div class="qitem" data-correct="Hàng quý">
<p class="qtext"><strong>6.</strong> Bản tin &#x27;AI Fluency&#x27; của Anthropic cung cấp các nghiên cứu và tài nguyên về sự hợp tác giữa người và AI theo định kỳ như thế nào?</p>
<div class="qchoices"><label data-choice="Hàng tuần"><input type="radio" name="quiz-08_Connecting-your-tools-medium-5" value="0"> Hàng tuần</label><label data-choice="Hàng quý"><input type="radio" name="quiz-08_Connecting-your-tools-medium-5" value="1"> Hàng quý</label><label data-choice="Hàng tháng"><input type="radio" name="quiz-08_Connecting-your-tools-medium-5" value="2"> Hàng tháng</label><label data-choice="Hàng năm"><input type="radio" name="quiz-08_Connecting-your-tools-medium-5" value="3"> Hàng năm</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu nêu rõ bản tin AI Fluency được gửi định kỳ hàng quý (quarterly) tới hộp thư đến của người dùng.</div>
</div><div class="qitem" data-correct="Máy chủ phải có thể truy cập được qua internet công cộng">
<p class="qtext"><strong>7.</strong> Khi sử dụng các trình kết nối tùy chỉnh (Custom Connectors) qua MCP từ xa, yêu cầu kỹ thuật quan trọng đối với máy chủ của bạn là gì?</p>
<div class="qchoices"><label data-choice="Máy chủ phải nằm trong cùng mạng LAN với máy tính người dùng"><input type="radio" name="quiz-08_Connecting-your-tools-medium-6" value="0"> Máy chủ phải nằm trong cùng mạng LAN với máy tính người dùng</label><label data-choice="Máy chủ phải có thể truy cập được qua internet công cộng"><input type="radio" name="quiz-08_Connecting-your-tools-medium-6" value="1"> Máy chủ phải có thể truy cập được qua internet công cộng</label><label data-choice="Máy chủ không được phép sử dụng bất kỳ tường lửa nào"><input type="radio" name="quiz-08_Connecting-your-tools-medium-6" value="2"> Máy chủ không được phép sử dụng bất kỳ tường lửa nào</label><label data-choice="Phải chạy trên hệ điều hành macOS"><input type="radio" name="quiz-08_Connecting-your-tools-medium-6" value="3"> Phải chạy trên hệ điều hành macOS</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Vì Anthropic&#x27;s cloud cần kết nối tới máy chủ MCP của bạn, nó phải hiện diện trên internet công cộng hoặc được cấu hình qua tường lửa.</div>
</div><div class="qitem" data-correct="Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính">
<p class="qtext"><strong>8.</strong> Tính năng &#x27;Remote Control&#x27; trên ứng dụng di động cho phép người dùng thực hiện hành động nào sau đây?</p>
<div class="qchoices"><label data-choice="Điều khiển máy ảnh của điện thoại từ máy tính"><input type="radio" name="quiz-08_Connecting-your-tools-medium-7" value="0"> Điều khiển máy ảnh của điện thoại từ máy tính</label><label data-choice="Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính"><input type="radio" name="quiz-08_Connecting-your-tools-medium-7" value="1"> Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính</label><label data-choice="Thay đổi hình nền của ứng dụng Desktop"><input type="radio" name="quiz-08_Connecting-your-tools-medium-7" value="2"> Thay đổi hình nền của ứng dụng Desktop</label><label data-choice="Tắt nguồn máy tính từ xa"><input type="radio" name="quiz-08_Connecting-your-tools-medium-7" value="3"> Tắt nguồn máy tính từ xa</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Remote Control cho phép bắt đầu tác vụ mã hóa từ xa và truy cập vào môi trường phát triển cục bộ thông qua ứng dụng di động.</div>
</div><div class="qitem" data-correct="Một (1)">
<p class="qtext"><strong>9.</strong> Người dùng ở gói Miễn phí (Free) có thể thêm tối đa bao nhiêu trình kết nối tùy chỉnh (custom connectors)?</p>
<div class="qchoices"><label data-choice="Không giới hạn"><input type="radio" name="quiz-08_Connecting-your-tools-medium-8" value="0"> Không giới hạn</label><label data-choice="Một (1)"><input type="radio" name="quiz-08_Connecting-your-tools-medium-8" value="1"> Một (1)</label><label data-choice="Năm (5)"><input type="radio" name="quiz-08_Connecting-your-tools-medium-8" value="2"> Năm (5)</label><label data-choice="Mười (10)"><input type="radio" name="quiz-08_Connecting-your-tools-medium-8" value="3"> Mười (10)</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu ghi rõ người dùng gói miễn phí bị giới hạn ở một trình kết nối tùy chỉnh duy nhất.</div>
</div><div class="qitem" data-correct="Chỉ có thể tìm kiếm và tóm tắt dữ liệu mà không thể chỉnh sửa hay tạo mới">
<p class="qtext"><strong>10.</strong> Khi quản trị viên của gói Enterprise hạn chế quyền hành động của một Connector (ví dụ: Read-only), người dùng có thể làm gì?</p>
<div class="qchoices"><label data-choice="Ghi đè cài đặt này nếu họ có quyền admin trong ứng dụng nguồn"><input type="radio" name="quiz-08_Connecting-your-tools-medium-9" value="0"> Ghi đè cài đặt này nếu họ có quyền admin trong ứng dụng nguồn</label><label data-choice="Chỉ có thể tìm kiếm và tóm tắt dữ liệu mà không thể chỉnh sửa hay tạo mới"><input type="radio" name="quiz-08_Connecting-your-tools-medium-9" value="1"> Chỉ có thể tìm kiếm và tóm tắt dữ liệu mà không thể chỉnh sửa hay tạo mới</label><label data-choice="Vẫn có thể thực hiện mọi hành động nếu họ dùng ứng dụng Desktop"><input type="radio" name="quiz-08_Connecting-your-tools-medium-9" value="2"> Vẫn có thể thực hiện mọi hành động nếu họ dùng ứng dụng Desktop</label><label data-choice="Yêu cầu Claude tự động cấp lại quyền cho mình"><input type="radio" name="quiz-08_Connecting-your-tools-medium-9" value="3"> Yêu cầu Claude tự động cấp lại quyền cho mình</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Nếu quyền được đặt là Read-only, Claude có thể đọc dữ liệu để trả lời nhưng bị chặn các hành động viết (write/delete).</div>
</div></div><div class="quiz-panel" data-level="hard" style="display:none"><div class="qitem" data-correct="USB-C">
<p class="qtext"><strong>1.</strong> Giao thức Model Context Protocol (MCP) được ví như tiêu chuẩn kỹ thuật nào để mô tả khả năng kết nối linh hoạt của Claude với các ứng dụng khác?</p>
<div class="qchoices"><label data-choice="Bluetooth"><input type="radio" name="quiz-08_Connecting-your-tools-hard-0" value="0"> Bluetooth</label><label data-choice="USB-C"><input type="radio" name="quiz-08_Connecting-your-tools-hard-0" value="1"> USB-C</label><label data-choice="HDMI"><input type="radio" name="quiz-08_Connecting-your-tools-hard-0" value="2"> HDMI</label><label data-choice="Thunderbolt"><input type="radio" name="quiz-08_Connecting-your-tools-hard-0" value="3"> Thunderbolt</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu ví MCP như USB-C dành cho AI vì đây là chuẩn mở và nhất quán, cho phép kết nối nhiều ứng dụng qua một giao diện duy nhất.</div>
</div><div class="qitem" data-correct="Owner hoặc Primary Owner">
<p class="qtext"><strong>2.</strong> Trong gói Enterprise, ai là người có thẩm quyền cao nhất để kích hoạt các connector cho toàn bộ tổ chức?</p>
<div class="qchoices"><label data-choice="Mọi thành viên trong nhóm"><input type="radio" name="quiz-08_Connecting-your-tools-hard-1" value="0"> Mọi thành viên trong nhóm</label><label data-choice="Quản trị viên IT (IT Admin)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-1" value="1"> Quản trị viên IT (IT Admin)</label><label data-choice="Owner hoặc Primary Owner"><input type="radio" name="quiz-08_Connecting-your-tools-hard-1" value="2"> Owner hoặc Primary Owner</label><label data-choice="Developer có quyền API"><input type="radio" name="quiz-08_Connecting-your-tools-hard-1" value="3"> Developer có quyền API</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Chủ sở hữu hoặc Chủ sở hữu chính phải bật connector trong phần cài đặt tổ chức trước khi các thành viên có thể sử dụng.</div>
</div><div class="qitem" data-correct="Môi trường thực thi kết nối">
<p class="qtext"><strong>3.</strong> Điểm khác biệt cốt lõi về mặt vận hành giữa &#x27;Web connectors&#x27; và &#x27;Desktop extensions&#x27; là gì?</p>
<div class="qchoices"><label data-choice="Khả năng bảo mật dữ liệu"><input type="radio" name="quiz-08_Connecting-your-tools-hard-2" value="0"> Khả năng bảo mật dữ liệu</label><label data-choice="Vị trí lưu trữ dữ liệu nguồn"><input type="radio" name="quiz-08_Connecting-your-tools-hard-2" value="1"> Vị trí lưu trữ dữ liệu nguồn</label><label data-choice="Môi trường thực thi kết nối"><input type="radio" name="quiz-08_Connecting-your-tools-hard-2" value="2"> Môi trường thực thi kết nối</label><label data-choice="Phí đăng ký hàng tháng"><input type="radio" name="quiz-08_Connecting-your-tools-hard-2" value="3"> Phí đăng ký hàng tháng</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Web connectors liên kết với dịch vụ đám mây, trong khi Desktop extensions chạy cục bộ thông qua ứng dụng Claude Desktop.</div>
</div><div class="qitem" data-correct="On demand (Theo yêu cầu)">
<p class="qtext"><strong>4.</strong> Chế độ truy cập công cụ (Tool access) nào được khuyến nghị sử dụng khi người dùng có từ 10 connector trở lên để tối ưu không gian hội thoại?</p>
<div class="qchoices"><label data-choice="Auto (Tự động)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-3" value="0"> Auto (Tự động)</label><label data-choice="Manual (Thủ công)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-3" value="1"> Manual (Thủ công)</label><label data-choice="Always On (Luôn bật)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-3" value="2"> Always On (Luôn bật)</label><label data-choice="On demand (Theo yêu cầu)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-3" value="3"> On demand (Theo yêu cầu)</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Chế độ này giúp tiết kiệm không gian hội thoại bằng cách chỉ tải connector khi thực sự cần thiết.</div>
</div><div class="qitem" data-correct="Phải có thể truy cập được từ internet công cộng">
<p class="qtext"><strong>5.</strong> Khi sử dụng custom connector thông qua remote MCP, máy chủ (server) của người dùng cần đáp ứng điều kiện mạng nào sau đây?</p>
<div class="qchoices"><label data-choice="Chỉ cần nằm trong mạng LAN nội bộ"><input type="radio" name="quiz-08_Connecting-your-tools-hard-4" value="0"> Chỉ cần nằm trong mạng LAN nội bộ</label><label data-choice="Phải có thể truy cập được từ internet công cộng"><input type="radio" name="quiz-08_Connecting-your-tools-hard-4" value="1"> Phải có thể truy cập được từ internet công cộng</label><label data-choice="Phải sử dụng kết nối VPN riêng biệt"><input type="radio" name="quiz-08_Connecting-your-tools-hard-4" value="2"> Phải sử dụng kết nối VPN riêng biệt</label><label data-choice="Không cần kết nối internet"><input type="radio" name="quiz-08_Connecting-your-tools-hard-4" value="3"> Không cần kết nối internet</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Vì custom connector kết nối từ đám mây của Anthropic, server của bạn phải có địa chỉ công khai hoặc được cấu hình cho phép truy cập từ bên ngoài.</div>
</div><div class="qitem" data-correct="Claude Code CLI">
<p class="qtext"><strong>6.</strong> Tính năng &#x27;Remote Control&#x27; trên ứng dụng di động của Claude được thiết kế để tương tác với công cụ nào?</p>
<div class="qchoices"><label data-choice="Claude Code CLI"><input type="radio" name="quiz-08_Connecting-your-tools-hard-5" value="0"> Claude Code CLI</label><label data-choice="Google Drive"><input type="radio" name="quiz-08_Connecting-your-tools-hard-5" value="1"> Google Drive</label><label data-choice="Slack"><input type="radio" name="quiz-08_Connecting-your-tools-hard-5" value="2"> Slack</label><label data-choice="Bảng điều khiển bảng tính (Dashboard)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-5" value="3"> Bảng điều khiển bảng tính (Dashboard)</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Remote Control cho phép người dùng gửi các tác vụ từ điện thoại đến giao diện dòng lệnh Claude Code trên máy tính.</div>
</div><div class="qitem" data-correct="Cấu hình Tool permissions (Quyền công cụ)">
<p class="qtext"><strong>7.</strong> Đối với các gói Team và Enterprise, hành động nào sau đây giúp hạn chế Claude thực hiện việc gửi tin nhắn Slack nhưng vẫn cho phép đọc tin nhắn?</p>
<div class="qchoices"><label data-choice="Ngắt kết nối hoàn toàn connector Slack"><input type="radio" name="quiz-08_Connecting-your-tools-hard-6" value="0"> Ngắt kết nối hoàn toàn connector Slack</label><label data-choice="Cấu hình Tool permissions (Quyền công cụ)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-6" value="1"> Cấu hình Tool permissions (Quyền công cụ)</label><label data-choice="Chỉnh sửa tệp cấu hình MSIX"><input type="radio" name="quiz-08_Connecting-your-tools-hard-6" value="2"> Chỉnh sửa tệp cấu hình MSIX</label><label data-choice="Sử dụng tài khoản Slack miễn phí"><input type="radio" name="quiz-08_Connecting-your-tools-hard-6" value="3"> Sử dụng tài khoản Slack miễn phí</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Người quản trị có thể thiết lập các quyền như &#x27;Always allow&#x27;, &#x27;Needs approval&#x27; hoặc &#x27;Blocked&#x27; cho từng hành động cụ thể của connector.</div>
</div><div class="qitem" data-correct="Các phiên làm việc cục bộ sẽ ở lại trên thiết bị (on-device)">
<p class="qtext"><strong>8.</strong> Trong hệ thống Claude Cowork, điều gì xảy ra với các phiên làm việc (sessions) khi người dùng đăng nhập trên nhiều thiết bị khác nhau?</p>
<div class="qchoices"><label data-choice="Tất cả các phiên làm việc đều đồng bộ lên đám mây"><input type="radio" name="quiz-08_Connecting-your-tools-hard-7" value="0"> Tất cả các phiên làm việc đều đồng bộ lên đám mây</label><label data-choice="Các phiên làm việc cục bộ sẽ ở lại trên thiết bị (on-device)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-7" value="1"> Các phiên làm việc cục bộ sẽ ở lại trên thiết bị (on-device)</label><label data-choice="Phiên làm việc cũ sẽ bị ghi đè bởi thiết bị mới nhất"><input type="radio" name="quiz-08_Connecting-your-tools-hard-7" value="2"> Phiên làm việc cũ sẽ bị ghi đè bởi thiết bị mới nhất</label><label data-choice="Phiên làm việc chỉ tồn tại trong bộ nhớ RAM"><input type="radio" name="quiz-08_Connecting-your-tools-hard-7" value="3"> Phiên làm việc chỉ tồn tại trong bộ nhớ RAM</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu khẳng định trong Claude Cowork, các phiên làm việc cục bộ không được đồng bộ hóa qua các thiết bị khác.</div>
</div><div class="qitem" data-correct="Ứng dụng máy để bàn phải đang chạy và máy không ở chế độ ngủ">
<p class="qtext"><strong>9.</strong> Để đảm bảo Claude Cowork có thể hoàn thành các tác vụ được giao, trạng thái máy tính của người dùng phải như thế nào?</p>
<div class="qchoices"><label data-choice="Chỉ cần có kết nối Wi-Fi"><input type="radio" name="quiz-08_Connecting-your-tools-hard-8" value="0"> Chỉ cần có kết nối Wi-Fi</label><label data-choice="Ứng dụng máy để bàn phải đang chạy và máy không ở chế độ ngủ"><input type="radio" name="quiz-08_Connecting-your-tools-hard-8" value="1"> Ứng dụng máy để bàn phải đang chạy và máy không ở chế độ ngủ</label><label data-choice="Máy tính có thể ở chế độ Hibernate (Ngủ đông)"><input type="radio" name="quiz-08_Connecting-your-tools-hard-8" value="2"> Máy tính có thể ở chế độ Hibernate (Ngủ đông)</label><label data-choice="Chỉ cần ứng dụng di động đang mở"><input type="radio" name="quiz-08_Connecting-your-tools-hard-8" value="3"> Chỉ cần ứng dụng di động đang mở</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude Desktop cần phải đang chạy để thực hiện tác vụ; nếu máy tính ngủ, Claude sẽ không thể tiếp tục làm việc.</div>
</div><div class="qitem" data-correct="PKG">
<p class="qtext"><strong>10.</strong> Loại tệp cài đặt nào được hỗ trợ để triển khai Claude Desktop cho người dùng máy tính Mac trong môi trường doanh nghiệp?</p>
<div class="qchoices"><label data-choice="MSIX"><input type="radio" name="quiz-08_Connecting-your-tools-hard-9" value="0"> MSIX</label><label data-choice="DMG"><input type="radio" name="quiz-08_Connecting-your-tools-hard-9" value="1"> DMG</label><label data-choice="PKG"><input type="radio" name="quiz-08_Connecting-your-tools-hard-9" value="2"> PKG</label><label data-choice="EXE"><input type="radio" name="quiz-08_Connecting-your-tools-hard-9" value="3"> EXE</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu xác nhận trình cài đặt PKG được hỗ trợ cho việc triển khai hàng loạt trên hệ điều hành Mac.</div>
</div></div></div>




## Thẻ học

<div class="fc-deck" id="fc-08_Connecting-your-tools" data-cards="[{&quot;front&quot;: &quot;Anthropic Academy cung cấp các chứng chỉ sau khi hoàn thành các khóa học về chủ đề gì?&quot;, &quot;back&quot;: &quot;AI Fluency, phát triển API, Model Context Protocol và Claude Code.&quot;}, {&quot;front&quot;: &quot;Bản tin &#x27;AI Fluency&#x27; của Anthropic được gửi đến hộp thư của người đăng ký theo định kỳ nào?&quot;, &quot;back&quot;: &quot;Hàng quý (Quarterly).&quot;}, {&quot;front&quot;: &quot;Kể tên 4 mô hình Claude hiện có theo tài liệu.&quot;, &quot;back&quot;: &quot;Mythos preview, Opus, Sonnet và Haiku.&quot;}, {&quot;front&quot;: &quot;Tính năng &#x27;Claude Cowork&#x27; yêu cầu ứng dụng nào phải đang chạy để hoàn thành tác vụ?&quot;, &quot;back&quot;: &quot;Ứng dụng máy tính (Desktop app).&quot;}, {&quot;front&quot;: &quot;Giao thức nào được ví như &#x27;USB-C cho AI&#x27; giúp Claude kết nối với nhiều ứng dụng khác nhau?&quot;, &quot;back&quot;: &quot;Model Context Protocol (MCP).&quot;}, {&quot;front&quot;: &quot;Hai loại trình kết nối (connectors) chính trong hệ sinh thái Claude là gì?&quot;, &quot;back&quot;: &quot;Trình kết nối web (web connectors) và tiện ích mở rộng máy tính (desktop extensions).&quot;}, {&quot;front&quot;: &quot;Trình kết nối web (web connectors) cho phép Claude liên kết với các dịch vụ nào?&quot;, &quot;back&quot;: &quot;Các dịch vụ đám mây như Google Drive, Notion, Slack và Asana.&quot;}, {&quot;front&quot;: &quot;Tiện ích mở rộng máy tính (desktop extensions) cung cấp quyền truy cập vào các nguồn dữ liệu nào?&quot;, &quot;back&quot;: &quot;Các tệp cục bộ (local files) và ứng dụng gốc trên máy tính của người dùng.&quot;}, {&quot;front&quot;: &quot;Claude kế thừa quyền hạn truy cập (permissions) từ đâu khi sử dụng trình kết nối?&quot;, &quot;back&quot;: &quot;Kế thừa trực tiếp từ quyền của người dùng trong dịch vụ được kết nối.&quot;}, {&quot;front&quot;: &quot;Trong các gói Team và Enterprise, ai là người có quyền bật trình kết nối cho toàn tổ chức?&quot;, &quot;back&quot;: &quot;Chủ sở hữu (Owner) hoặc Chủ sở hữu chính (Primary Owner).&quot;}, {&quot;front&quot;: &quot;Chế độ &#x27;Tool access&#x27; mặc định khi có nhiều trình kết nối là gì?&quot;, &quot;back&quot;: &quot;Chế độ Tự động (Auto).&quot;}, {&quot;front&quot;: &quot;Khi nào người dùng nên chuyển sang chế độ &#x27;On demand&#x27; cho Tool access?&quot;, &quot;back&quot;: &quot;Khi có từ 10 trình kết nối trở lên đang hoạt động.&quot;}, {&quot;front&quot;: &quot;Claude Desktop hỗ trợ các loại trình cài đặt tiêu chuẩn nào cho doanh nghiệp?&quot;, &quot;back&quot;: &quot;MSIX (cho Windows) và PKG (cho Mac).&quot;}, {&quot;front&quot;: &quot;Tính năng &#x27;Quick entry&#x27; là lợi thế của ứng dụng nào so với phiên bản trình duyệt?&quot;, &quot;back&quot;: &quot;Ứng dụng máy tính (Desktop app).&quot;}, {&quot;front&quot;: &quot;Làm thế nào để đưa một cuộc hội thoại CLI từ Claude Code vào ứng dụng máy tính?&quot;, &quot;back&quot;: &quot;Sử dụng lệnh /desktop.&quot;}, {&quot;front&quot;: &quot;Các trình kết nối tùy chỉnh (custom connectors) sử dụng MCP từ xa bị giới hạn số lượng như thế nào đối với người dùng miễn phí?&quot;, &quot;back&quot;: &quot;Bị giới hạn tối đa 1 trình kết nối tùy chỉnh.&quot;}, {&quot;front&quot;: &quot;Tại sao một máy chủ MCP tùy chỉnh có thể không kết nối được dù ứng dụng Claude đang chạy cục bộ?&quot;, &quot;back&quot;: &quot;Vì trình kết nối tùy chỉnh kết nối từ đám mây của Anthropic chứ không phải từ thiết bị cục bộ.&quot;}, {&quot;front&quot;: &quot;Người dùng gói nào có thể sử dụng các ứng dụng di động của Claude?&quot;, &quot;back&quot;: &quot;Tất cả các gói, bao gồm Miễn phí (Free), Pro, Max, Team và Enterprise.&quot;}, {&quot;front&quot;: &quot;Claude có thể thực hiện những hành động gì thông qua trình kết nối?&quot;, &quot;back&quot;: &quot;Tìm kiếm tệp, truy xuất tài liệu, phân tích dữ liệu, tạo nội dung mới và cập nhật hồ sơ.&quot;}, {&quot;front&quot;: &quot;Chủ sở hữu gói Team/Enterprise có thể hạn chế hành động nào của trình kết nối để đảm bảo an toàn?&quot;, &quot;back&quot;: &quot;Hạn chế quyền ghi (write) hoặc xóa trong khi vẫn cho phép quyền đọc (read).&quot;}, {&quot;front&quot;: &quot;Để gán tác vụ cho Cowork từ điện thoại, người dùng cần những gì?&quot;, &quot;back&quot;: &quot;Cần cả ứng dụng di động và ứng dụng máy tính (đang chạy).&quot;}, {&quot;front&quot;: &quot;Tính năng &#x27;Remote Control&#x27; trên di động có mục đích gì?&quot;, &quot;back&quot;: &quot;Gửi các tác vụ từ điện thoại đến Claude Code CLI trên máy tính.&quot;}, {&quot;front&quot;: &quot;Tiện ích Claude cho Chrome cho phép Claude thực hiện hành động gì trực tiếp trên trình duyệt?&quot;, &quot;back&quot;: &quot;Điều hướng, nhấp chuột và điền biểu mẫu.&quot;}, {&quot;front&quot;: &quot;Các cuộc hội thoại có nội dung được đồng bộ hóa (synced content) từ trình kết nối có thể chia sẻ được không?&quot;, &quot;back&quot;: &quot;Không, các cuộc hội thoại này không thể chia sẻ.&quot;}, {&quot;front&quot;: &quot;Trình kết nối chỉ khả dụng trong loại dự án nào đối với các gói Team và Enterprise?&quot;, &quot;back&quot;: &quot;Dự án riêng tư (private projects).&quot;}, {&quot;front&quot;: &quot;Danh mục &#x27;Solutions&#x27; của Anthropic bao gồm các ngành dọc nào?&quot;, &quot;back&quot;: &quot;Giáo dục, Dịch vụ tài chính, Chính phủ, Chăm sóc sức khỏe, Khoa học đời sống và Phi lợi nhuận.&quot;}, {&quot;front&quot;: &quot;Claude Desktop Extensions được cài đặt ở đâu?&quot;, &quot;back&quot;: &quot;Được cài đặt cục bộ trên máy tính của người dùng.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để tìm các trình kết nối có khả năng hiển thị giao diện trực tiếp như bảng điều khiển (dashboards)?&quot;, &quot;back&quot;: &quot;Tìm các trình kết nối có huy hiệu &#x27;Interactive&#x27; (Tương tác) trong danh mục.&quot;}, {&quot;front&quot;: &quot;Điều kiện cần thiết để máy chủ MCP tùy chỉnh có thể hoạt động là gì?&quot;, &quot;back&quot;: &quot;Máy chủ phải có thể truy cập được qua internet công cộng.&quot;}, {&quot;front&quot;: &quot;Dữ liệu nào được đồng bộ hóa giữa các thiết bị khi đăng nhập cùng một tài khoản Claude?&quot;, &quot;back&quot;: &quot;Các cuộc hội thoại, dự án, bộ nhớ (memory) và các tùy chọn cá nhân.&quot;}, {&quot;front&quot;: &quot;Claude Code hỗ trợ các hoạt động phát triển phần mềm nào trực tiếp trong ứng dụng máy tính?&quot;, &quot;back&quot;: &quot;Xem trước máy chủ đang chạy, xem lại các thay đổi mã cục bộ và theo dõi trạng thái pull request.&quot;}, {&quot;front&quot;: &quot;Mô tả mục đích của khóa học &#x27;Claude 101&#x27;.&quot;, &quot;back&quot;: &quot;Cung cấp kiến thức cơ bản và hướng dẫn sử dụng Claude cho các nhu cầu công việc và đời sống.&quot;}, {&quot;front&quot;: &quot;Khi cấu hình quyền hạn cho công cụ (Tool permissions), ba lựa chọn phản hồi là gì?&quot;, &quot;back&quot;: &quot;Luôn cho phép (Always allow), Cần phê duyệt (Needs approval), hoặc Bị chặn (Blocked).&quot;}, {&quot;front&quot;: &quot;Tại sao việc kết nối email công việc với Claude không cho phép nó đọc email của CEO?&quot;, &quot;back&quot;: &quot;Vì Claude chỉ có thể truy cập dữ liệu mà chính người dùng đó có quyền truy cập.&quot;}, {&quot;front&quot;: &quot;Tính năng &#x27;Enterprise Search&#x27; dành cho đối tượng người dùng nào?&quot;, &quot;back&quot;: &quot;Người dùng Claude for Work.&quot;}, {&quot;front&quot;: &quot;Những nền tảng đám mây nào là đối tác cung cấp Claude Platform?&quot;, &quot;back&quot;: &quot;Amazon Bedrock, Google Cloud&#x27;s Vertex AI và Microsoft Foundry.&quot;}, {&quot;front&quot;: &quot;Điều gì xảy ra với các phiên làm việc cục bộ trong Claude Cowork khi chuyển đổi thiết bị?&quot;, &quot;back&quot;: &quot;Các phiên làm việc cục bộ sẽ vẫn ở lại trên thiết bị đó (stay on-device).&quot;}, {&quot;front&quot;: &quot;Mục &#x27;Help and security&#x27; của Anthropic cung cấp thông tin về những gì?&quot;, &quot;back&quot;: &quot;Khả dụng (Availability), Trạng thái (Status) và Trung tâm hỗ trợ (Support center).&quot;}, {&quot;front&quot;: &quot;Hành động &#x27;Restrict actions&#x27; của quản trị viên có thể ghi đè lên quyền của hệ thống nguồn không?&quot;, &quot;back&quot;: &quot;Không, nó chỉ có thể thu hẹp quyền chứ không bao giờ cấp nhiều quyền hơn hệ thống nguồn cho phép.&quot;}, {&quot;front&quot;: &quot;Để khắc phục sự cố xác thực trình kết nối, bước đầu tiên nên thử là gì?&quot;, &quot;back&quot;: &quot;Ngắt kết nối và kết nối lại từ mục Customize &gt; Connectors.&quot;}, {&quot;front&quot;: &quot;Claude for Slack và Claude for Microsoft 365 thuộc danh mục sản phẩm nào?&quot;, &quot;back&quot;: &quot;Các tính năng (Features) hoặc Tiện ích mở rộng của Claude.&quot;}, {&quot;front&quot;: &quot;Vai trò của &#x27;Skills&#x27; trong hệ sinh thái Claude là gì?&quot;, &quot;back&quot;: &quot;Là các khả năng đặc thù mà Claude có thể thực hiện được liệt kê trong danh mục sản phẩm.&quot;}, {&quot;front&quot;: &quot;Dịch vụ nào giúp Claude tìm kiếm các tệp tin trong Google Drive?&quot;, &quot;back&quot;: &quot;Trình kết nối Google Drive (Google Drive connector).&quot;}, {&quot;front&quot;: &quot;Người dùng có thể quản lý tất cả các trình kết nối của mình ở đâu trong giao diện Claude?&quot;, &quot;back&quot;: &quot;Trong phần Customize &gt; Connectors.&quot;}, {&quot;front&quot;: &quot;Mô hình nào của Claude được ghi chú là đang ở trạng thái &#x27;preview&#x27;?&quot;, &quot;back&quot;: &quot;Mythos.&quot;}, {&quot;front&quot;: &quot;Đâu là đường dẫn chính để cài đặt các trình kết nối tùy chỉnh theo tài liệu?&quot;, &quot;back&quot;: &quot;Thông qua Claude Desktop và phiên bản web.&quot;}, {&quot;front&quot;: &quot;Mục &#x27;Economic Futures&#x27; trong danh mục công ty đề cập đến điều gì?&quot;, &quot;back&quot;: &quot;Các nghiên cứu hoặc cam kết của Anthropic về tương lai kinh tế liên quan đến AI.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để Claude gợi ý ứng dụng đã kết nối trong một cuộc hội thoại?&quot;, &quot;back&quot;: &quot;Claude tự động đưa ứng dụng vào khi nó phù hợp với yêu cầu của người dùng mà không cần phải gọi tên.&quot;}, {&quot;front&quot;: &quot;Ứng dụng Claude dành cho thiết bị di động nào hiện đã có sẵn?&quot;, &quot;back&quot;: &quot;iOS và Android.&quot;}, {&quot;front&quot;: &quot;Tiện ích mở rộng máy tính cung cấp quyền truy cập vào các trình duyệt cục bộ như thế nào?&quot;, &quot;back&quot;: &quot;Thông qua các tiện ích được cài đặt cục bộ và tích hợp với ứng dụng máy tính.&quot;}]" data-cur="0" data-known="[]">
<div class="fc-progress">1 / 50</div>
<div class="fc-scene" onclick="fcFlip(this)"><div class="fc-card-inner"><div class="fc-front">Anthropic Academy cung cấp các chứng chỉ sau khi hoàn thành các khóa học về chủ đề gì?</div><div class="fc-back">AI Fluency, phát triển API, Model Context Protocol và Claude Code.</div></div></div>
<p class="fc-hint">Nhấn thẻ để lật · Dùng nút để điều hướng</p>
<div class="fc-nav">
<button onclick="fcMove('fc-08_Connecting-your-tools',-1)">← Trước</button>
<button class="fc-know" onclick="fcKnow('fc-08_Connecting-your-tools',true)">Nhớ rồi ✓</button>
<button class="fc-unknown" onclick="fcKnow('fc-08_Connecting-your-tools',false)">Học lại ✗</button>
<button onclick="fcMove('fc-08_Connecting-your-tools',1)">Tiếp →</button>
</div>
<div class="fc-stats">Nhớ: 0 / 50</div>
</div>




## Sơ đồ tư duy

<div class="mm-wrap">
<svg id="mm-08_Connecting-your-tools" class="markmap"></svg>
</div>
<script>
(function(){
  var data={"name": "Hệ sinh thái Anthropic & Claude", "children": [{"name": "Sản phẩm & Mô hình", "children": [{"name": "Ứng dụng Claude", "children": [{"name": "Claude Web & Mobile (iOS/Android)"}, {"name": "Claude Desktop"}, {"name": "Claude Code (CLI)"}, {"name": "Claude Cowork"}]}, {"name": "Mô hình AI", "children": [{"name": "Opus (Mạnh nhất)"}, {"name": "Sonnet (Cân bằng)"}, {"name": "Haiku (Nhanh/Nhẹ)"}, {"name": "Mythos preview"}]}, {"name": "Gói dịch vụ", "children": [{"name": "Free & Pro"}, {"name": "Max & Team"}, {"name": "Enterprise"}]}]}, {"name": "Tính năng Kết nối (Connectors)", "children": [{"name": "Phân loại", "children": [{"name": "Web Connectors (Google Drive, Slack, Notion)"}, {"name": "Desktop Extensions (File cục bộ, Figma)"}, {"name": "Custom Connectors (Remote MCP)"}]}, {"name": "Giao thức MCP", "children": [{"name": "Tiêu chuẩn mở cho AI"}, {"name": "Kết nối ứng dụng nhất quán"}]}, {"name": "Quản lý & Bảo mật", "children": [{"name": "Phân quyền theo người dùng"}, {"name": "Kiểm soát hành động (Read/Write)"}, {"name": "Dữ liệu mã hóa"}]}]}, {"name": "Đào tạo & Tài nguyên", "children": [{"name": "Anthropic Academy", "children": [{"name": "Khóa học Claude 101"}, {"name": "Hướng dẫn API & MCP"}, {"name": "Chứng chỉ hoàn thành"}]}, {"name": "Hỗ trợ", "children": [{"name": "Trung tâm trợ giúp (Help Center)"}, {"name": "Cộng đồng & Blog"}, {"name": "Bản tin AI Fluency"}]}]}, {"name": "Giải pháp & Ngành nghề", "children": [{"name": "Lĩnh vực", "children": [{"name": "Giáo dục & Nghiên cứu"}, {"name": "Tài chính & Y tế"}, {"name": "Chính phủ & Phi lợi nhuận"}]}, {"name": "Công việc chuyên môn", "children": [{"name": "Lập trình & Hiện đại hóa code"}, {"name": "Hỗ trợ khách hàng"}, {"name": "Đại lý AI (AI Agents)"}]}]}, {"name": "Triết lý & Chính sách", "children": [{"name": "Hiến pháp Claude (Constitution)"}, {"name": "Chính sách mở rộng có trách nhiệm"}, {"name": "Quyền riêng tư & Minh bạch"}]}]};
  function toMM(n){return{content:n.name||'',children:(n.children||[]).map(toMM)};}
  function init(){
    if(window.markmap&&window.markmap.Markmap){
      window.markmap.Markmap.create('#mm-08_Connecting-your-tools',null,toMM(data));
    } else {
      setTimeout(init,200);
    }
  }
  document.addEventListener('DOMContentLoaded',init);
})();
</script>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://claude.ai/download](https://claude.ai/download)
- [https://support.anthropic.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp](https://support.anthropic.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)
- [https://forms.gle/sY9ou5fqZBd3TjHF8](https://forms.gle/sY9ou5fqZBd3TjHF8)



---
*[Nguồn gốc](https://anthropic.skilljar.com/claude-101/383397){: target="_blank" }*
