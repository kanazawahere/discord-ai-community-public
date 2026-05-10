---
title: "Working with skills"
parent: Claude 101
nav_order: 7
---

# Working with skills

Explain what Skills are and how Claude uses them
Identify Anthropic's built-in Skills for document creation
Enable and manage Skills in your settings
Plan availability:
Skills are currently a feature preview for Pro, Max, Team, and Enterprise plans. If you're on the Free plan, you can read along to understand the concept and skip the hands-on steps.
What are Skills?
Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Think of them as expertise packages—they teach Claude how to complete specific tasks in a repeatable way.
You've already seen Skills at work if you've used Claude to create Excel spreadsheets, PowerPoint presentations, Word documents, or PDFs. Those file creation capabilities are powered by Skills running behind the scenes. But Skills go far beyond document creation. Custom Skills can codify entire repeatable workflows — a quarterly variance analysis methodology, a brand voice review process, or a compliance checklist — so Claude follows the same rigorous steps every time.
Types of Skills
There are two categories of Skills you'll encounter:
Anthropic Skills
are created and maintained by Anthropic. These include enhanced document creation capabilities for Excel, Word, PowerPoint, and PDF files. Anthropic Skills are available to all paid users and Claude invokes them automatically when relevant—you don't need to do anything special to use them.
Custom Skills
are ones you or your organization create for specialized workflows and domain-specific tasks. For example, you might create a skill that applies your company's brand guidelines to presentations, structures meeting notes in a specific format, or executes your organization's data analysis workflows.
Enabling Skills
Skills are currently available as a feature preview for users on Pro, Max, Team, and Enterprise plans. To use Skills, you'll need to have Code execution and file creation enabled, since Skills require Claude's secure sandboxed computing environment to function.
Here's how to enable Skills:
Navigate to
Settings > Capabilities
Ensure that
Code execution and file creation
is toggled on
Scroll to the
Skills
section
Toggle individual skills on or off as needed
For
Enterprise plans
, organization Owners must first enable both Code execution and Skills in Admin settings before individual members can access them.
For
Team plans
, this feature preview is enabled by default at the organization level.
Once enabled, you'll see available Skills listed in your settings, including Anthropic's built-in Skills and any custom Skills you've uploaded.
Using Skills in practice
The beauty of Skills is that you typically don't need to think about them—Claude handles skill selection automatically based on your request. Here are some examples of prompts that would invoke Skills:
"Create an Excel spreadsheet tracking monthly expenses with formulas for totals"
"Turn this meeting notes document into a PowerPoint presentation"
"Generate a PDF report summarizing this data"
"Build a financial model in Excel with scenario analysis"
When Claude uses a Skill, you'll see it mentioned in Claude's chain of thought as it works. The output will be a downloadable file you can save to your computer or directly to Google Drive.
File execution
Claude works with you on slides, spreadsheets, and contract redlines
This same capability means that Claude can work with
your actual files
(within a contained environment) to create updated versions of your files (note: in Chat, Claude creates a new version of the document rather than editing the original in place). Upload slides, spreadsheets, contracts, (or any .xlsx, .pptx, .docx, or .pdf files) and watch as Claude creates slides, performs analyses, and adds suggested edits. When Claude is done, you can download these files or open them in Drive.
Note: To use these capabilities you'll need to give Claude access to external data sources. Simply toggle Allow limited network access on when prompted:
Security considerations
Because Skills can include executable code, it's important to use them thoughtfully:
Only install custom Skills from trusted sources
Anthropic's built-in Skills are tested and maintained by Anthropic
Custom Skills you upload are private to your individual account
If you're installing a custom Skill from an external source, review its contents before use to understand what it does.
Creating custom skills
While Anthropic's built-in Skills cover common document creation tasks, the real power of Skills comes from creating your own. Custom Skills let you teach Claude your specific workflows, brand guidelines, and ways of working—so Claude can apply that knowledge automatically whenever it's relevant.
The easiest way to create a custom Skill is through conversation with Claude itself. You don't need to write code or manually create files—Claude handles the technical structure for you.
Here's how to create a Skill through conversation:
Start a new chat
and tell Claude what you want to create. For example: "I want to create a skill for writing quarterly business reviews" or "I need a skill that applies our brand guidelines to presentations."
Answer Claude's questions.
Claude will interview you about your workflow, asking things like: What should this skill do? What makes good output for this type of work? Can you give examples of when you'd use this skill?
Upload reference materials
if you have them. Templates, style guides, brand assets, or examples of work you're proud of all help Claude understand exactly what you're looking for.
Save your skill.
When finished, Claude generates a file containing your properly structured skill. All you have to do is save it and the skill will be ready for Claude to use.
See your skills.
Find the Customize tab in the left sidebar. There you can see all of the skills that are available to you and even edit the skills you use manually or by chatting with Claude.
Your custom Skill will appear in your Skills list alongside Anthropic's built-in Skills. From that point forward, Claude will automatically invoke it whenever you work on relevant tasks—no manual triggering needed. You can improve your skills with iteration — ask Claude to edit a skill and it will update the files for you.
Skills vs. Projects
You might be wondering—if both skills and projects can be used to give more context to Claude, when should I use each? Think of it this way:
projects store knowledge, skills perform tasks
.
Projects
are knowledge hubs. They hold the reference materials Claude needs to understand your work—project specs, meeting notes, research documents. When you upload files to a project, Claude draws on that information across every conversation within that project.
Skills
are procedural machines. They encode
how
Claude should execute a task—the specific steps, order of operations, and methodology you want followed every time. Skills shine when you have repeatable workflows you want Claude to run consistently.
The two features complement each other. A skill can reference knowledge stored in a project—your "customer call prep" skill might pull from customer profiles uploaded to a project's knowledge base. The project provides the
what
(information), the skill provides the
how
(process).
Projects
Skills
Purpose
Store knowledge Claude references
Define processes Claude executes
Best for
Long-term context, reference materials, team collaboration
Repeatable workflows, multi-step tasks, consistent methodology
Example
Customer hub, research buddy, feedback generator
Process guidelines (like brand or legal), Blog drafting, PDF creation
Persistence
Knowledge available across all chats in the project
Instructions applied when the skill is invoked
Lesson reflection
Before moving on, consider:
What types of documents do you create regularly that could benefit from Claude's built-in Skills?
Are there repetitive workflows in your work that might be good candidates for custom Skills?
How might Skills change the way you think about document creation and data analysis?
What's next
In the next set of lessons, you'll start to expand Claude's reach with connectors. These powerful tools make information gathering seamless, and can give Claude the ability to perform actions right inside the tools where your work is happening.
For more information on Skills, including how to create your own custom Skills, visit the
Anthropic Help Center
.
Feedback
As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work and any feedback you may have. Share your feedback
here
.
Acknowledgments and license
Copyright 2025 Anthropic. All rights reserved.
## Video

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin-bottom:1.5rem;">
  <iframe src="https://www.youtube.com/embed/LpGpwhORWr0?rel=0"
          style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
          allowfullscreen loading="lazy" title="Working with skills"></iframe>
</div>

## Câu hỏi ôn tập

- What types of documents do you create regularly that could benefit from Claude&#x27;s built-in Skills?
- Are there repetitive workflows in your work that might be good candidates for custom Skills?
- How might Skills change the way you think about document creation and data analysis?



## Tóm tắt

This document serves as an instructional guide on **Skills**, a dynamic feature that allows Claude to execute **specialized tasks and repeatable workflows** with high precision. While **Anthropic Skills** automatically handle standard document creation like spreadsheets and presentations, users can also develop **Custom Skills** to codify unique methodologies, such as brand reviews or compliance checks. These tools function as **procedural machines** that define the specific steps Claude should follow, distinguishing them from Projects, which primarily act as static knowledge hubs. By enabling these capabilities in their settings, eligible users can transform the AI into a consistent assistant that **independently invokes the correct expertise** to generate sophisticated, downloadable files.

