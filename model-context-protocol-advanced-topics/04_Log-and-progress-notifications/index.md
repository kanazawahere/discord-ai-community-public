---
title: "Log and progress notifications"
parent: MCP Advanced Topics
nav_order: 4
---

# Log and progress notifications

details
Log and progress notifications
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 2 minutes, 41 seconds
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
02:41
02:41
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
Logging and progress notifications are simple to implement but make a huge difference in user experience when working with MCP servers. They help users understand what's happening during long-running operations instead of wondering if something has broken.
When Claude calls a tool that takes time to complete - like researching a topic or processing data - users typically see nothing until the operation finishes. This can be frustrating because they don't know if the tool is working or has stalled.
With logging and progress notifications enabled, users get real-time feedback showing exactly what's happening behind the scenes. They can see progress bars, status messages, and detailed logs as the operation runs.
How It Works
In the Python MCP SDK, logging and progress notifications work through the Context argument that's automatically provided to your tool functions. This context object gives you methods to communicate back to the client during execution.
@mcp.tool(
name="research",
description="Research a given topic"
)
async def research(
topic: str = Field(description="Topic to research"),
*,
context: Context
):
await context.info("About to do research...")
await context.report_progress(20, 100)
sources = await do_research(topic)

await context.info("Writing report...")
await context.report_progress(70, 100)
results = await generate_report(sources)

return results
The key methods you'll use are:
context.info()
- Send log messages to the client
context.report_progress()
- Update progress with current and total values
Client-Side Implementation
On the client side, you need to set up callback functions to handle these notifications. The server emits these messages, but it's up to your client application to decide how to present them to users.
async def logging_callback(params: LoggingMessageNotificationParams):
print(params.data)

async def print_progress_callback(
progress: float, total: float | None, message: str | None
):
if total is not None:
percentage = (progress / total) * 100
print(f"Progress: {progress}/{total} ({percentage:.1f}%)")
else:
print(f"Progress: {progress}")

async def run():
async with stdio_client(server_params) as (read, write):
async with ClientSession(
read,
write,
logging_callback=logging_callback
) as session:
await session.initialize()

await session.call_tool(
name="add",
arguments={"a": 1, "b": 3},
progress_callback=print_progress_callback,
)
You provide the logging callback when creating the client session, and the progress callback when making individual tool calls. This gives you flexibility to handle different types of notifications appropriately.
Presentation Options
How you present these notifications depends on your application type:
CLI applications
- Simply print messages and progress to the terminal
Web applications
- Use WebSockets, server-sent events, or polling to push updates to the browser
Desktop applications
- Update progress bars and status displays in your UI
Remember that implementing these notifications is entirely optional. You can choose to ignore them completely, show only certain types, or present them however makes sense for your application. They're purely user experience enhancements to help users understand what's happening during long-running operations.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/Log and progress notifications.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296284){: target="_blank" }*
