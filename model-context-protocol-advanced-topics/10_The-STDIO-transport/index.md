---
title: "The STDIO transport"
parent: MCP Advanced Topics
nav_order: 10
---

# The STDIO transport

details
The STDIO transport
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 9 minutes, 28 seconds
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
09:28
09:28
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
MCP clients and servers communicate by exchanging JSON messages, but how do these messages actually get transmitted? The communication channel used is called a
transport
, and there are several ways to implement this - from HTTP requests to WebSockets to even writing JSON on a postcard (though that last one isn't recommended for production use).
The Stdio Transport
When you're first developing an MCP server or client, the most commonly used transport is the
stdio transport
. This approach is straightforward: the client launches the MCP server as a subprocess and communicates through standard input and output streams.
Here's how it works:
Client sends messages to the server using the server's
stdin
Server responds by writing to
stdout
Either the server or client can send a message at any time
Only works when client and server run on the same machine
Seeing Stdio in Action
You can actually test an MCP server directly from your terminal without writing a separate client. When you run a server with
uv run server.py
, it listens to stdin and writes responses to stdout. This means you can paste JSON messages directly into your terminal and see the server's responses immediately.
The terminal output shows the complete message exchange, including example messages for initialization and tool calls.
MCP Connection Sequence
Every MCP connection must start with a specific three-message handshake:
Initialize Request
- Client sends this first
Initialize Result
- Server responds with capabilities
Initialized Notification
- Client confirms (no response expected)
Only after this handshake can you send other requests like tool calls or prompt listings.
Message Types and Flow
MCP supports various message types that flow in both directions:
The key insight is that some messages require responses (requests → results) while others don't (notifications). Both client and server can initiate communication at any time.
Four Communication Scenarios
With any transport, you need to handle four different communication patterns:
**Client → Server request**: Client writes to stdin
**Server → Client response**: Server writes to stdout
**Server → Client request**: Server writes to stdout
**Client → Server response**: Client writes to stdin
The beauty of stdio transport is its simplicity - either party can initiate communication at any time using these two channels.
Why This Matters
Understanding stdio transport is crucial because it represents the "ideal" case where bidirectional communication is seamless. When we move to other transports like HTTP, we'll encounter limitations where the server cannot always initiate requests to the client. The stdio transport serves as our baseline for understanding what full MCP communication looks like before we tackle the constraints of other transport methods.
For development and testing, stdio transport is perfect. For production deployments where client and server need to run on different machines, you'll need to consider other transport options with their own trade-offs.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/The STDIO transport.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296291){: target="_blank" }*
