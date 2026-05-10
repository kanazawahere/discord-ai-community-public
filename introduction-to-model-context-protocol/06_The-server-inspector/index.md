---
title: "The server inspector"
parent: Introduction to MCP
nav_order: 6
---

# The server inspector

details
The server inspector
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 3 minutes, 52 seconds
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
03:52
03:52
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.
Starting the Inspector
First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:
mcp dev mcp_server.py
This starts a development server and gives you a local URL, typically something like
http://127.0.0.1:6274
. Open this URL in your browser to access the MCP Inspector.
Using the Inspector Interface
The inspector interface is actively being developed, so it may look different when you use it. However, the core functionality remains consistent. Look for these key elements:
A
Connect
button to start your MCP server
Navigation tabs for
Resources
,
Tools
,
Prompts
, and other features
A tools listing and testing panel
Click the Connect button first to initialize your server. You'll see the connection status change from "Disconnected" to "Connected".
Testing Your Tools
Navigate to the Tools section and click "List Tools" to see all available tools from your server. When you select a tool, the right panel shows its details and input fields.
For example, to test a document reading tool:
Select the
read_doc_contents
tool
Enter a document ID (like "deposition.md")
Click "Run Tool"
Check the results for success and expected output
The inspector shows both the success status and the actual returned data, making it easy to verify your tool works correctly.
Testing Tool Interactions
You can test multiple tools in sequence to verify complex workflows. For instance, after using an edit tool to modify a document, immediately test the read tool to confirm the changes were applied correctly.
The inspector maintains your server state between tool calls, so edits persist and you can verify the complete functionality of your MCP server.
Development Workflow
The MCP Inspector becomes an essential part of your development process. Instead of writing separate test scripts or connecting to full applications, you can:
Quickly iterate on tool implementations
Test edge cases and error conditions
Verify tool interactions and state management
Debug issues in real-time
This immediate feedback loop makes MCP server development much more efficient and helps catch issues early in the development process.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/The server inspector.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296693){: target="_blank" }*
