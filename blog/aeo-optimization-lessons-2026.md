---
layout: post
title: "What I Learned Optimizing a Website for AI Search: An AEO Checklist for 2026"
description: "Two phases of hands-on Answer Engine Optimization work on bynorthlight.ca — what actually moves the needle, what's overhyped, and a practical AEO checklist for 2026."
og_title: "What I Learned Optimizing a Website for AI Search: An AEO Checklist for 2026"
og_description: "Hands-on lessons from two phases of AEO work on a real Canadian small business website — schema, citations, entity signals, and what the AI tools actually say about your site."
date: 2026-07-09
date_modified: "2026-07-09"
published_time: "2026-07-09T00:00:00.000Z"
permalink: /blog/aeo-optimization-lessons-2026.html
source_label: "Blog · Guide"
source_class: source-essay
read_time: 12
tags:
  - AEO
  - GEO
  - AI search
  - SEO
  - schema markup
  - ChatGPT
  - Perplexity
  - Gemini
related_reading:
  - title: "I Built Three AI Tools for My Own Work. Now They're on MCP Market."
    url: /blog/northlight-mcp-skills-market.html
  - title: "Your AI Strategy Is Running on the Wrong Clock"
    url: /blog/ai-strategy-wrong-clock.html
  - title: "How We Built Northlight Vault: Privacy-First Thinking"
    url: /blog/how-we-built-northlight-vault-privacy-first.html
faq:
  - q: "What is Answer Engine Optimization (AEO)?"
    a: "Answer Engine Optimization (AEO) is the practice of optimizing a website so AI-powered answer engines — ChatGPT, Perplexity, Gemini, Claude — can find, understand, and cite it accurately. Unlike traditional SEO, AI systems don't rank pages; they synthesize answers from what they can read and verify. The goal is to be the clearest, most extractable source for a given topic — not just the most linked."
  - q: "What is the difference between AEO and GEO?"
    a: "AEO (Answer Engine Optimization) and GEO (Generative Engine Optimization) refer to the same general practice — optimizing for AI citation — with slightly different emphases. AEO focuses on getting cited in direct answer responses from AI tools. GEO is the broader term covering optimization for all generative AI outputs. In practice they're used interchangeably."
  - q: "Does llms.txt actually help with AI citations?"
    a: "llms.txt is a structured plain-text file at the root of your site that tells AI systems what your site is, what it covers, and how to navigate it. It's the AI equivalent of a sitemap — not guaranteed to work for every AI, but adds a useful crawlable signal for systems that check for it. It costs almost nothing to implement and is worth doing."
  - q: "What schema types matter most for AEO?"
    a: "The five schema types that matter most for AEO are: Organization (entity identity), Person (founder/author identity), Article (content with dateModified — freshness signal), FAQPage (direct Q&A extraction), and HowTo (step-by-step content). FAQPage is the highest-leverage for citation because it gives AI models pre-formatted question-answer pairs to pull from."
  - q: "How do you measure AEO performance?"
    a: "Run a set of target prompts across ChatGPT, Perplexity, and Gemini monthly and record whether your site is cited. Tools like HubSpot's AI Search Optimization tool and Chatbeat track this at scale. The Protect/Improve/Pursue (P/I/P) framework helps triage: protect prompts where you're already cited, improve prompts where you appear but could rank higher, pursue prompts where you're not cited yet."
---

<div class="at-a-glance">
<h2>At a glance</h2>
<ul>
<li>AEO (Answer Engine Optimization) optimizes for AI citation, not search ranking</li>
<li>The five schema types that matter: Organization, Person, Article (with dateModified), FAQPage, HowTo</li>
<li>llms.txt is low-cost and worth doing — it's an AI-readable index of your site</li>
<li>AI crawlers (GPTBot, ClaudeBot, PerplexityBot) need to be explicitly allowed in robots.txt / Cloudflare</li>
<li>Citation gap is usually a content channel problem, not a technical problem</li>
<li>Gemini entity collision is a real risk if another org shares your name</li>
</ul>
</div>

I spent the better part of two months doing AEO work on [bynorthlight.ca](/) — the Northlight Advisory Services website. Two structured phases, dozens of schema implementations, an llms.txt file, AI crawler configuration, off-site authority building, and a 36-prompt testing matrix across ChatGPT, Perplexity, and Gemini.

