---
name: task-creator
description: Create fully-wired ClickUp tasks across Northlight, BlueBear, and You Belong Here. Dispatcher-ready tasks get the correct subtask chain, skill tags, and waiting_on dependencies per the Phase 2 template spec. All tasks get the Five Commandments. Creates and organises — does not delete.
---

# task-creator

Create ClickUp tasks across Northlight, BlueBear Home Comfort, and You Belong Here.
Dispatcher-ready tasks are created with full subtask chains, `skill:*` tags, and `waiting_on` dependency wiring.
Creates and organises — does not delete.

---

## The Five Commandments

Every task MUST have all five. No exceptions.

1. **Start Date** — when work begins
2. **Due Date** — when the task is fully complete
3. **Assignee** — Elizabeth (26199820) or Claude (101209983); always Claude unless told otherwise
4. **Priority** — urgent / high / normal / low
5. **Detailed Description** — enough for Elizabeth to execute without asking anyone what it means

If any are missing from the request, ask before creating.

---

## Step 1 — Identify task type

Ask if not clear from context:

> "What type of task is this?"
> - LinkedIn post
> - Threads post
> - Aurora Brief (newsletter)
> - Blog post (standalone)
> - Company Setup document
> - BlueBear or You Belong Here task
> - Other / generic

**LinkedIn, Threads, Aurora Brief, Blog, and Company Setup document tasks are dispatcher-aware** — use the templates below to create full subtask chains with `skill:*` tags and `waiting_on` wiring.

**BlueBear, You Belong Here, and generic tasks** are human-managed — create a single task with Five Commandments and route to the correct list.

---

## Step 2 — Collect required info

### Dispatcher tasks (Templates A–E)

Collect:
- **Topic / subject line** — what this piece of content is about
- **Key message or brief** — what Elizabeth wants to say (can be a rough note)
- **Start date** — when work begins
- **Due date** — when the fully completed task is done (post date is not the due date — see template notes)
- **Priority**
- **Graphic needed?** (LinkedIn and Aurora Brief only — yes/no)

### Non-dispatcher tasks

Collect all Five Commandments fields. Ask for any that are missing.

---

## Step 3 — Confirm before creating

Show a confirmation block and wait for explicit approval:

```
Ready to create:

  Type:        [task type / template]
  Title:       [title]
  List:        [Space › Folder › List name]
  Start:       [start date]
  Due:         [due date]
  Priority:    [priority]
  Assignee:    [Elizabeth / Claude]
  Subtasks:    [count] — [names listed]
  Dependencies: chained in sequence
  Graphic:     [yes / no / n/a]

Create this task?
```

If Elizabeth corrects anything, update and re-confirm.

---

## Step 4 — Create the task

### Dispatcher tasks — creation sequence

Always create in this order:
1. Create the **parent task** first — capture its ID
2. Create each **subtask** in sequence — capture each ID immediately
3. After all tasks exist, wire **`waiting_on` dependencies** in sequence using `clickup_add_task_dependency`

**Dependency chain:** each task waits_on the one immediately before it.
Parent → Subtask 1 → Subtask 2 → ... (linear chain)

**Status rules:**
- Parent task: `ready`
- First subtask: `ready`
- All other subtasks: `backlog`

**Assignee rules:**
- Tasks with a `skill:*` tag → Claude (101209983)
- Tasks without a skill tag (approval, publish, analytics) → Elizabeth (26199820)

---

## Templates

---

### Template A — LinkedIn Post

**List:** LinkedIn Content Calendar (`901713940624`)

| # | Name | Skill tag | Assignee | Status |
|---|------|-----------|----------|--------|
| Parent | [topic title] | `skill:content-intake` | Claude | ready |
| 1 | Strategy brief | `skill:content-strategist` | Claude | ready |
| 2 | Draft copy | `skill:draft` | Claude | backlog |
| 3 | Critic review | `skill:content-critic` | Claude | backlog |
| 4 | Polish | `skill:polish` | Claude | backlog |
| 5 | Design *(if graphic needed)* | `skill:design-social` | Claude | backlog |
| 6 | Elizabeth approval | *(none)* | Elizabeth | backlog |
| 7 | Publish | *(none)* | Elizabeth | backlog |
| 8 | Analytics check-in | *(none)* | Elizabeth | backlog |