**Từ khóa:** `Claude Skills` · `Custom Skill Creation` · `Anthropic Built-in Skills` · `Document Workflow Automation` · `Skills vs Projects`




## Câu hỏi kiểm tra

<div class="quiz-vn" id="quiz-07_Working-with-skills"><div class="quiz-tabs"><button class="qtab active" data-level="easy" onclick="qTab(this,'quiz-07_Working-with-skills')">🟢 Cơ bản (10)</button><button class="qtab " data-level="medium" onclick="qTab(this,'quiz-07_Working-with-skills')">🟡 Nâng cao (10)</button><button class="qtab " data-level="hard" onclick="qTab(this,'quiz-07_Working-with-skills')">🔴 Thử thách (10)</button></div><div class="quiz-panel" data-level="easy" ><div class="qitem" data-correct="Folders of instructions, scripts, and resources loaded dynamically to improve performance.">
<p class="qtext"><strong>1.</strong> According to the Anthropic Academy materials, what are &#x27;Skills&#x27;?</p>
<div class="qchoices"><label data-choice="Folders of instructions, scripts, and resources loaded dynamically to improve performance."><input type="radio" name="quiz-07_Working-with-skills-easy-0" value="0"> Folders of instructions, scripts, and resources loaded dynamically to improve performance.</label><label data-choice="Static datasets used to train the underlying Claude models."><input type="radio" name="quiz-07_Working-with-skills-easy-0" value="1"> Static datasets used to train the underlying Claude models.</label><label data-choice="A list of hardware requirements needed to run Claude locally."><input type="radio" name="quiz-07_Working-with-skills-easy-0" value="2"> A list of hardware requirements needed to run Claude locally.</label><label data-choice="Subscription tiers that determine how many messages a user can send."><input type="radio" name="quiz-07_Working-with-skills-easy-0" value="3"> Subscription tiers that determine how many messages a user can send.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills are designed as packages of expertise that teach Claude how to complete specific tasks in a repeatable way.</div>
</div><div class="qitem" data-correct="Mythos">
<p class="qtext"><strong>2.</strong> Which of the following models is currently listed as a &#x27;preview&#x27; model in the Anthropic resources?</p>
<div class="qchoices"><label data-choice="Mythos"><input type="radio" name="quiz-07_Working-with-skills-easy-1" value="0"> Mythos</label><label data-choice="Opus"><input type="radio" name="quiz-07_Working-with-skills-easy-1" value="1"> Opus</label><label data-choice="Sonnet"><input type="radio" name="quiz-07_Working-with-skills-easy-1" value="2"> Sonnet</label><label data-choice="Haiku"><input type="radio" name="quiz-07_Working-with-skills-easy-1" value="3"> Haiku</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">The source material specifically lists Mythos as a preview model alongside established models like Opus and Sonnet.</div>
</div><div class="qitem" data-correct="Projects provide static background knowledge, while Skills provide procedural workflows.">
<p class="qtext"><strong>3.</strong> What is the main functional difference between &#x27;Projects&#x27; and &#x27;Skills&#x27; in Claude?</p>
<div class="qchoices"><label data-choice="Projects provide static background knowledge, while Skills provide procedural workflows."><input type="radio" name="quiz-07_Working-with-skills-easy-2" value="0"> Projects provide static background knowledge, while Skills provide procedural workflows.</label><label data-choice="Projects are for personal use, while Skills are only available for Enterprise users."><input type="radio" name="quiz-07_Working-with-skills-easy-2" value="1"> Projects are for personal use, while Skills are only available for Enterprise users.</label><label data-choice="Projects require coding knowledge, while Skills are strictly text-based instructions."><input type="radio" name="quiz-07_Working-with-skills-easy-2" value="2"> Projects require coding knowledge, while Skills are strictly text-based instructions.</label><label data-choice="Projects are updated quarterly, while Skills are updated in real-time by the user."><input type="radio" name="quiz-07_Working-with-skills-easy-2" value="3"> Projects are updated quarterly, while Skills are updated in real-time by the user.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Projects serve as knowledge hubs for reference materials, whereas Skills are procedural machines that define how to execute tasks.</div>
</div><div class="qitem" data-correct="Code execution and file creation">
<p class="qtext"><strong>4.</strong> To use Skills in Claude, which setting must be enabled by the user or organization owner?</p>
<div class="qchoices"><label data-choice="Code execution and file creation"><input type="radio" name="quiz-07_Working-with-skills-easy-3" value="0"> Code execution and file creation</label><label data-choice="Two-factor authentication"><input type="radio" name="quiz-07_Working-with-skills-easy-3" value="1"> Two-factor authentication</label><label data-choice="The AI Fluency newsletter subscription"><input type="radio" name="quiz-07_Working-with-skills-easy-3" value="2"> The AI Fluency newsletter subscription</label><label data-choice="A public developer profile"><input type="radio" name="quiz-07_Working-with-skills-easy-3" value="3"> A public developer profile</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills function within a secure sandboxed computing environment and require code execution to be toggled on to work.</div>
</div><div class="qitem" data-correct="To ensure Skills created for Claude can work across other AI platforms that adopt the standard.">
<p class="qtext"><strong>5.</strong> What is the purpose of the &#x27;Agent Skills&#x27; open standard available at agentskills.io?</p>
<div class="qchoices"><label data-choice="To ensure Skills created for Claude can work across other AI platforms that adopt the standard."><input type="radio" name="quiz-07_Working-with-skills-easy-4" value="0"> To ensure Skills created for Claude can work across other AI platforms that adopt the standard.</label><label data-choice="To provide a leaderboard for the most popular AI prompts."><input type="radio" name="quiz-07_Working-with-skills-easy-4" value="1"> To provide a leaderboard for the most popular AI prompts.</label><label data-choice="To act as a payment gateway for purchasing premium Skills."><input type="radio" name="quiz-07_Working-with-skills-easy-4" value="2"> To act as a payment gateway for purchasing premium Skills.</label><label data-choice="To host the legal terms of service for Anthropic models."><input type="radio" name="quiz-07_Working-with-skills-easy-4" value="3"> To host the legal terms of service for Anthropic models.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">The open standard prevents vendor lock-in, allowing the same Skill format to be utilized by various AI tools and platforms.</div>
</div><div class="qitem" data-correct="Quarterly">
<p class="qtext"><strong>6.</strong> How often is the &#x27;AI Fluency&#x27; newsletter delivered to subscribers?</p>
<div class="qchoices"><label data-choice="Quarterly"><input type="radio" name="quiz-07_Working-with-skills-easy-5" value="0"> Quarterly</label><label data-choice="Weekly"><input type="radio" name="quiz-07_Working-with-skills-easy-5" value="1"> Weekly</label><label data-choice="Daily"><input type="radio" name="quiz-07_Working-with-skills-easy-5" value="2"> Daily</label><label data-choice="Annually"><input type="radio" name="quiz-07_Working-with-skills-easy-5" value="3"> Annually</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">The source material explicitly states the newsletter is delivered quarterly to the user&#x27;s inbox.</div>
</div><div class="qitem" data-correct="By interviewing the user about their workflow and goals.">
<p class="qtext"><strong>7.</strong> When creating a custom Skill through conversation, how does Claude gather the necessary details?</p>
<div class="qchoices"><label data-choice="By interviewing the user about their workflow and goals."><input type="radio" name="quiz-07_Working-with-skills-easy-6" value="0"> By interviewing the user about their workflow and goals.</label><label data-choice="By automatically scanning the user&#x27;s local hard drive for templates."><input type="radio" name="quiz-07_Working-with-skills-easy-6" value="1"> By automatically scanning the user&#x27;s local hard drive for templates.</label><label data-choice="By requiring the user to write a complete Python script first."><input type="radio" name="quiz-07_Working-with-skills-easy-6" value="2"> By requiring the user to write a complete Python script first.</label><label data-choice="By analyzing the user&#x27;s previous 100 chats to guess their needs."><input type="radio" name="quiz-07_Working-with-skills-easy-6" value="3"> By analyzing the user&#x27;s previous 100 chats to guess their needs.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude initiates a conversational process, asking questions about what the skill should do and what constitutes high-quality output.</div>
</div><div class="qitem" data-correct="Partner skills">
<p class="qtext"><strong>8.</strong> Which type of Skill is professionally built by partners like Figma or Notion to work with MCP connectors?</p>
<div class="qchoices"><label data-choice="Partner skills"><input type="radio" name="quiz-07_Working-with-skills-easy-7" value="0"> Partner skills</label><label data-choice="Anthropic Skills"><input type="radio" name="quiz-07_Working-with-skills-easy-7" value="1"> Anthropic Skills</label><label data-choice="Organization provisioned skills"><input type="radio" name="quiz-07_Working-with-skills-easy-7" value="2"> Organization provisioned skills</label><label data-choice="Custom instructions"><input type="radio" name="quiz-07_Working-with-skills-easy-7" value="3"> Custom instructions</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Partner skills are specifically designed by third-party organizations to integrate their services deeply with Claude.</div>
</div><div class="qitem" data-correct="It prevents context window overload by loading only relevant information.">
<p class="qtext"><strong>9.</strong> What is the primary benefit of &#x27;progressive disclosure&#x27; in the context of Claude Skills?</p>
<div class="qchoices"><label data-choice="It prevents context window overload by loading only relevant information."><input type="radio" name="quiz-07_Working-with-skills-easy-8" value="0"> It prevents context window overload by loading only relevant information.</label><label data-choice="It hides the cost of API calls from the end user."><input type="radio" name="quiz-07_Working-with-skills-easy-8" value="1"> It hides the cost of API calls from the end user.</label><label data-choice="It prevents users from seeing the internal logic of the Skill."><input type="radio" name="quiz-07_Working-with-skills-easy-8" value="2"> It prevents users from seeing the internal logic of the Skill.</label><label data-choice="It allows Claude to bypass the safety filters of the model."><input type="radio" name="quiz-07_Working-with-skills-easy-8" value="3"> It allows Claude to bypass the safety filters of the model.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">By loading only the information needed for a specific task, Claude remains efficient and avoids filling its memory with unnecessary data.</div>
</div><div class="qitem" data-correct="False">
<p class="qtext"><strong>10.</strong> True or False: Custom Skills you upload to your individual account are automatically shared with all other Claude users globally.</p>
<div class="qchoices"><label data-choice="False"><input type="radio" name="quiz-07_Working-with-skills-easy-9" value="0"> False</label><label data-choice="True"><input type="radio" name="quiz-07_Working-with-skills-easy-9" value="1"> True</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">The source material states that custom Skills you upload are private to your individual account unless provisioned by an organization owner.</div>
</div></div><div class="quiz-panel" data-level="medium" style="display:none"><div class="qitem" data-correct="They are folders of instructions and resources loaded dynamically to improve performance on specialized tasks.">
<p class="qtext"><strong>1.</strong> What is the primary technical function of &#x27;Skills&#x27; in the Claude ecosystem?</p>
<div class="qchoices"><label data-choice="They serve as static databases that Claude references for historical facts."><input type="radio" name="quiz-07_Working-with-skills-medium-0" value="0"> They serve as static databases that Claude references for historical facts.</label><label data-choice="They are folders of instructions and resources loaded dynamically to improve performance on specialized tasks."><input type="radio" name="quiz-07_Working-with-skills-medium-0" value="1"> They are folders of instructions and resources loaded dynamically to improve performance on specialized tasks.</label><label data-choice="They are permanent system prompts that apply to every conversation across all platforms."><input type="radio" name="quiz-07_Working-with-skills-medium-0" value="2"> They are permanent system prompts that apply to every conversation across all platforms.</label><label data-choice="They are hard-coded software updates that require manual installation by the user."><input type="radio" name="quiz-07_Working-with-skills-medium-0" value="3"> They are hard-coded software updates that require manual installation by the user.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills are designed as expertise packages that teach Claude how to complete tasks in a repeatable, efficient way.</div>
</div><div class="qitem" data-correct="Projects provide static background knowledge, while Skills provide procedural knowledge for executing tasks.">
<p class="qtext"><strong>2.</strong> When comparing Skills and Projects in Claude, which statement best describes their distinct roles?</p>
<div class="qchoices"><label data-choice="Projects define the &#x27;how&#x27; (processes), while Skills provide the &#x27;what&#x27; (knowledge)."><input type="radio" name="quiz-07_Working-with-skills-medium-1" value="0"> Projects define the &#x27;how&#x27; (processes), while Skills provide the &#x27;what&#x27; (knowledge).</label><label data-choice="Projects provide static background knowledge, while Skills provide procedural knowledge for executing tasks."><input type="radio" name="quiz-07_Working-with-skills-medium-1" value="1"> Projects provide static background knowledge, while Skills provide procedural knowledge for executing tasks.</label><label data-choice="Skills are for Team plans only, whereas Projects are available to all users."><input type="radio" name="quiz-07_Working-with-skills-medium-1" value="2"> Skills are for Team plans only, whereas Projects are available to all users.</label><label data-choice="Projects require coding knowledge to set up, while Skills are created using only Markdown."><input type="radio" name="quiz-07_Working-with-skills-medium-1" value="3"> Projects require coding knowledge to set up, while Skills are created using only Markdown.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Projects act as knowledge hubs for reference, while Skills act as procedural machines to execute specific methodologies.</div>
</div><div class="qitem" data-correct="Code execution and file creation">
<p class="qtext"><strong>3.</strong> Which setting must be enabled for Skills to function within the Claude environment?</p>
<div class="qchoices"><label data-choice="Automated Email Responses"><input type="radio" name="quiz-07_Working-with-skills-medium-2" value="0"> Automated Email Responses</label><label data-choice="Developer Mode Preview"><input type="radio" name="quiz-07_Working-with-skills-medium-2" value="1"> Developer Mode Preview</label><label data-choice="Code execution and file creation"><input type="radio" name="quiz-07_Working-with-skills-medium-2" value="2"> Code execution and file creation</label><label data-choice="Third-party Cookie Tracking"><input type="radio" name="quiz-07_Working-with-skills-medium-2" value="3"> Third-party Cookie Tracking</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills require Claude&#x27;s secure sandboxed computing environment to execute the scripts and instructions they contain.</div>
</div><div class="qitem" data-correct="Claude creates a new version of the document rather than editing the original in place.">
<p class="qtext"><strong>4.</strong> How does Claude typically handle existing files when using document-related Skills in a chat?</p>
<div class="qchoices"><label data-choice="Claude overwrites the original file permanently on your local drive."><input type="radio" name="quiz-07_Working-with-skills-medium-3" value="0"> Claude overwrites the original file permanently on your local drive.</label><label data-choice="Claude creates a new version of the document rather than editing the original in place."><input type="radio" name="quiz-07_Working-with-skills-medium-3" value="1"> Claude creates a new version of the document rather than editing the original in place.</label><label data-choice="Claude deletes the source file once the analysis is complete."><input type="radio" name="quiz-07_Working-with-skills-medium-3" value="2"> Claude deletes the source file once the analysis is complete.</label><label data-choice="Claude can only read files but cannot generate new versions of spreadsheets or slides."><input type="radio" name="quiz-07_Working-with-skills-medium-3" value="3"> Claude can only read files but cannot generate new versions of spreadsheets or slides.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">For security and version control, Claude generates a fresh output file based on your instructions and the source material.</div>
</div><div class="qitem" data-correct="It ensures that skills created for Claude are compatible with other AI platforms that adopt the standard.">
<p class="qtext"><strong>5.</strong> What is the primary benefit of the &#x27;Agent Skills&#x27; open standard available at agentskills.io?</p>
<div class="qchoices"><label data-choice="It ensures that skills created for Claude are compatible with other AI platforms that adopt the standard."><input type="radio" name="quiz-07_Working-with-skills-medium-4" value="0"> It ensures that skills created for Claude are compatible with other AI platforms that adopt the standard.</label><label data-choice="It provides a marketplace where users must buy Skills using digital currency."><input type="radio" name="quiz-07_Working-with-skills-medium-4" value="1"> It provides a marketplace where users must buy Skills using digital currency.</label><label data-choice="It limits the use of Skills to only Python-based applications."><input type="radio" name="quiz-07_Working-with-skills-medium-4" value="2"> It limits the use of Skills to only Python-based applications.</label><label data-choice="It automatically translates all Skills into multiple languages without human review."><input type="radio" name="quiz-07_Working-with-skills-medium-4" value="3"> It automatically translates all Skills into multiple languages without human review.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">The open standard prevents vendor lock-in, allowing procedural knowledge to be portable across different tools.</div>
</div><div class="qitem" data-correct="Organization Owners">
<p class="qtext"><strong>6.</strong> In the context of organization-wide deployment, who is responsible for provisioning Skills for all users on Team and Enterprise plans?</p>
<div class="qchoices"><label data-choice="Individual end-users"><input type="radio" name="quiz-07_Working-with-skills-medium-5" value="0"> Individual end-users</label><label data-choice="Anthropic Support Staff"><input type="radio" name="quiz-07_Working-with-skills-medium-5" value="1"> Anthropic Support Staff</label><label data-choice="Organization Owners"><input type="radio" name="quiz-07_Working-with-skills-medium-5" value="2"> Organization Owners</label><label data-choice="The Agent Skills Open Standard Committee"><input type="radio" name="quiz-07_Working-with-skills-medium-5" value="3"> The Agent Skills Open Standard Committee</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Owners have the administrative authority to provision and manage Skills in the Admin settings for their entire team.</div>
</div><div class="qitem" data-correct="MCP connects Claude to external services, while Skills provide the &#x27;how-to&#x27; procedural knowledge for tasks.">
<p class="qtext"><strong>7.</strong> Which of the following is a key difference between Skills and the Model Context Protocol (MCP)?</p>
<div class="qchoices"><label data-choice="Skills provide external data connections, while MCP provides internal instructions."><input type="radio" name="quiz-07_Working-with-skills-medium-6" value="0"> Skills provide external data connections, while MCP provides internal instructions.</label><label data-choice="MCP connects Claude to external services, while Skills provide the &#x27;how-to&#x27; procedural knowledge for tasks."><input type="radio" name="quiz-07_Working-with-skills-medium-6" value="1"> MCP connects Claude to external services, while Skills provide the &#x27;how-to&#x27; procedural knowledge for tasks.</label><label data-choice="Skills are only for document creation, while MCP is only for coding."><input type="radio" name="quiz-07_Working-with-skills-medium-6" value="2"> Skills are only for document creation, while MCP is only for coding.</label><label data-choice="Skills are loaded automatically, while MCP connections must be manually typed into every prompt."><input type="radio" name="quiz-07_Working-with-skills-medium-6" value="3"> Skills are loaded automatically, while MCP connections must be manually typed into every prompt.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">MCP acts as the connector to tools like Notion or Figma, while Skills teach Claude how to use those tools effectively.</div>
</div><div class="qitem" data-correct="Engaging in a conversation with Claude where it interviews you about your workflow.">
<p class="qtext"><strong>8.</strong> What is the recommended &#x27;easiest&#x27; way to create a custom Skill according to Anthropic&#x27;s learning resources?</p>
<div class="qchoices"><label data-choice="Writing complex Python scripts from scratch in a dedicated IDE."><input type="radio" name="quiz-07_Working-with-skills-medium-7" value="0"> Writing complex Python scripts from scratch in a dedicated IDE.</label><label data-choice="Engaging in a conversation with Claude where it interviews you about your workflow."><input type="radio" name="quiz-07_Working-with-skills-medium-7" value="1"> Engaging in a conversation with Claude where it interviews you about your workflow.</label><label data-choice="Downloading a template from a third-party social media site."><input type="radio" name="quiz-07_Working-with-skills-medium-7" value="2"> Downloading a template from a third-party social media site.</label><label data-choice="Submitting a formal request ticket to the Anthropic Academy."><input type="radio" name="quiz-07_Working-with-skills-medium-7" value="3"> Submitting a formal request ticket to the Anthropic Academy.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Claude can guide the creation process by asking about goals, examples, and rules, then generating the skill file for you.</div>
</div><div class="qitem" data-correct="Anthropic Skills">
<p class="qtext"><strong>9.</strong> Which type of Skill is described as being &#x27;automatically invoked&#x27; by Claude without requiring manual user intervention?</p>
<div class="qchoices"><label data-choice="Partner Skills"><input type="radio" name="quiz-07_Working-with-skills-medium-8" value="0"> Partner Skills</label><label data-choice="Anthropic Skills"><input type="radio" name="quiz-07_Working-with-skills-medium-8" value="1"> Anthropic Skills</label><label data-choice="Organization-provisioned Skills"><input type="radio" name="quiz-07_Working-with-skills-medium-8" value="2"> Organization-provisioned Skills</label><label data-choice="Legacy Skills"><input type="radio" name="quiz-07_Working-with-skills-medium-8" value="3"> Legacy Skills</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Anthropic-built skills for document creation (like Excel or PDF) are invoked by Claude as soon as the task becomes relevant.</div>
</div><div class="qitem" data-correct="A mention of the Skill will typically appear in Claude&#x27;s &#x27;chain of thought&#x27; as it processes the task.">
<p class="qtext"><strong>10.</strong> What happens when Claude loads a Skill during a conversation?</p>
<div class="qchoices"><label data-choice="The entire chat history is deleted to make room for the new instructions."><input type="radio" name="quiz-07_Working-with-skills-medium-9" value="0"> The entire chat history is deleted to make room for the new instructions.</label><label data-choice="A mention of the Skill will typically appear in Claude&#x27;s &#x27;chain of thought&#x27; as it processes the task."><input type="radio" name="quiz-07_Working-with-skills-medium-9" value="1"> A mention of the Skill will typically appear in Claude&#x27;s &#x27;chain of thought&#x27; as it processes the task.</label><label data-choice="The user is logged out and must re-authenticate to verify security permissions."><input type="radio" name="quiz-07_Working-with-skills-medium-9" value="2"> The user is logged out and must re-authenticate to verify security permissions.</label><label data-choice="Claude stops the conversation and requires the user to manually click a &#x27;Load&#x27; button."><input type="radio" name="quiz-07_Working-with-skills-medium-9" value="3"> Claude stops the conversation and requires the user to manually click a &#x27;Load&#x27; button.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Users can observe Claude identifying and applying the relevant Skill as part of its internal reasoning process.</div>
</div></div><div class="quiz-panel" data-level="hard" style="display:none"><div class="qitem" data-correct="It prevents context window overload by only loading relevant procedural information as needed.">
<p class="qtext"><strong>1.</strong> How does the &#x27;progressive disclosure&#x27; mechanism specifically improve Claude&#x27;s efficiency when utilizing Skills?</p>
<div class="qchoices"><label data-choice="It prevents context window overload by only loading relevant procedural information as needed."><input type="radio" name="quiz-07_Working-with-skills-hard-0" value="0"> It prevents context window overload by only loading relevant procedural information as needed.</label><label data-choice="It allows Claude to bypass the token limit by storing instructions in an external cache."><input type="radio" name="quiz-07_Working-with-skills-hard-0" value="1"> It allows Claude to bypass the token limit by storing instructions in an external cache.</label><label data-choice="It prioritizes Anthropic-built Skills over custom Skills to ensure security compliance."><input type="radio" name="quiz-07_Working-with-skills-hard-0" value="2"> It prioritizes Anthropic-built Skills over custom Skills to ensure security compliance.</label><label data-choice="It encrypts user data before processing it through the sandboxed computing environment."><input type="radio" name="quiz-07_Working-with-skills-hard-0" value="3"> It encrypts user data before processing it through the sandboxed computing environment.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Loading only the necessary instructions for the current task helps keep the context window clear of unnecessary data.</div>
</div><div class="qitem" data-correct="Skills">
<p class="qtext"><strong>2.</strong> An organization wants to ensure all employees use a specific methodology for financial auditing. Which feature is most appropriate for this repeatable, step-by-step procedural requirement?</p>
<div class="qchoices"><label data-choice="Projects"><input type="radio" name="quiz-07_Working-with-skills-hard-1" value="0"> Projects</label><label data-choice="Model Context Protocol (MCP)"><input type="radio" name="quiz-07_Working-with-skills-hard-1" value="1"> Model Context Protocol (MCP)</label><label data-choice="Skills"><input type="radio" name="quiz-07_Working-with-skills-hard-1" value="2"> Skills</label><label data-choice="Custom Instructions"><input type="radio" name="quiz-07_Working-with-skills-hard-1" value="3"> Custom Instructions</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills act as expertise packages that define procedural knowledge and repeatable methodologies for Claude to follow.</div>
</div><div class="qitem" data-correct="Code execution and file creation must be enabled within the Capabilities menu.">
<p class="qtext"><strong>3.</strong> Which technical prerequisite must be met in Claude&#x27;s settings for Skills to function correctly?</p>
<div class="qchoices"><label data-choice="A Max or Enterprise subscription is the only way to access the Skills interface."><input type="radio" name="quiz-07_Working-with-skills-hard-2" value="0"> A Max or Enterprise subscription is the only way to access the Skills interface.</label><label data-choice="Code execution and file creation must be enabled within the Capabilities menu."><input type="radio" name="quiz-07_Working-with-skills-hard-2" value="1"> Code execution and file creation must be enabled within the Capabilities menu.</label><label data-choice="The Agent Skills open standard must be manually installed via an external SDK."><input type="radio" name="quiz-07_Working-with-skills-hard-2" value="2"> The Agent Skills open standard must be manually installed via an external SDK.</label><label data-choice="All files must be converted to Markdown format before being uploaded to a Skill folder."><input type="radio" name="quiz-07_Working-with-skills-hard-2" value="3"> All files must be converted to Markdown format before being uploaded to a Skill folder.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills rely on Claude&#x27;s secure sandboxed computing environment, which requires these specific capabilities to be active.</div>
</div><div class="qitem" data-correct="It allows Skills created for Claude to be used across other AI platforms that adopt the standard.">
<p class="qtext"><strong>4.</strong> What is a primary advantage of the &#x27;Agent Skills&#x27; specification being an open standard available at agentskills.io?</p>
<div class="qchoices"><label data-choice="It allows Skills created for Claude to be used across other AI platforms that adopt the standard."><input type="radio" name="quiz-07_Working-with-skills-hard-3" value="0"> It allows Skills created for Claude to be used across other AI platforms that adopt the standard.</label><label data-choice="It guarantees that all Skills in the directory have been verified by Anthropic&#x27;s security team."><input type="radio" name="quiz-07_Working-with-skills-hard-3" value="1"> It guarantees that all Skills in the directory have been verified by Anthropic&#x27;s security team.</label><label data-choice="It automatically converts Python scripts into Markdown instructions for easier editing."><input type="radio" name="quiz-07_Working-with-skills-hard-3" value="2"> It automatically converts Python scripts into Markdown instructions for easier editing.</label><label data-choice="It removes the need for Code Execution to be toggled on in individual user settings."><input type="radio" name="quiz-07_Working-with-skills-hard-3" value="3"> It removes the need for Code Execution to be toggled on in individual user settings.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Portability ensures that users are not locked into a single ecosystem when developing complex procedural workflows.</div>
</div><div class="qitem" data-correct="Claude generates a new version of the document with the suggested changes or analyses.">
<p class="qtext"><strong>5.</strong> In the context of document editing, how does Claude handle an uploaded PowerPoint file when a relevant Skill is invoked?</p>
<div class="qchoices"><label data-choice="Claude edits the original file in its source location via a direct API connection."><input type="radio" name="quiz-07_Working-with-skills-hard-4" value="0"> Claude edits the original file in its source location via a direct API connection.</label><label data-choice="Claude generates a new version of the document with the suggested changes or analyses."><input type="radio" name="quiz-07_Working-with-skills-hard-4" value="1"> Claude generates a new version of the document with the suggested changes or analyses.</label><label data-choice="Claude converts the file to a PDF permanently to ensure formatting consistency."><input type="radio" name="quiz-07_Working-with-skills-hard-4" value="2"> Claude converts the file to a PDF permanently to ensure formatting consistency.</label><label data-choice="Claude requires the user to manually copy the generated code into a local compiler to create the file."><input type="radio" name="quiz-07_Working-with-skills-hard-4" value="3"> Claude requires the user to manually copy the generated code into a local compiler to create the file.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">In Chat, Claude works within a contained environment to output an updated version, preserving the original file.</div>
</div><div class="qitem" data-correct="Provisioned skills are automatically distributed to all team members&#x27; lists by Owners.">
<p class="qtext"><strong>6.</strong> How do &#x27;Organization provisioned skills&#x27; differ from &#x27;Custom Skills&#x27; in a Team or Enterprise environment?</p>
<div class="qchoices"><label data-choice="Provisioned skills are automatically distributed to all team members&#x27; lists by Owners."><input type="radio" name="quiz-07_Working-with-skills-hard-5" value="0"> Provisioned skills are automatically distributed to all team members&#x27; lists by Owners.</label><label data-choice="Provisioned skills are restricted to document creation, while custom skills handle data analysis."><input type="radio" name="quiz-07_Working-with-skills-hard-5" value="1"> Provisioned skills are restricted to document creation, while custom skills handle data analysis.</label><label data-choice="Provisioned skills do not require code execution to be enabled at the user level."><input type="radio" name="quiz-07_Working-with-skills-hard-5" value="2"> Provisioned skills do not require code execution to be enabled at the user level.</label><label data-choice="Provisioned skills are publicly accessible in the Skills Directory for all Anthropic users."><input type="radio" name="quiz-07_Working-with-skills-hard-5" value="3"> Provisioned skills are publicly accessible in the Skills Directory for all Anthropic users.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Provisioning allows for centralized management and consistency across an entire organization without individual setup.</div>
</div><div class="qitem" data-correct="Claude generates a structured file which the user must then save to their account.">
<p class="qtext"><strong>7.</strong> When creating a Custom Skill through conversation, what is the final step in the process according to the training materials?</p>
<div class="qchoices"><label data-choice="Manually coding a manifest.json file to define the skill&#x27;s entry point."><input type="radio" name="quiz-07_Working-with-skills-hard-6" value="0"> Manually coding a manifest.json file to define the skill&#x27;s entry point.</label><label data-choice="Claude generates a structured file which the user must then save to their account."><input type="radio" name="quiz-07_Working-with-skills-hard-6" value="1"> Claude generates a structured file which the user must then save to their account.</label><label data-choice="Submitting the skill to the Anthropic Academy for certificate validation."><input type="radio" name="quiz-07_Working-with-skills-hard-6" value="2"> Submitting the skill to the Anthropic Academy for certificate validation.</label><label data-choice="Toggling on &#x27;Allow limited network access&#x27; in the Admin console."><input type="radio" name="quiz-07_Working-with-skills-hard-6" value="3"> Toggling on &#x27;Allow limited network access&#x27; in the Admin console.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">The final step involves saving the structured skill file Claude produces during the interview process.</div>
</div><div class="qitem" data-correct="Skills provide the procedural &#x27;how-to&#x27; instructions, while MCP provides the &#x27;access&#x27; to external tools and data.">
<p class="qtext"><strong>8.</strong> What is the primary relationship between Skills and the Model Context Protocol (MCP)?</p>
<div class="qchoices"><label data-choice="Skills provide the procedural &#x27;how-to&#x27; instructions, while MCP provides the &#x27;access&#x27; to external tools and data."><input type="radio" name="quiz-07_Working-with-skills-hard-7" value="0"> Skills provide the procedural &#x27;how-to&#x27; instructions, while MCP provides the &#x27;access&#x27; to external tools and data.</label><label data-choice="MCP replaces the need for Skills by allowing Claude to learn procedures directly from external websites."><input type="radio" name="quiz-07_Working-with-skills-hard-7" value="1"> MCP replaces the need for Skills by allowing Claude to learn procedures directly from external websites.</label><label data-choice="Skills are a subset of MCP designed specifically for legacy document formats like .doc and .xls."><input type="radio" name="quiz-07_Working-with-skills-hard-7" value="2"> Skills are a subset of MCP designed specifically for legacy document formats like .doc and .xls.</label><label data-choice="A Skill must be converted into an MCP connector before it can be shared with an organization."><input type="radio" name="quiz-07_Working-with-skills-hard-7" value="3"> A Skill must be converted into an MCP connector before it can be shared with an organization.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills and MCP are complementary: one handles the logic and workflow, while the other handles the external connections.</div>
</div><div class="qitem" data-correct="False">
<p class="qtext"><strong>9.</strong> True or False: Users on the Free plan can currently execute custom Skills but cannot create them.</p>
<div class="qchoices"><label data-choice="True"><input type="radio" name="quiz-07_Working-with-skills-hard-8" value="0"> True</label><label data-choice="False"><input type="radio" name="quiz-07_Working-with-skills-hard-8" value="1"> False</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Skills are a feature preview for paid plans; while Free users might read about them, the capability is not currently available for them.</div>
</div><div class="qitem" data-correct="Always review the contents of a custom Skill from an external source before use.">
<p class="qtext"><strong>10.</strong> Which of these is a cited security best practice when working with Custom Skills?</p>
<div class="qchoices"><label data-choice="Always review the contents of a custom Skill from an external source before use."><input type="radio" name="quiz-07_Working-with-skills-hard-9" value="0"> Always review the contents of a custom Skill from an external source before use.</label><label data-choice="Disable the sandboxed computing environment to speed up script execution."><input type="radio" name="quiz-07_Working-with-skills-hard-9" value="1"> Disable the sandboxed computing environment to speed up script execution.</label><label data-choice="Only use Skills that contain no Markdown formatting."><input type="radio" name="quiz-07_Working-with-skills-hard-9" value="2"> Only use Skills that contain no Markdown formatting.</label><label data-choice="Upload all company passwords to a central &#x27;Security Skill&#x27; for easy access."><input type="radio" name="quiz-07_Working-with-skills-hard-9" value="3"> Upload all company passwords to a central &#x27;Security Skill&#x27; for easy access.</label></div>
<button class="qcheck" onclick="checkAnswer(this)">Kiểm tra</button>
<div class="qfeedback" style="display:none">Because Skills can include executable code, verifying their logic is essential for maintaining a secure environment.</div>
</div></div></div>




