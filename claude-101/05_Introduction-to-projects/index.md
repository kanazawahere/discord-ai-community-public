---
title: "Introduction to projects"
parent: Claude 101
nav_order: 5
---

# Introduction to projects

Explain what projects are and when to use them
Create a new project with a name, description, and visibility settings
Add documents and files to your project's knowledge base
Write effective project instructions to guide Claude's behavior
Share projects with teammates (for Claude for Work (Team and Enterprise plan) users)
Video
[Video: Introduction to Projects - Getting started with projects in Claude.ai]
Key takeaways
Projects are self-contained workspaces
with their own memory, chat histories, knowledge bases, and customized instructions. Think of them as dedicated environments for specific work streams.
Project knowledge enhances Claude's understanding
by letting you upload relevant documents that Claude references across all chats within that project. No more re-uploading the same files each time.
Project instructions guide Claude's behavior
—you can specify tone, expertise level, response style, and more. These instructions apply to every conversation within the project.
Projects scale automatically.
When your knowledge base approaches context limits, Claude seamlessly enables Retrieval Augmented Generation (RAG) mode to expand capacity by up to 10x while maintaining response quality.
For Claude for Work users, projects enable collaboration.
Share projects with teammates so everyone benefits from the same context, instructions, and accumulated knowledge.
What are Projects?
Projects are ideal for storing knowledge Claude should reference, organizing related chats around a specific topic or work area, and collaborating with team members who need access to the same shared context.
When to use Projects
Projects are particularly valuable when you're working on something ongoing—not just a one-off question. Consider creating a project when you have a workflow with:
Reference materials you'll use repeatedly
(meeting notes, survey results, reports, historical data, etc.)
Consistent requirements
for how Claude should respond (always use formal language, always cite sources, always follow our template)
Team collaboration needs
where multiple people should work from the same foundation
Creating your first project
Setting up a project takes just a few minutes. Here's how to get started:
Step 1: Set up your project
Hover over the left sidebar and click "Projects," or navigate directly to claude.ai/projects
Click "+ New Project" in the upper right corner
Give your project a descriptive name (e.g., "Q4 Marketing Campaign" or "Product Documentation")
Add a brief description of what you're working on. While Claude doesn't see this description directly, it helps you and your teammates understand the project's purpose.
Choose your visibility settings: keep it private or share with your organization (for Claude for Work users)
Step 2: Add project instructions
Project instructions tell Claude how to behave across all conversations in this project. Click on "Instructions" to open the instructions panel.
Good project instructions typically include:
Context about what you're working on:
"This project is for creating marketing content for our B2B software product."
Process instructions:
"First consider a blog structure that will entice this audience, then write the draft."
Tone and style preferences:
"Use a professional but conversational tone. Avoid jargon when possible."
Specific requirements:
"Always include a call-to-action at the end of marketing copy."
Once you've written your instructions, click "Save instructions." These will apply to every chat in this project and work alongside any user preferences and styles you've set.
You can also use project instructions to automate workflows — for example, "When I upload a meeting transcript, create a structured summary using this template." Think of instructions as programming Claude's behavior for this project.
Step 3: Build your knowledge base
Your project's knowledge base is where you upload documents that Claude should reference. You'll find the files menu on the right side of your project's main page.
Click the "+" button to add content. You can upload various file types including PDF, DOCX, CSV, TXT, HTML, and more. You can also connect to Google Drive to link documents directly.
What to upload:
Reference documents (brand guidelines, style guides, templates)
Background materials (research reports, meeting notes, requirements docs)
Examples of work you want Claude to emulate
Technical documentation or specifications
Pro tip:
Name your files descriptively. Claude uses file names to understand and retrieve the right information, so "Q4-2024-Brand-Guidelines.pdf" is more helpful than "document1.pdf."
How projects handle large knowledge bases
You might wonder what happens when you upload a lot of content. Projects automatically scale to handle large amounts through a process called Retrieval Augmented Generation (RAG). At a high level, this means that Claude can automatically find and use the most relevant parts of your uploaded documents when answering, without you needing to tell it which file to look at.
When your project knowledge approaches the context window limit, Claude seamlessly enables RAG mode. Instead of loading all project content into memory at once, Claude intelligently searches and retrieves only the most relevant information needed to answer your questions. This expands your project's capacity by up to 10x while maintaining response quality.
You'll see a visual indicator when your project is RAG-enabled, but the experience should feel the same—you can still upload documents, chat with Claude, and get context-aware responses.
Working within your project
Once your project is set up, you can start chatting with Claude. Each conversation within the project automatically has access to your knowledge base and follows your project instructions.
Collaboration features
For users on Claude for Work (Team and Enterprise) plans, projects become even more powerful through collaboration features.
Permission levels
When sharing a project, you can choose from three permission levels:
Can view:
Members can see project contents, access knowledge, and chat—but can't make changes. Think of this as read-only access with discussion rights.
Can edit:
Members have full collaboration power. They can modify instructions, update knowledge, manage other members, and actively contribute to the project.
Owner:
Project creators control everything, including who sees the project. They can share with specific people or make projects visible to the entire organization.
Sharing your project
To share a project:
Open the project you want to share
Click the "Share project" button to the right of the project name
Add individual members using their name or email, or copy and paste a list of email addresses for bulk sharing (in this case, the project will show up in their "Shared with you" section)
Or, share with "Everyone at [your organization]" to make your project discoverable within the Team tab
Team members will receive email notifications when you share a project with them, and they can find shared projects in their "Shared with me" tab.
Example projects to inspire you
Not sure where to start? Here are some common project types across different functions:
Q4 product launch:
Upload your product specs, competitive analysis, and messaging brainstorming notes. Claude will have this context top of mind for any inquiry or document draft.
Research support:
Centralize your competitive review, user research data, and customer feedback. Claude can help you synthesize sources, draft reports, and maintain consistency across recommendations.
Client account hub:
Keep your client's brand guidelines, past deliverables, and communication history in one place. Set instructions so Claude matches their tone and references their specific context when creating proposals or reports.
Event planning workspace:
Upload venue contracts, speaker bios, and attendee data. Claude can help generate run-of-show documents, attendee communications, and post-event reports that stay consistent with your event's theme.
Job description generator:
Gather past job descriptions, team charters, and internal headcount request docs. Work with Claude to draft job descriptions that reflect your team's actual work and culture.
Best practices for projects
To get the most out of projects:
Start focused, then expand.
Begin with a specific use case rather than trying to create one project for everything. You can always add more content as you go.
Keep your knowledge base current.
Outdated documents can lead to outdated responses. Review and update your project knowledge periodically.
Write clear instructions.
Be specific about what you want. Vague instructions lead to inconsistent results.
Name your documents descriptively.
(e.g., 'Q4-2025-Sales-Report.pdf' not 'report.pdf') and group related files together. Claude uses filenames and proximity to understand relationships between documents.
Reference documents by name.
When asking questions, you can mention specific documents to help Claude focus its search: "Based on our Q3 report, what were the top customer concerns?"
Lesson reflection
Before moving on, consider:
What ongoing work could benefit from having a dedicated project with persistent context?
What documents do you expect you'll be re-uploading or re-explaining to Claude on a regular basis?
If you're on a team, are there projects that would benefit from shared knowledge and instructions?
What's next
In the next lesson, we'll learn how to create mini-apps with Artifacts — actual outputs that Claude build and you can share right away.
For more information on getting started with projects, visit the
Anthropic Help Center
.
Feedback
As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work and any feedback you may have. Share your feedback
here
.
Acknowledgments and license
Copyright 2025 Anthropic. All rights reserved.
## Video

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin-bottom:1.5rem;">
  <iframe src="https://www.youtube.com/embed/GJ5jTgcbRHA?rel=0"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
          allowfullscreen loading="lazy" title="Introduction to projects"></iframe>
</div>

## Câu hỏi ôn tập

- What ongoing work could benefit from having a dedicated project with persistent context?
- What documents do you expect you&#x27;ll be re-uploading or re-explaining to Claude on a regular basis?
- If you&#x27;re on a team, are there projects that would benefit from shared knowledge and instructions?



## Tóm tắt

**Dự án (Projects)** trên Claude là các **không gian làm việc chuyên biệt** giúp người dùng tổ chức các cuộc hội thoại, dữ liệu và hướng dẫn tùy chỉnh cho từng mục tiêu cụ thể. Bằng cách xây dựng một **cơ sở tri thức (knowledge base)** thông qua việc tải lên các tài liệu liên quan, bạn giúp Claude có khả năng **tham chiếu thông tin nhất quán** mà không cần phải cung cấp lại dữ liệu nhiều lần. Điểm nổi bật của tính năng này là khả năng **tự động mở rộng quy mô thông qua RAG** khi dữ liệu lớn, cùng hệ thống **hướng dẫn dự án (project instructions)** giúp định hình phong cách và chuyên môn của AI. Đối với môi trường doanh nghiệp, công cụ này đóng vai trò là một **nền tảng cộng tác mạnh mẽ**, cho phép các nhóm cùng chia sẻ ngữ cảnh và làm việc hiệu quả dựa trên một nguồn thông tin duy nhất.

**Từ khóa:** `Tạo lập dự án` · `Cơ sở kiến thức` · `Hướng dẫn tùy chỉnh` · `Công nghệ RAG` · `Tính năng cộng tác`




## Câu hỏi kiểm tra

