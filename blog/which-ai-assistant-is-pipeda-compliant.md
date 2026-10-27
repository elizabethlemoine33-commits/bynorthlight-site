---
layout: post
title: "Which AI Assistant Is PIPEDA Compliant? None of Them"
seo_title: "Which AI Assistant Is PIPEDA Compliant?"
description: "No AI tool is PIPEDA compliant on its own. Learn what Canadian businesses must do: policy, team tools, vendor documents, and shadow AI breaches."
og_title: "Which AI Assistant Is PIPEDA Compliant? None of Them"
og_description: "No AI tool is PIPEDA compliant on its own. Learn what Canadian businesses must do: policy, team tools, vendor documents, and shadow AI breaches."
date: 2026-10-27
date_modified: "2026-10-27"
published_time: "2026-10-27T00:00:00.000Z"
permalink: /blog/which-ai-assistant-is-pipeda-compliant.html
source_label: "Blog · Essay"
source_class: source-essay
read_time: 6
tags:
  - AI Compliance
  - PIPEDA
  - AI Governance
  - Compliance
related_reading:
  - title: "Implementing AI Without Breaking Canadian Privacy Law: A PIPEDA Guide for Business Owners"
    url: /blog/pipeda-privacy-first-ai-canada.html
  - title: "Shadow AI Is the New Shadow IT — What Leaders Need to Know"
    url: /blog/shadow-ai-is-the-new-shadow-it.html
  - title: "AI Adoption Checklist for Canadian Businesses (2026)"
    url: /blog/ai-adoption-checklist-canadian-businesses-2026.html
faq:
  - q: "Which AI assistant is PIPEDA compliant?"
    a: "None of them, on their own. PIPEDA compliance depends on what your organisation does with a tool, not on a certification the tool holds. The OPC's principles for generative AI put responsibility on the organisation using it."
  - q: "Does \"we don't train on your data\" mean an AI tool is safe for personal information?"
    a: "Not necessarily. Training settings can be switched on or off later, and details differ by plan. Read the vendor's terms of service, data addendum, data processing agreements, and privacy policy against each other."
  - q: "Does storing data in Canada protect it from foreign laws?"
    a: "Not by itself. One Canadian law firm notes that storing data in Canada does not on its own prevent access under foreign laws such as the US CLOUD Act. Who controls the data matters more than where it sits."
  - q: "Is an employee using a personal AI account for work a data breach?"
    a: "At the least, it's a misuse of the organisation's data, and possibly an unauthorised disclosure. In my reading it is a data breach of some sort, though that is not settled law. The OPC's breach guidance doesn't address personal AI accounts specifically. I'd treat it as a breach, follow your breach protocol, and investigate fully."
  - q: "How long do I need to keep breach records in Canada?"
    a: "The OPC guidance says you must keep records of all breaches for two years, whether or not there is a real risk of significant harm. Reporting to the OPC and notifying affected people apply when there is a real risk of significant harm."
---

<div class="at-a-glance" role="note">
  <h2>At a Glance</h2>
  <ul>
    <li>No AI assistant is <a href="https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/" rel="noopener">PIPEDA</a> compliant on its own. Compliance depends on what your organisation does with the tool.</li>
    <li>"We don't train on your data" isn't enough. Read the plan details, the vendor's documents, and who owns the tool.</li>
    <li>Write a policy, give your team a tool you can see into, make personal data hard to export, and read vendor documents against each other.</li>
    <li>Using personal AI accounts for organisational data is, at the least, a misuse of that data. Treat it as a breach.</li>
  </ul>
</div>

Which AI assistant is [PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/){:rel="noopener"} compliant? None of them. And the question is the wrong one, which is why you get unhelpful answers.

If you typed some version of that question into a search bar, you were probably hoping someone would name a tool, hand you a checkmark, and let you get back to work. I understand the hope. I also think you have suspected it wouldn't be that simple, which is why you're still reading.

## Can an AI tool be PIPEDA compliant?