## Thẻ học

<div class="fc-deck" id="fc-07_Working-with-skills" data-cards="[{&quot;front&quot;: &quot;Anthropic Academy cung cấp các tài nguyên chính nào cho người dùng?&quot;, &quot;back&quot;: &quot;Hướng dẫn phát triển API và các phương pháp triển khai doanh nghiệp tốt nhất.&quot;}, {&quot;front&quot;: &quot;Các chủ đề chính trong các khóa học mới của Anthropic Academy bao gồm những gì?&quot;, &quot;back&quot;: &quot;Sự lưu loát về AI (AI Fluency), phát triển API, Giao thức ngữ cảnh mô hình (MCP) và Claude Code.&quot;}, {&quot;front&quot;: &quot;Bản tin &#x27;AI Fluency&#x27; của Anthropic được gửi đến hộp thư với tần suất như thế nào?&quot;, &quot;back&quot;: &quot;Hàng quý (mỗi 3 tháng một lần).&quot;}, {&quot;front&quot;: &quot;Liệt kê 4 mô hình trí tuệ nhân tạo được nhắc đến của Anthropic.&quot;, &quot;back&quot;: &quot;Mythos preview, Opus, Sonnet và Haiku.&quot;}, {&quot;front&quot;: &quot;Sản phẩm &#x27;Claude Code&#x27; bao gồm các phiên bản nào cho doanh nghiệp?&quot;, &quot;back&quot;: &quot;Claude Code Enterprise và Claude Code Security.&quot;}, {&quot;front&quot;: &quot;Định nghĩa về &#x27;Skills&#x27; (Kỹ năng) trong Claude là gì?&quot;, &quot;back&quot;: &quot;Các thư mục chứa hướng dẫn, kịch bản và tài nguyên được tải linh hoạt để cải thiện hiệu suất cho các tác vụ chuyên biệt.&quot;}, {&quot;front&quot;: &quot;Tính năng Skills khả dụng cho những đối tượng người dùng nào?&quot;, &quot;back&quot;: &quot;Người dùng các gói Free, Pro, Max, Team và Enterprise.&quot;}, {&quot;front&quot;: &quot;Điều kiện tiên quyết về cài đặt để Skills có thể hoạt động là gì?&quot;, &quot;back&quot;: &quot;Tính năng thực thi mã (code execution) phải được bật.&quot;}, {&quot;front&quot;: &quot;Cơ chế &#x27;tiết lộ lũy tiến&#x27; (progressive disclosure) của Skills hoạt động như thế nào?&quot;, &quot;back&quot;: &quot;Claude xác định Skill nào phù hợp và chỉ tải thông tin cần thiết để hoàn thành tác vụ.&quot;}, {&quot;front&quot;: &quot;Lợi ích chính của cơ chế tải linh hoạt trong Skills là gì?&quot;, &quot;back&quot;: &quot;Giúp ngăn ngừa tình trạng quá tải cửa sổ ngữ cảnh (context window overload).&quot;}, {&quot;front&quot;: &quot;Anthropic Skills là gì?&quot;, &quot;back&quot;: &quot;Các kỹ năng do Anthropic tạo ra và duy trì, ví dụ như tạo tài liệu Excel, Word, PowerPoint và PDF nâng cao.&quot;}, {&quot;front&quot;: &quot;Custom Skills (Kỹ năng tùy chỉnh) được sử dụng cho mục đích gì?&quot;, &quot;back&quot;: &quot;Dành cho các quy trình làm việc chuyên biệt và các tác vụ đặc thù của cá nhân hoặc tổ chức.&quot;}, {&quot;front&quot;: &quot;Trong gói Team và Enterprise, ai có quyền cung cấp (provision) skills cho toàn bộ người dùng?&quot;, &quot;back&quot;: &quot;Chủ sở hữu tổ chức (Organization Owners).&quot;}, {&quot;front&quot;: &quot;Partner skills (Kỹ năng đối tác) có thể được tìm thấy ở đâu?&quot;, &quot;back&quot;: &quot;Trong Danh mục Kỹ năng (Skills Directory), từ các đối tác như Notion, Figma và Atlassian.&quot;}, {&quot;front&quot;: &quot;Lợi ích của việc sử dụng Skills đối với kiến thức tổ chức là gì?&quot;, &quot;back&quot;: &quot;Giúp đóng gói các quy trình làm việc, phương pháp hay nhất và kiến thức của công ty để Claude sử dụng nhất quán.&quot;}, {&quot;front&quot;: &quot;Người dùng không biết lập trình có thể tạo Skills bằng cách nào?&quot;, &quot;back&quot;: &quot;Viết hướng dẫn bằng định dạng Markdown mà không cần viết mã (no coding required).&quot;}, {&quot;front&quot;: &quot;Tiêu chuẩn mở dành cho các kỹ năng của AI agent được công bố tại địa chỉ website nào?&quot;, &quot;back&quot;: &quot;agentskills.io&quot;}, {&quot;front&quot;: &quot;Ngôn ngữ lập trình nào được sử dụng cho SDK tham chiếu của tiêu chuẩn Agent Skills?&quot;, &quot;back&quot;: &quot;Python&quot;}, {&quot;front&quot;: &quot;Sự khác biệt cơ bản về mục đích giữa &#x27;Projects&#x27; và &#x27;Skills&#x27; là gì?&quot;, &quot;back&quot;: &quot;Projects dùng để lưu trữ kiến thức tĩnh, trong khi Skills dùng để thực hiện các quy trình tác vụ.&quot;}, {&quot;front&quot;: &quot;Khi nào thông tin trong &#x27;Projects&#x27; được tải vào cuộc trò chuyện?&quot;, &quot;back&quot;: &quot;Luôn luôn được tải sẵn khi bắt đầu các cuộc trò chuyện bên trong dự án đó.&quot;}, {&quot;front&quot;: &quot;Mối quan hệ hỗ trợ giữa MCP và Skills là gì?&quot;, &quot;back&quot;: &quot;MCP kết nối Claude với dữ liệu bên ngoài, còn Skills dạy Claude cách sử dụng các công cụ đó hiệu quả.&quot;}, {&quot;front&quot;: &quot;So sánh phạm vi áp dụng giữa &#x27;Custom instructions&#x27; và &#x27;Skills&#x27;.&quot;, &quot;back&quot;: &quot;Custom instructions áp dụng cho mọi cuộc trò chuyện, còn Skills chỉ tải khi phù hợp với tác vụ cụ thể.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể tìm kiếm và khám phá các Skills có sẵn ở đâu trong tài khoản?&quot;, &quot;back&quot;: &quot;Trong mục &#x27;Customize&#x27;, sau đó điều hướng đến &#x27;Skills&#x27;.&quot;}, {&quot;front&quot;: &quot;Thời gian ước tính để hoàn thành bài học &#x27;Làm việc với Skills&#x27; là bao lâu?&quot;, &quot;back&quot;: &quot;15 phút.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để biết Claude đang sử dụng một Skill trong khi thực hiện yêu cầu?&quot;, &quot;back&quot;: &quot;Người dùng sẽ thấy Skill đó được nhắc đến trong chuỗi tư duy (chain of thought) của Claude.&quot;}, {&quot;front&quot;: &quot;Kết quả đầu ra khi Claude sử dụng Skill tạo tài liệu thường là gì?&quot;, &quot;back&quot;: &quot;Một tệp có thể tải xuống máy tính hoặc lưu trực tiếp vào Google Drive.&quot;}, {&quot;front&quot;: &quot;Khi thực hiện chỉnh sửa tài liệu trong Chat, Claude sẽ làm gì với tệp gốc?&quot;, &quot;back&quot;: &quot;Claude tạo ra một phiên bản mới của tài liệu thay vì chỉnh sửa trực tiếp trên tệp gốc.&quot;}, {&quot;front&quot;: &quot;Để sử dụng khả năng làm việc với tệp, người dùng cần bật tùy chọn mạng nào khi được nhắc?&quot;, &quot;back&quot;: &quot;Cho phép truy cập mạng hạn chế (Allow limited network access).&quot;}, {&quot;front&quot;: &quot;Lưu ý an toàn quan trọng nhất khi cài đặt Custom Skills là gì?&quot;, &quot;back&quot;: &quot;Chỉ cài đặt các Kỹ năng tùy chỉnh từ những nguồn đáng tin cậy.&quot;}, {&quot;front&quot;: &quot;Các Custom Skills mà người dùng tự tải lên có được chia sẻ công khai không?&quot;, &quot;back&quot;: &quot;Không, chúng ở chế độ riêng tư đối với tài khoản cá nhân của người dùng đó.&quot;}, {&quot;front&quot;: &quot;Cách dễ nhất để tạo một Custom Skill là gì?&quot;, &quot;back&quot;: &quot;Thông qua việc trò chuyện (interview) trực tiếp với Claude.&quot;}, {&quot;front&quot;: &quot;Sau khi Claude hoàn tất việc phỏng vấn người dùng về quy trình, Claude sẽ tạo ra tệp gì?&quot;, &quot;back&quot;: &quot;Một tệp chứa cấu trúc kỹ năng đã được định dạng đúng.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể làm gì để cải thiện các Skills hiện có theo thời gian?&quot;, &quot;back&quot;: &quot;Yêu cầu Claude chỉnh sửa kỹ năng và nó sẽ tự động cập nhật các tệp cho người dùng.&quot;}, {&quot;front&quot;: &quot;Ví dụ về một quy trình làm việc lặp lại có thể biến thành Skill là gì?&quot;, &quot;back&quot;: &quot;Đánh giá giọng điệu thương hiệu hoặc danh sách kiểm tra tuân thủ.&quot;}, {&quot;front&quot;: &quot;Trong bảng so sánh, &#x27;Projects&#x27; được ví như là &#x27;Knowledge hubs&#x27;, vậy &#x27;Skills&#x27; được ví là gì?&quot;, &quot;back&quot;: &quot;Các máy quy trình (Procedural machines).&quot;}, {&quot;front&quot;: &quot;Đâu là đường dẫn trong cài đặt để bật tính năng Skills?&quot;, &quot;back&quot;: &quot;Settings &gt; Capabilities &gt; Code execution and file creation.&quot;}, {&quot;front&quot;: &quot;Đối với gói Enterprise, điều kiện để thành viên truy cập Skills là gì?&quot;, &quot;back&quot;: &quot;Chủ sở hữu tổ chức phải bật cả Code execution và Skills trong phần Admin settings.&quot;}, {&quot;front&quot;: &quot;Đối với gói Team, tính năng xem trước Skills (feature preview) có mặc định không?&quot;, &quot;back&quot;: &quot;Có, nó được bật mặc định ở cấp độ tổ chức.&quot;}, {&quot;front&quot;: &quot;Claude Skills yêu cầu môi trường tính toán nào để hoạt động an toàn?&quot;, &quot;back&quot;: &quot;Môi trường tính toán hộp cát an toàn (secure sandboxed computing environment).&quot;}, {&quot;front&quot;: &quot;Tại sao tài liệu tham khảo (style guides, brand assets) lại quan trọng khi tạo Skill?&quot;, &quot;back&quot;: &quot;Chúng giúp Claude hiểu chính xác các tiêu chuẩn và kết quả mong đợi của người dùng.&quot;}, {&quot;front&quot;: &quot;Trong Claude 101, feedback từ người dùng được thu thập nhằm mục đích gì?&quot;, &quot;back&quot;: &quot;Để cải thiện các phiên bản tương lai của khóa học.&quot;}, {&quot;front&quot;: &quot;Tài liệu &#x27;Claude 101 course feedback&#x27; yêu cầu người dùng thừa nhận chính sách nào?&quot;, &quot;back&quot;: &quot;Chính sách quyền riêng tư của Anthropic (Anthropic Privacy Policy).&quot;}, {&quot;front&quot;: &quot;Người dùng có thể cung cấp thông tin liên hệ nào trong biểu mẫu feedback để Anthropic theo dõi?&quot;, &quot;back&quot;: &quot;Tên và Email (tùy chọn).&quot;}, {&quot;front&quot;: &quot;Claude Code là một công cụ hỗ trợ cho đối tượng nào?&quot;, &quot;back&quot;: &quot;Các lập trình viên (Developers).&quot;}, {&quot;front&quot;: &quot;Claude cho Chrome và Claude cho Slack là các ví dụ về loại sản phẩm nào?&quot;, &quot;back&quot;: &quot;Tiện ích mở rộng và tích hợp nền tảng của Claude.&quot;}, {&quot;front&quot;: &quot;Trong &#x27;Solutions&#x27;, Anthropic cung cấp giải pháp cho các ngành nghề nào?&quot;, &quot;back&quot;: &quot;Dịch vụ tài chính, chính phủ, y tế, khoa học đời sống và phi lợi nhuận.&quot;}, {&quot;front&quot;: &quot;Bản tin AI Fluency được gửi qua hình thức nào?&quot;, &quot;back&quot;: &quot;Email.&quot;}, {&quot;front&quot;: &quot;Gói đăng ký cao nhất dành cho doanh nghiệp lớn được gọi là gì?&quot;, &quot;back&quot;: &quot;Enterprise plan.&quot;}, {&quot;front&quot;: &quot;Địa chỉ website để xem tài liệu dành cho nhà phát triển là gì?&quot;, &quot;back&quot;: &quot;Developer docs (trong Claude Platform).&quot;}, {&quot;front&quot;: &quot;Năm bản quyền được ghi chú trên các tài liệu của Anthropic trong nguồn là năm nào?&quot;, &quot;back&quot;: &quot;2026 (hoặc 2025 trong một số đoạn văn bản).&quot;}, {&quot;front&quot;: &quot;Mô hình Claude nào được đánh dấu là phiên bản &#x27;preview&#x27;?&quot;, &quot;back&quot;: &quot;Mythos preview.&quot;}, {&quot;front&quot;: &quot;Người dùng có thể tìm thấy các ví dụ về câu chuyện khách hàng (customer stories) ở đâu?&quot;, &quot;back&quot;: &quot;Trong phần Resources (Tài nguyên) trên trang web của Anthropic.&quot;}, {&quot;front&quot;: &quot;Skills giúp cải thiện hiệu suất cụ thể ở những khía cạnh nào?&quot;, &quot;back&quot;: &quot;Tính nhất quán, tốc độ và khả năng hoàn thành các nhiệm vụ phức tạp.&quot;}, {&quot;front&quot;: &quot;Nội dung của một Custom Skill bao gồm những thành phần cơ bản nào?&quot;, &quot;back&quot;: &quot;Hướng dẫn (instructions), kịch bản (scripts) và các tài nguyên liên quan.&quot;}, {&quot;front&quot;: &quot;Làm thế nào để truy cập vào Skills Directory?&quot;, &quot;back&quot;: &quot;Nhấp vào &#x27;Customize&#x27; &gt; &#x27;Skills&#x27; &gt; &#x27;+&#x27; &gt; &#x27;Browse skills&#x27;.&quot;}, {&quot;front&quot;: &quot;Để thực hiện phân tích dữ liệu chuyên sâu với Excel, Claude sử dụng loại Skill nào?&quot;, &quot;back&quot;: &quot;Anthropic Skills (Kỹ năng có sẵn của Anthropic).&quot;}, {&quot;front&quot;: &quot;Nếu một người dùng ở gói &#x27;Free&#x27; muốn thử nghiệm Skills thì sao?&quot;, &quot;back&quot;: &quot;Hiện tại họ chỉ có thể đọc để hiểu khái niệm vì đây là tính năng xem trước cho các gói trả phí.&quot;}, {&quot;front&quot;: &quot;Khi tạo Skill, bước cuối cùng sau khi Claude hoàn tất phỏng vấn là gì?&quot;, &quot;back&quot;: &quot;Lưu kỹ năng (Save your skill) để nó xuất hiện trong danh sách kỹ năng.&quot;}, {&quot;front&quot;: &quot;Ví dụ về một Skill đối tác tích hợp với MCP là gì?&quot;, &quot;back&quot;: &quot;Kỹ năng của Figma hoặc Atlassian hoạt động với các trình kết nối MCP tương ứng.&quot;}, {&quot;front&quot;: &quot;Sự khác biệt giữa &#x27;Anthropic Skills&#x27; và &#x27;Custom Skills&#x27; về mặt kích hoạt là gì?&quot;, &quot;back&quot;: &quot;Anthropic Skills tự động kích hoạt, còn Custom Skills do người dùng bật/tắt trong cài đặt.&quot;}]" data-cur="0" data-known="[]">
<div class="fc-progress">1 / 60</div>
<div class="fc-scene" onclick="fcFlip(this)"><div class="fc-card-inner"><div class="fc-front">Anthropic Academy cung cấp các tài nguyên chính nào cho người dùng?</div><div class="fc-back">Hướng dẫn phát triển API và các phương pháp triển khai doanh nghiệp tốt nhất.</div></div></div>
<p class="fc-hint">Nhấn thẻ để lật · Dùng nút để điều hướng</p>
<div class="fc-nav">
<button onclick="fcMove('fc-07_Working-with-skills',-1)">← Trước</button>
<button class="fc-know" onclick="fcKnow('fc-07_Working-with-skills',true)">Nhớ rồi ✓</button>
<button class="fc-unknown" onclick="fcKnow('fc-07_Working-with-skills',false)">Học lại ✗</button>
<button onclick="fcMove('fc-07_Working-with-skills',1)">Tiếp →</button>
</div>
<div class="fc-stats">Nhớ: 0 / 60</div>
</div>




