---
layout: post
title: "What Belongs in an AI Risk Register? A Starter for Canadian Small Business"
seo_title: "AI Risk Register for Canada"
description: "Canada has no AI-specific law yet. Here is how to build an AI risk register anyway, using the NIST, EU and ISO approaches and the one I keep."
og_title: "What Belongs in an AI Risk Register? A Starter for Canadian Small Business"
og_description: "Canada has no AI-specific law yet. Here is how to build an AI risk register anyway, using the NIST, EU and ISO approaches and the one I keep."
date: 2026-10-31
date_modified: "2026-10-31"
published_time: "2026-10-31T00:00:00.000Z"
permalink: /blog/ai-risk-register-canadian-small-business.html
source_label: "Blog · Guide"
source_class: source-essay
read_time: 8
tags:
  - "AI Governance"
  - "Canadian Business"
  - "Operations"
related_reading:
  - title: "Shadow AI Is the New Shadow IT: What Leaders Need to Know"
    url: /blog/shadow-ai-is-the-new-shadow-it.html
  - title: "AI Policy Template for Canadian Small Business"
    url: /blog/ai-policy-template-canadian-small-business.html
  - title: "Implementing AI Without Breaking Canadian Privacy Law: A PIPEDA Guide"
    url: /blog/pipeda-privacy-first-ai-canada.html
faq:
  - q: "What is an AI risk register?"
    a: "A central record of the risks that come from the AI you use: what could go wrong, how likely and how bad it would be, what you decided to do about it, and who owns it. NIST defines a risk register as a central record of current risks and related information for a given scope or organization."
  - q: "Does Canadian law require an AI risk register?"
    a: "As far as I can tell from the government's own pages, Canada has no regulatory framework specific to AI. Existing laws, including privacy law, still apply to how you use AI. A register is a way to know what you use and how, and to show you considered the risk. This is not legal advice."
  - q: "Do I need ISO 42001 certification to keep a risk register?"
    a: "No. ISO/IEC 42001 is a standard for managing AI, and you can work from it without certifying. I have done that: policies, procedures and a documented AI risk assessment, without going for certification."
  - q: "How often should I review an AI risk register?"
    a: "At least once a year, and whenever an AI system you rely on changes materially. Mine is reviewed each September and when a tool is added or a system changes."
---

<div class="at-a-glance" role="note">
  <h2>At a Glance</h2>
  <ul>
    <li>An AI risk register is a central record of your AI risks: what could go wrong, how bad, what you decided, and who owns it.</li>
    <li>Canada has no AI-specific regulation yet, but you are still responsible for knowing what you use and how.</li>
    <li>The U.S. NIST framework, the EU AI Act and ISO/IEC 42001 each take a different route to the same idea.</li>
    <li>You can build a useful register on a 1 to 5 scale in an afternoon, and review it once a year.</li>
  </ul>
</div>

Canada has no AI-specific law yet, and that is not the same as having no responsibility. If your team uses AI tools, you are still accountable for what goes into them and what comes out. The simplest way to show that you know what you are using, and how, is a risk register.

I keep one for Northlight Advisory Services. It is part of a set of policies and procedures I wrote while working through ISO standards, without going for certification. This is what a register is, how the main frameworks compare, and how to build your own.

## What is an AI risk register?

<div class="answer-block">
<p>A central record of the risks that come from the AI you use: what could go wrong, how likely and how bad it would be, what you decided to do about it, and who owns it. NIST defines a risk register as a central record of current risks and related information for a given scope or organization.</p>
</div>