<div class="answer-block">
<p>No. Compliance isn't a certification a tool holds; it depends on what your organisation does with the tool. Under the OPC's principles, responsibility sits with the organisation using it.</p>
</div>

No tool certification makes you compliant. It's always about what you do. [PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/){:rel="noopener"} (the Personal Information Protection and Electronic Documents Act) is federal privacy law, and the Office of the Privacy Commissioner of Canada (OPC) explains how it works in its [PIPEDA requirements in brief](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/){:rel="noopener"}.

The OPC's [principles for generative AI](https://www.priv.gc.ca/en/privacy-topics/technology/artificial-intelligence/gd_principles_ai/){:rel="noopener"} put the responsibility on the organisation using the tool, not on the tool, and say organisations should choose tools that respect privacy law.

Read that as a business owner and the question changes. It stops being "is this tool safe?" and becomes "what are we doing with it, who decided, and can we see it?" Our [AI adoption checklist for Canadian businesses](/blog/ai-adoption-checklist-canadian-businesses-2026.html) is built around those questions. If a tool can't be compliant on its own, the licence owner is responsible. If your staff are using personal accounts for the organisation's data, the organisation is responsible too.

One note on provinces. Some provinces have their own private-sector privacy laws that apply instead of [PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/){:rel="noopener"} for information collected, used, and disclosed within the province, while [PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/){:rel="noopener"} still covers cross-border and interprovincial transfers. The OPC page above explains which is which; check it for where you operate.

## Why isn't "we don't train on your data" enough?

<div class="answer-block">
<p>Because training settings can be switched on or off later, and details differ by plan. A promise on a vendor's front page and the fine print don't always match, and where the tool is owned matters as much as where it is hosted.</p>
</div>

Vendors will tell you they don't train on your data. I'd still read further, because you can switch training settings on or off later, and details differ by plan.

OpenAI's [help page for ChatGPT Business](https://help.openai.com/en/articles/8798634-managing-data-sharing-and-privacy-in-chatgpt-business){:rel="noopener"} says business workspace data is excluded from training by default. It also says members don't automatically see each other's chats, and that the workspace owner can export a member's data. Anthropic's [help page on model training](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training){:rel="noopener"} says that conversations flagged for safety review may still be used to improve its models even when you have opted out of training. That page covers its consumer products, so read the business terms for whatever plan you use.

I'm not pointing at these two to say one is better. I'm pointing them out because a promise on the front page and the details further down aren't always the same. As long as your information has the potential to be leaked, I'm hesitant to put it in.

