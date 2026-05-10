---
title: "Sampling walkthrough"
parent: MCP Advanced Topics
nav_order: 3
---

# Sampling walkthrough

details
1
download
Sampling walkthrough
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
1. Initiating sampling
On the server, during a tool call, run the
create_message()
method, passing in some messages that you wish to send to a language model.
2. Sampling callbacks
On the client, you must implement a sampling callback. It will receive a list of messages provided by the server.
3. Message formats
The list of messages provided by the server are formatted for communication in MCP. The individual messages aren't guaranteed to be compatible with whatever LLM SDK you are using.
For example, if you're using the Anthropic SDK, you'll have to write a little bit of conversion logic to turn the MCP messages into a format compatible with Anthropic's SDK.
4. Returning generated text
After generating text with the LLM, you'll return a
CreateMessageResult
, which contains the generated text.
5. Connecting the callback
Don't forget: the callback on the client needs to be passed into the
ClientSession
call.
6. Getting the result
After the client has generated and returned some text, it will be sent to the server. You can do anything with this text:
Use it as part of a workflow in your tool
Decide to make another sampling call
Return the generated text
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
TextContent
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
summarize
(
text_to_summarize:
str
,
ctx: Context
)
:
prompt = f
"""
Please summarize
the following
text:
{text_to_summarize
}
"""
result =
await
ctx.
session.create_message
(
messages=
[
SamplingMessag
e
(
role=
"user
"
,
content=Te
xtContent
(
type
=
"tex
t"
,
text=promp
t
)
)
]
,
max_tokens=
4000
,
system_prompt=
"You
are a helpful
Summary
Downloads
sampling.zip
(opens in new tab)
Tutorial Steps
Let's get a better sense of how to implement this feature by walking through a sample project.
Skip
Next


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749755739/sampling.zip?response-content-disposition=attachment&amp;Expires=1778356865&amp;Signature=WUow~1HXm39JcpXzrNB0wMCexldVOTVV2u7Zt5qFq8LKd-CSPOlSjimX-cT0AKifOrousgqO-ka~TzXs5ejogMvNS6lTnM1pi58v-ILMfWuWOcfRH4vZH1QVdsWH10aOiMDKkdj0ieRbVcTozplqZdbT2O7SsxuMb967W~zL1anPrvUrv6bKeilb1Jq2-A0~Rm~D6U-LvXAau5ZvW4GnDYzCjR98H27S2JaSLf3Vx-cdjhKUZ2ULN9WCC83bcniV~eDTxkX68aFELUP-KNm1e2moWL~1atk-SUE-6BTPNGlry~P9ohUYZkPoeXivWFj7LWPaefWXHXt818NV3FIfjQ__&amp;Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749755739/sampling.zip?response-content-disposition=attachment&Expires=1778356865&Signature=WUow~1HXm39JcpXzrNB0wMCexldVOTVV2u7Zt5qFq8LKd-CSPOlSjimX-cT0AKifOrousgqO-ka~TzXs5ejogMvNS6lTnM1pi58v-ILMfWuWOcfRH4vZH1QVdsWH10aOiMDKkdj0ieRbVcTozplqZdbT2O7SsxuMb967W~zL1anPrvUrv6bKeilb1Jq2-A0~Rm~D6U-LvXAau5ZvW4GnDYzCjR98H27S2JaSLf3Vx-cdjhKUZ2ULN9WCC83bcniV~eDTxkX68aFELUP-KNm1e2moWL~1atk-SUE-6BTPNGlry~P9ohUYZkPoeXivWFj7LWPaefWXHXt818NV3FIfjQ__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

## Tài liệu PDF

- [sampling.zip?response-content-disposition=attachment&Expires=1778356865&Signature=WUow~1HXm39JcpXzrNB0wMCexldVOTVV2u7Zt5qFq8LKd-CSPOlSjimX-cT0AKifOrousgqO-ka~TzXs5ejogMvNS6lTnM1pi58v-ILMfWuWOcfRH4vZH1QVdsWH10aOiMDKkdj0ieRbVcTozplqZdbT2O7SsxuMb967W~zL1anPrvUrv6bKeilb1Jq2-A0~Rm~D6U-LvXAau5ZvW4GnDYzCjR98H27S2JaSLf3Vx-cdjhKUZ2ULN9WCC83bcniV~eDTxkX68aFELUP-KNm1e2moWL~1atk-SUE-6BTPNGlry~P9ohUYZkPoeXivWFj7LWPaefWXHXt818NV3FIfjQ__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](../pdfs/sampling.zip?response-content-disposition=attachment&Expires=1778356865&Signature=WUow~1HXm39JcpXzrNB0wMCexldVOTVV2u7Zt5qFq8LKd-CSPOlSjimX-cT0AKifOrousgqO-ka~TzXs5ejogMvNS6lTnM1pi58v-ILMfWuWOcfRH4vZH1QVdsWH10aOiMDKkdj0ieRbVcTozplqZdbT2O7SsxuMb967W~zL1anPrvUrv6bKeilb1Jq2-A0~Rm~D6U-LvXAau5ZvW4GnDYzCjR98H27S2JaSLf3Vx-cdjhKUZ2ULN9WCC83bcniV~eDTxkX68aFELUP-KNm1e2moWL~1atk-SUE-6BTPNGlry~P9ohUYZkPoeXivWFj7LWPaefWXHXt818NV3FIfjQ__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)


---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172){: target="_blank" }*
