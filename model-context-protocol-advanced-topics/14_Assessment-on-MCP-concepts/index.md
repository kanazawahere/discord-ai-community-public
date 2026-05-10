---
title: "Assessment on MCP concepts"
parent: MCP Advanced Topics
nav_order: 14
---

# Assessment on MCP concepts

Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
Assessment on MCP Concepts
10 questions
Start

## Quiz

**Câu 1.** Your MCP server needs to use Claude to summarize data, but you don&#x27;t want the server to handle API costs. What feature should you use?

- ○ Roots
- ○ Progress notifications
- ○ Logging
- ○ Sampling

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 2.** Your MCP tool sends a &quot;Call Tool Request&quot; and expects to get back results. What type of message pattern is this?

- ○ Progress message
- ○ Notification message
- ○ Request-result message
- ○ Logging message

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 3.** Your StreamableHTTP server needs to send progress updates to clients, but HTTP doesn&#x27;t normally allow server-initiated requests. How does StreamableHTTP solve this?

- ✅ It creates Server-Sent Events (SSE) connections
- ○ It stores messages in a database
- ○ It uses WebSockets instead
- ○ It switches to stdio transport

**Câu 4.** A user asks Claude to &quot;convert video.mp4&quot; but Claude doesn&#x27;t know where the file is located. What MCP feature helps solve this?

- ✅ Roots
- ○ Progress notifications
- ○ JSON messages
- ○ Sampling

**Câu 5.** You want simpler HTTP responses without streaming, just getting the final result as plain JSON. Which flag should you enable?

- ○ streaming=False
- ○ simple_mode=True
- ○ stateless_http=True
- ○ json_response=True

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 6.** You&#x27;re developing an MCP server locally and want the simplest way to test communication between client and server on the same machine. Which transport should you use?

- ○ HTTP transport
- ○ WebSocket transport
- ○ StreamableHTTP transport
- ○ Stdio transport

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 7.** Which transport method requires both client and server to run on the same machine?

- ○ TCP transport
- ○ Stdio transport
- ○ WebSocket transport
- ○ HTTP transport

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 8.** What are roots in MCP?

- ○ The main configuration files for MCP servers
- ○ Administrative users with full system access
- ○ A system that tells MCP servers what files/folders it can access
- ○ The primary communication endpoints between clients and servers

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 9.** What is the correct sequence for MCP connection initialization?

- ○ Initialized Notification → Initialize Request → Initialize Result
- ○ Initialize Request → Initialized Notification → Initialize Result
- ○ Initialize Result → Initialize Request → Initialized Notification
- ○ Initialize Request → Initialize Result → Initialized Notification

<details><summary>Đáp án</summary>Chưa có đáp án</details>

**Câu 10.** What is sampling in MCP?

- ○ A method for collecting data from multiple sources
- ○ A way for servers to access language models through connected MCP clients
- ○ A process for validating client credentials
- ○ A technique for optimizing server performance

<details><summary>Đáp án</summary>Chưa có đáp án</details>

## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296301){: target="_blank" }*
