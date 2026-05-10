---
title: "MCP clients"
parent: Introduction to MCP
nav_order: 3
---

# MCP clients

details
MCP clients
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 4 minutes, 56 seconds
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
04:56
04:56
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
The MCP client serves as the communication bridge between your server and MCP servers. It's your access point to all the tools that an MCP server provides, handling the message exchange and protocol details so your application doesn't have to.
Transport Agnostic Communication
One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can communicate over different protocols depending on your setup.
The most common setup runs both the MCP client and server on the same machine, communicating through standard input/output. But you can also connect them over:
HTTP
WebSockets
Various other network protocols
MCP Message Types
Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:
ListToolsRequest/ListToolsResult:
The client asks the server "what tools do you provide?" and gets back a list of available tools.
CallToolRequest/CallToolResult:
The client asks the server to run a specific tool with given arguments, then receives the results.
How It All Works Together
Here's a complete example showing how a user query flows through the entire system - from your server, through the MCP client, to external services like GitHub, and back to Claude.
Let's say a user asks "What repositories do I have?" Here's the step-by-step flow:
User Query:
The user submits their question to your server
Tool Discovery:
Your server needs to know what tools are available to send to Claude
List Tools Exchange:
Your server asks the MCP client for available tools
MCP Communication:
The MCP client sends a
ListToolsRequest
to the MCP server and receives a
ListToolsResult
Claude Request:
Your server sends the user's query plus the available tools to Claude
Tool Use Decision:
Claude decides it needs to call a tool to answer the question
Tool Execution Request:
Your server asks the MCP client to run the tool Claude specified
External API Call:
The MCP client sends a
CallToolRequest
to the MCP server, which makes the actual GitHub API call
Results Flow Back:
GitHub responds with repository data, which flows back through the MCP server as a
CallToolResult
Tool Result to Claude:
Your server sends the tool results back to Claude
Final Response:
Claude formulates a final answer using the repository data
User Gets Answer:
Your server delivers Claude's response back to the user
Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on your application logic while still getting access to powerful external tools and data sources.
Understanding this flow is crucial because you'll see all these pieces when building your own MCP clients and servers in the upcoming sections.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/MCP clients.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296690){: target="_blank" }*
