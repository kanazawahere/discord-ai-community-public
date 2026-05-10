---
title: "The StreamableHTTP transport"
parent: MCP Advanced Topics
nav_order: 11
---

# The StreamableHTTP transport

details
The StreamableHTTP transport
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 6 minutes, 26 seconds
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
06:26
06:26
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
The streamable HTTP transport enables MCP clients to connect to remotely hosted servers over HTTP connections. Unlike the standard I/O transport that requires both client and server on the same machine, this transport opens up possibilities for public MCP servers that anyone can access.
However, there's an important caveat: some configuration settings can significantly limit your MCP server's functionality. If your application works perfectly with standard I/O transport locally but breaks when deployed with HTTP transport, this is likely the culprit.
Configuration Settings That Matter
Two key settings control how the streamable HTTP transport behaves:
stateless_http
- Controls connection state management
json_response
- Controls response format handling
By default, both settings are
false
, but certain deployment scenarios may force you to set them to
true
. When enabled, these settings can break core functionality like progress notifications, logging, and server-initiated requests.
The HTTP Communication Challenge
To understand why these limitations exist, we need to review how HTTP communication works. In standard HTTP:
Clients can easily initiate requests to servers (the server has a known URL)
Servers can easily respond to these requests
Servers cannot easily initiate requests to clients (clients don't have known URLs)
Response patterns from client back to server become problematic
MCP Message Types Affected
This HTTP limitation impacts specific MCP communication patterns. The following message types become difficult to implement with plain HTTP:
Server-initiated requests:
Create Message requests, List Roots requests
Notifications:
Progress notifications, Logging notifications, Initialized notifications, Cancelled notifications
These are exactly the features that break when you enable the restrictive HTTP settings. Progress bars disappear, logging stops working, and server-initiated sampling requests fail.
The Streamable HTTP Solution
The streamable HTTP transport does provide a clever solution to work around HTTP's limitations, but it comes with trade-offs. When you're forced to use
stateless_http=True
or
json_response=True
, you're essentially telling the transport to operate within HTTP's constraints rather than working around them.
Understanding these limitations helps you make informed decisions about:
Which transport to use for different deployment scenarios
How to design your MCP server to gracefully handle HTTP constraints
When to accept reduced functionality for the benefits of remote hosting
The key is knowing that these restrictions exist and planning your MCP server architecture accordingly. If your application heavily relies on server-initiated requests or real-time notifications, you may need to reconsider your transport choice or implement alternative communication patterns.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/The StreamableHTTP transport.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287){: target="_blank" }*
