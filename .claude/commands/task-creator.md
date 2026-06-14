---
name: task-creator
description: Create and organise ClickUp tasks across Northlight, BlueBear Home Comfort, and You Belong Here. Handles all task types including content calendar posts, workspace structure, and template application. Creates and organises — does not delete.
---

# task-creator

Create and organise ClickUp tasks across Northlight, BlueBear Home Comfort, and You Belong Here.
Creates and organises — does not delete.

---

## The Five Commandments

Every task MUST have all five. No exceptions, no shortcuts.

1. **Start Date** — when work begins
2. **Due Date** — when the task is fully complete (not when it goes live — when it is done)
3. **Assignee** — Elizabeth (26199820) or Claude (101209983); always Elizabeth unless told otherwise
4. **Priority** — urgent / high / normal / low
5. **Detailed Description** — enough for Elizabeth to execute without asking anyone what it means

If any of these are missing from the request, ask before creating.

---

## Workspace Reference

| Item | ID |
|------|----|
| Workspace | 14151173 |
| Northlight Space | 90175613993 |
| Marketing Folder | 90178928032 |
| LinkedIn Content Calendar List | 901713940624 |
| Threads Content Calendar List | 901713947133 |
| Northlight Vault Folder | 90178713336 |
| Northlight Company Setup Folder | 90178713345 |
| Elizabeth's User ID | 26199820 |
| Claude's User ID | 101209983 |

---

## Routing Table

Pick the best list from the table below. If two lists are plausible, pick the most specific one.

### Northlight — Vault (folder 90178713336)

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Backlog | 901713647819 | features, improvements, bugs, dev work, technical debt, product ideas |
| User Feedback | 901713782135 | user reports, testimonials, feedback, reviews |
| Release | 901713831117 | shipping, deploy, release notes, launch prep |
| Northlight Vault Release — Early Access | 901713905175 | early access launch specifically |

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

| List | ID | Route when task involves… |
|------|----|--------------------------|
| LinkedIn Content Calendar | 901713940624 | LinkedIn posts |
| Threads Content Calendar | 901713947133 | Threads posts |

### Northlight — TableReady (folder 90178759586)

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Meal Planning App | 901713706238 | meal planning, recipes, TableReady app |

### Northlight — Advisory Board Bot System

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Advisory Board Bot System | 901713706243 | advisory board, bot advisors, board simulation |

---

### BlueBear Home Comfort — MVP Sprint (folder 90178962707)

| List | ID | Route when task involves… |
|------|----|--------------------------|
| Legal & Financial | 901713987097 | BlueBear contracts, permits, insurance, finances |
| Operations & Systems | 901713987100 | BlueBear scheduling, processes, systems, tools |
| Contractor Recruitment & Onboarding | 901713987105 | hiring contractors, onboarding, job postings |
| Website & Marketing | 901713987112 | BlueBear website, marketing, ads |
| First Jobs & Validation | 901713987115 | first customers, test jobs, validation |
| Dependencies & Blockers | 901713987120 | anything blocked or dependent on something else |

---

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

**Content Calendar lists (LinkedIn, Threads):**
To Do → In Progress → Posted → Done → Blocked

**All other lists:**
To Do → In Progress → Done → Blocked

---

## Content Calendar Task Pattern

When creating a post task in any content calendar list, always apply this structure automatically unless Elizabeth says otherwise.

**Parent Task**
- Name: `Post [#] — [Date] — [Pillar] — [Topic summary]`
- Start date: 3 days before post date
- Due date: 7 days after post date (task is done when analytics are collected)
- Assignee: Elizabeth
- Priority: Vault/launch posts = urgent or high; thought leadership = normal
- Description: post copy, graphic requirements, alt text (if applicable), link instructions, hashtag guidance, engagement prompt

**Subtask 1 — Review & finalise copy**
- Due: 3 days before post date
- Description: Finalise copy for accuracy, voice, Canadian English, character limit. Confirm graphic and alt text are ready for graphic posts.

