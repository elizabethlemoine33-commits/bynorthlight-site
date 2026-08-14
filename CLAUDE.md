# bynorthlight.ca — Site Rules

Jekyll static site. Pushes to GitHub → Railway auto-deploys.

## source_label taxonomy (locked August 2026)

Every blog post frontmatter must use one of these exact `source_label` values:

| Label | Use for |
|---|---|
| `Blog · Essay` | First-person thinking, opinion, experience — any topic |
| `Blog · Guide` | Practical how-to content, topic guides, comparison guides |
| `Blog · Review` | Books, tools, frameworks, websites |
| `Northlight · About` | Content explicitly about Northlight as a company |
| `Aurora Brief · Essay` | Content that originated in or mirrors an Aurora Brief issue |

**Rule:** Topics belong in `tags` and sidebar filter pills — not in the label.

**Deprecated labels (do not use):** `Essay`, `Northlight · Essay`, `Northlight · Guide`, `Northlight · Practitioner's View`, `Northlight · Building in Public`, `Blog · Topic Guide`, `Blog · Comparison Guide`, `Blog · AI`, `Blog · AI Strategy`, `Blog · Operations`

The matching CSS classes in `blog/index.html` are:
- `source-essay` — boreal blue — for `Blog · Essay` and `Blog · Guide`
- `source-review` — glacial teal — for `Blog · Review`
- `source-aurora` — dusk purple — for `Aurora Brief · Essay`

## Blog index

`blog/index.html` is hand-maintained. When adding a new post:
1. Add a post card at the top of `#post-cards` (newest first)
2. Add any new `data-topics` values as filter pills in the sidebar
3. Increment the post count

## Key rules

- Author is always Elizabeth Lemoine — hardcoded in `_layouts/post.html`
- PIPEDA mentions must link to `https://www.priv.gc.ca/`
- Registered entity name is "Northlight Advisory Services" — never shorten in schema, sameAs, or legal contexts
- Internal links open in the same tab (no `target="_blank"`)
