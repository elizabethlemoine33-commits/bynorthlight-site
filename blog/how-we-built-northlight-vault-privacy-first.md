---
layout: post
title: "How We Built Northlight Vault: Privacy-First Thinking in a World of Unnecessary Data"
description: "I have no idea who downloaded Northlight Vault this week. None. And I think that's exactly right. On privacy-first design and the choices behind Vault."
og_title: "How We Built Northlight Vault: Privacy-First Thinking in a World of Unnecessary Data"
og_description: "I have no idea who downloaded Northlight Vault this week. None. And I think that's exactly right."
date: 2026-06-15
date_modified: "2026-08-07"
published_time: "2026-06-15T00:00:00.000Z"
permalink: /blog/how-we-built-northlight-vault-privacy-first.html
source_label: "Aurora Brief · Essay"
source_class: source-aurora
read_time: 4
tags:
  - Vault
  - Privacy
  - canadian privacy
  - PIPEDA
  - product design
  - data minimization
related_reading:
  - title: "Implementing AI Without Breaking Canadian Privacy Law: A PIPEDA Guide"
    url: /blog/pipeda-privacy-first-ai-canada.html
  - title: "I Built Three AI Tools for My Own Work. Now They're on MCP Market."
    url: /blog/northlight-mcp-skills-market.html
  - title: "What I Learned Optimizing for AI Search: AEO Checklist 2026"
    url: /blog/aeo-optimization-lessons-2026.html
faq:
  - q: "What user data does Northlight Vault not collect?"
    a: "Northlight Vault collects no personal information from users. You don't register, create an account, or give a name — the app doesn't report back which cloud accounts you've connected or what files you've viewed. The only analytics Northlight collects is aggregate, anonymised web data through Plausible: visitor counts, page views, approximate location, and operating system. No profiles. No individual tracking. If someone asks 'what do you know about me?', the answer is: nothing, unless they've chosen to share it."
  - q: "Can you grow a product without tracking users?"
    a: "Yes — with a narrower but more defensible data set. Aggregate, anonymised analytics through Plausible tells Northlight what matters without building individual profiles: whether Mac users are landing on a Windows-only product page, which pages get traffic, roughly where users are located. Too much data stops being useful anyway — when you have everything, you can't find anything, and you've still violated someone's privacy to get there. The practical principle: collect only what you can explain, specifically, what you'll do with."
  - q: "Why does privacy-first design matter for Northlight's products?"
    a: "Privacy-first isn't a feature or a compliance checkbox — it's the design principle that determines what Northlight collects before anyone asks. The result: if someone asks 'what do you know about me?', the answer is first name, email address, and what they've chosen to share. Nothing else, because nothing else was taken. That's the kind of organisation Northlight Advisory Services is building: one that has less to answer for because it asked less in the first place."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How We Built Northlight Vault: Privacy-First Thinking in a World of Unnecessary Data",
  "description": "I have no idea who downloaded Northlight Vault this week. None. And I think that's exactly right. On privacy-first design and the choices behind Vault.",
  "datePublished": "2026-06-15",
  "dateModified": "2026-08-07",
  "author": {
    "@type": "Person",
    "name": "Elizabeth Lemoine",
    "url": "https://bynorthlight.ca/about.html"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Northlight Advisory Services",
    "url": "https://bynorthlight.ca"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://bynorthlight.ca/blog/how-we-built-northlight-vault-privacy-first.html"
  }
}
</script>

I have no idea who downloaded Northlight Vault this week. None. And I think that's exactly right.

