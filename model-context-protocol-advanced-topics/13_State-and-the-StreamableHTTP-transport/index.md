---
title: "State and the StreamableHTTP transport"
parent: MCP Advanced Topics
nav_order: 13
---

# State and the StreamableHTTP transport

details
1
download
State and the StreamableHTTP transport
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 6 minutes, 29 seconds
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
06:29
06:29
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
The
stateless_http
and
json_response
flags in MCP servers control fundamental aspects of how your server behaves. Understanding when and why to use them is crucial, especially if you're planning to scale your server or deploy it in production.
When You Need Stateless HTTP
Imagine you build an MCP server that becomes popular. Initially, you might have just a few clients connecting to a single server instance:
As your server grows, you might have thousands of clients trying to connect. Running a single server instance won't scale to handle all that traffic:
The typical solution is horizontal scaling - running multiple server instances behind a load balancer:
But here's where things get complicated. Remember that MCP clients need two separate connections:
A GET SSE connection for receiving server-to-client requests
POST requests for calling tools and receiving responses
With a load balancer, these requests might get routed to different server instances. If your tool needs to use Claude (through sampling), the server handling the POST request would need to coordinate with the server handling the GET SSE connection. This creates a complex coordination problem between servers.
How Stateless HTTP Solves This
Setting
stateless_http=True
eliminates this coordination problem, but with significant trade-offs:
When stateless HTTP is enabled:
Clients don't get session IDs
- the server can't track individual clients
No server-to-client requests
- the GET SSE pathway becomes unavailable
No sampling
- can't use Claude or other AI models
No progress reports
- can't send progress updates during long operations
No subscriptions
- can't notify clients about resource updates
However, there's one benefit:
client initialization is no longer required
. Clients can make requests directly without the initial handshake process.
Understanding JSON Response
The
json_response=True
flag is simpler - it just disables streaming for POST request responses. Instead of getting multiple SSE messages as a tool executes, you get only the final result as plain JSON.
With streaming disabled:
No intermediate progress messages
No log statements during execution
Just the final tool result
When to Use These Flags
Use stateless HTTP when:
You need horizontal scaling with load balancers
You don't need server-to-client communication
Your tools don't require AI model sampling
You want to minimize connection overhead
Use JSON response when:
You don't need streaming responses
You prefer simpler, non-streaming HTTP responses
You're integrating with systems that expect plain JSON
Development vs Production
If you're developing locally with standard I/O transport but planning to deploy with HTTP transport, test with the same transport you'll use in production. The behavior differences between stateful and stateless modes can be significant, and it's better to catch any issues during development rather than after deployment.
These flags fundamentally change how your MCP server operates, so choose them based on your specific scaling and functionality requirements.
Downloads
transport-http.zip
(opens in new tab)
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/State and the StreamableHTTP transport.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749756073/transport-http.zip?response-content-disposition=attachment&amp;Expires=1778356973&amp;Signature=gq74t8hZaTqIr8~sIhdc-Ey~UxcQHZDV9Lxb8j~jpLYanpJpqlw-o-m-qJtt6q6F8VfPEtllCc20UnuOt3hp5ltXMtFvxFv3M~EWrTjPOcPKT2EnI0ihybqfTIsCGLb8nu-Et8b6IOZ9wKtUfcW9zp3qOg7SvtElte1XoMhr27lfb4AVkvYQAPUhAK0MnglFcQesBm~ppNph-ZHk8OftPsVl0UjFv-DTuS3ihZWdBpdxQXZPs76h5rMQcI7JoButPvBiw2eIg24GRLnn1ym2vI2stF1Zt4F8eGyuYhHRfcURfJyQl-GdcAzQj2a9~SUHv7mbsz9qNqJKKQ~F1vaEUg__&amp;Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749756073/transport-http.zip?response-content-disposition=attachment&Expires=1778356973&Signature=gq74t8hZaTqIr8~sIhdc-Ey~UxcQHZDV9Lxb8j~jpLYanpJpqlw-o-m-qJtt6q6F8VfPEtllCc20UnuOt3hp5ltXMtFvxFv3M~EWrTjPOcPKT2EnI0ihybqfTIsCGLb8nu-Et8b6IOZ9wKtUfcW9zp3qOg7SvtElte1XoMhr27lfb4AVkvYQAPUhAK0MnglFcQesBm~ppNph-ZHk8OftPsVl0UjFv-DTuS3ihZWdBpdxQXZPs76h5rMQcI7JoButPvBiw2eIg24GRLnn1ym2vI2stF1Zt4F8eGyuYhHRfcURfJyQl-GdcAzQj2a9~SUHv7mbsz9qNqJKKQ~F1vaEUg__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

## Tài liệu PDF

- [transport-http.zip?response-content-disposition=attachment&Expires=1778356973&Signature=gq74t8hZaTqIr8~sIhdc-Ey~UxcQHZDV9Lxb8j~jpLYanpJpqlw-o-m-qJtt6q6F8VfPEtllCc20UnuOt3hp5ltXMtFvxFv3M~EWrTjPOcPKT2EnI0ihybqfTIsCGLb8nu-Et8b6IOZ9wKtUfcW9zp3qOg7SvtElte1XoMhr27lfb4AVkvYQAPUhAK0MnglFcQesBm~ppNph-ZHk8OftPsVl0UjFv-DTuS3ihZWdBpdxQXZPs76h5rMQcI7JoButPvBiw2eIg24GRLnn1ym2vI2stF1Zt4F8eGyuYhHRfcURfJyQl-GdcAzQj2a9~SUHv7mbsz9qNqJKKQ~F1vaEUg__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](../pdfs/transport-http.zip?response-content-disposition=attachment&Expires=1778356973&Signature=gq74t8hZaTqIr8~sIhdc-Ey~UxcQHZDV9Lxb8j~jpLYanpJpqlw-o-m-qJtt6q6F8VfPEtllCc20UnuOt3hp5ltXMtFvxFv3M~EWrTjPOcPKT2EnI0ihybqfTIsCGLb8nu-Et8b6IOZ9wKtUfcW9zp3qOg7SvtElte1XoMhr27lfb4AVkvYQAPUhAK0MnglFcQesBm~ppNph-ZHk8OftPsVl0UjFv-DTuS3ihZWdBpdxQXZPs76h5rMQcI7JoButPvBiw2eIg24GRLnn1ym2vI2stF1Zt4F8eGyuYhHRfcURfJyQl-GdcAzQj2a9~SUHv7mbsz9qNqJKKQ~F1vaEUg__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)


---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296285){: target="_blank" }*