[NIST's glossary](https://csrc.nist.gov/glossary/term/risk_register){:rel="noopener"} gives two definitions: a repository of risk information, including what is understood about risks over time, and a central record of current risks and related information. It adds that "current risks" include both accepted risks and risks with a planned fix. That matters. A register is not only a list of problems. It also shows which risks you looked at and chose to accept.

## Why keep one when no Canadian law requires it?

<div class="answer-block">
<p>Because the law that already exists still applies, and a register is how you show you know what you are using. The federal government's own page says there is currently no regulatory framework in Canada specific to AI. That does not mean AI sits outside the rules.</p>
</div>

The government's page on the proposed Artificial Intelligence and Data Act [describes it as proposed](https://ised-isde.canada.ca/site/innovation-better-canada/en/artificial-intelligence-and-data-act){:rel="noopener"} and says "currently, there is no regulatory framework in Canada specific to AI." The page is archived, so check the current status before you rely on it. In the meantime, the Office of the Privacy Commissioner and provincial commissioners [said in December 2023](https://www.priv.gc.ca/en/privacy-topics/technology/artificial-intelligence/gd_principles_ai/){:rel="noopener"} that generative AI does not sit outside current legislative frameworks. They say organizations stay accountable for decisions their systems influence. That is guidance, not law.

So until something is handed down, what I recommend is simple: know what you have, consider the risk, map it out. The first step is an inventory. I wrote about that in [shadow AI and how to audit it](/blog/shadow-ai-is-the-new-shadow-it.html). A register is the step after the audit.

## How do NIST, the EU AI Act and ISO 42001 compare?

<div class="answer-block">
<p>NIST is a voluntary U.S. framework, the EU AI Act is binding European law with fixed risk levels, and ISO/IEC 42001 is an international management standard. They agree on the core idea: know your AI systems, rate the risk, decide what to accept, record it and review it.</p>
</div>

| | NIST AI Risk Management Framework | EU AI Act | ISO/IEC 42001 |
|---|---|---|---|
| **What it is** | A voluntary U.S. framework, version 1.0 released January 2023 | An EU regulation, Regulation (EU) 2024/1689 | An international standard for an AI management system, published 2023 |
| **How it sorts risk** | Govern, map, measure and manage. You set your own tolerance. | Four fixed levels: unacceptable (banned), high, limited (transparency duties) and minimal | A structured way to manage AI risks and opportunities |
| **Who it covers** | Anyone who chooses to use it | AI developers and deployers, with fines for non-compliance | Organizations of any size that develop, provide or use AI |

[NIST](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/){:rel="noopener"} asks you to document your risk tolerance, assess the most significant risks first, and respond by mitigating, transferring, avoiding or accepting each one. The [European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai){:rel="noopener"} says the AI Act entered into force on 1 August 2024. Its ban on prohibited practices and its AI literacy duties started on 2 February 2025, and most of the rest applies from 2 August 2026. For high-risk systems in listed areas, such as recruitment and credit scoring, the dates run to 2 December 2027. [ISO describes ISO/IEC 42001](https://www.iso.org/standard/42001){:rel="noopener"} as the first AI management system standard, for organizations of any size.

### Why a Canadian business should care about the EU

The AI Act reaches beyond Europe. [Article 2](https://artificialintelligenceact.eu/article/2/){:rel="noopener"} applies to providers that place AI systems on the EU market wherever they are based, and to providers and deployers in other countries when the output of their AI system is used in the Union. GDPR works in a similar way: [Article 3](https://gdpr-info.eu/art-3-gdpr/){:rel="noopener"} covers organizations outside the EU that process the personal data of people in the EU in order to offer them goods or services, or to monitor their behaviour there.

If you want to do business in Europe, these rules matter even from Canada. Whether they apply to you is a legal question, so check with a lawyer before you assume either way. What a register gives you is the starting point: you cannot tell what applies if you do not know what you use.

## What goes in the register?

<div class="answer-block">
<p>Each row names an AI system and your role, describes one risk, scores how likely and how bad it is, records what you will do about it, and gives it an owner and a review date.</p>
</div>

Mine has a section for the systems in scope and a section for the risks. For each system I record my position: AI user, API consumer, system developer and operator, or software vendor. Those positions carry different responsibilities, and it is easy to miss that you can be more than one.

For each risk, the register records:

1. **A description** of what could go wrong.
2. **Likelihood,** from 1 (rare) to 5 (almost certain).
3. **Impact,** from 1 (negligible) to 5 (severe).
4. **A score,** which is likelihood times impact.
5. **A decision:** I accept scores of 6 or lower. Scores from 7 to 12 need treatment. Scores of 13 or more need immediate treatment.
6. **Treatment:** the policy, process or control that reduces the risk.
7. **A residual score,** which is the score after treatment.
8. **An owner and a review date.**

The inherent score, before any treatment, and the residual score, after it, tell you whether your controls are doing anything. A risk that scores 8 before treatment and 4 after it has been dealt with. A risk that scores 8 both times has not.

I review mine every year, and whenever an AI system changes materially. Adding a new tool, or letting a tool take on a new job, is a reason to reassess before you go live, not after.

## Which risks should you start with?

<div class="answer-block">
<p>Start with the ones nearly every small business using AI has: personal information in prompts, wrong content reaching clients, dependence on one provider, bias, undisclosed AI use, prompt injection into automated tools, and adopting a tool without reassessing.</p>
</div>

These are the generic risks that appear in mine, and several connect to the privacy principles in the Office of the Privacy Commissioner's guidance, such as consent, appropriate purposes, accuracy, openness and safeguards.

- **Client personal information in prompts.** Someone pastes client details into an AI tool, and a third party now has them.
- **Wrong content reaching clients.** AI output contains errors or invented sources, and nobody checked it.
- **Dependence on one provider.** A price change, a terms change or an outage stops your work.
- **Bias in client-facing content.** Output is stereotyped or culturally off, and it goes out under your name.
- **Undisclosed AI use.** A client does not know AI was part of the work.
- **Prompt injection.** Content that an automated tool reads contains instructions that make it do something you did not intend.
- **Adopting a tool without reassessing.** A new tool or a new use slips in before anyone updates the register.

The federal government's [voluntary code of conduct](https://ised-isde.canada.ca/site/ised/en/voluntary-code-conduct-responsible-development-and-management-advanced-generative-ai-systems){:rel="noopener"} for advanced generative AI systems lists six areas that make a useful checklist for your own categories: accountability, safety, fairness and equity, transparency, human oversight, and validity and robustness. It is aimed at developers of those systems, so use it as a source of categories, not as a rule for your business.

## How do you start?

<div class="answer-block">
<p>Take an inventory of the AI tools in use, name one owner, score each risk on a 1 to 5 scale, decide what you will accept, and set a review date.</p>
</div>

1. **List the AI you use,** including the tools people brought in themselves.
2. **Name one person** who owns the register and decides what is acceptable.
3. **Write down the risks,** starting with the list above, one row each.
4. **Score them,** using a 1 to 5 scale for likelihood and impact, and decide what you will accept.
5. **Set a review date,** once a year and whenever your tools change.

You can do the first pass in an afternoon. Do not wait for a perfect framework. Pick the one that suits your size, and keep it simple enough that you will actually update it.

This post is general information, not legal advice. If you want a second pair of eyes on your register, or help turning an inventory into one, you can [get in touch](/contact.html).