**Notes:**
- Omit Design subtask if no graphic needed
- Publish is manual until LinkedIn Marketing API is resolved
- Parent due date = date post is fully done (analytics collected, not post date)
- Priority rubric: Vault/launch posts = urgent or high; thought leadership = normal

---

### Template B — Threads Post

**List:** Threads Content Calendar (`901713947133`)

| # | Name | Skill tag | Assignee | Status |
|---|------|-----------|----------|--------|
| Parent | [topic title] | `skill:content-intake` | Claude | ready |
| 1 | Strategy brief | `skill:content-strategist` | Claude | ready |
| 2 | Draft copy | `skill:draft` | Claude | backlog |
| 3 | Critic review | `skill:content-critic` | Claude | backlog |
| 4 | Polish | `skill:polish` | Claude | backlog |
| 5 | Publish | *(none)* | Elizabeth | backlog |
| 6 | Analytics | *(none)* | Elizabeth | backlog |

**Notes:**
- Publish and analytics become dispatcher skills (`skill:publish`, `skill:content-analyst`) once Meta API integration is active. Update the template at that time.

---

### Template C — Aurora Brief (Newsletter)

**List:** Aurora Brief Content Calendar (`901714143773`)

| # | Name | Skill tag | Assignee | Status |
|---|------|-----------|----------|--------|
| Parent | [issue title] | `skill:content-intake` | Claude | ready |
| 1 | Strategy brief | `skill:content-strategist` | Claude | ready |
| 2 | Draft copy | `skill:draft` | Claude | backlog |
| 3 | Critic review | `skill:content-critic` | Claude | backlog |
| 4 | Polish | `skill:polish` | Claude | backlog |
| 5 | Design *(if graphic needed)* | `skill:design-social` | Claude | backlog |
| 6 | Blog post | `skill:blog-polish` | Claude | backlog |
| 7 | Elizabeth approval | *(none)* | Elizabeth | backlog |
| 8 | Publish | `skill:publish` | Claude | backlog |
| 9 | Analytics | *(none)* | Elizabeth | backlog |

**Notes:**
- Blog post (step 6) is created every issue — not optional
- Design (step 5) only when graphic needed — ask if not stated
- Publish = Claude creates a Kit draft; Elizabeth manually sends it
- Pipeline text in intake task descriptions should read: `content-intake ✅ → content-strategist → draft → critic → polish → [design-social] → blog-polish → Elizabeth approval → skill:publish (Kit draft) → analytics`

---

### Template D — Blog Post (standalone)

**List:** Blog Content Calendar (`901714340283`)

| # | Name | Skill tag | Assignee | Status |
|---|------|-----------|----------|--------|
| Parent | [post title] | `skill:content-intake` | Claude | ready |
| 1 | Strategy brief | `skill:content-strategist` | Claude | ready |
| 2 | Draft copy | `skill:draft` | Claude | backlog |
| 3 | Critic review | `skill:content-critic` | Claude | backlog |
| 4 | Polish | `skill:polish` | Claude | backlog |
| 5 | Blog polish | `skill:blog-polish` | Claude | backlog |
| 6 | Elizabeth approval | *(none)* | Elizabeth | backlog |
| 7 | Publish | `skill:publish` | Claude | backlog |
| 8 | Analytics | `skill:content-analyst` | Claude | backlog |

---

### Template E — Company Setup Document

**List:** Route to the correct Company Setup list (see routing table below)

| # | Name | Skill tag | Assignee | Notes |
|---|------|-----------|----------|-------|
| Parent | [document title] | *(none)* | Elizabeth | Parent holds the context |
| 1 | Research *(if needed)* | `skill:research` | Claude | Omit if no research required — ask |
| 2 | Draft | `skill:draft` | Claude | |
| 3 | Elizabeth review | *(none)* | Elizabeth | Manual gate — she approves or sends back |
| 4 | Polish | `skill:polish` | Claude | |
| 5 | File output *(if needed)* | `skill:file-output` | Claude | Omit if no Drive export needed |