<div class="quiz-vn" id="quiz-05_Introduction-to-projects"><div class="quiz-tabs"><button class="qtab active" data-level="easy" onclick="qTab(this,'quiz-05_Introduction-to-projects')">🟢 Cơ bản (10)</button><button class="qtab " data-level="medium" onclick="qTab(this,'quiz-05_Introduction-to-projects')">🟡 Nâng cao (10)</button><button class="qtab " data-level="hard" onclick="qTab(this,'quiz-05_Introduction-to-projects')">🔴 Thử thách (10)</button></div><div class="quiz-panel" data-level="easy" ><div class="qitem" data-correct="Một môi trường khép kín với lịch sử trò chuyện, cơ sở kiến thức và cài đặt tùy chỉnh riêng.">
<p class="qtext"><strong>1.</strong> Trong Claude, một &#x27;Dự án&#x27; (Project) được định nghĩa là gì?</p>
<div class="qchoices"><label data-choice="Một môi trường khép kín với lịch sử trò chuyện, cơ sở kiến thức và cài đặt tùy chỉnh riêng."><input type="radio" name="quiz-05_Introduction-to-projects-easy-0" value="0"> Một môi trường khép kín với lịch sử trò chuyện, cơ sở kiến thức và cài đặt tùy chỉnh riêng.</label><label data-choice="Một tính năng chỉ dùng để lưu trữ các tệp tin PDF lớn mà không thể trò chuyện trực tiếp."><input type="radio" name="quiz-05_Introduction-to-projects-easy-0" value="1"> Một tính năng chỉ dùng để lưu trữ các tệp tin PDF lớn mà không thể trò chuyện trực tiếp.</label><label data-choice="Một công cụ chỉnh sửa mã nguồn trực tuyến thay thế hoàn toàn cho các trình soạn thảo code."><input type="radio" name="quiz-05_Introduction-to-projects-easy-0" value="2"> Một công cụ chỉnh sửa mã nguồn trực tuyến thay thế hoàn toàn cho các trình soạn thảo code.</label><label data-choice="Một thư mục chứa tất cả các cuộc trò chuyện từ trước đến nay của người dùng để dễ tìm kiếm."><input type="radio" name="quiz-05_Introduction-to-projects-easy-0" value="3"> Một thư mục chứa tất cả các cuộc trò chuyện từ trước đến nay của người dùng để dễ tìm kiếm.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Dự án cho phép người dùng tổ chức các luồng công việc cụ thể bằng cách tách biệt ngữ cảnh và tài liệu tham khảo cho từng mục đích sử dụng.</div>
</div><div class="qitem" data-correct="5 dự án">
<p class="qtext"><strong>2.</strong> Người dùng tài khoản miễn phí (free account) có thể tạo tối đa bao nhiêu dự án?</p>
<div class="qchoices"><label data-choice="5 dự án"><input type="radio" name="quiz-05_Introduction-to-projects-easy-1" value="0"> 5 dự án</label><label data-choice="1 dự án"><input type="radio" name="quiz-05_Introduction-to-projects-easy-1" value="1"> 1 dự án</label><label data-choice="10 dự án"><input type="radio" name="quiz-05_Introduction-to-projects-easy-1" value="2"> 10 dự án</label><label data-choice="Không giới hạn số lượng"><input type="radio" name="quiz-05_Introduction-to-projects-easy-1" value="3"> Không giới hạn số lượng</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Theo tài liệu Trung tâm Hỗ trợ của Claude, người dùng miễn phí bị giới hạn ở con số 5 để quản lý tài nguyên hệ thống.</div>
</div><div class="qitem" data-correct="Claude tự động kích hoạt chế độ RAG (Retrieval Augmented Generation) để mở rộng dung lượng.">
<p class="qtext"><strong>3.</strong> Điều gì xảy ra khi kiến thức dự án (Project Knowledge) tiếp cận giới hạn cửa sổ ngữ cảnh?</p>
<div class="qchoices"><label data-choice="Claude tự động kích hoạt chế độ RAG (Retrieval Augmented Generation) để mở rộng dung lượng."><input type="radio" name="quiz-05_Introduction-to-projects-easy-2" value="0"> Claude tự động kích hoạt chế độ RAG (Retrieval Augmented Generation) để mở rộng dung lượng.</label><label data-choice="Hệ thống sẽ yêu cầu người dùng xóa bớt các tệp tin cũ để có thể tiếp tục trò chuyện."><input type="radio" name="quiz-05_Introduction-to-projects-easy-2" value="1"> Hệ thống sẽ yêu cầu người dùng xóa bớt các tệp tin cũ để có thể tiếp tục trò chuyện.</label><label data-choice="Claude sẽ ngừng sử dụng các tệp tin trong cơ sở kiến thức và chỉ dựa vào dữ liệu huấn luyện gốc."><input type="radio" name="quiz-05_Introduction-to-projects-easy-2" value="2"> Claude sẽ ngừng sử dụng các tệp tin trong cơ sở kiến thức và chỉ dựa vào dữ liệu huấn luyện gốc.</label><label data-choice="Dự án sẽ tự động bị chuyển sang trạng thái lưu trữ (Archived) cho đến khi người dùng nâng cấp gói cước."><input type="radio" name="quiz-05_Introduction-to-projects-easy-2" value="3"> Dự án sẽ tự động bị chuyển sang trạng thái lưu trữ (Archived) cho đến khi người dùng nâng cấp gói cước.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Chế độ RAG cho phép Claude tìm kiếm thông minh và truy xuất các phần liên quan nhất từ kho dữ liệu khổng lồ mà không làm quá tải bộ nhớ.</div>
</div><div class="qitem" data-correct="Quy định cách Claude hành xử và phản hồi trong mọi cuộc trò chuyện thuộc dự án đó.">
<p class="qtext"><strong>4.</strong> Tính năng &#x27;Project Instructions&#x27; (Hướng dẫn dự án) có vai trò gì chính yếu?</p>
<div class="qchoices"><label data-choice="Quy định cách Claude hành xử và phản hồi trong mọi cuộc trò chuyện thuộc dự án đó."><input type="radio" name="quiz-05_Introduction-to-projects-easy-3" value="0"> Quy định cách Claude hành xử và phản hồi trong mọi cuộc trò chuyện thuộc dự án đó.</label><label data-choice="Chỉ dùng để mô tả mục tiêu của dự án cho các thành viên khác trong nhóm đọc."><input type="radio" name="quiz-05_Introduction-to-projects-easy-3" value="1"> Chỉ dùng để mô tả mục tiêu của dự án cho các thành viên khác trong nhóm đọc.</label><label data-choice="Dùng để liệt kê các nhiệm vụ cần làm (To-do list) cho Claude thực hiện theo lịch trình."><input type="radio" name="quiz-05_Introduction-to-projects-easy-3" value="2"> Dùng để liệt kê các nhiệm vụ cần làm (To-do list) cho Claude thực hiện theo lịch trình.</label><label data-choice="Tự động dịch các tài liệu trong cơ sở kiến thức sang ngôn ngữ được chỉ định."><input type="radio" name="quiz-05_Introduction-to-projects-easy-3" value="3"> Tự động dịch các tài liệu trong cơ sở kiến thức sang ngôn ngữ được chỉ định.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Hướng dẫn dự án giúp thiết lập giọng văn, mức độ chuyên môn và phong cách phản hồi nhất quán cho toàn bộ không gian làm việc.</div>
</div><div class="qitem" data-correct="Xem nội dung dự án, truy cập kiến thức và trò chuyện, nhưng không thể thay đổi cài đặt hoặc tài liệu.">
<p class="qtext"><strong>5.</strong> Trong các gói Claude cho công việc (Team hoặc Enterprise), quyền &#x27;Can view&#x27; cho phép thành viên làm gì?</p>
<div class="qchoices"><label data-choice="Xem nội dung dự án, truy cập kiến thức và trò chuyện, nhưng không thể thay đổi cài đặt hoặc tài liệu."><input type="radio" name="quiz-05_Introduction-to-projects-easy-4" value="0"> Xem nội dung dự án, truy cập kiến thức và trò chuyện, nhưng không thể thay đổi cài đặt hoặc tài liệu.</label><label data-choice="Chỉ được phép xem danh sách tên các dự án mà không được đọc nội dung bên trong."><input type="radio" name="quiz-05_Introduction-to-projects-easy-4" value="1"> Chỉ được phép xem danh sách tên các dự án mà không được đọc nội dung bên trong.</label><label data-choice="Được toàn quyền chỉnh sửa hướng dẫn dự án nhưng không được thêm thành viên mới."><input type="radio" name="quiz-05_Introduction-to-projects-easy-4" value="2"> Được toàn quyền chỉnh sửa hướng dẫn dự án nhưng không được thêm thành viên mới.</label><label data-choice="Chỉ được xem các cuộc trò chuyện công khai mà không được phép tự khởi tạo cuộc trò chuyện mới."><input type="radio" name="quiz-05_Introduction-to-projects-easy-4" value="3"> Chỉ được xem các cuộc trò chuyện công khai mà không được phép tự khởi tạo cuộc trò chuyện mới.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Quyền này tương đương với quyền truy cập &#x27;chỉ đọc&#x27; kết hợp với quyền thảo luận để bảo vệ cấu trúc dự án do người tạo thiết lập.</div>
</div><div class="qitem" data-correct="Tất cả các quyền chia sẻ sẽ bị thiết lập lại thành riêng tư vì mục đích bảo mật.">
<p class="qtext"><strong>6.</strong> Khi một dự án bị đưa vào kho lưu trữ (Archive), điều quan trọng nào sau đây sẽ xảy ra?</p>
<div class="qchoices"><label data-choice="Tất cả các quyền chia sẻ sẽ bị thiết lập lại thành riêng tư vì mục đích bảo mật."><input type="radio" name="quiz-05_Introduction-to-projects-easy-5" value="0"> Tất cả các quyền chia sẻ sẽ bị thiết lập lại thành riêng tư vì mục đích bảo mật.</label><label data-choice="Toàn bộ các tệp tin trong cơ sở kiến thức sẽ bị xóa vĩnh viễn và không thể khôi phục."><input type="radio" name="quiz-05_Introduction-to-projects-easy-5" value="1"> Toàn bộ các tệp tin trong cơ sở kiến thức sẽ bị xóa vĩnh viễn và không thể khôi phục.</label><label data-choice="Dự án sẽ biến mất hoàn toàn khỏi tài khoản và người dùng phải liên hệ hỗ trợ để tìm lại."><input type="radio" name="quiz-05_Introduction-to-projects-easy-5" value="2"> Dự án sẽ biến mất hoàn toàn khỏi tài khoản và người dùng phải liên hệ hỗ trợ để tìm lại.</label><label data-choice="Người dùng có thể xóa trực tiếp dự án đó ngay khi nó đang ở trạng thái lưu trữ."><input type="radio" name="quiz-05_Introduction-to-projects-easy-5" value="3"> Người dùng có thể xóa trực tiếp dự án đó ngay khi nó đang ở trạng thái lưu trữ.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Theo hướng dẫn, việc lưu trữ sẽ xóa bỏ ngữ cảnh chia sẻ trước đó để đảm bảo an toàn dữ liệu cho những dự án không còn hoạt động.</div>
</div><div class="qitem" data-correct="Nhấp vào mũi tên thả xuống bên cạnh tên cuộc trò chuyện và chọn &#x27;Add to project&#x27;.">
<p class="qtext"><strong>7.</strong> Làm thế nào để đưa một cuộc trò chuyện riêng lẻ (standalone chat) vào trong một dự án?</p>
<div class="qchoices"><label data-choice="Nhấp vào mũi tên thả xuống bên cạnh tên cuộc trò chuyện và chọn &#x27;Add to project&#x27;."><input type="radio" name="quiz-05_Introduction-to-projects-easy-6" value="0"> Nhấp vào mũi tên thả xuống bên cạnh tên cuộc trò chuyện và chọn &#x27;Add to project&#x27;.</label><label data-choice="Phải sao chép toàn bộ văn bản cuộc trò chuyện và dán vào một cuộc hội thoại mới trong dự án."><input type="radio" name="quiz-05_Introduction-to-projects-easy-6" value="1"> Phải sao chép toàn bộ văn bản cuộc trò chuyện và dán vào một cuộc hội thoại mới trong dự án.</label><label data-choice="Tính năng này hiện chỉ dành cho phiên bản Claude Desktop và không có trên trình duyệt web."><input type="radio" name="quiz-05_Introduction-to-projects-easy-6" value="2"> Tính năng này hiện chỉ dành cho phiên bản Claude Desktop và không có trên trình duyệt web.</label><label data-choice="Chỉ có thể di chuyển nếu cuộc trò chuyện đó chưa có tệp tin đính kèm nào."><input type="radio" name="quiz-05_Introduction-to-projects-easy-6" value="3"> Chỉ có thể di chuyển nếu cuộc trò chuyện đó chưa có tệp tin đính kèm nào.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude cung cấp tính năng di chuyển linh hoạt để người dùng có thể tổ chức lại các cuộc hội thoại ngẫu nhiên vào đúng ngữ cảnh dự án.</div>
</div><div class="qitem" data-correct="10 lần">
<p class="qtext"><strong>8.</strong> Công nghệ RAG giúp tăng khả năng xử lý dung lượng của dự án lên gấp khoảng bao nhiêu lần?</p>
<div class="qchoices"><label data-choice="10 lần"><input type="radio" name="quiz-05_Introduction-to-projects-easy-7" value="0"> 10 lần</label><label data-choice="2 lần"><input type="radio" name="quiz-05_Introduction-to-projects-easy-7" value="1"> 2 lần</label><label data-choice="100 lần"><input type="radio" name="quiz-05_Introduction-to-projects-easy-7" value="2"> 100 lần</label><label data-choice="50 lần"><input type="radio" name="quiz-05_Introduction-to-projects-easy-7" value="3"> 50 lần</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tài liệu giới thiệu về Dự án khẳng định việc sử dụng RAG giúp mở rộng dung lượng ngữ cảnh hiệu quả gấp 10 lần so với thông thường.</div>
</div><div class="qitem" data-correct="Sử dụng tên tệp có tính mô tả cụ thể (ví dụ: &#x27;Q4-2025-Sales-Report.pdf&#x27;).">
<p class="qtext"><strong>9.</strong> Điều nào sau đây là một &#x27;Best Practice&#x27; (Thực hành tốt nhất) khi đặt tên tài liệu tải lên dự án?</p>
<div class="qchoices"><label data-choice="Sử dụng tên tệp có tính mô tả cụ thể (ví dụ: &#x27;Q4-2025-Sales-Report.pdf&#x27;)."><input type="radio" name="quiz-05_Introduction-to-projects-easy-8" value="0"> Sử dụng tên tệp có tính mô tả cụ thể (ví dụ: &#x27;Q4-2025-Sales-Report.pdf&#x27;).</label><label data-choice="Đặt tên tệp càng ngắn càng tốt như &#x27;1.pdf&#x27; hoặc &#x27;a.txt&#x27; để tiết kiệm bộ nhớ."><input type="radio" name="quiz-05_Introduction-to-projects-easy-8" value="1"> Đặt tên tệp càng ngắn càng tốt như &#x27;1.pdf&#x27; hoặc &#x27;a.txt&#x27; để tiết kiệm bộ nhớ.</label><label data-choice="Chỉ nên sử dụng các ký tự số để Claude xử lý dữ liệu nhanh hơn."><input type="radio" name="quiz-05_Introduction-to-projects-easy-8" value="2"> Chỉ nên sử dụng các ký tự số để Claude xử lý dữ liệu nhanh hơn.</label><label data-choice="Đặt tên tệp trùng với tên dự án để đảm bảo tính đồng bộ."><input type="radio" name="quiz-05_Introduction-to-projects-easy-8" value="3"> Đặt tên tệp trùng với tên dự án để đảm bảo tính đồng bộ.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude sử dụng tên tệp để hiểu và truy xuất thông tin chính xác hơn khi người dùng đặt câu hỏi liên quan đến một tài liệu cụ thể.</div>
</div><div class="qitem" data-correct="Claude 101">
<p class="qtext"><strong>10.</strong> Trong Anthropic Academy, khóa học nào tập trung vào việc giới thiệu các khái niệm cơ bản về Claude?</p>
<div class="qchoices"><label data-choice="Claude 101"><input type="radio" name="quiz-05_Introduction-to-projects-easy-9" value="0"> Claude 101</label><label data-choice="Claude Code in action"><input type="radio" name="quiz-05_Introduction-to-projects-easy-9" value="1"> Claude Code in action</label><label data-choice="Model Context Protocol"><input type="radio" name="quiz-05_Introduction-to-projects-easy-9" value="2"> Model Context Protocol</label><label data-choice="AI Fluency newsletter"><input type="radio" name="quiz-05_Introduction-to-projects-easy-9" value="3"> AI Fluency newsletter</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Khóa học Claude 101 được thiết kế để cung cấp những kiến thức nền tảng và cách bắt đầu sử dụng Claude hiệu quả.</div>
</div></div><div class="quiz-panel" data-level="medium" style="display:none"><div class="qitem" data-correct="Tạo các môi trường làm việc độc lập với lịch sử trò chuyện và cơ sở kiến thức riêng.">
<p class="qtext"><strong>1.</strong> Tính năng &#x27;Dự án&#x27; (Projects) trên Claude được thiết kế chủ yếu để làm gì?</p>
<div class="qchoices"><label data-choice="Tạo các môi trường làm việc độc lập với lịch sử trò chuyện và cơ sở kiến thức riêng."><input type="radio" name="quiz-05_Introduction-to-projects-medium-0" value="0"> Tạo các môi trường làm việc độc lập với lịch sử trò chuyện và cơ sở kiến thức riêng.</label><label data-choice="Tự động gửi email thông báo cho khách hàng về các cập nhật mới của Anthropic."><input type="radio" name="quiz-05_Introduction-to-projects-medium-0" value="1"> Tự động gửi email thông báo cho khách hàng về các cập nhật mới của Anthropic.</label><label data-choice="Thay thế hoàn toàn nhu cầu sử dụng API cho các nhà phát triển phần mềm."><input type="radio" name="quiz-05_Introduction-to-projects-medium-0" value="2"> Thay thế hoàn toàn nhu cầu sử dụng API cho các nhà phát triển phần mềm.</label><label data-choice="Chỉ dùng để lưu trữ các tệp tin PDF mà không cần tương tác với mô hình AI."><input type="radio" name="quiz-05_Introduction-to-projects-medium-0" value="3"> Chỉ dùng để lưu trữ các tệp tin PDF mà không cần tương tác với mô hình AI.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Dự án cho phép người dùng tổ chức các luồng công việc cụ thể bằng cách tách biệt ngữ cảnh, tài liệu và chỉ dẫn cho từng mục tiêu khác nhau.</div>
</div><div class="qitem" data-correct="5 dự án">
<p class="qtext"><strong>2.</strong> Đối với người dùng tài khoản Claude miễn phí, số lượng dự án tối đa có thể tạo là bao nhiêu?</p>
<div class="qchoices"><label data-choice="5 dự án"><input type="radio" name="quiz-05_Introduction-to-projects-medium-1" value="0"> 5 dự án</label><label data-choice="1 dự án"><input type="radio" name="quiz-05_Introduction-to-projects-medium-1" value="1"> 1 dự án</label><label data-choice="10 dự án"><input type="radio" name="quiz-05_Introduction-to-projects-medium-1" value="2"> 10 dự án</label><label data-choice="Không giới hạn số lượng"><input type="radio" name="quiz-05_Introduction-to-projects-medium-1" value="3"> Không giới hạn số lượng</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Theo tài liệu hỗ trợ, người dùng miễn phí được giới hạn tạo tối đa 5 dự án.</div>
</div><div class="qitem" data-correct="Tự động kích hoạt chế độ RAG (Retrieval Augmented Generation) để mở rộng dung lượng.">
<p class="qtext"><strong>3.</strong> Khi kiến thức trong một dự án tiến gần đến giới hạn cửa sổ ngữ cảnh, Claude sẽ thực hiện hành động gì?</p>
<div class="qchoices"><label data-choice="Tự động kích hoạt chế độ RAG (Retrieval Augmented Generation) để mở rộng dung lượng."><input type="radio" name="quiz-05_Introduction-to-projects-medium-2" value="0"> Tự động kích hoạt chế độ RAG (Retrieval Augmented Generation) để mở rộng dung lượng.</label><label data-choice="Yêu cầu người dùng nâng cấp lên gói Enterprise ngay lập tức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-2" value="1"> Yêu cầu người dùng nâng cấp lên gói Enterprise ngay lập tức.</label><label data-choice="Xóa bớt các tệp tin cũ nhất trong cơ sở kiến thức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-2" value="2"> Xóa bớt các tệp tin cũ nhất trong cơ sở kiến thức.</label><label data-choice="Ngừng phản hồi cho đến khi người dùng tạo dự án mới."><input type="radio" name="quiz-05_Introduction-to-projects-medium-2" value="3"> Ngừng phản hồi cho đến khi người dùng tạo dự án mới.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Chế độ RAG giúp Claude tìm kiếm thông tin liên quan từ cơ sở kiến thức thay vì tải toàn bộ tài liệu vào bộ nhớ cùng lúc.</div>
</div><div class="qitem" data-correct="Xem nội dung dự án, truy cập kiến thức và trò chuyện nhưng không thể thay đổi cài đặt.">
<p class="qtext"><strong>4.</strong> Trong một tổ chức sử dụng gói Team hoặc Enterprise, quyền &#x27;Có thể xem&#x27; (Can view) cho phép thành viên làm gì?</p>
<div class="qchoices"><label data-choice="Xem nội dung dự án, truy cập kiến thức và trò chuyện nhưng không thể thay đổi cài đặt."><input type="radio" name="quiz-05_Introduction-to-projects-medium-3" value="0"> Xem nội dung dự án, truy cập kiến thức và trò chuyện nhưng không thể thay đổi cài đặt.</label><label data-choice="Sửa đổi chỉ dẫn dự án và cập nhật cơ sở kiến thức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-3" value="1"> Sửa đổi chỉ dẫn dự án và cập nhật cơ sở kiến thức.</label><label data-choice="Xóa dự án và quản lý quyền truy cập của các thành viên khác."><input type="radio" name="quiz-05_Introduction-to-projects-medium-3" value="2"> Xóa dự án và quản lý quyền truy cập của các thành viên khác.</label><label data-choice="Chỉ có thể nhìn thấy tên dự án mà không được đọc các tài liệu bên trong."><input type="radio" name="quiz-05_Introduction-to-projects-medium-3" value="3"> Chỉ có thể nhìn thấy tên dự án mà không được đọc các tài liệu bên trong.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Quyền này tương đương với quyền truy cập &#x27;chỉ đọc&#x27; kết hợp với khả năng thảo luận trong dự án.</div>
</div><div class="qitem" data-correct="Tên và phần mô tả (description) của dự án.">
<p class="qtext"><strong>5.</strong> Dữ liệu nào sau đây Claude sẽ KHÔNG thể xem được khi bạn thiết lập dự án?</p>
<div class="qchoices"><label data-choice="Tên và phần mô tả (description) của dự án."><input type="radio" name="quiz-05_Introduction-to-projects-medium-4" value="0"> Tên và phần mô tả (description) của dự án.</label><label data-choice="Các tệp tin PDF được tải lên cơ sở kiến thức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-4" value="1"> Các tệp tin PDF được tải lên cơ sở kiến thức.</label><label data-choice="Các đoạn mã (code snippets) được dán vào phần kiến thức dự án."><input type="radio" name="quiz-05_Introduction-to-projects-medium-4" value="2"> Các đoạn mã (code snippets) được dán vào phần kiến thức dự án.</label><label data-choice="Nội dung trong mục &#x27;Chỉ dẫn dự án&#x27; (Project instructions)."><input type="radio" name="quiz-05_Introduction-to-projects-medium-4" value="3"> Nội dung trong mục &#x27;Chỉ dẫn dự án&#x27; (Project instructions).</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Theo hướng dẫn, Claude không có quyền truy cập vào các chi tiết định danh này mà chỉ dựa vào chỉ dẫn và kiến thức tải lên.</div>
</div><div class="qitem" data-correct="Phải hủy lưu trữ (unarchive) dự án đó trước khi tùy chọn xóa xuất hiện.">
<p class="qtext"><strong>6.</strong> Làm thế nào để xóa hoàn toàn một dự án đã được đưa vào kho lưu trữ (archived)?</p>
<div class="qchoices"><label data-choice="Phải hủy lưu trữ (unarchive) dự án đó trước khi tùy chọn xóa xuất hiện."><input type="radio" name="quiz-05_Introduction-to-projects-medium-5" value="0"> Phải hủy lưu trữ (unarchive) dự án đó trước khi tùy chọn xóa xuất hiện.</label><label data-choice="Nhấp vào dấu ba chấm tại mục &#x27;Dự án đã lưu trữ&#x27; và chọn &#x27;Xóa vĩnh viễn&#x27;."><input type="radio" name="quiz-05_Introduction-to-projects-medium-5" value="1"> Nhấp vào dấu ba chấm tại mục &#x27;Dự án đã lưu trữ&#x27; và chọn &#x27;Xóa vĩnh viễn&#x27;.</label><label data-choice="Dự án đã lưu trữ sẽ tự động bị xóa sau 30 ngày."><input type="radio" name="quiz-05_Introduction-to-projects-medium-5" value="2"> Dự án đã lưu trữ sẽ tự động bị xóa sau 30 ngày.</label><label data-choice="Chỉ quản trị viên hệ thống mới có quyền xóa các dự án đã lưu trữ."><input type="radio" name="quiz-05_Introduction-to-projects-medium-5" value="3"> Chỉ quản trị viên hệ thống mới có quyền xóa các dự án đã lưu trữ.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Hệ thống hiện tại không cho phép xóa trực tiếp từ trạng thái lưu trữ để tránh mất dữ liệu ngoài ý muốn.</div>
</div><div class="qitem" data-correct="Tệp trong cơ sở kiến thức sẽ được chia sẻ cho tất cả các cuộc trò chuyện trong dự án đó.">
<p class="qtext"><strong>7.</strong> Điểm khác biệt chính giữa việc tải tệp lên cơ sở kiến thức dự án và tải tệp trực tiếp vào một cuộc trò chuyện là gì?</p>
<div class="qchoices"><label data-choice="Tệp trong cơ sở kiến thức sẽ được chia sẻ cho tất cả các cuộc trò chuyện trong dự án đó."><input type="radio" name="quiz-05_Introduction-to-projects-medium-6" value="0"> Tệp trong cơ sở kiến thức sẽ được chia sẻ cho tất cả các cuộc trò chuyện trong dự án đó.</label><label data-choice="Tệp tải lên cuộc trò chuyện sẽ có dung lượng lớn hơn tệp trong cơ sở kiến thức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-6" value="1"> Tệp tải lên cuộc trò chuyện sẽ có dung lượng lớn hơn tệp trong cơ sở kiến thức.</label><label data-choice="Claude chỉ có thể đọc được các tệp văn bản nếu chúng nằm trong cơ sở kiến thức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-6" value="2"> Claude chỉ có thể đọc được các tệp văn bản nếu chúng nằm trong cơ sở kiến thức.</label><label data-choice="Tệp trong cuộc trò chuyện sẽ tự động được thêm vào cơ sở kiến thức sau khi trò chuyện kết thúc."><input type="radio" name="quiz-05_Introduction-to-projects-medium-6" value="3"> Tệp trong cuộc trò chuyện sẽ tự động được thêm vào cơ sở kiến thức sau khi trò chuyện kết thúc.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Cơ sở kiến thức tạo ra một nguồn tài liệu chung giúp duy trì sự nhất quán trên nhiều cuộc hội thoại khác nhau.</div>
</div><div class="qitem" data-correct="Claude duy trì các bản tóm tắt bộ nhớ riêng biệt cho từng dự án cá nhân.">
<p class="qtext"><strong>8.</strong> Tính năng &#x27;Bộ nhớ&#x27; (Memory) hoạt động như thế nào trong môi trường Dự án của Claude?</p>
<div class="qchoices"><label data-choice="Claude duy trì các bản tóm tắt bộ nhớ riêng biệt cho từng dự án cá nhân."><input type="radio" name="quiz-05_Introduction-to-projects-medium-7" value="0"> Claude duy trì các bản tóm tắt bộ nhớ riêng biệt cho từng dự án cá nhân.</label><label data-choice="Tất cả kiến thức từ mọi dự án đều được gộp chung vào một bộ nhớ duy nhất để Claude thông minh hơn."><input type="radio" name="quiz-05_Introduction-to-projects-medium-7" value="1"> Tất cả kiến thức từ mọi dự án đều được gộp chung vào một bộ nhớ duy nhất để Claude thông minh hơn.</label><label data-choice="Dự án không sử dụng tính năng bộ nhớ để đảm bảo tính bảo mật tuyệt đối."><input type="radio" name="quiz-05_Introduction-to-projects-medium-7" value="2"> Dự án không sử dụng tính năng bộ nhớ để đảm bảo tính bảo mật tuyệt đối.</label><label data-choice="Bộ nhớ chỉ hoạt động nếu dự án được đặt ở chế độ &#x27;Công khai cho toàn tổ chức&#x27;."><input type="radio" name="quiz-05_Introduction-to-projects-medium-7" value="3"> Bộ nhớ chỉ hoạt động nếu dự án được đặt ở chế độ &#x27;Công khai cho toàn tổ chức&#x27;.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Điều này giúp đảm bảo rằng thông tin từ một dự án chuyên biệt không làm nhiễu ngữ cảnh của các dự án khác hoặc hội thoại chung.</div>
</div><div class="qitem" data-correct="Để quy định tông giọng, mức độ chuyên môn và phong cách phản hồi nhất quán cho mọi hội thoại.">
<p class="qtext"><strong>9.</strong> Mục đích của việc đặt &#x27;Chỉ dẫn dự án&#x27; (Project instructions) là gì?</p>
<div class="qchoices"><label data-choice="Để quy định tông giọng, mức độ chuyên môn và phong cách phản hồi nhất quán cho mọi hội thoại."><input type="radio" name="quiz-05_Introduction-to-projects-medium-8" value="0"> Để quy định tông giọng, mức độ chuyên môn và phong cách phản hồi nhất quán cho mọi hội thoại.</label><label data-choice="Để hạn chế số lượng câu hỏi mà các thành viên trong nhóm có thể đặt ra."><input type="radio" name="quiz-05_Introduction-to-projects-medium-8" value="1"> Để hạn chế số lượng câu hỏi mà các thành viên trong nhóm có thể đặt ra.</label><label data-choice="Để tự động dịch tất cả các tài liệu tải lên sang một ngôn ngữ khác."><input type="radio" name="quiz-05_Introduction-to-projects-medium-8" value="2"> Để tự động dịch tất cả các tài liệu tải lên sang một ngôn ngữ khác.</label><label data-choice="Để liệt kê danh sách email của các thành viên cần được mời vào dự án."><input type="radio" name="quiz-05_Introduction-to-projects-medium-8" value="3"> Để liệt kê danh sách email của các thành viên cần được mời vào dự án.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Chỉ dẫn giúp &#x27;lập trình&#x27; cách Claude hành xử, đảm bảo mọi câu trả lời đều tuân thủ các quy tắc đã đặt ra cho dự án đó.</div>
</div><div class="qitem" data-correct="Gắn dấu sao (Starring) dự án.">
<p class="qtext"><strong>10.</strong> Để truy cập nhanh một dự án từ thanh bên trái của tài khoản, bạn nên sử dụng tính năng nào?</p>
<div class="qchoices"><label data-choice="Gắn dấu sao (Starring) dự án."><input type="radio" name="quiz-05_Introduction-to-projects-medium-9" value="0"> Gắn dấu sao (Starring) dự án.</label><label data-choice="Đổi tên dự án thành chữ in hoa."><input type="radio" name="quiz-05_Introduction-to-projects-medium-9" value="1"> Đổi tên dự án thành chữ in hoa.</label><label data-choice="Di chuyển dự án vào mục &#x27;Lưu trữ&#x27; (Archive)."><input type="radio" name="quiz-05_Introduction-to-projects-medium-9" value="2"> Di chuyển dự án vào mục &#x27;Lưu trữ&#x27; (Archive).</label><label data-choice="Chia sẻ dự án với tất cả mọi người trong tổ chức."><input type="radio" name="quiz-05_Introduction-to-projects-medium-9" value="3"> Chia sẻ dự án với tất cả mọi người trong tổ chức.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Gắn dấu sao giúp đưa dự án lên vị trí dễ tìm thấy trong danh sách dự án và trò chuyện ở thanh bên.</div>
</div></div><div class="quiz-panel" data-level="hard" style="display:none"><div class="qitem" data-correct="Hệ thống kích hoạt chế độ RAG (Truy xuất tạo tăng cường) để tìm kiếm thông tin có liên quan thay vì tải toàn bộ nội dung.">
<p class="qtext"><strong>1.</strong> Khi một dự án trong Claude đạt đến giới hạn cửa sổ ngữ cảnh của mô hình, cơ chế nào sau đây sẽ được kích hoạt tự động để duy trì hiệu suất?</p>
<div class="qchoices"><label data-choice="Mô hình sẽ tự động nén các tệp cũ nhất trong cơ sở kiến thức để nhường chỗ cho dữ liệu mới."><input type="radio" name="quiz-05_Introduction-to-projects-hard-0" value="0"> Mô hình sẽ tự động nén các tệp cũ nhất trong cơ sở kiến thức để nhường chỗ cho dữ liệu mới.</label><label data-choice="Hệ thống kích hoạt chế độ RAG (Truy xuất tạo tăng cường) để tìm kiếm thông tin có liên quan thay vì tải toàn bộ nội dung."><input type="radio" name="quiz-05_Introduction-to-projects-hard-0" value="1"> Hệ thống kích hoạt chế độ RAG (Truy xuất tạo tăng cường) để tìm kiếm thông tin có liên quan thay vì tải toàn bộ nội dung.</label><label data-choice="Claude sẽ yêu cầu người dùng xóa bớt các đoạn hội thoại cũ để giải phóng bộ nhớ đệm cho dự án."><input type="radio" name="quiz-05_Introduction-to-projects-hard-0" value="2"> Claude sẽ yêu cầu người dùng xóa bớt các đoạn hội thoại cũ để giải phóng bộ nhớ đệm cho dự án.</label><label data-choice="Dự án sẽ tạm dừng khả năng đọc tệp và chỉ dựa vào dữ liệu huấn luyện sẵn có của mô hình."><input type="radio" name="quiz-05_Introduction-to-projects-hard-0" value="3"> Dự án sẽ tạm dừng khả năng đọc tệp và chỉ dựa vào dữ liệu huấn luyện sẵn có của mô hình.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Cơ chế này cho phép Claude xử lý lượng nội dung gấp $10x$ bằng cách chỉ truy xuất những phần dữ liệu cần thiết nhất cho mỗi câu hỏi.</div>
</div><div class="qitem" data-correct="Tất cả các quyền chia sẻ sẽ được đặt lại về chế độ riêng tư vì lý do bảo mật.">
<p class="qtext"><strong>2.</strong> Điều gì sẽ xảy ra với các tùy chọn chia sẻ và quyền truy cập khi một dự án được chuyển vào kho lưu trữ (Archive)?</p>
<div class="qchoices"><label data-choice="Các thành viên có quyền &#x27;Can edit&#x27; vẫn có thể tiếp tục thay đổi hướng dẫn dự án nhưng không thể thêm tệp mới."><input type="radio" name="quiz-05_Introduction-to-projects-hard-1" value="0"> Các thành viên có quyền &#x27;Can edit&#x27; vẫn có thể tiếp tục thay đổi hướng dẫn dự án nhưng không thể thêm tệp mới.</label><label data-choice="Tất cả các quyền chia sẻ sẽ được đặt lại về chế độ riêng tư vì lý do bảo mật."><input type="radio" name="quiz-05_Introduction-to-projects-hard-1" value="1"> Tất cả các quyền chia sẻ sẽ được đặt lại về chế độ riêng tư vì lý do bảo mật.</label><label data-choice="Dự án vẫn giữ nguyên các quyền truy cập hiện tại nhưng chỉ ở chế độ &#x27;Read-only&#x27;."><input type="radio" name="quiz-05_Introduction-to-projects-hard-1" value="2"> Dự án vẫn giữ nguyên các quyền truy cập hiện tại nhưng chỉ ở chế độ &#x27;Read-only&#x27;.</label><label data-choice="Dự án sẽ tự động hiển thị cho toàn bộ tổ chức để bất kỳ ai cũng có thể tham khảo trong tương lai."><input type="radio" name="quiz-05_Introduction-to-projects-hard-1" value="3"> Dự án sẽ tự động hiển thị cho toàn bộ tổ chức để bất kỳ ai cũng có thể tham khảo trong tương lai.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Đây là một biện pháp an toàn của Anthropic để đảm bảo rằng thông tin cũ không bị truy cập ngoài ý muốn sau khi dự án không còn hoạt động.</div>
</div><div class="qitem" data-correct="Người có quyền &#x27;Can edit&#x27; có khả năng sửa đổi hướng dẫn dự án và cập nhật cơ sở kiến thức, trong khi &#x27;Can view&#x27; thì không.">
<p class="qtext"><strong>3.</strong> Trong gói Claude for Work, sự khác biệt cốt lõi giữa quyền &#x27;Can view&#x27; và &#x27;Can edit&#x27; trong một dự án là gì?</p>
<div class="qchoices"><label data-choice="Người có quyền &#x27;Can view&#x27; chỉ thấy được tên dự án mà không thể đọc được nội dung các tệp đã tải lên."><input type="radio" name="quiz-05_Introduction-to-projects-hard-2" value="0"> Người có quyền &#x27;Can view&#x27; chỉ thấy được tên dự án mà không thể đọc được nội dung các tệp đã tải lên.</label><label data-choice="Người có quyền &#x27;Can edit&#x27; có khả năng sửa đổi hướng dẫn dự án và cập nhật cơ sở kiến thức, trong khi &#x27;Can view&#x27; thì không."><input type="radio" name="quiz-05_Introduction-to-projects-hard-2" value="1"> Người có quyền &#x27;Can edit&#x27; có khả năng sửa đổi hướng dẫn dự án và cập nhật cơ sở kiến thức, trong khi &#x27;Can view&#x27; thì không.</label><label data-choice="Quyền &#x27;Can view&#x27; cho phép tạo cuộc trò chuyện mới nhưng không cho phép xem các cuộc trò chuyện công khai của người khác."><input type="radio" name="quiz-05_Introduction-to-projects-hard-2" value="2"> Quyền &#x27;Can view&#x27; cho phép tạo cuộc trò chuyện mới nhưng không cho phép xem các cuộc trò chuyện công khai của người khác.</label><label data-choice="Chỉ những người có quyền &#x27;Can edit&#x27; mới có thể sử dụng các Artifacts được tạo ra trong dự án."><input type="radio" name="quiz-05_Introduction-to-projects-hard-2" value="3"> Chỉ những người có quyền &#x27;Can edit&#x27; mới có thể sử dụng các Artifacts được tạo ra trong dự án.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Quyền chỉnh sửa bao gồm khả năng quản lý các thành phần cốt lõi tạo nên ngữ cảnh của dự án đó.</div>
</div><div class="qitem" data-correct="Phải khôi phục (unarchive) dự án đó trở lại trạng thái hoạt động trước khi tùy chọn xóa xuất hiện.">
<p class="qtext"><strong>4.</strong> Để xóa hoàn toàn một dự án đã được lưu trữ (archived), người dùng phải thực hiện bước chuẩn bị nào?</p>
<div class="qchoices"><label data-choice="Phải xóa tất cả các tệp trong cơ sở kiến thức của dự án đó trước."><input type="radio" name="quiz-05_Introduction-to-projects-hard-3" value="0"> Phải xóa tất cả các tệp trong cơ sở kiến thức của dự án đó trước.</label><label data-choice="Phải khôi phục (unarchive) dự án đó trở lại trạng thái hoạt động trước khi tùy chọn xóa xuất hiện."><input type="radio" name="quiz-05_Introduction-to-projects-hard-3" value="1"> Phải khôi phục (unarchive) dự án đó trở lại trạng thái hoạt động trước khi tùy chọn xóa xuất hiện.</label><label data-choice="Phải đợi ít nhất $30$ ngày kể từ thời điểm đưa vào kho lưu trữ."><input type="radio" name="quiz-05_Introduction-to-projects-hard-3" value="2"> Phải đợi ít nhất $30$ ngày kể từ thời điểm đưa vào kho lưu trữ.</label><label data-choice="Phải chuyển tất cả các cuộc trò chuyện hiện có ra khỏi dự án đó."><input type="radio" name="quiz-05_Introduction-to-projects-hard-3" value="3"> Phải chuyển tất cả các cuộc trò chuyện hiện có ra khỏi dự án đó.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Hệ thống hiện tại không cho phép xóa trực tiếp từ kho lưu trữ để tránh việc vô tình mất dữ liệu quan trọng.</div>
</div><div class="qitem" data-correct="Người dùng phải đưa thông tin hoặc tài liệu đó vào phần &#x27;Project Knowledge&#x27; (Kiến thức dự án).">
<p class="qtext"><strong>5.</strong> Làm thế nào để đảm bảo thông tin từ một cuộc trò chuyện này được Claude tham chiếu trong một cuộc trò chuyện khác trong cùng một dự án?</p>
<div class="qchoices"><label data-choice="Thông tin sẽ tự động được chia sẻ giữa các cuộc trò chuyện trong cùng một dự án mà không cần thao tác gì thêm."><input type="radio" name="quiz-05_Introduction-to-projects-hard-4" value="0"> Thông tin sẽ tự động được chia sẻ giữa các cuộc trò chuyện trong cùng một dự án mà không cần thao tác gì thêm.</label><label data-choice="Người dùng phải đưa thông tin hoặc tài liệu đó vào phần &#x27;Project Knowledge&#x27; (Kiến thức dự án)."><input type="radio" name="quiz-05_Introduction-to-projects-hard-4" value="1"> Người dùng phải đưa thông tin hoặc tài liệu đó vào phần &#x27;Project Knowledge&#x27; (Kiến thức dự án).</label><label data-choice="Người dùng cần &#x27;Star&#x27; (đánh dấu sao) cuộc trò chuyện chứa thông tin quan trọng."><input type="radio" name="quiz-05_Introduction-to-projects-hard-4" value="2"> Người dùng cần &#x27;Star&#x27; (đánh dấu sao) cuộc trò chuyện chứa thông tin quan trọng.</label><label data-choice="Sử dụng tính năng &#x27;Global Memory&#x27; để đồng bộ hóa mọi dữ liệu dự án vào bộ nhớ chính của Claude."><input type="radio" name="quiz-05_Introduction-to-projects-hard-4" value="3"> Sử dụng tính năng &#x27;Global Memory&#x27; để đồng bộ hóa mọi dữ liệu dự án vào bộ nhớ chính của Claude.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Cơ sở kiến thức dự án đóng vai trò là kho lưu trữ chung được Claude tham chiếu trong mọi cuộc hội thoại thuộc dự án đó.</div>
</div><div class="qitem" data-correct="Chúng cung cấp ngữ cảnh về vai trò, giọng điệu và yêu cầu cụ thể mà Claude sẽ áp dụng cho mọi cuộc chat trong dự án đó.">
<p class="qtext"><strong>6.</strong> Tính năng &#x27;Project Instructions&#x27; (Hướng dẫn dự án) có tác động như thế nào đến phản hồi của Claude?</p>
<div class="qchoices"><label data-choice="Chúng ghi đè hoàn toàn lên mọi phong cách phản hồi mà người dùng đã chọn trong cài đặt cá nhân."><input type="radio" name="quiz-05_Introduction-to-projects-hard-5" value="0"> Chúng ghi đè hoàn toàn lên mọi phong cách phản hồi mà người dùng đã chọn trong cài đặt cá nhân.</label><label data-choice="Chúng cung cấp ngữ cảnh về vai trò, giọng điệu và yêu cầu cụ thể mà Claude sẽ áp dụng cho mọi cuộc chat trong dự án đó."><input type="radio" name="quiz-05_Introduction-to-projects-hard-5" value="1"> Chúng cung cấp ngữ cảnh về vai trò, giọng điệu và yêu cầu cụ thể mà Claude sẽ áp dụng cho mọi cuộc chat trong dự án đó.</label><label data-choice="Chúng chỉ có tác dụng khi người dùng nhắc lại tiêu đề của hướng dẫn trong cửa sổ chat."><input type="radio" name="quiz-05_Introduction-to-projects-hard-5" value="2"> Chúng chỉ có tác dụng khi người dùng nhắc lại tiêu đề của hướng dẫn trong cửa sổ chat.</label><label data-choice="Chúng giới hạn Claude chỉ được trả lời các câu hỏi dựa trên các tệp đã tải lên."><input type="radio" name="quiz-05_Introduction-to-projects-hard-5" value="3"> Chúng giới hạn Claude chỉ được trả lời các câu hỏi dựa trên các tệp đã tải lên.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Đây là cách hiệu quả để thiết lập &#x27;tính cách&#x27; hoặc quy trình làm việc chuẩn cho một dự án cụ thể mà không cần lặp lại yêu cầu.</div>
</div><div class="qitem" data-correct="$5$">
<p class="qtext"><strong>7.</strong> Đối với người dùng tài khoản Claude miễn phí, giới hạn tối đa số lượng dự án có thể tạo là bao nhiêu?</p>
<div class="qchoices"><label data-choice="$1$"><input type="radio" name="quiz-05_Introduction-to-projects-hard-6" value="0"> $1$</label><label data-choice="$3$"><input type="radio" name="quiz-05_Introduction-to-projects-hard-6" value="1"> $3$</label><label data-choice="$5$"><input type="radio" name="quiz-05_Introduction-to-projects-hard-6" value="2"> $5$</label><label data-choice="Không giới hạn số lượng dự án."><input type="radio" name="quiz-05_Introduction-to-projects-hard-6" value="3"> Không giới hạn số lượng dự án.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Theo tài liệu hướng dẫn, người dùng miễn phí được phép tạo tối đa $5$ dự án để tổ chức công việc của mình.</div>
</div><div class="qitem" data-correct="Nó cho phép người dùng kiểm soát những gì được đưa vào bản tóm tắt bộ nhớ riêng biệt của dự án đó.">
<p class="qtext"><strong>8.</strong> Việc di chuyển một cuộc trò chuyện từ bên ngoài vào trong một dự án có lợi ích gì trong việc quản lý bộ nhớ (Memory) của Claude?</p>
<div class="qchoices"><label data-choice="Nó giúp gộp tất cả lịch sử trò chuyện vào một bản tóm tắt bộ nhớ duy nhất cho toàn bộ tài khoản."><input type="radio" name="quiz-05_Introduction-to-projects-hard-7" value="0"> Nó giúp gộp tất cả lịch sử trò chuyện vào một bản tóm tắt bộ nhớ duy nhất cho toàn bộ tài khoản.</label><label data-choice="Nó cho phép người dùng kiểm soát những gì được đưa vào bản tóm tắt bộ nhớ riêng biệt của dự án đó."><input type="radio" name="quiz-05_Introduction-to-projects-hard-7" value="1"> Nó cho phép người dùng kiểm soát những gì được đưa vào bản tóm tắt bộ nhớ riêng biệt của dự án đó.</label><label data-choice="Nó sẽ tự động xóa các phần thông tin không liên quan khỏi bộ nhớ của Claude để tiết kiệm dung lượng."><input type="radio" name="quiz-05_Introduction-to-projects-hard-7" value="2"> Nó sẽ tự động xóa các phần thông tin không liên quan khỏi bộ nhớ của Claude để tiết kiệm dung lượng.</label><label data-choice="Nó làm cho cuộc trò chuyện đó biến mất khỏi lịch sử chat chung để tăng tính bảo mật."><input type="radio" name="quiz-05_Introduction-to-projects-hard-7" value="3"> Nó làm cho cuộc trò chuyện đó biến mất khỏi lịch sử chat chung để tăng tính bảo mật.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Việc di chuyển chat giúp phân loại thông tin, đảm bảo bộ nhớ của dự án chỉ chứa những dữ liệu liên quan đến mục tiêu của dự án đó.</div>
</div><div class="qitem" data-correct="Vì Claude sử dụng tên tệp như một phần gợi ý để hiểu nội dung và truy xuất thông tin chính xác hơn.">
<p class="qtext"><strong>9.</strong> Tại sao việc đặt tên tệp một cách mô tả (ví dụ: &#x27;Bao-cao-ban-hang-Q3-2025.pdf&#x27;) lại được khuyến nghị khi xây dựng cơ sở kiến thức dự án?</p>
<div class="qchoices"><label data-choice="Vì Claude sử dụng tên tệp như một phần gợi ý để hiểu nội dung và truy xuất thông tin chính xác hơn."><input type="radio" name="quiz-05_Introduction-to-projects-hard-8" value="0"> Vì Claude sử dụng tên tệp như một phần gợi ý để hiểu nội dung và truy xuất thông tin chính xác hơn.</label><label data-choice="Vì hệ thống không cho phép tải lên các tệp có tên chứa ký tự số hoặc ký hiệu đặc biệt."><input type="radio" name="quiz-05_Introduction-to-projects-hard-8" value="1"> Vì hệ thống không cho phép tải lên các tệp có tên chứa ký tự số hoặc ký hiệu đặc biệt.</label><label data-choice="Vì tên tệp dài sẽ giúp tăng giới hạn cửa sổ ngữ cảnh của dự án một cách nhân tạo."><input type="radio" name="quiz-05_Introduction-to-projects-hard-8" value="2"> Vì tên tệp dài sẽ giúp tăng giới hạn cửa sổ ngữ cảnh của dự án một cách nhân tạo.</label><label data-choice="Vì Claude chỉ có thể đọc nội dung bên trong nếu tên tệp phản ánh đúng tiêu đề chính của tài liệu."><input type="radio" name="quiz-05_Introduction-to-projects-hard-8" value="3"> Vì Claude chỉ có thể đọc nội dung bên trong nếu tên tệp phản ánh đúng tiêu đề chính của tài liệu.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Tên tệp rõ ràng giúp mô hình dễ dàng xác định tài liệu nào chứa câu trả lời tốt nhất cho yêu cầu của người dùng.</div>
</div><div class="qitem" data-correct="Dự án trở nên công khai và có thể được tìm thấy bởi bất kỳ thành viên nào trong tổ chức thông qua tab Team.">
<p class="qtext"><strong>10.</strong> Khi sử dụng dự án cho mục đích cộng tác trong tổ chức, chế độ hiển thị &#x27;Share with your broader organization&#x27; có ý nghĩa gì?</p>
<div class="qchoices"><label data-choice="Mọi người trong công ty đều nhận được thông báo email mời tham gia chỉnh sửa dự án ngay lập tức."><input type="radio" name="quiz-05_Introduction-to-projects-hard-9" value="0"> Mọi người trong công ty đều nhận được thông báo email mời tham gia chỉnh sửa dự án ngay lập tức.</label><label data-choice="Dự án trở nên công khai và có thể được tìm thấy bởi bất kỳ thành viên nào trong tổ chức thông qua tab Team."><input type="radio" name="quiz-05_Introduction-to-projects-hard-9" value="1"> Dự án trở nên công khai và có thể được tìm thấy bởi bất kỳ thành viên nào trong tổ chức thông qua tab Team.</label><label data-choice="Claude sẽ tự động gửi các phản hồi từ dự án này đến các kênh Slack chung của công ty."><input type="radio" name="quiz-05_Introduction-to-projects-hard-9" value="2"> Claude sẽ tự động gửi các phản hồi từ dự án này đến các kênh Slack chung của công ty.</label><label data-choice="Dự án sẽ được công khai trên mạng internet để các đối tác bên ngoài cũng có thể truy cập."><input type="radio" name="quiz-05_Introduction-to-projects-hard-9" value="3"> Dự án sẽ được công khai trên mạng internet để các đối tác bên ngoài cũng có thể truy cập.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Điều này thúc đẩy việc chia sẻ kiến thức và cho phép các đồng nghiệp sử dụng những nguồn lực đã được thiết lập sẵn.</div>
</div></div></div>




## Thẻ học

<div class="fc-deck" id="fc-05_Introduction-to-projects" data-cards="[{&quot;front&quot;: &quot;Claude Projects là gì?&quot;, &quot;back&quot;: &quot;Đây là các môi trường làm việc độc lập có lịch sử chat, cơ sở kiến thức và cài đặt hướng dẫn riêng biệt.&quot;}, {&quot;front&quot;: &quot;Tính năng &#x27;Project knowledge&#x27; trong Claude Projects có chức năng chính là gì?&quot;, &quot;back&quot;: &quot;Cho phép người dùng tải lên các tài liệu liên quan để Claude tham chiếu trong mọi cuộc trò chuyện thuộc dự án đó.&quot;}, {&quot;front&quot;: &quot;Mục đích của việc thiết lập &#x27;Project instructions&#x27; (Hướng dẫn dự án) là gì?&quot;, &quot;back&quot;: &quot;Để tùy chỉnh cách Claude phản hồi, chẳng hạn như quy định tông giọng, phong cách hoặc vai trò cụ thể.&quot;}, {&quot;front&quot;: &quot;Đối với người dùng gói Claude miễn phí, số lượng dự án tối đa có thể tạo là bao nhiêu?&quot;, &quot;back&quot;: &quot;Tối đa 5 dự án.&quot;}, {&quot;front&quot;: &quot;Claude sử dụng công nghệ nào để xử lý các dự án có lượng thông tin lớn vượt quá giới hạn ngữ cảnh?&quot;, &quot;back&quot;: &quot;Công nghệ RAG (Retrieval Augmented Generation - Truy xuất tăng cường tạo).&quot;}, {&quot;front&quot;: &quot;Chế độ RAG giúp mở rộng dung lượng dự án của Claude lên gấp bao nhiêu lần?&quot;, &quot;back&quot;: &quot;Lên tới 10 lần.&quot;}, {&quot;front&quot;: &quot;Claude có thể truy cập trực tiếp vào tên và mô tả (description) của dự án không?&quot;, &quot;back&quot;: &quot;Không, Claude không có quyền truy cập vào các chi tiết này.&quot;}, {&quot;front&quot;: &quot;Quyền &#x27;Can view&#x27; (Có thể xem) trong dự án cho phép thành viên thực hiện những hành động nào?&quot;, &quot;back&quot;: &quot;Xem nội dung, truy cập kiến thức và trò chuyện nhưng không được phép thay đổi cài đặt dự án.&quot;}, {&quot;front&quot;: &quot;Sự khác biệt chính giữa quyền &#x27;Can edit&#x27; và &#x27;Can view&#x27; trong dự án là gì?&quot;, &quot;back&quot;: &quot;Quyền &#x27;Can edit&#x27; cho phép sửa đổi hướng dẫn, cập nhật kiến thức và quản lý thành viên.&quot;}, {&quot;front&quot;: &quot;Trong một dự án, ai là người có quyền quyết định khả năng hiển thị và chia sẻ dự án với tổ chức?&quot;, &quot;back&quot;: &quot;Người tạo dự án (Project Creator).&quot;}, {&quot;front&quot;: &quot;Để thêm tài liệu vào dự án, người dùng cần nhấp vào biểu tượng nào trên trang chính của dự án?&quot;, &quot;back&quot;: &quot;Biểu tượng dấu cộng \&quot;+\&quot; trong menu tệp ở phía bên phải.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để truy cập nhanh vào một dự án cụ thể từ danh sách chat?&quot;, &quot;back&quot;: &quot;Gắn dấu sao (star) cho dự án đó để nó xuất hiện trong mục các mục ưu tiên.&quot;}, {&quot;front&quot;: &quot;Điều gì xảy ra với các quyền chia sẻ khi một dự án được chuyển vào kho lưu trữ (archive)?&quot;, &quot;back&quot;: &quot;Tất cả quyền chia sẻ sẽ bị đặt lại thành riêng tư (private) vì lý do bảo mật.&quot;}, {&quot;front&quot;: &quot;Để xóa một dự án đã được lưu trữ (archived), người dùng phải thực hiện bước trung gian nào?&quot;, &quot;back&quot;: &quot;Phải hủy lưu trữ (unarchive) dự án đó trước khi có thể xóa.&quot;}, {&quot;front&quot;: &quot;Thông tin ngữ cảnh có được chia sẻ giữa các cuộc chat khác nhau trong cùng một dự án không?&quot;, &quot;back&quot;: &quot;Không, trừ khi thông tin đó được thêm trực tiếp vào cơ sở kiến thức (knowledge base) của dự án.&quot;}, {&quot;front&quot;: &quot;Tại sao việc đặt tên tệp mô tả (ví dụ: &#x27;Q4-Brand-Guidelines.pdf&#x27;) lại quan trọng trong dự án?&quot;, &quot;back&quot;: &quot;Giúp Claude hiểu và truy xuất thông tin chính xác hơn từ cơ sở kiến thức.&quot;}, {&quot;front&quot;: &quot;Tính năng &#x27;Memory&#x27; (Bộ nhớ) của Claude quản lý tóm tắt dự án như thế nào?&quot;, &quot;back&quot;: &quot;Claude duy trì các bản tóm tắt bộ nhớ riêng biệt cho từng dự án cá nhân.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để di chuyển một cuộc trò chuyện độc lập vào trong một dự án?&quot;, &quot;back&quot;: &quot;Sử dụng mũi tên thả xuống cạnh tên chat và chọn \&quot;Add to project\&quot;.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể tải lên những loại tệp nào vào cơ sở kiến thức của dự án?&quot;, &quot;back&quot;: &quot;Các tệp PDF, tài liệu (.docx), CSV, tệp văn bản (.txt) hoặc kết nối trực tiếp với Google Drive.&quot;}, {&quot;front&quot;: &quot;Trong môi trường làm việc nhóm, tab nào giúp người dùng tìm thấy các dự án mà người khác đã chia sẻ với họ?&quot;, &quot;back&quot;: &quot;Tab \&quot;Shared with me\&quot; (Được chia sẻ với tôi).&quot;}, {&quot;front&quot;: &quot;Lợi ích của việc tải tài liệu trực tiếp trong cuộc trò chuyện thay vì thêm vào cơ sở kiến thức dự án là gì?&quot;, &quot;back&quot;: &quot;Tài liệu sẽ không làm lộn xộn cơ sở kiến thức chung của toàn bộ dự án.&quot;}, {&quot;front&quot;: &quot;Theo tài liệu, dự án &#x27;Client account hub&#x27; thường chứa những loại tài liệu nào?&quot;, &quot;back&quot;: &quot;Hướng dẫn thương hiệu, các sản phẩm đã bàn giao trước đó và lịch sử giao tiếp của khách hàng.&quot;}, {&quot;front&quot;: &quot;Khóa học &#x27;Claude 101&#x27; trong Anthropic Academy cung cấp điều gì cho người hoàn thành?&quot;, &quot;back&quot;: &quot;Chứng chỉ hoàn thành khóa học.&quot;}, {&quot;front&quot;: &quot;Bản tin &#x27;AI Fluency&#x27; của Anthropic được gửi đến hộp thư người đăng ký với tần suất như thế nào?&quot;, &quot;back&quot;: &quot;Hàng quý ( quarterly).&quot;}, {&quot;front&quot;: &quot;Bốn mô hình chính của Claude được liệt kê trong danh sách &#x27;Models&#x27; là gì?&quot;, &quot;back&quot;: &quot;Opus, Sonnet, Haiku và Mythos preview.&quot;}, {&quot;front&quot;: &quot;Dịch vụ nào của Anthropic được thiết kế cho việc hiện đại hóa mã nguồn (code modernization)?&quot;, &quot;back&quot;: &quot;Claude Code.&quot;}, {&quot;front&quot;: &quot;Nền tảng Claude (Claude Platform) có thể được truy cập thông qua những đối tác đám mây nào?&quot;, &quot;back&quot;: &quot;Amazon Bedrock, Google Cloud&#x27;s Vertex AI và Microsoft Foundry.&quot;}, {&quot;front&quot;: &quot;Một ví dụ về việc sử dụng dự án cho mục tiêu cá nhân là gì?&quot;, &quot;back&quot;: &quot;Theo dõi, phân tích và lập kế hoạch tài chính cá nhân hoặc quản lý cải tạo nhà cửa.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể làm gì để Claude tự động tóm tắt biên bản họp theo một mẫu nhất định trong dự án?&quot;, &quot;back&quot;: &quot;Thiết lập quy trình này trong phần &#x27;Project instructions&#x27; (Hướng dẫn dự án).&quot;}, {&quot;front&quot;: &quot;Tại sao người dùng nên định kỳ xem lại và cập nhật cơ sở kiến thức của dự án?&quot;, &quot;back&quot;: &quot;Để tránh việc Claude đưa ra các phản hồi dựa trên tài liệu đã cũ hoặc lỗi thời.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để di chuyển nhiều cuộc trò chuyện vào dự án cùng một lúc?&quot;, &quot;back&quot;: &quot;Sử dụng tính năng chọn hàng loạt (bulk move) từ trang lịch sử chat.&quot;}, {&quot;front&quot;: &quot;Quyền truy cập dự án &#x27;ReadOnly&#x27; với quyền thảo luận tương ứng với cấp độ quyền nào?&quot;, &quot;back&quot;: &quot;Quyền &#x27;Can view&#x27;.&quot;}, {&quot;front&quot;: &quot;Khi nào người dùng nên cân nhắc tạo một dự án thay vì chỉ chat thông thường?&quot;, &quot;back&quot;: &quot;Khi công việc đang diễn ra liên tục và cần tham chiếu tài liệu nhiều lần.&quot;}, {&quot;front&quot;: &quot;Dự án giúp đội ngũ thương hiệu (brand team) cộng tác như thế nào?&quot;, &quot;back&quot;: &quot;Họ có thể tạo dự án với hướng dẫn về giọng văn để giúp mọi người trong công ty viết đúng phong cách marketing.&quot;}, {&quot;front&quot;: &quot;Tính năng nào cho phép người dùng xem các ghi chú phát hành (release notes) và tài liệu API?&quot;, &quot;back&quot;: &quot;Claude Help Center hoặc Developer docs.&quot;}, {&quot;front&quot;: &quot;Anthropic Academy cung cấp các tài liệu đào tạo từ cấp độ phát triển API đến _____.&quot;, &quot;back&quot;: &quot;Các phương pháp triển khai tốt nhất cho doanh nghiệp (enterprise deployment best practices).&quot;}, {&quot;front&quot;: &quot;Những lĩnh vực giải pháp (Solutions) nào mà Claude hỗ trợ cụ thể?&quot;, &quot;back&quot;: &quot;Dịch vụ tài chính, chính phủ, y tế, khoa học đời sống và các tổ chức phi lợi nhuận.&quot;}, {&quot;front&quot;: &quot;Tài liệu &#x27;Claude&#x27;s Constitution&#x27; đề cập đến nội dung gì?&quot;, &quot;back&quot;: &quot;Các nguyên tắc đạo đức và quy tắc cốt lõi hướng dẫn hành vi của Claude.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể làm gì để Claude tập trung tìm kiếm vào một tài liệu cụ thể khi đặt câu hỏi?&quot;, &quot;back&quot;: &quot;Nhắc tên tài liệu đó trực tiếp trong câu hỏi (ví dụ: &#x27;Dựa trên báo cáo Q3...&#x27;).&quot;}, {&quot;front&quot;: &quot;Hệ thống quản lý bộ nhớ của Claude duy trì sự tách biệt như thế nào giữa các dự án?&quot;, &quot;back&quot;: &quot;Mỗi dự án có một tóm tắt bộ nhớ riêng, tách biệt với các cuộc chat không thuộc dự án.&quot;}, {&quot;front&quot;: &quot;Nếu một cuộc chat không liên quan bị bắt đầu nhầm trong một dự án, người dùng nên làm gì để quản lý bộ nhớ?&quot;, &quot;back&quot;: &quot;Chọn \&quot;Remove from project\&quot; để nó được tính vào tóm tắt bộ nhớ chung.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để người tạo dự án chia sẻ dự án với toàn bộ tổ chức?&quot;, &quot;back&quot;: &quot;Trong cài đặt khả năng hiển thị, chọn \&quot;Share with your broader organization\&quot;.&quot;}, {&quot;front&quot;: &quot;Trong khóa học Claude 101, mục tiêu của việc khảo sát người học là gì?&quot;, &quot;back&quot;: &quot;Để cải thiện các phiên bản khóa học trong tương lai và đảm bảo đáp ứng đa dạng nhu cầu.&quot;}, {&quot;front&quot;: &quot;Mô hình Claude nào được mô tả là phiên bản &#x27;preview&#x27;?&quot;, &quot;back&quot;: &quot;Mythos preview.&quot;}, {&quot;front&quot;: &quot;Những loại vai trò nghề nghiệp nào được liệt kê trong biểu mẫu phản hồi Claude 101?&quot;, &quot;back&quot;: &quot;Nhà giáo dục, sinh viên, chuyên gia công nghệ, chuyên gia kinh doanh, y tế, sáng tạo và chính phủ.&quot;}, {&quot;front&quot;: &quot;Anthropic cam kết điều gì thông qua &#x27;Responsible Scaling Policy&#x27;?&quot;, &quot;back&quot;: &quot;Chính sách mở rộng quy mô có trách nhiệm nhằm đảm bảo an toàn AI.&quot;}, {&quot;front&quot;: &quot;Để bảo mật thông tin cá nhân, Anthropic khuyến cáo người dùng không bao giờ gửi thông tin gì qua Google Forms?&quot;, &quot;back&quot;: &quot;Mật khẩu (passwords).&quot;}, {&quot;front&quot;: &quot;Dự án hỗ trợ việc &#x27;Code modernization&#x27; như thế nào?&quot;, &quot;back&quot;: &quot;Bằng cách tập trung tài liệu kỹ thuật, quy định mã nguồn và hướng dẫn thực thi vào một nơi.&quot;}, {&quot;front&quot;: &quot;Khi chia sẻ dự án qua email, người dùng có thể thêm thành viên bằng cách nào?&quot;, &quot;back&quot;: &quot;Nhập từng tên/email hoặc dán một danh sách email để chia sẻ hàng loạt.&quot;}, {&quot;front&quot;: &quot;Dự án đã lưu trữ (archived) nằm ở vị trí nào trong giao diện?&quot;, &quot;back&quot;: &quot;Ở dưới cùng của danh sách dự án chính hoặc trong tab dự án đã lưu trữ.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể tìm thấy các câu chuyện thành công của khách hàng ở đâu?&quot;, &quot;back&quot;: &quot;Trong phần &#x27;Customer stories&#x27; của mục Resources trên trang web Anthropic.&quot;}, {&quot;front&quot;: &quot;Khóa học &#x27;Claude Code in action&#x27; tập trung vào đối tượng nào?&quot;, &quot;back&quot;: &quot;Các lập trình viên và những người phát triển ứng dụng dựa trên Claude API.&quot;}, {&quot;front&quot;: &quot;Phần &#x27;Regional compliance&#x27; trong Claude Platform đề cập đến vấn đề gì?&quot;, &quot;back&quot;: &quot;Việc tuân thủ các quy định pháp lý tại các khu vực địa lý khác nhau.&quot;}, {&quot;front&quot;: &quot;Dự án giúp việc thiết lập một khóa học giáo dục như thế nào?&quot;, &quot;back&quot;: &quot;Tổ chức tài liệu học tập, sử dụng Claude giải thích khái niệm khó và cải thiện nội dung khóa học theo thời gian.&quot;}, {&quot;front&quot;: &quot;Claude Cowork là sản phẩm nhắm đến mục tiêu gì?&quot;, &quot;back&quot;: &quot;Tổ chức và quản lý các nhiệm vụ công việc thông qua các dự án cộng tác.&quot;}, {&quot;front&quot;: &quot;Khi nào RAG mode được tự động kích hoạt trong dự án?&quot;, &quot;back&quot;: &quot;Khi cơ sở kiến thức của dự án tiến gần đến giới hạn cửa sổ ngữ cảnh.&quot;}, {&quot;front&quot;: &quot;Nếu muốn thay đổi quyền của một thành viên trong dự án, người tạo dự án cần làm gì?&quot;, &quot;back&quot;: &quot;Mở menu chia sẻ, nhấp vào vai trò hiện tại của thành viên đó và chọn vai trò mới.&quot;}, {&quot;front&quot;: &quot;Claude for Chrome và Claude for Slack là ví dụ của loại sản phẩm nào?&quot;, &quot;back&quot;: &quot;Các tiện ích mở rộng (extensions) và tích hợp (integrations) của Claude.&quot;}, {&quot;front&quot;: &quot;Anthropic Academy cung cấp chứng chỉ cho những khóa học nào?&quot;, &quot;back&quot;: &quot;AI Fluency, API development, Model Context Protocol và Claude Code.&quot;}, {&quot;front&quot;: &quot;Trong hướng dẫn dự án, việc chỉ định &#x27;expertise level&#x27; (cấp độ chuyên gia) giúp gì cho Claude?&quot;, &quot;back&quot;: &quot;Giúp Claude điều chỉnh độ phức tạp và chi tiết của câu trả lời phù hợp với người dùng.&quot;}, {&quot;front&quot;: &quot;Dự án &#x27;Event planning workspace&#x27; có thể giúp quản lý những thông tin gì?&quot;, &quot;back&quot;: &quot;Hợp đồng địa điểm, tiểu sử diễn giả, dữ liệu người tham gia và kịch bản chương trình.&quot;}, {&quot;front&quot;: &quot;Tại sao việc đặt tên dự án mang tính mô tả (ví dụ: &#x27;Q4 Marketing Campaign&#x27;) lại hữu ích?&quot;, &quot;back&quot;: &quot;Giúp bạn và đồng đội dễ dàng hiểu được mục đích và phạm vi của dự án đó.&quot;}, {&quot;front&quot;: &quot;Điều gì xảy ra với các cuộc hội thoại trong một dự án sau khi nó bị lưu trữ?&quot;, &quot;back&quot;: &quot;Người dùng vẫn có thể truy cập và xem lại các cuộc hội thoại đó.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để biết một dự án đã được kích hoạt chế độ RAG?&quot;, &quot;back&quot;: &quot;Sẽ có một chỉ báo hình ảnh (visual indicator) xuất hiện trên giao diện dự án.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể thực hiện hành động gì nếu một dự án không còn cần thiết nhưng vẫn muốn giữ dữ liệu tham khảo?&quot;, &quot;back&quot;: &quot;Lưu trữ (Archive) dự án thay vì xóa nó.&quot;}, {&quot;front&quot;: &quot;Hướng dẫn dự án hoạt động song song với những yếu tố cá nhân nào của người dùng?&quot;, &quot;back&quot;: &quot;Tùy chọn cá nhân (user preferences) và phong cách (styles) đã được thiết lập sẵn.&quot;}, {&quot;front&quot;: &quot;Dự án &#x27;Job description generator&#x27; sử dụng những nguồn dữ liệu nào để hỗ trợ tuyển dụng?&quot;, &quot;back&quot;: &quot;Mô tả công việc cũ, hiến chương nhóm và tài liệu yêu cầu nhân sự nội bộ.&quot;}, {&quot;front&quot;: &quot;Để đảm bảo an toàn, các chính sách như &#x27;Usage policy&#x27; và &#x27;Privacy policy&#x27; của Anthropic được đặt ở đâu?&quot;, &quot;back&quot;: &quot;Trong phần &#x27;Terms and policies&#x27; ở chân trang web.&quot;}, {&quot;front&quot;: &quot;Tab &#x27;Team&#x27; trong mục Projects dùng để làm gì?&quot;, &quot;back&quot;: &quot;Để khám phá các dự án được chia sẻ công khai trong toàn bộ tổ chức.&quot;}, {&quot;front&quot;: &quot;Người tạo dự án có thể thu hồi quyền truy cập của một thành viên bằng cách nào?&quot;, &quot;back&quot;: &quot;Vào menu chia sẻ, nhấp vào vai trò của thành viên và chọn \&quot;Remove access\&quot;.&quot;}, {&quot;front&quot;: &quot;Claude hỗ trợ bao nhiêu ngôn ngữ chính trong Help Center (ví dụ)?&quot;, &quot;back&quot;: &quot;Hỗ trợ nhiều ngôn ngữ như Tiếng Anh, Pháp, Đức, Indonesia, Ý, Nhật, Hàn, Bồ Đào Nha, Nga, Trung (Giản thể/Phồn thể) và Tây Ban Nha.&quot;}, {&quot;front&quot;: &quot;Lợi ích của việc kết nối dự án với Google Drive là gì?&quot;, &quot;back&quot;: &quot;Cho phép liên kết và cập nhật tài liệu trực tiếp mà không cần tải lên thủ công nhiều lần.&quot;}, {&quot;front&quot;: &quot;Project Creator có quyền kiểm soát những gì so với Can Edit members?&quot;, &quot;back&quot;: &quot;Project Creator kiểm soát mọi thứ cộng thêm quyền quyết định ai có thể thấy dự án và xóa dự án.&quot;}, {&quot;front&quot;: &quot;Tại sao Claude Projects được gọi là &#x27;self-contained environments&#x27;?&quot;, &quot;back&quot;: &quot;Vì mỗi dự án hoạt động độc lập với kho tri thức và quy tắc riêng, không ảnh hưởng đến các dự án khác.&quot;}, {&quot;front&quot;: &quot;Dự án &#x27;Eco-friendly water bottle&#x27; là ví dụ cho loại dự án nào?&quot;, &quot;back&quot;: &quot;Quản lý quá trình phát triển sản phẩm mới từ ý tưởng đến khi ra mắt.&quot;}, {&quot;front&quot;: &quot;Trong Anthropic Academy, &#x27;AI Fluency&#x27; nhắm đến việc đào tạo điều gì?&quot;, &quot;back&quot;: &quot;Cách mọi người cộng tác và làm việc hiệu quả với AI.&quot;}]" data-cur="0" data-known="[]">
<div class="fc-progress">1 / 76</div>
<div class="fc-scene" onclick="fcFlip(this)"><div class="fc-card-inner"><div class="fc-front">Claude Projects là gì?</div><div class="fc-back">Đây là các môi trường làm việc độc lập có lịch sử chat, cơ sở kiến thức và cài đặt hướng dẫn riêng biệt.</div></div></div>
<p class="fc-hint">Nhấn thẻ để lật · Dùng nút để điều hướng</p>
<div class="fc-nav">
<button onclick="fcMove('fc-05_Introduction-to-projects',-1)">← Trước</button>
<button class="fc-know" onclick="fcKnow('fc-05_Introduction-to-projects',true)">Nhớ rồi ✓</button>
<button class="fc-unknown" onclick="fcKnow('fc-05_Introduction-to-projects',false)">Học lại ✗</button>
<button onclick="fcMove('fc-05_Introduction-to-projects',1)">Tiếp →</button>
</div>
<div class="fc-stats">Nhớ: 0 / 76</div>
</div>




## Sơ đồ tư duy

<div class="mm-wrap">
<div class="markmap" style="width:100%;height:440px">
# Dự án trên Claude (Claude Projects)
## Tổng quan & Tính năng chính
### Môi trường tự chứa (Self-contained)
### Bộ nhớ & Lịch sử chat riêng biệt
### Cơ sở tri thức (Knowledge Base) tùy chỉnh
### Hướng dẫn dự án (Project Instructions)
### Công nghệ RAG (Tự động mở rộng quy mô)
## Quản lý Dự án
### Thiết lập ban đầu
#### Đặt tên & Mô tả
#### Cài đặt quyền riêng tư
### Thao tác quản lý
#### Gắn dấu sao (Starring)
#### Lưu trữ (Archive)
#### Xóa (Delete)
#### Di chuyển hội thoại vào dự án
## Cơ sở tri thức & Hướng dẫn
### Tải lên nội dung
#### Tài liệu (PDF, DOCX, CSV, TXT)
#### Kết nối Google Drive
#### Đoạn mã (Code snippets)
### Nội dung hướng dẫn
#### Xác định vai trò & Chuyên môn
#### Giọng văn & Phong cách phản hồi
#### Quy trình làm việc cụ thể
## Cộng tác (Gói Team/Enterprise)
### Mức độ quyền hạn
#### Can view (Chỉ xem/chat)
#### Can edit (Chỉnh sửa nội dung)
#### Owner (Toàn quyền điều khiển)
### Chia sẻ trong tổ chức
### Tab 'Shared with me'
## Ví dụ ứng dụng
### Ra mắt sản phẩm mới
### Hỗ trợ nghiên cứu & Phân tích
### Phát triển khóa học giáo dục
### Quản lý tài chính cá nhân
### Lập kế hoạch cải tạo nhà
## Hệ sinh thái Anthropic
### Anthropic Academy (Khóa học)
### Claude Platform (API, Dev docs)
### Các dòng mô hình (Opus, Sonnet, Haiku)
</div>
</div>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [https://forms.gle/sY9ou5fqZBd3TjHF8](https://forms.gle/sY9ou5fqZBd3TjHF8)



---
*[Nguồn gốc](https://anthropic.skilljar.com/claude-101/383393){: target="_blank" }*
