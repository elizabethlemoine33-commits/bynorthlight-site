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
- Quebec Law 25 mentions must link to CAI's Law 25 page (French only — no real English page exists): `https://www.cai.gouv.qc.ca/protection-renseignements-personnels/sujets-et-domaines-dinteret/principaux-changements-loi-25`
- Registered entity name is "Northlight Advisory Services" — never shorten in schema, sameAs, or legal contexts
- Internal links open in the same tab (no `target="_blank"`)
- Email addresses (decided Oct 14 2026): `support@bynorthlight.ca` for privacy pages and privacy or data requests (and general support); `communications@bynorthlight.ca` for newsletter and social (Aurora Brief sender, subscription pages). `elizabeth@bynorthlight.ca` is allowed for personal contact, but avoid adding it to new pages. `hello@bynorthlight.ca` does not exist — never use it
- Privacy-law links (PIPEDA, GDPR, Quebec Law 25, BC and Alberta privacy law) are always dusk purple (#8B6FD4; darker #6B4FB8 on printables). This is a CSS rule keyed on the link address in each layout, so new links are purple automatically. Other content links stay teal. "Subscribe" and "Back to post" links stay visually prominent (not plain teal)
- Text on a gradient button or gradient background is always white, never teal (teal on the gradient is unreadable). Brand gradients (all four colours): bars and dividers 90deg 0/30/65/100%; gradient text 105deg 0/33/66/100%; fills 135deg 0/33/66/100%; primary buttons 105deg 0/33/66/100%. Colours #4FC3C8, #5B8DD9, #8B6FD4, #C46FAA