## Sơ đồ tư duy

<div class="mm-wrap">
<svg id="mm-07_Working-with-skills" class="markmap"></svg>
</div>
<script>
(function(){
  var data={"name": "Anthropic AI Learning & Resources", "children": [{"name": "Anthropic Academy", "children": [{"name": "Featured Courses", "children": [{"name": "Claude 101"}, {"name": "Claude Code in Action"}, {"name": "AI Fluency"}, {"name": "Model Context Protocol"}]}, {"name": "Learning Paths", "children": [{"name": "Build with Claude (API)"}, {"name": "Claude for Work (Enterprise)"}, {"name": "Claude for Personal"}]}]}, {"name": "Skills Feature", "children": [{"name": "Definition", "children": [{"name": "Procedural Knowledge"}, {"name": "Dynamic Loading"}, {"name": "Instruction Folders"}]}, {"name": "Types of Skills", "children": [{"name": "Anthropic Built-in (Docs/Excel)"}, {"name": "Custom (User-created)"}, {"name": "Organization Provisioned"}, {"name": "Partner (Notion/Figma)"}]}, {"name": "Management", "children": [{"name": "Enable Code Execution"}, {"name": "Skills Directory"}, {"name": "Agent Skills Open Standard"}]}, {"name": "Comparison", "children": [{"name": "Skills vs Projects (Process vs Knowledge)"}, {"name": "Skills vs MCP (Procedural vs Connectivity)"}, {"name": "Skills vs Custom Instructions (Task-specific)"}]}]}, {"name": "Product Ecosystem", "children": [{"name": "Models", "children": [{"name": "Opus"}, {"name": "Sonnet"}, {"name": "Haiku"}, {"name": "Mythos"}]}, {"name": "Platforms", "children": [{"name": "Claude Code"}, {"name": "Claude Cowork"}, {"name": "Claude for Slack/Chrome"}, {"name": "API Console"}]}]}, {"name": "Resources & Support", "children": [{"name": "AI Fluency Newsletter"}, {"name": "Developer Docs"}, {"name": "Claude 101 Feedback Form"}, {"name": "Help Center & Tutorials"}]}]};
  function toMM(n){return{content:n.name||'',children:(n.children||[]).map(toMM)};}
  function init(){
    if(window.markmap&&window.markmap.Markmap){
      window.markmap.Markmap.create('#mm-07_Working-with-skills',null,toMM(data));
    } else {
      setTimeout(init,200);
    }
  }
  document.addEventListener('DOMContentLoaded',init);
})();
</script>


## Tài liệu liên quan

- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://www.anthropic.com/learn](https://www.anthropic.com/learn)
- [https://support.claude.com/en/articles/12512176-what-are-skills](https://support.claude.com/en/articles/12512176-what-are-skills)
- [https://forms.gle/sY9ou5fqZBd3TjHF8](https://forms.gle/sY9ou5fqZBd3TjHF8)



---
*[Nguồn gốc](https://anthropic.skilljar.com/claude-101/383396){: target="_blank" }*
