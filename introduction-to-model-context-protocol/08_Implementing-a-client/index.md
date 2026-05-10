---
title: "Implementing a client"
parent: Introduction to MCP
nav_order: 8
---

# Implementing a client

details
Implementing a client
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 7 minutes, 26 seconds
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
07:26
07:26
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
Now that we have our MCP server working, it's time to build the client side. The client is what allows our application code to communicate with the MCP server and access its functionality.
Understanding the Client Architecture
In most real-world projects, you'll either implement an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.
The MCP client consists of two main components:
MCP Client
- A custom class we create to make using the session easier
Client Session
- The actual connection to the server (part of the MCP Python SDK)
The client session requires careful resource management - we need to properly clean up connections when we're done. That's why we wrap it in our own class that handles all the cleanup automatically.
How the Client Fits Into Our Application
Remember our application flow diagram? The client is what enables our code to interact with the MCP server at two key points:
Our CLI code uses the client to:
Get a list of available tools to send to Claude
Execute tools when Claude requests them
Implementing Core Client Functions
We need to implement two essential functions:
list_tools()
and
call_tool()
.
List Tools Function
This function gets all available tools from the MCP server:
async def list_tools(self) -> list[types.Tool]:
result = await self.session().list_tools()
return result.tools
It's straightforward - we access our session (the connection to the server), call the built-in
list_tools()
method, and return the tools from the result.
Call Tool Function
This function executes a specific tool on the server:
async def call_tool(
self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
return await self.session().call_tool(tool_name, tool_input)
We pass the tool name and input parameters (provided by Claude) to the server and return the result.
Testing the Client
The client file includes a simple test harness at the bottom. You can run it directly to verify everything works:
uv run mcp_client.py
This will connect to your MCP server and print out the available tools. You should see output showing your tool definitions, including descriptions and input schemas.
Putting It All Together
Once the client functions are implemented, you can test the complete flow by running your main application:
uv run main.py
Try asking: "What is the contents of the report.pdf document?"
Here's what happens behind the scenes:
Your application uses the client to get available tools
These tools are sent to Claude along with your question
Claude decides to use the read_doc_contents tool
Your application uses the client to execute that tool
The result is returned to Claude, who then responds to you
The client acts as the bridge between your application logic and the MCP server's functionality, making it easy to integrate powerful tools into your AI workflows.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/Implementing a client.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296696){: target="_blank" }*