This post is a synthesis of what I learned. Not what the theory says. What actually happened when I did it on a real small Canadian business website.

## What is AEO and why does it matter in 2026?

<div class="answer-block"><p>Answer Engine Optimization (AEO) is the practice of making your website citable to AI-powered answer systems — ChatGPT, Perplexity, Gemini, Claude. Unlike traditional SEO, which targets search rankings, AEO targets the answers AI generates. For service businesses, being cited in an AI response is a direct acquisition channel that most small businesses haven't touched yet.</p></div>

Answer Engine Optimization (AEO) — sometimes called Generative Engine Optimization (GEO) — is the practice of making your website visible and citable to AI-powered answer systems: ChatGPT, Perplexity, Gemini, Claude.

Traditional SEO gets you ranked in Google. AEO gets you cited when someone asks an AI a question. These are increasingly different things. Perplexity users don't click to page two of results — the AI synthesizes an answer and cites sources. ChatGPT's response to "who are the best fractional COOs in Canada" either includes your name or it doesn't.

For a service business like Northlight Advisory Services, being cited in an AI response to a relevant prompt is equivalent to being mentioned in an article a prospect would read before they reach out. It is a real acquisition channel, and right now it's largely uncontested terrain for small businesses who do the work.

## What we did in Phase 1 and Phase 2

<div class="answer-block"><p>Phase 1 built the technical foundation: llms.txt, robots.txt AI crawler allowances, sitemap.xml, and Organization and FAQPage schema. Phase 2 completed all five priority schema types, rewrote every blog post H2 to question format, added freshness signals, and built off-site authority across Clutch, Crunchbase, LinkedIn, and directory listings. Then tested across 36 prompts in ChatGPT, Perplexity, and Gemini.</p></div>

### Phase 1 — Foundation

Built the site as a flat HTML site on GitHub Pages. From day one, implemented:

- **llms.txt** — a structured plain-text file at the root of the site that tells AI systems who we are, what we do, and what pages exist. Think of it as a sitemap for AI.
- **robots.txt with explicit AI crawler allowances** — GPTBot, ClaudeBot, PerplexityBot, Google-Extended all explicitly allowed.
- **sitemap.xml** submitted to Google Search Console
- **Basic Organization schema** on the homepage
- **FAQPage schema** on the FAQ page

### Phase 2 — AEO completion + authority building

Phase 2 was more structured and covered:

