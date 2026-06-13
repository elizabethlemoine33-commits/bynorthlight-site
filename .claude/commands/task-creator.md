# skill: task-creator

Create a ClickUp task in the correct Northlight, BlueBear, or You Belong Here list.
Do NOT use this skill for marketing/content tasks — those go through the subtask chain templates.

## Steps

### 1. Collect task info

If `$ARGUMENTS` contains the task description, use it as the title/description seed.
Otherwise ask: "What's the task? Give me a title and any details."

Then ensure you have all four required fields. Collect any that are missing:
- **Title** — short, action-oriented
- **Description** — what needs to happen and why (can be empty if obvious)
- **Due date** — ask "When is this due?" if not stated; accept relative dates (tomorrow, next Friday, end of sprint, etc.)
- **Priority** — urgent / high / normal / low; default to normal if not specified
- **Assignee** — "you" (Elizabeth) or "Claude"; if ambiguous, ask

### 2. Infer the target list

Use the task content to pick the best list from the routing table below.
If two lists are plausible, pick the most specific one.

#### Routing table

**Northlight — Vault** (folder 90178713336)
| List | ID | Route when task involves… |
|------|----|--------------------------|
| Backlog | 901713647819 | features, improvements, bugs, dev work, technical debt, ideas for the product |
| User Feedback | 901713782135 | user reports, testimonials, feedback, reviews |
| Release | 901713831117 | shipping, deploy, release notes, launch prep |
| Northlight Vault Release — Early Access | 901713905175 | early access specifically |

**Northlight — Company Setup** (folder 90178713345)
| List | ID | Route when task involves… |
|------|----|--------------------------|
| Accounting | 901713710660 | invoices, expenses, bookkeeping, tax, payments |
| Business Registration | 901713710653 | LLC, incorporation, EIN, permits, registration |
| Branding | 901713647799 | logo, colors, brand identity, design system |
| Legal | 901713710666 | contracts, agreements, compliance, IP |
| Operations | 901713710712 | SOPs, admin, processes, internal ops |
| Website | 901713710677 | website copy, landing pages, web updates |
| Product Features | 901713710715 | product roadmap, feature specs, requirements |

**Northlight — TableReady** (folder 90178759586)
| List | ID | Route when task involves… |
|------|----|--------------------------|
| Meal Planning App | 901713706238 | meal planning, recipes, TableReady app |

**Northlight — Advisory Board Bot System** (standalone list 901713706243)
Route when task involves: advisory board, bot advisors, board simulation

---

**BlueBear — MVP Sprint** (folder 90178962707)
| List | ID | Route when task involves… |
|------|----|--------------------------|
| Legal & Financial | 901713987097 | BlueBear contracts, permits, insurance, finances |
| Operations & Systems | 901713987100 | BlueBear scheduling, processes, systems, tools |
| Contractor Recruitment & Onboarding | 901713987105 | hiring contractors, onboarding, job postings |
| Website & Marketing | 901713987112 | BlueBear website, marketing, ads |
| First Jobs & Validation | 901713987115 | first customers, test jobs, validation |
| Dependencies & Blockers | 901713987120 | anything blocked or dependent on something else |

---

**You Belong Here**
| List | ID | Route when task involves… |
|------|----|--------------------------|
| Content Development — Phase 1 | 901714003416 | course content, lessons, scripts, YBH Phase 1 |
| Udemy Setup & Publishing | 901714003418 | Udemy platform, publishing, course setup |
| Phase 1 Evaluation & Gate | 901714003419 | reviewing Phase 1, gate decision |
| Phase 2 — Northlight Positioning | 901714003422 | YBH Phase 2, Northlight integration |
| Phase 3 — Full Course Development | 901714003425 | YBH Phase 3, full course build-out |

### 3. Confirm before creating

Show a confirmation block:

```
Ready to create:

  Title:    [title]
  List:     [Space › Folder › List name]
  Due:      [due date]
  Priority: [priority]
  Assignee: [Elizabeth / Claude]
  Description: [description or "(none)"]

Create this task?
```

Wait for explicit yes/approval before proceeding.
If Elizabeth corrects the list placement, update and re-confirm.

### 4. Create the task

Call `mcp__ClickUp__clickup_create_task` with:
- `list_id`: the confirmed list ID from the routing table
- `name`: title
- `description`: description (omit if empty)
- `due_date`: convert the confirmed date to a Unix timestamp in milliseconds
- `priority`: 1=urgent, 2=high, 3=normal, 4=low
- `assignees`: resolve Elizabeth's ClickUp user ID via `mcp__ClickUp__clickup_find_member_by_name` if assigning to her; omit if assigning to Claude (Claude is not a ClickUp member)

### 5. Confirm success

Reply with the task name and a direct ClickUp link if available. One sentence.