I built Vault for myself first. I had too many cloud accounts — [Dropbox](https://www.dropbox.com){:rel="noopener"}, [Google Drive](https://workspace.google.com/products/drive/){:rel="noopener"}, [OneDrive](https://www.microsoft.com/en-ca/microsoft-365/onedrive/online-cloud-storage){:rel="noopener"} — and I was spending more time logging in and out than actually finding anything. So I built a tool that lets me browse all of them from one place, on my own computer, without touching the web.

Then I realised other people had the same problem. And that changed everything — not because the technical problem got harder, but because the responsibility did.

When you're building something just for yourself, you make decisions by instinct: what feels safe, what feels clean, what feels right. I wanted Vault to be locked down. That wasn't a policy decision or a compliance checkbox; it was just mine, and I didn't want anyone else in it. But then I decided to share it with other people, and that meant thinking about them — their data, their needs, and our responsibilities. We had to be able to answer a harder question: what are we actually collecting from them, and why?

I've experienced instances where privacy was an afterthought; where people working on a project genuinely believed that collecting vast amounts of personal information was fine because the cause was good. I understand that sentiment — it comes from a good place. But good intentions don't change what data is. When you're holding someone's personal information, you have a responsibility to it. Full stop. The reason you collected it doesn't make the obligation smaller.

That's where I started with Vault. Not "what do we need to be compliant" but "what do we actually need, and what can we leave alone?" That question is actually at the heart of [PIPEDA](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/){:rel="noopener"} — Canada's federal private-sector privacy law — which requires that personal information be collected only for an identified purpose, and only to the extent necessary for that purpose. But compliance was never the ceiling; it was the floor.

## What User Data Does Northlight Vault Not Collect?

<div class="answer-block"><p>Northlight Vault collects no personal information from users. You don't register, create an account, or give a name — the app doesn't report back which cloud accounts you've connected or what files you've viewed. The only analytics Northlight collects is aggregate, anonymised web data through Plausible: visitor counts, page views, approximate location, and operating system. No profiles. No individual tracking. If someone asks 'what do you know about me?', the answer is: nothing, unless they've chosen to share it.</p></div>

Specifically, Vault does not collect:

- Login credentials or account information
- Which cloud accounts you've connected
- What files you've viewed or accessed
- Your name, email, or any personal identifier

As of July 2026, here's where we landed — and why it matters.

When you install Vault, it lives on your computer. It's self-contained. You don't register it; you don't create an account; you don't give us your name. I can't tell you who signed in today because the app doesn't report that back to us. I don't know which cloud accounts you've connected. I don't know what files you've looked at. That's yours — it stays on your machine, and we have no access to it.

We don't need to know who you are to build a better file browser. **Knowing your name doesn't make the product better. It just means we have something we didn't earn.**

I'll be honest about what that costs, though. I can't reach out to the people using Vault to ask how it's working for them. If you downloaded it last week and ran into something frustrating, I have no way of knowing — unless you [tell us](https://forms.clickup.com/14151173/f/dfvg5-2317/FF757UNUCJJTY2UIBF){:rel="noopener"}. Some days that makes things harder — every user's experience matters this early, and not being able to ask directly is a real trade-off. But the alternative is collecting your information to serve my curiosity, and **it's not a trade I'm willing to make.** If you want to tell me how it's going, the door is open. I just won't knock on yours first.

For Aurora Brief — which you're reading right now — we collect your first name and your email address. Your first name so we can say hello to you like a person; your email address so we can send this. That's it. If we ever decide we need more than that, we're going to stop and ask ourselves why — because **the burden of proof should always be on collection, not on privacy.**

## Can You Grow a Product Without Tracking Users?

<div class="answer-block"><p>Yes — with a narrower but more defensible data set. Aggregate, anonymised analytics through Plausible tells Northlight what matters without building individual profiles: whether Mac users are landing on a Windows-only product page, which pages get traffic, roughly where users are located. Too much data stops being useful anyway — when you have everything, you can't find anything, and you've still violated someone's privacy to get there. The practical principle: collect only what you can explain, specifically, what you'll do with.</p></div>

The obvious pushback: how do you grow without tracking? How do you know what's working?

We do track some things; I'm not going to pretend otherwise. We use [Plausible Analytics](https://plausible.io/privacy-focused-web-analytics){:rel="noopener"} on the website — aggregate, anonymised data. I can see how many people visited, which pages they looked at, roughly where in the world they came from, and what operating system they're using. That last one matters more than it might sound: we built Vault for Windows first. If people are landing on the site from a Mac, that tells us there's interest we haven't served yet — and that's worth knowing. That's the kind of data that earns its place; you can look at it and explain exactly what you're doing with it.

What I can't do — and won't do — is tell you that a specific person with a specific name looked at a specific page for a specific amount of time and then clicked this link. I can't build a profile. I don't want to.

There are two real problems with over-collection. The first is obvious: you know more about a person than you have any right to know. [The Office of the Privacy Commissioner of Canada](https://www.priv.gc.ca/en/opc-news/speeches/2023/sp-d_20230427/){:rel="noopener"} has been consistent on this for years: the principle of data minimization isn't just good ethics, it's a legal expectation under Canadian privacy law. The second problem is less talked about: too much data stops being useful. When you have everything, you can't find anything; you end up drowning in information you can't parse into anything meaningful, and you've still violated someone's privacy to get there.

The less we know, the better — not as a slogan, but as a practical design principle.

## Why Does Privacy-First Design Matter for Northlight's Products?

<div class="answer-block"><p>Privacy-first isn't a feature or a compliance checkbox — it's the design principle that determines what Northlight collects before anyone asks. The result: if someone asks 'what do you know about me?', the answer is first name, email address, and what they've chosen to share. Nothing else, because nothing else was taken. That's the kind of organisation Northlight Advisory Services is building: one that has less to answer for because it asked less in the first place.</p></div>

Northlight is a small organisation. We're building tools and doing advisory work; we're not going to win on scale, and we're not going to out-resource the big players.

What we can do is be trustworthy — actually, concretely, demonstrably trustworthy; not because we say so, but because of the choices we make before anyone's looking.

**Privacy-first isn't a feature. It's core to how we operate.** It means that when someone asks us "what do you know about me?", the answer is: your first name, your email address, and what you've chosen to tell us. We can say exactly why we have each thing. We can explain what we do with it. There's nothing to hide because we haven't taken anything we don't need.

That's the kind of organisation I want to build — one that has less to answer for because it asked less in the first place.

*Northlight Vault is free to download at [bynorthlight.ca](/vault.html). If you have thoughts on this — or on privacy design more broadly — [just reply](mailto:hello@bynorthlight.ca). I'd like to hear them.*

If you're curious about the advisory and strategy side of what Northlight Advisory Services does — beyond the tools — [this is the right place to start](/who-we-help.html).
