---
layout: printable
title: "AI Agent Deployment Go/No-Go Checklist"
description: "A pre-deployment checklist for AI agents — covering identity, permissions, boundaries, auditability, and readiness. Use before giving any agent autonomous access."
og_title: "AI Agent Deployment Go/No-Go — Northlight Advisory Services"
og_description: "Pre-deployment checklist for AI agents: identity, permissions, boundaries, containment, auditability, and readiness. Free from Northlight Advisory Services."
permalink: /blog/ai-agent-deployment-checklist-printable.html
---

<div class="no-print-bar">
  <p>Use your browser's Print function to save as PDF — File → Print → Save as PDF.</p>
  <a href="/blog/your-agents-need-a-chain-of-command.html">← Back to post</a>
</div>

<div class="print-header">
  <div class="wordmark">Northlight Advisory Services</div>
  <div class="print-url">bynorthlight.ca</div>
</div>

<h1 class="doc-title">AI Agent Deployment Go/No-Go</h1>
<p class="doc-subtitle">Complete before giving any agent autonomous access</p>

<div class="step">
  <div class="step-header">
    <span class="step-number">Section 1</span>
    <span class="step-title">Identity &amp; Permissions</span>
  </div>
  <div class="step-rule"></div>
  <ul class="checklist">
    <li><div class="check-box"></div>Agent has its own identity, separate from any human developer</li>
    <li><div class="check-box"></div>Agent permissions are explicitly defined and documented</li>
    <li><div class="check-box"></div>Agent is operating at the appropriate autonomy level (1–4) for the task</li>
    <li><div class="check-box"></div>High-stakes actions require explicit human approval before execution</li>
  </ul>
</div>

<div class="step">
  <div class="step-header">
    <span class="step-number">Section 2</span>
    <span class="step-title">Boundaries &amp; Containment</span>
  </div>
  <div class="step-rule"></div>
  <ul class="checklist">
    <li><div class="check-box"></div>Network access is restricted — agent cannot reach untrusted external domains</li>
    <li><div class="check-box"></div>Agent cannot write directly to protected branches or production systems</li>
    <li><div class="check-box"></div>Agent has been told its boundaries explicitly (not just blocked silently)</li>
    <li><div class="check-box"></div>A "controlled failure" path exists — blocked actions are logged and surfaced, not just dropped</li>
  </ul>
</div>

<div class="step">
  <div class="step-header">
    <span class="step-number">Section 3</span>
    <span class="step-title">Auditability</span>
  </div>
  <div class="step-rule"></div>
  <ul class="checklist">
    <li><div class="check-box"></div>Every agent action is logged with full attribution</li>
    <li><div class="check-box"></div>Compliance team can audit agent actions with the same rigour as human actions</li>
    <li><div class="check-box"></div>Security team has been briefed and signed off</li>
    <li><div class="check-box"></div>An incident response plan exists if the agent behaves unexpectedly</li>
  </ul>
</div>

<div class="step">
  <div class="step-header">
    <span class="step-number">Section 4</span>
    <span class="step-title">Readiness</span>
  </div>
  <div class="step-rule"></div>
  <ul class="checklist">
    <li><div class="check-box"></div>Agent has been given structured context upfront — not starting cold</li>
    <li><div class="check-box"></div>A pilot has been run with a low-risk use case first</li>
    <li><div class="check-box"></div>Success metrics are defined before deployment, not after</li>
  </ul>
</div>

<div class="print-footer">
  <span class="footer-note">Autonomy without guardrails is risk. Guardrails without clarity are friction. Get both right, and agents can scale with you.</span>
  <span class="footer-url">bynorthlight.ca</span>
</div>