- All five priority schema types completed across the site (Organization, Person, Article, FAQPage, HowTo)
- All 10 blog post H2s rewritten to question format for AI extractability
- `dateModified` added to all Article JSON-LD (freshness signal)
- Off-site authority signals built: [Clutch](https://clutch.co){:rel="noopener"}, Fractionus, Digital Reference, [Crunchbase](https://www.crunchbase.com){:rel="noopener"}, GitHub org, LinkedIn company page
- [HubSpot AI Search Optimization](https://www.hubspot.com/products/marketing/ai-visibility){:rel="noopener"} course completed and 36-prompt testing matrix run across ChatGPT, Perplexity, and Gemini

## What the prompt testing revealed

<div class="answer-block"><p>ChatGPT was the most accurate — naming Northlight Advisory Services in a comparison table alongside major consulting firms on a high-value prompt. Gemini was wrong on every tested prompt, confusing Northlight Advisory Services with a different company called Northlight Solutions Group and inventing services that don't exist. Perplexity was directionally accurate where it had data.</p></div>

### ChatGPT is the most accurate

ChatGPT was GREEN (accurate, cites the right entity) on most of the Protect and Improve prompts we tested. One standout: on "Who are the best business strategy consultants for Canadian mid-market firms?" — a Pursue-category prompt we weren't expecting to appear in — ChatGPT named Northlight Advisory Services in a comparison table alongside McKinsey, BCG, Level5 Strategy, Deloitte, and Accenture. That's a meaningful signal that the foundational work is registering.

### Gemini has a serious entity collision problem

Gemini was RED on 100% of tested prompts — not because it ignored us, but because it confused us with a completely different organisation called Northlight Solutions Group (NSG), a Salesforce/Agentforce implementation firm. Gemini invented a fictional 5-stage methodology, "Baseline AI" training program, and Lead-to-Cash architecture — none of which are real Northlight Advisory Services offerings.

This is the most significant AEO risk for small businesses with common names: if another entity shares your name (even partially), AI systems can conflate them. The fix is content-based disambiguation — dense entity-signal pages and explicit llms.txt sections naming the other entity and distinguishing from it.

<div class="callout-block"><p><strong>Lesson:</strong> If another organisation uses a name that overlaps with yours, AI models may conflate them. Write an explicit disambiguation page. Name the other entity directly. AI systems respond to direct disambiguation much better than to simply asserting your own identity.</p></div>

### Perplexity is directionally accurate where it has data

Perplexity was mostly accurate on the prompts we ran. The challenge was a search limit — we hit the free tier cap partway through testing. We'll complete the remaining prompts in the next monthly triage cycle.

## The citation gap: a content channel problem, not a technical problem

<div class="answer-block"><p>A technically optimized site can still have zero citation visibility if it's absent from the content channels AI actually pulls from. For fractional advisory queries, AI consistently cites listicle and directory sites — not individual firm websites. No schema improvement fixes that. The gap is a distribution problem: you need to be listed on the sites AI is already citing for your target prompts.</p></div>

After two phases of AEO work, bynorthlight.ca is technically well-optimized. AI crawlers are reading the site. Schema is implemented correctly. llms.txt is current. And yet: on all 10 HubSpot-tracked advisory prompts, we were at 0% citation visibility at the end of Phase 2.

That's not a schema problem. It's a content channel problem.

When we used HubSpot's Chatbeat feature to see what AI actually cites for fractional advisory prompts, the pattern was clear: AI consistently cites listicle-format sites (capstacker.io, chiefjobs.com, gofractional.com) for these queries. Those are "Peer channel" citations — curated lists and directories of advisors and service providers. bynorthlight.ca is not in any of them.

No amount of schema optimization fixes a citation gap that's caused by being absent from the content channels AI is actually pulling from. The technical work is necessary but not sufficient. You also need to be in the right places.

<div class="callout-block"><p><strong>Lesson:</strong> Use HubSpot's AI Search Optimization tool (or similar) to see what AI actually cites for your target prompts. If the sources are all listicle sites and directories, that's your gap — not your schema.</p></div>

## What robots.txt AI crawler warnings actually mean

<div class="answer-block"><p>A robots.txt warning from an AI audit tool doesn't mean AI crawlers are actually blocked. If your site runs on Cloudflare, verify crawler status in the Cloudflare AI Security dashboard — that's the authoritative source. Ours showed GPTBot, ClaudeBot, and PerplexityBot all active with real request counts. The audit tool had misread Cloudflare's managed robots.txt syntax.</p></div>

We received a HIGH priority warning from HubSpot's tool about our robots.txt: "Allow AI search crawlers." When I fetched the robots.txt directly and asked an AI to summarize it, it described rules that seemed to block GPTBot, ClaudeBot, and Google-Extended.

This was wrong. The site is on [Cloudflare](https://www.cloudflare.com){:rel="noopener"}, which manages a section of robots.txt automatically. The Cloudflare AI Security dashboard showed all major AI crawlers in "Allowed" status with active request counts (GPTBot: 8 requests, ClaudeBot: 11, PerplexityBot: 4). The AI summarizing the robots.txt file had misread the Cloudflare-managed section structure.

<div class="callout-block"><p><strong>Lesson:</strong> Verify AI crawler allowance at your CDN or WAF control panel — not by reading robots.txt through another AI. If you're on Cloudflare, the AI Security dashboard is the authoritative source. HubSpot's warning was a false alarm caused by the tool not understanding Cloudflare's robots.txt syntax.</p></div>

## The AEO checklist for 2026

<div class="answer-block"><p>The five highest-leverage AEO actions for a small business: create an llms.txt file at your site root, explicitly allow AI crawlers in robots.txt, add Organization schema with sameAs links to your homepage, rewrite blog H2s as direct questions, and run a 20–40 prompt test matrix across ChatGPT, Perplexity, and Gemini before doing anything else. The prompt test tells you what kind of problem you actually have.</p></div>

Based on what we actually did, here is what I'd recommend for a small business starting AEO work:

### Technical foundation

- ☑ **[llms.txt](https://llmstxt.org/){:rel="noopener"}** — create at root of your site. Include: entity name, founder, location, description, services, products, current blog posts, preferred sources, what you are not.
- ☑ **robots.txt** — explicitly allow GPTBot, ClaudeBot, PerplexityBot, Google-Extended. Verify at your CDN dashboard, not by reading the file.
- ☑ **sitemap.xml** — submit to [Google Search Console](https://search.google.com/search-console/about){:rel="noopener"}. Keep it current.
- ☑ **Organization schema** on homepage — name, url, address, founder, description, sameAs (LinkedIn, Crunchbase etc).
- ☑ **Person schema** on about page — founder name, jobTitle, worksFor, sameAs.
- ☑ **Article schema** on every blog post — with dateModified. Freshness matters for AI.
- ☑ **FAQPage schema** — highest leverage for citation. Use on FAQ page and blog posts with Q&A content.
- ☑ **HowTo schema** — for step-by-step content. Strong citation signal for procedural queries.

### Content optimization

- ☑ **Question-format H2s** on all blog posts — AI extracts H2s as candidate answers. "How do I choose a fractional advisor?" outperforms "Choosing an Advisor."
- ☑ **Answer-first paragraphs** — put the answer in the first sentence after each H2. AI models extract the opening of each section.
- ☐ **Entity disambiguation page** if another org shares your name — name the other entity explicitly. Don't just assert your own identity.
- ☐ **Listicle content** in the citation channel AI uses for your prompts — build content in the format AI is actually citing.

### Off-site authority

- ☑ **Crunchbase profile** — AI frequently checks Crunchbase for entity verification.
- ☑ **LinkedIn company page** — consistent name, address, URL.
- ☑ **Industry directories** (Clutch, Fractionus, Digital Reference, relevant niche sites) — consistent NAP data (Name, Address, Phone/URL) across all.
- ☐ **Wikipedia** — [40% of ChatGPT citations come from Wikipedia](https://offers.hubspot.com/state-of-aeo){:rel="noopener"}. Worth pursuing once you have enough external signals to meet notability requirements.
- ☐ **Peer channel listings** — get listed on the sites AI already cites for your target prompts. This is often more impactful than any technical work.

### Measurement

- ☑ **Prompt testing matrix** — create a set of 20–40 prompts across ChatGPT, Perplexity, Gemini. Categorize as Protect / Improve / Pursue. Run monthly.
- ☐ **[HubSpot AI Search Optimization tool](https://www.hubspot.com/products/marketing/ai-visibility){:rel="noopener"}** (or similar) — gives you citation visibility % and Chatbeat source data. Free 28-day trial.
- ☑ **Google Search Console** — baseline your traditional search performance. AEO and SEO reinforce each other.
- ☐ **Gemini-specific retest** — if Gemini is confusing you with another entity, retest monthly after publishing disambiguation content. Takes 30–60 days for training data to update.

## What I'd do differently

<div class="answer-block"><p>Start with the technical foundation on day one — llms.txt, robots.txt, and Organization schema take two hours and cost nothing to have in place early. Run the prompt testing matrix in week one, before any other work — it tells you whether you have a technical problem, a content problem, or a citation channel problem, and those have entirely different fixes. Then spend at least as much time on off-site signals as on schema.</p></div>

If I were starting AEO work from scratch on a new site today, I'd do the technical foundation (llms.txt, robots.txt, Organization/Person schema) on day one — it's two hours of work and it costs nothing to have it in place before you need it.

I'd run a prompt testing matrix in week one, before doing anything else, to understand where AI currently puts me. That tells you whether you have a technical problem, a content problem, or a citation channel problem — and those have very different fixes.

And I'd spend at least as much time on off-site signals as on on-site schema. AI citation is an authority and trust problem as much as it's a technical problem. Being in the right directories, being mentioned in the right places, being findable through multiple consistent signals — that's what moves citations, not incremental schema refinements.