Where the tool lives matters, and who owns it matters more. A Canadian-owned tool on Canadian servers is one thing. An American tool on a Canadian server is still an American tool: in the words of one Canadian law firm, [storing data in Canada does not, by itself, prevent access under foreign laws](https://www.blg.com/en/insights/2026/04/data-sovereignty-and-the-cloud-act-what-canadian-organizations-should-know){:rel="noopener"}, and who controls the data matters more than where it sits. That is the [US CLOUD Act](https://www.blg.com/en/insights/2026/04/data-sovereignty-and-the-cloud-act-what-canadian-organizations-should-know){:rel="noopener"} at work. American tools can still be a reasonable choice, as long as you tell people. Your [privacy policy](/blog/pipeda-privacy-first-ai-canada.html) should say their data may be processed by AI, and in another country.

## What steps should a Canadian business take to use AI responsibly?

<div class="answer-block">
<p>Write an AI policy, give the team a tool you can see into, block exports of personal data where you can't rely on people, and read all of a vendor's documents against each other. It also takes real investment in your team, policies, procedures, and tools.</p>
</div>

Here are four steps, in the order I'd do them.

1. **Write a policy for what can and can't go into AI.** It needs consequences, sign-off, and awareness by everyone. My own gut test is simple: does this data contain personal information? If yes, then the answer is just no. If you want a starting point, we have an [AI policy template](/blog/ai-policy-template-canadian-small-business.html) and a [printable PIPEDA checklist](/blog/pipeda-ai-compliance-checklist-printable.html).
2. **Give the team a team AI tool.** Claude, ChatGPT, or something else. Check what your plan lets the owner see before you choose. Claude's [plan comparison](https://claude.com/pricing){:rel="noopener"} lists usage analytics and spend controls on its team plan, with [audit logs](https://support.claude.com/en/articles/9970975-access-audit-logs){:rel="noopener"} and the compliance API on enterprise. OpenAI's [ChatGPT Business page](https://help.openai.com/en/articles/8798634-managing-data-sharing-and-privacy-in-chatgpt-business){:rel="noopener"} describes workspace usage and spend controls, and its [compliance platform](https://help.openai.com/en/articles/9261474-openai-compliance-platform-for-enterprise-and-edu-customers){:rel="noopener"} is for enterprise and Edu workspaces. People are excited and they want to try.
3. **Where you can't trust people to follow the policy, make it so they can't.** Block exports and copy-paste of personal data.
4. **Read all of a vendor's documents against each other.** That means the terms of service, the data addendum, the data processing and sharing agreements, and the privacy policy. Pull all the papers out, go through it, highlight, post-it note. Documents drift, and they can say different things. What you find should shape your own privacy policy, your terms and agreements, and what you tell clients, partners, and participants.

There is a real cost. If you choose to use AI, you need to invest in your team, your policies, your procedures, and your tools. There's no way around it.

## What happens when someone uses a personal AI account for work?

<div class="answer-block">
<p>At the least, it's a misuse of your organisation's data, and possibly an unauthorised disclosure. In my reading, treat it as a data breach: follow your breach protocol, investigate fully, and keep a record. That is not settled law.</p>
</div>

This is the quiet one, often called shadow AI, and it's the part I most want you to hear. Our posts on [shadow AI](/blog/shadow-ai-is-the-new-shadow-it.html) and the [shadow AI governance checklist](/blog/shadow-ai-governance-checklist-printable.html) go further. People get excited about AI and try everything through it. I don't think they're doing something they believe is wrong. They aren't stopping to consider what they can and can't upload. People have uploaded spreadsheets of financial data for advice without checking whether it is secure.

But if someone puts the organisation's data into a personal AI account, that is, at the least, a misuse of that data, and it may be an unauthorised disclosure of it. I believe that makes it a data breach of some sort. That is my reading, not settled law. The OPC defines a breach of security safeguards as the loss of, unauthorised access to, or unauthorised disclosure of personal information, and its [breach guidance](https://www.priv.gc.ca/en/privacy-topics/business-privacy/breaches-and-safeguards/privacy-breaches-at-your-business/gd_pb_201810/){:rel="noopener"} doesn't address staff using personal AI accounts specifically.

I'd treat it as a breach. Follow your breach protocol and the law that applies to you. Investigate fully:

- What happened, and what data was involved.
- Whether training was switched off on that account.
- Whether there is reputational risk.
- Whether your data insurance needs to be told.
- What else that person has done with it.

After investigating, there may be consequences, up to and including someone losing their job. It depends on how far it went and what was disclosed.

Keep a log of every breach. The OPC guidance says you must keep records of all breaches for two years, whether or not there is a real risk of significant harm. Reporting to the OPC and notifying the people affected apply when there is a real risk of significant harm. That test governs reporting and notifying; your own due diligence still applies as if the harm were real.

## How do you make informed choices about AI and privacy?

<div class="answer-block">
<p>There's no blanket answer, in either direction. Because this changes daily, make informed choices: write the policy, give your team a tool you can see into, make personal data hard to export, and read the documents against each other.</p>
</div>

There's no blanket answer, in either direction. This changes daily, so you have to make informed choices. Write the policy. Give your team a tool you can see into. Make personal data hard to export. Read the documents against each other. And if you'd like help writing or auditing an AI policy, email support@bynorthlight.ca.

This isn't legal advice. The pages I've linked are where you can check what applies to you.
