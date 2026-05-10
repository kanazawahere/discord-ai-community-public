---
title: "Accessing resources"
parent: Introduction to MCP
nav_order: 10
---

# Accessing resources

details
Accessing resources
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
0 seconds of 4 minutes, 38 seconds
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
04:38
04:38
This video is still being processed. Please check back later and refresh the page.
Uh oh! Something went wrong, please try again.
Summary
Summary
Resources in MCP allow your server to expose information that can be directly included in prompts, rather than requiring tool calls to access data. This creates a more efficient way to provide context to AI models.
The diagram above shows how resources work: when a user types something like "What's in the @..." our code recognizes this as a resource request, sends a ReadResourceRequest to the MCP server, and gets back a ReadResourceResult with the actual content.
Implementing Resource Reading
To enable resource access in your MCP client, you need to implement a
read_resource
function. First, add the necessary imports:
import json
from pydantic import AnyUrl
The core function makes a request to the MCP server and processes the response based on its MIME type:
async def read_resource(self, uri: str) -> Any:
result = await self.session().read_resource(AnyUrl(uri))
resource = result.contents[0]

if isinstance(resource, types.TextResourceContents):
if resource.mimeType == "application/json":
return json.loads(resource.text)

return resource.text
Understanding the Response Structure
When you request a resource, the server returns a result with a
contents
list. We access the first element since we typically only need one resource at a time. The response includes:
The actual content (text or data)
A MIME type that tells us how to parse the content
Other metadata about the resource
Content Type Handling
The function checks the MIME type to determine how to process the content:
If it's
application/json
, parse the text as JSON and return the parsed object
Otherwise, return the raw text content
This approach handles both structured data (like JSON) and plain text documents seamlessly.
Testing Resource Access
Once implemented, you can test the resource functionality through your CLI application. When you type "@" followed by a resource name, the system will:
Show available resources in an autocomplete list
Let you select a resource using arrow keys and space
Include the resource content directly in your prompt
Send everything to the AI model without requiring additional tool calls
This creates a much smoother user experience compared to having the AI model make separate tool calls to access document contents. The resource content becomes part of the initial context, allowing for immediate responses about the data.
## Video

<video controls style="max-width:100%;margin-bottom:1rem;">
  <source src="../videos/Accessing resources.mp4" type="video/mp4">
</video>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)



---
*[Nguồn gốc](https://anthropic.skilljar.com/introduction-to-model-context-protocol/296695){: target="_blank" }*