**Send-back mechanic:** When Elizabeth sends back a draft — she is prompted for comments (via OS/Slack), her comments are posted to the draft ClickUp task, the task status auto-resets to `ready`, and a Slack alert goes to Claude. The dispatcher picks up the draft on the next run. No new subtask is created.

---

## Routing Table

### Northlight — Vault (folder 90178713336)

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Backlog | 901713647819 | features, improvements, bugs, dev work, technical debt, product ideas |
| User Feedback | 901713782135 | user reports, testimonials, feedback, reviews |
| Release | 901713831117 | shipping, deploy, release notes, launch prep |
| Early Access | 901713905175 | early access launch specifically |

### Northlight — Company Setup (folder 90178713345)

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Accounting | 901713710660 | invoices, expenses, bookkeeping, tax, payments |
| Business Registration | 901713710653 | LLC, incorporation, EIN, permits, registration |
| Branding | 901713647799 | logo, colours, brand identity, design system |
| Legal | 901713710666 | contracts, agreements, compliance, IP |
| Operations | 901713710712 | SOPs, admin, processes, internal ops |
| Website | 901713710677 | website copy, landing pages, web updates |
| Product Features | 901713710715 | product roadmap, feature specs, requirements |

### Northlight — Marketing (folder 90178928032)

| List | ID |
|------|----|
| LinkedIn Content Calendar | 901713940624 |
| Threads Content Calendar | 901713947133 |
| Aurora Brief Content Calendar | 901714143773 |
| Blog Content Calendar | 901714340283 |

### Northlight — TableReady

| List | ID |
|------|----|
| Meal Planning App | 901713706238 |

### Northlight — Advisory Board Bot System

| List | ID |
|------|----|
| Advisory Board Bot System | 901713706243 |

### BlueBear Home Comfort — MVP Sprint (folder 90178962707)

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Legal & Financial | 901713987097 | BlueBear contracts, permits, insurance, finances |
| Operations & Systems | 901713987100 | BlueBear scheduling, processes, systems, tools |
| Contractor Recruitment & Onboarding | 901713987105 | hiring contractors, onboarding, job postings |
| Website & Marketing | 901713987112 | BlueBear website, marketing, ads |
| First Jobs & Validation | 901713987115 | first customers, test jobs, validation |
| Dependencies & Blockers | 901713987120 | anything blocked or dependent on something else |

### You Belong Here

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Content Development — Phase 1 | 901714003416 | course content, lessons, scripts, YBH Phase 1 |
| Udemy Setup & Publishing | 901714003418 | Udemy platform, publishing, course setup |
| Phase 1 Evaluation & Gate | 901714003419 | reviewing Phase 1, gate decision |
| Phase 2 — Northlight Positioning | 901714003422 | YBH Phase 2, Northlight integration |
| Phase 3 — Full Course Development | 901714003425 | YBH Phase 3, full course build-out |

---

## Valid Statuses

**Content Calendar lists (LinkedIn, Threads, Aurora Brief, Blog):**
`ready` → `in progress` → `posted` → `done` → `blocked` (also: `backlog`)

**All other lists:**
`to do` → `in progress` → `done` → `blocked`

---

## Workspace Reference

| Item | ID |
|------|----|
| Workspace | 14151173 |
| Northlight Space | 90175613993 |
| Marketing Folder | 90178928032 |
| Elizabeth's User ID | 26199820 |
| Claude's User ID | 101209983 |

---

## Reporting Format

After creating any task or structure:

```
✅ Created: [Task title]
📍 Location: [Space → Folder → List]
🔗 Link: [URL]
📅 Dates: Start [date] → Due [date]
👤 Assigned: [Elizabeth / Claude]
⚡ Priority: [priority]
📋 Subtasks: [count] created, [count] dependencies wired
```

If something couldn't be done, say why and what Elizabeth needs to provide or decide.

---

## Priority Guidance

| Situation | Priority |
|-----------|----------|
| Vault launch or active release tasks | Urgent |
| Vault/launch posts, product milestones, client deadlines | High |
| Standard thought leadership, regular admin | Normal |
| Nice-to-have, no deadline | Low |

---

## Canadian English

All task names and descriptions: colour, behaviour, organisation, recognise, analyse, programme, licence (noun).
