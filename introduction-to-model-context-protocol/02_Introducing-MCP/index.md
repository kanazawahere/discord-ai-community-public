---
title: "Introducing MCP"
parent: Introduction to MCP
nav_order: 2
---

# Introducing MCP

details
Introducing MCP
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 4 minutes, 40 seconds
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
04:40
04:40
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Think of it as a way to shift the burden of tool definitions and execution away from your server to specialized MCP servers.
When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connecting to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to some outside service.
The Problem MCP Solves
Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To handle this, Claude needs tools to access GitHub's API.
GitHub has massive functionality - repositories, pull requests, issues, projects, and tons more. Without MCP, you'd need to create an incredible number of tool schemas and functions to handle all of GitHub's features.
This means writing, testing, and maintaining all that integration code yourself. That's a lot of effort and ongoing maintenance burden.
How MCP Works
MCP shifts this burden by moving tool definitions and execution from your server to dedicated MCP servers. Instead of you authoring all those GitHub tools, an MCP Server for GitHub handles it.
The MCP Server wraps up tons of functionality around GitHub and exposes it as a standardized set of tools. Your application connects to this MCP server instead of implementing everything from scratch.
MCP Servers Explained
MCP Servers provide access to data or functionality implemented by outside services. They act as specialized interfaces that expose tools, prompts, and resources in a standardized way.
In our GitHub example, the MCP Server for GitHub contains tools like
get_repos()
and connects directly to GitHub's API. Your server communicates with the MCP server, which handles all the GitHub-specific implementation details.
Common Questions
Who authors MCP Servers?
Anyone can create an MCP server implementation. Often, service providers themselves will make their own official MCP implementations. For example, AWS might release an official MCP server with tools for their various services.
How is this different from calling APIs directly?
MCP servers provide tool schemas and functions already defined for you. If you want to call an API directly, you'll be authoring those tool definitions on your own. MCP saves you that implementation work.
Isn't MCP just the same as tool use?
This is a common misconception. MCP servers and tool use are complementary but different concepts. MCP servers provide tool schemas and functions already defined for you, while tool use is about how Claude actually calls those tools. The key difference is who does the work - with MCP, someone else has already implemented the tools for you.
The benefit is clear: instead of maintaining a complex set of integrations yourself, you can leverage MCP servers that handle the heavy lifting of connecting to external services.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/Introducing MCP.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296689){: target="_blank" }*