**Subtask 2 — Schedule/publish (personal account)**
- Due: 2 days before post date
- Description: Platform-specific instructions (e.g. Threads link attachment field, LinkedIn image alt text field, hashtag rules)

**Subtask 3 — @northlightcomms repost (Threads) OR Company page amplification (LinkedIn)**
- Due: post date
- Description: Threads: repost from @northlightcomms immediately after personal post goes live. Vault posts: reply with "Download here → bynorthlight.ca/vault — free, Windows, no account required." Cross-post to Instagram Stories via native one-tap share. LinkedIn: amplify company-page posts with a personal note (see calendar for suggested copy).

**Subtask 4 — 7-day analytics check-in**
- Due: 7 days after post date (same as parent due date)
- Description: Review post analytics: reply count, likes, profile visits, link clicks (Vault posts). Note any unanswered comments. Record key metrics. Mark parent task Done when complete.

Post already live or scheduled: mark Subtasks 1 and 2 as Done immediately on creation.

---

## Accessibility Standard

Every content calendar post task that includes a graphic MUST include alt text in the description, labelled clearly:

> Alt text (add in [platform]'s alt text field before publishing): [description]

If alt text is not provided in the request, draft it based on the graphic description. Alt text should describe: the visual design elements, the headline text shown in the graphic, any URL shown, and the overall purpose of the image.

---

## New List or Folder Creation

**Step 1 — Confirm before creating.** Ask:
- What is this for? (one sentence)
- Does it belong inside an existing folder, or is it a standalone list in the space?
- What statuses does it need? (default: To Do / In Progress / Done / Blocked)

**Step 2 — Apply naming conventions:**
- Folder inside Northlight space: "Northlight [Topic]"
- List inside a folder: "[Topic] [Type]" — skip "Northlight" prefix if already inside a Northlight folder

**Step 3 — Create and confirm.** Report back: what was created, where, the list/folder ID, and what tasks should be created inside it next.

---

## Priority Guidance

| Situation | Priority |
|-----------|----------|
| Vault launch or active release tasks | Urgent |
| Graphic Vault posts, product milestones, client deadlines | High |
| Standard thought leadership posts, regular admin | Normal |
| Nice-to-have, no deadline | Low |

---

## Template System

Templates have not yet been built in ClickUp. When they exist, apply them by reading the template task and replicating its structure (subtasks, description format, fields) to the new task.

| Template | Purpose | Key Fields |
|----------|---------|------------|
| Content Calendar Post | Any social media post task | Start = 3 days before, Due = 7 days after, 4 subtasks |
| Strategy Advisory Task | Client deliverable or engagement task | Milestone dates, deliverable description |
| Vault Development Task | Vault feature or bug task | Release target, acceptance criteria |
| Company Setup Task | One-time admin/setup task | Deadline, linked document |

When no template exists yet: build manually using the patterns in this skill, and note to Elizabeth that a formal template could be created if she uses this task type repeatedly.

---

## Confirm Before Creating

Show a confirmation block and wait for explicit approval before touching ClickUp:

```
Ready to create:

  Title:       [title]
  List:        [Space › Folder › List name]
  Start:       [start date]
  Due:         [due date]
  Priority:    [priority]
  Assignee:    [Elizabeth / Claude]
  Description: [description or "(none)"]
  Subtasks:    [count, or "none"]

Create this task?
```

If Elizabeth corrects anything, update and re-confirm.

---

## Reporting Format

After creating any task or structure, report back in this format:

```
✅ Created: [Task/List/Folder Name]
📍 Location: [Space → Folder → List]
🔗 Link: [URL]
📅 Dates: Start [date] → Due [date]
👤 Assigned: [Elizabeth / Claude]
⚡ Priority: [priority]
📋 Subtasks: [count] created
```

If something couldn't be done, say why clearly and what Elizabeth needs to provide or decide.

---

## Canadian English

All task names and descriptions use Canadian English: colour, behaviour, organisation, recognise, analyse, programme, licence (noun).
