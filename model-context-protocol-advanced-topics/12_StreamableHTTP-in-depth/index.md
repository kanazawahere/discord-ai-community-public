---
title: "StreamableHTTP in depth"
parent: MCP Advanced Topics
nav_order: 12
---

# StreamableHTTP in depth

details
StreamableHTTP in depth
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 10 minutes, 28 seconds
Volume 90%
Press shift question mark to access a list of keyboard shortcuts
Keyboard Shortcuts
Enabled
Disabled
Shortcuts Open/Close
/ or ?
Play/Pause
SPACE
Increase Volume
↑
Decrease Volume
↓
Seek Forward
→
Seek Backward
←
Captions On/Off
c
Fullscreen/Exit Fullscreen
f
Mute/Unmute
m
Decrease Caption Size
-
Increase Caption Size
+ or =
Seek %
0-9
Subtitle Settings
Off
English
French
German
Japanese
Korean
Portuguese
Spanish
Font Color
White
Font Opacity
100%
Font Size
100%
Font Family
Arial
Character Edge
None
Edge Color
Black
Background Color
Black
Background Opacity
50%
Window Color
Black
Window Opacity
0%
Reset
White
Black
Red
Green
Blue
Yellow
Magenta
Cyan
100%
75%
50%
25%
200%
175%
150%
125%
100%
75%
50%
Arial
Courier
Georgia
Impact
Lucida Console
Tahoma
Times New Roman
Trebuchet MS
Verdana
None
Raised
Depressed
Uniform
Drop Shadow
White
Black
Red
Green
Blue
Yellow
Magenta
Cyan
White
Black
Red
Green
Blue
Yellow
Magenta
Cyan
100%
75%
50%
25%
0%
White
Black
Red
Green
Blue
Yellow
Magenta
Cyan
100%
75%
50%
25%
0%
0.5x
0.75x
1x
1.25x
1.5x
2x
Auto
406p
1080p
720p
406p
270p
180p
Live
00:00
10:28
10:28
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
StreamableHTTP is MCP's solution to a fundamental problem: some MCP functionality requires the server to make requests to the client, but HTTP makes this challenging. Let's explore how StreamableHTTP works around this limitation and when you might need to break that workaround.
The Core Problem
Some MCP features like sampling, notifications, and logging rely on the server initiating requests to the client. However, HTTP is designed for clients to make requests to servers, not the other way around. StreamableHTTP solves this with a clever workaround using Server-Sent Events (SSE).
How StreamableHTTP Works
The magic happens through a multi-step process that establishes persistent connections between client and server.
Initial Connection Setup
The process starts like any MCP connection:
Client sends an
Initialize Request
to the server
Server responds with an
Initialize Result
that includes a special
mcp-session-id
header
Client sends an
Initialized Notification
with the session ID
This session ID is crucial - it uniquely identifies the client and must be included in all future requests.
The SSE Workaround
After initialization, the client can make a GET request to establish a Server-Sent Events connection. This creates a long-lived HTTP response that the server can use to stream messages back to the client at any time.
This SSE connection is the key to allowing server-to-client communication. The server can now send requests, notifications, and other messages through this persistent channel.
Tool Calls and Dual SSE Connections
When the client makes a tool call, things get more complex. The system creates two separate SSE connections:
Primary SSE Connection:
Used for server-initiated requests and stays open indefinitely
Tool-Specific SSE Connection:
Created for each tool call and closes automatically when the tool result is sent
Message Routing
Different types of messages get routed through different connections:
Progress notifications:
Sent through the primary SSE connection
Logging messages and tool results:
Sent through the tool-specific SSE connection
Configuration Flags That Break the Workaround
StreamableHTTP includes two important configuration options:
stateless_http
json_response
Setting these to
True
can break the SSE workaround mechanism. You might want to enable these flags in certain scenarios, but doing so limits the full MCP functionality that depends on server-to-client communication.
Key Takeaways
StreamableHTTP is more complex than other MCP transports because it has to work around HTTP's limitations. The SSE-based workaround enables full MCP functionality over HTTP, but understanding the dual-connection model is crucial for debugging and optimization.
When building MCP applications with StreamableHTTP, remember that session IDs are required for all requests after initialization, and the system automatically manages multiple SSE connections to handle different types of server-to-client communication.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/StreamableHTTP in depth.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296286){: target="_blank" }*
