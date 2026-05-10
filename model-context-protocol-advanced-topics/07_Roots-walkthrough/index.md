---
title: "Roots walkthrough"
parent: MCP Advanced Topics
nav_order: 7
---

# Roots walkthrough

details
1
download
Roots walkthrough
Anthropic
Open in Claude
Anthropic
Open in Claude
Ask questions about this course
Copy notes
Copy full course notes for LLMs
1. Defining roots
Ideally, a user will dictate which files/folders can be accessed by the MCP server.
This program is set up to accept a list of CLI arguments, which are interpretted as paths that the user wants to allow access to.
That list of paths is provided to the
MCPClient
down on lines 42.
2. Creating root objects
According to the MCP spec, all roots should have a URI that begins with
file://
.
This function takes the list of paths of that the user provided and turns them into
Root
objects.
3. Roots callback
The client doesn't immediately provide the list of roots to the server. Instead, the server can make a request to the client at some future point in time. We make a callback that will be executed when the server requests the roots. The callback needs to return the list of roots inside of a
ListRootsResult
object.
This callback is passed into the ClientSession down on line 58.
4. Using the roots
On to the server. The server will use the roots in two scenarios:
Whenever a tool attempts to access a file or folder
When a LLM (like Claude) needs to resolve a file or folder to a full path. Think of when a user says 'read the todos.txt file' - Claude needs to figure out where the text file is, and might do so by looking at the list of roots
To handle the second case, we can either define a tool that lists out the roots or inject them directly in a prompt.
5. Accessing the roots
Roots are accessed by calling
ctx.session.list_roots()
.
This sends a message back to the client, which causes it to run the root-listing callback.
6. Authorizing access
Remember: the MCP SDK does not attempt to limit what files or folders your tools attempt to read! You must implement that check yourself.
Consider implementing a function like
is_path_allowed
, which will decide whether a path is accessible by comparing it to the list of roots.
7. Authorizing access
Once you've put an authorization function together - like
is_path_allowed
- use it throughout your tools to ensure the requested path is accessible.
← Previous
Next →
Files
📂
core
📄
__init__.py
📄
chat.py
📄
claude.py
📄
cli_chat.py
📄
cli.py
📄
tools.py
📄
utils.py
📄
video_converter.py
📄
.env.example
📄
.gitignore
📄
main.py
📄
mcp_client.py
📄
mcp_server.py
📄
pyproject.toml
📄
README.md
main.py
×
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
env"
assert
anthropic_api_key,
(
"Error:
ANTHROPIC_API_KEY
cannot be empty.
Update .env"
)
async
def
main
(
)
:
claude_service =
Claude
(
model=claude_model
)
# Get root
directories from
command line arguments
root_paths = sys.argv
[
1
:
]
if
not
root_paths:
print
(
"Usage: uv
run main.py
<root1>
[root2] ..."
)
print
(
"Example:
uv run main.py /
path/to/videos /
another/path"
)
sys.exit
(
1
)
clients =
{
}
async
with
AsyncExitStack
(
)
as
stack:
# Create the MCP
Summary
Downloads
roots.zip
(opens in new tab)
Tutorial Steps
Let's get a better sense of how to implement this feature by walking through a sample project.
Skip
Next


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749755968/roots.zip?response-content-disposition=attachment&amp;Expires=1778356902&amp;Signature=L9v2nOCEjAoYV8ilZkB3fOn~3xRM829ZGElrecp-NhlV6usO3XvKYvMSck17Y0F3XtRmpvQXEZh96m2bVPrzqVJMlGIZ0-nb-Uc~A2cOnM~NxclvQ9GLt~GzuH5oxBO9aLrqj6euTm3nSxmdRxIKaKALkP7xDQEztDN1NH0SW-XsRerZpBc18KPSAMzewPuclJHTnZc37Veu3UNs~bnsvKZC7BX-WuqCkQxnmcJ7c34MQG8VakUzMNJvIEaIr1tjvC2hmHvT~cRExFASJj2Toe3~4Kk6zzDEkiKuXwk5696E2YkhQHcRObZnB-FGSZdU61EiBRp--M9ymlyLAzHNkw__&amp;Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1749755968/roots.zip?response-content-disposition=attachment&Expires=1778356902&Signature=L9v2nOCEjAoYV8ilZkB3fOn~3xRM829ZGElrecp-NhlV6usO3XvKYvMSck17Y0F3XtRmpvQXEZh96m2bVPrzqVJMlGIZ0-nb-Uc~A2cOnM~NxclvQ9GLt~GzuH5oxBO9aLrqj6euTm3nSxmdRxIKaKALkP7xDQEztDN1NH0SW-XsRerZpBc18KPSAMzewPuclJHTnZc37Veu3UNs~bnsvKZC7BX-WuqCkQxnmcJ7c34MQG8VakUzMNJvIEaIr1tjvC2hmHvT~cRExFASJj2Toe3~4Kk6zzDEkiKuXwk5696E2YkhQHcRObZnB-FGSZdU61EiBRp--M9ymlyLAzHNkw__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

## Tài liệu PDF

- [roots.zip?response-content-disposition=attachment&Expires=1778356902&Signature=L9v2nOCEjAoYV8ilZkB3fOn~3xRM829ZGElrecp-NhlV6usO3XvKYvMSck17Y0F3XtRmpvQXEZh96m2bVPrzqVJMlGIZ0-nb-Uc~A2cOnM~NxclvQ9GLt~GzuH5oxBO9aLrqj6euTm3nSxmdRxIKaKALkP7xDQEztDN1NH0SW-XsRerZpBc18KPSAMzewPuclJHTnZc37Veu3UNs~bnsvKZC7BX-WuqCkQxnmcJ7c34MQG8VakUzMNJvIEaIr1tjvC2hmHvT~cRExFASJj2Toe3~4Kk6zzDEkiKuXwk5696E2YkhQHcRObZnB-FGSZdU61EiBRp--M9ymlyLAzHNkw__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ](../pdfs/roots.zip?response-content-disposition=attachment&Expires=1778356902&Signature=L9v2nOCEjAoYV8ilZkB3fOn~3xRM829ZGElrecp-NhlV6usO3XvKYvMSck17Y0F3XtRmpvQXEZh96m2bVPrzqVJMlGIZ0-nb-Uc~A2cOnM~NxclvQ9GLt~GzuH5oxBO9aLrqj6euTm3nSxmdRxIKaKALkP7xDQEztDN1NH0SW-XsRerZpBc18KPSAMzewPuclJHTnZc37Veu3UNs~bnsvKZC7BX-WuqCkQxnmcJ7c34MQG8VakUzMNJvIEaIr1tjvC2hmHvT~cRExFASJj2Toe3~4Kk6zzDEkiKuXwk5696E2YkhQHcRObZnB-FGSZdU61EiBRp--M9ymlyLAzHNkw__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)


---
*[Nguồn gốc](https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295839){: target="_blank" }*
