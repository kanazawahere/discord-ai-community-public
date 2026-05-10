---
title: "Notifications walkthrough"
parent: MCP Advanced Topics
nav_order: 5
---

# Notifications walkthrough

details
1
download
Notifications walkthrough
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
1. Tool function receives Context argument
Tool functions automatically receive 'Context' as their last argument. This object has methods for logging and reporting progress to the client.
2. Create logs and progress with context
Throughout your tool function, call the
info()
,
warning()
,
debug()
, or
error()
methods to log different types of messages for the client. Also call the
report_progress()
method to estimate the amount of remaining work for the tool call.
3. Define callbacks on the client
The client needs to define logging and progress callbacks, which will automatically be called whenever the server emits log or progress messages. These callbacks should try to display the provided logging and progress data to the user.
4. Pass callbacks to appropriate functions
Make sure you provide the logging callback to the
ClientSession
and the progress callback to the
call_tool()
function.
← Previous
Next →
Files
📄
.gitignore
📄
client.py
📄
pyproject.toml
📄
README.md
📄
server.py
server.py
×
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
from
mcp.server.fastmcp
import
FastMCP, Context
import
asyncio
mcp = FastMCP
(
name=
"Demo
Server"
)
@mcp
.tool
(
)
async
def
add
(
a:
int
, b:
int
, ctx: Context
)
->
int
:
await
ctx.info
(
"Preparing to add...
"
)
await
ctx.
report_progress
(
20
,
100
)
await
asyncio.sleep
(
2
)
await
ctx.info
(
"OK,
adding..."
)
await
ctx.
report_progress
(
80
,
100
)
return
a + b
if
__name__
==
"__main__"
:
mcp.run
(
transport=
"stdio"
)
Summary
Downloads
notifications.zip
(opens in new tab)
Tutorial Steps
Let's get a better sense of how to implement this feature by walking through a sample project.
Skip
Next


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749755834/notifications.zip?response-content-disposition=attachment&amp;Expires=1778356882&amp;Signature=t3~DnHxeypH-iMvq0wqbY0ytWbyLLXm6q6h7pRste4Q9P6-d0BTx5A3Ghzl2mn29X5~LLQ5LukVcnNUMpVEccSFslOn-Cm54N0iAKxl-HExZ5UvVuVaRCWMKOH2UgFZE3YNO5JPHK7JgD~Sm8KZJkJTi668wHGeTCgZ6kJh8igJZr30sAIcE0GqTZuBIzoWQScJ8LL23ZHGSIw1d1THz38y0u-KS4qHR6Z1dcqyb2A-mBBmmnqt2lQnCXl-v0clJlkp5mu3Mj-LlbYCKvS7D6p3cv2OWdzFT8I7XO74AHXtoglsyVxA3y2-lewUvndxMRGqZ8Ds4yWh64ykY4COW5A__&amp;Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749755834/notifications.zip?response-content-disposition=attachment&Expires=1778356882&Signature=t3~DnHxeypH-iMvq0wqbY0ytWbyLLXm6q6h7pRste4Q9P6-d0BTx5A3Ghzl2mn29X5~LLQ5LukVcnNUMpVEccSFslOn-Cm54N0iAKxl-HExZ5UvVuVaRCWMKOH2UgFZE3YNO5JPHK7JgD~Sm8KZJkJTi668wHGeTCgZ6kJh8igJZr30sAIcE0GqTZuBIzoWQScJ8LL23ZHGSIw1d1THz38y0u-KS4qHR6Z1dcqyb2A-mBBmmnqt2lQnCXl-v0clJlkp5mu3Mj-LlbYCKvS7D6p3cv2OWdzFT8I7XO74AHXtoglsyVxA3y2-lewUvndxMRGqZ8Ds4yWh64ykY4COW5A__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

## Tài liệu PDF

- [notifications.zip?response-content-disposition=attachment&Expires=1778356882&Signature=t3~DnHxeypH-iMvq0wqbY0ytWbyLLXm6q6h7pRste4Q9P6-d0BTx5A3Ghzl2mn29X5~LLQ5LukVcnNUMpVEccSFslOn-Cm54N0iAKxl-HExZ5UvVuVaRCWMKOH2UgFZE3YNO5JPHK7JgD~Sm8KZJkJTi668wHGeTCgZ6kJh8igJZr30sAIcE0GqTZuBIzoWQScJ8LL23ZHGSIw1d1THz38y0u-KS4qHR6Z1dcqyb2A-mBBmmnqt2lQnCXl-v0clJlkp5mu3Mj-LlbYCKvS7D6p3cv2OWdzFT8I7XO74AHXtoglsyVxA3y2-lewUvndxMRGqZ8Ds4yWh64ykY4COW5A__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](../pdfs/notifications.zip?response-content-disposition=attachment&Expires=1778356882&Signature=t3~DnHxeypH-iMvq0wqbY0ytWbyLLXm6q6h7pRste4Q9P6-d0BTx5A3Ghzl2mn29X5~LLQ5LukVcnNUMpVEccSFslOn-Cm54N0iAKxl-HExZ5UvVuVaRCWMKOH2UgFZE3YNO5JPHK7JgD~Sm8KZJkJTi668wHGeTCgZ6kJh8igJZr30sAIcE0GqTZuBIzoWQScJ8LL23ZHGSIw1d1THz38y0u-KS4qHR6Z1dcqyb2A-mBBmmnqt2lQnCXl-v0clJlkp5mu3Mj-LlbYCKvS7D6p3cv2OWdzFT8I7XO74AHXtoglsyVxA3y2-lewUvndxMRGqZ8Ds4yWh64ykY4COW5A__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)


---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036){: target="_blank" }*
