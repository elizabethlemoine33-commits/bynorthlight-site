# Northlight — Coding Session Learnings

A living reference capturing decisions made, lessons learned, and step-by-step processes from our work on the Northlight site and Vault. Updated as sessions happen.

---

## Table of Contents

1. [Architectural Decisions Log](#1-architectural-decisions-log)
2. [Processes — Step-by-Step Runbooks](#2-processes--step-by-step-runbooks)
3. [Lessons Learned](#3-lessons-learned)
4. [Current State Snapshot](#4-current-state-snapshot)

---

## 1. Architectural Decisions Log

Each decision in the format: **What / Why / What we ruled out / Date**.

---

### GitHub Pages for site hosting

**Decision:** Host bynorthlight-site on GitHub Pages with a custom domain (`bynorthlight.ca`).

**Why:** Zero cost, zero server maintenance, zero deployment pipeline for a static site. Files pushed to main go live automatically. Since the codebase is already on GitHub, it's the tightest possible workflow — no third-party hosting service to set up.

**Alternatives ruled out:** Vercel and Netlify are excellent but add unnecessary complexity (build settings, deploy configs, a third login) for a site with no build step whatsoever.

*May 16, 2026*

---

### Static HTML/CSS — no framework

**Decision:** Pure HTML and CSS files. No React, no Next.js, no Vite, no npm, no build process.

**Why:** The site is one landing page and one policy page. That's two files. There's nothing interactive except a single toggle button. A framework would add node_modules, a build command, a `package.json` to maintain, and a deployment pipeline — for zero user-facing benefit. When the site grows to warrant it, we can revisit.

**Alternatives ruled out:** React/Next.js (massive overkill), Astro (sensible but still a build step we don't need yet).

*May 16, 2026*

---

### CSS custom properties for the design system

**Decision:** All brand colors defined as CSS variables in `:root`, with semantic names tied to the aurora palette.

**Why:** Semantic names (`--glacial`, `--boreal`, `--dusk`, `--aurora`) make the code readable — you can see the intent, not just a hex value. When a color needs to change, one line updates the whole site. Avoids magic numbers scattered through the CSS.

**The full palette:**
```css
--midnight:   #0E0E14   /* page background */
--surface:    #12121E   /* elevated card/panel backgrounds */
--surface-2:  #10101C   /* secondary surface level */
--border:     #1E2035   /* subtle dividers */
--border-2:   #2A2A48   /* more visible borders */
--text:       #FFFFFF   /* primary text */
--cloud:      #C8CCE0   /* body text */
--haze:       #B0B8D8   /* secondary text */
--muted:      #8A92A8   /* placeholder, disabled */
--structural: #5A6080   /* UI chrome, labels */
--glacial:    #4FC3C8   /* cyan accent */
--boreal:     #5B8DD9   /* blue accent */
--dusk:       #8B6FD4   /* purple accent */
--aurora:     #C46FAA   /* magenta accent */
```

**Aurora gradient** (used on top bar, wordmark, accent lines):
```css
linear-gradient(90deg, #4fc3c8 0%, #5b8dd9 30%, #8b6fd4 65%, #c46faa 100%)
```

*May 16, 2026*

---

### Typography: Jost (display) + Outfit (body)

**Decision:** Two Google Fonts — Jost for headings, labels, and UI elements; Outfit for body copy.

**Why:** Jost is geometric and modern with excellent letter-spacing for display use. Outfit is clean and humanist — more readable at body sizes. The combination creates visual hierarchy without feeling heavy. Both are free via Google Fonts.

**Load pattern used:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
```

`preconnect` is important — it warms up the DNS and TLS connection to Google Fonts before the browser parses the stylesheet, reducing load time.

*May 16, 2026*

---

### Dark-only theme

**Decision:** The site is dark mode only. No light/dark toggle.

**Why:** The Northlight brand is built around a dark, northern aesthetic. Adding a light mode doubles the CSS to maintain and introduces edge cases in gradient rendering. The audience (businesses, professionals) browsing a consultancy site won't be surprised by a dark theme. If light mode becomes genuinely needed, it's a future project.

*May 16, 2026*

---

### Sentry for crash reporting — EU region

**Decision:** Use Sentry for Vault crash reporting. Selected EU region (`ingest.de.sentry.io`) at project creation.

**Why:** Crash visibility is essential for a production app. Without it, bugs appear only when users email to complain. Sentry is the industry standard and has excellent Electron support. EU region was chosen so crash data is subject to GDPR rather than US law — aligns with our privacy-first positioning and makes the privacy policy easier to write.

**Key configuration choices:**
- Performance tracing disabled (`tracesSampleRate: 0`) — Sentry only activates on crashes, not during normal use
- This is the *only* data that leaves a user's device automatically
- Raw minidumps are processed by Sentry and deleted; only the readable crash report is retained

**Alternatives ruled out:** No crash reporting (unacceptable blind spots in production). Bugsnag (also good, but Sentry's Electron SDK is more mature and EU region was straightforward to select).

*May 17, 2026*

---

### ClickUp for feedback storage

**Decision:** User feedback from the in-app form is stored in ClickUp (task management platform).

**Why:** ClickUp is already in use as our task manager, so no new tool, no new login, no new subscription. It's SOC 2 Type II certified, GDPR/CCPA/CPPA compliant, and multi-region AWS. Feedback arrives directly in the workflow where we'd action it anyway.

**Data stored:** name (optional), email, feedback type, cloud provider, feedback text, app version. 12-month retention.

**Alternatives considered:** Airtable (also SOC 2, clean UI, but another tool to manage). A custom backend (overkill for a small app; adds server infrastructure).

*May 16, 2026*

---

### Windows Credential Manager / DPAPI for OAuth token storage

**Decision:** OAuth tokens for cloud provider accounts are stored in Windows Credential Manager using the `keytar` (node-keytar) library, which writes via DPAPI (Data Protection API).

**Why:** DPAPI is OS-level encryption tied to the Windows user session. Tokens cannot be read from disk — they're only decryptable during an active Windows session for that user. This means tokens never exist as plain text, and are automatically protected without us managing encryption keys.

**Key detail:** Account metadata (display name, email, provider) is stored unencrypted in `AppData\Roaming\northlight-vault\config.json` — this is intentional. That data contains no credentials; it's only needed to display the connected account list in the sidebar.

**Alternatives ruled out:** Plain file storage (insecure), SQLite (still plain text without additional encryption layer), custom encryption (unnecessary when the OS provides it).

*May 16, 2026*

---

### GitHub API for software update checks

**Decision:** Vault checks for new versions by connecting directly to GitHub's API.

**Why:** This makes the update check a device-to-GitHub connection. Northlight has no server in the middle logging who is checking for updates when. It's private by design. GitHub is already where releases are published, so no additional infrastructure is needed.

*May 16, 2026*

---

### No analytics

**Decision:** No analytics tools on the website or in the Vault app.

**Why:** Analytics tracking would contradict Vault's core value proposition — a privacy-first local app. Even privacy-respecting analytics (Plausible, Fathom) would require disclosing data leaving the device, which complicates the privacy policy. The cost of not having analytics is that we rely on user feedback for product signal instead. That's an acceptable trade-off at this stage.

*May 16, 2026*

---

### PIPEDA compliance framing

**Decision:** The privacy policy is written to satisfy PIPEDA (Personal Information Protection and Electronic Documents Act) — Canada's federal privacy law.

**Why:** Elizabeth is based in Nova Scotia, Canada. PIPEDA is the applicable federal law. Nova Scotia doesn't have a provincial private-sector privacy law, so PIPEDA applies directly. The policy addresses all ten PIPEDA fair information principles: accountability, identifying purposes, consent, limiting collection, limiting use/disclosure/retention, accuracy, safeguards, openness, individual access, and challenging compliance.

**GDPR note:** We're not in the EU, but Sentry's EU servers bring the crash data under GDPR's jurisdiction — which is actually a stronger protection than PIPEDA. No extra work required; the stricter law applies automatically.

*May 16, 2026*

---

### `noindex, nofollow` on the privacy policy page

**Decision:** `vault-privacy.html` has `<meta name="robots" content="noindex, nofollow">`.

**Why:** The privacy policy should be findable by users via the footer link, but it shouldn't appear in Google search results. Legal pages indexed by search engines can create confusion (outdated versions cached, taken out of context). Users who need it can find it; robots shouldn't index it.

*May 16, 2026*

---

## 2. Processes — Step-by-Step Runbooks

---

### Process A: Setting up GitHub Pages with a custom domain

This is the process that caused the most friction in our first session. The key insight is that the CNAME file in the repo and the DNS record at your registrar are two different things. Changing one does not affect the other.

**The correct order:**

1. **Create your repository** on GitHub and push your initial files.

2. **Enable GitHub Pages:**
   - Go to the repository → Settings → Pages
   - Under "Source," select "Deploy from a branch"
   - Choose `main` branch, `/ (root)` folder
   - Click Save

3. **Add the CNAME file to your repo** — create a file named `CNAME` (no extension) in the repo root containing only your domain name:
   ```
   bynorthlight.ca
   ```
   No `https://`, no `www`, no trailing slash. Just the bare domain.

4. **Set the DNS record at your registrar** (this is the step that's easy to miss):
   - Log into wherever you bought your domain (e.g., Namecheap, Google Domains, Cloudflare)
   - Add a CNAME record: `@` (or `www`) pointing to `elizabethlemoine33-commits.github.io`
   - For apex domains (no `www`), some registrars require A records instead — GitHub's IPs are `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`

5. **Wait for DNS to propagate.** This can take anywhere from a few minutes to 48 hours. Deleting and recreating the CNAME file does nothing during this wait — that's a GitHub-side config, not DNS.

6. **Verify propagation:**
   ```bash
   dig bynorthlight.ca
   ```
   You should see GitHub's IPs in the answer. Until you do, the site won't work on the custom domain.

7. **Back in GitHub Pages settings**, enter your custom domain in the "Custom domain" field. This must match the CNAME file exactly.

8. **Enforce HTTPS** — the checkbox only becomes available after GitHub has provisioned an SSL certificate, which happens automatically once DNS is resolved. If it's greyed out, DNS hasn't propagated yet.

**Why we hit problems:** The first session involved 3 CNAME file creates and 2 deletes within 30 minutes. That was solving the wrong problem — the CNAME file was correct each time. The actual wait was for DNS to propagate. Once it did, everything worked.

---

### Process B: Adding Sentry to an Electron app

1. **Create a Sentry project:**
   - Go to sentry.io → New Project → Select "Electron"
   - **Critical:** Select EU region when prompted. This choice cannot be changed later. EU region uses `ingest.de.sentry.io` endpoint.
   - Name the project (e.g., `northlight-vault`)

2. **Copy your DSN** — it will look like:
   ```
   https://xxxxxxxxxxxx@ingest.de.sentry.io/xxxxxxx
   ```

3. **Install the Sentry Electron SDK:**
   ```bash
   npm install @sentry/electron
   ```

4. **Initialize in the main process** (before other requires, at the top of `main.js` or `main.ts`):
   ```js
   const { init } = require('@sentry/electron/main');
   
   init({
     dsn: 'YOUR_DSN_HERE',
     tracesSampleRate: 0,  // disable performance tracing — crashes only
   });
   ```

5. **Initialize in the renderer process** (if you want renderer-side error capture too):
   ```js
   import * as Sentry from '@sentry/electron/renderer';
   
   Sentry.init({
     dsn: 'YOUR_DSN_HERE',
     tracesSampleRate: 0,
   });
   ```

6. **Test it works** — trigger a deliberate error in development:
   ```js
   throw new Error('Sentry test — delete me');
   ```
   Check your Sentry dashboard for the event. Delete the test line.

7. **Update the privacy policy** — adding Sentry is a material change that requires disclosing:
   - That Sentry is used and when it activates (crashes only)
   - What it collects (error message, stack trace, minidumps, breadcrumbs, device info, app version)
   - What it does not collect (tokens, file names, PII)
   - Where data is stored (EU servers — `ingest.de.sentry.io`)
   - Link to Sentry's privacy policy

8. **Store the DSN securely** — the DSN is not a secret (it's embedded in the built app anyway), but it should be in an environment variable during development so it doesn't get committed:
   ```
   SENTRY_DSN=https://xxxx@ingest.de.sentry.io/xxxx
   ```

---

### Process C: Setting up a GitHub repository for a new project

1. **Go to github.com → New repository**
   - Choose the right owner (personal account vs. organisation)
   - Name it clearly (e.g., `bynorthlight-site`, `northlight-vault`)
   - Set visibility: Public for open source / GitHub Pages sites; Private for app code
   - Do NOT initialise with a README if you're pushing an existing local project — it creates a merge conflict

2. **Connect your local project:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

3. **For GitHub Pages sites**, follow Process A above after the initial push.

4. **Set up branch protection** (recommended for any project you care about):
   - Settings → Branches → Add branch protection rule
   - Branch name pattern: `main`
   - Enable "Require a pull request before merging" if working with others

5. **Add a `.gitignore`** before your first real commit — much easier than removing files after they're tracked:
   - For Node/Electron: `node_modules/`, `.env`, `dist/`, `out/`
   - For a static site: nothing needed, but add `.DS_Store` if on Mac

---

### Process D: Writing a PIPEDA-compliant privacy policy

Use this as a checklist for any future app or service.

**Required sections:**

- [ ] **Who you are** — operator name, business status, contact email, physical address, website
- [ ] **Purpose of the policy** — what app/service it covers, what laws it addresses
- [ ] **What you collect** — split into: local-only data, transmitted data, feedback data. Be specific about what is encrypted vs. unencrypted and why.
- [ ] **Third-party processors** — list each one by name with: what they do, where they store data, their compliance certifications, link to their privacy policy
- [ ] **Consent mechanism** — explain how users consent to each type of data collection. For feedback: explicit checkbox. For crash reporting: disclosed in the policy itself (crash data is necessary for the service to improve, which is a legitimate purpose under PIPEDA).
- [ ] **Data retention** — specific time periods (e.g., "12 months from submission date"), not vague language like "as long as necessary"
- [ ] **User rights under PIPEDA** — must include all five: right to know what's held, access, correction, withdrawal of consent, complaint to OPC
- [ ] **Contact for exercising rights** — a real email address that gets monitored
- [ ] **How you notify of material changes** — in-app messages, release notes, email, etc.
- [ ] **Children's privacy** — even a simple statement that the app is not for under-18 users

**What counts as a material change** (requires notifying users):
- Adding new data collection
- Changing retention periods
- Adding or removing third-party processors
- Changing how data is used or shared

**What does NOT require notification:** typo fixes, clarifications, reorganisation with no substantive change.

---

## 3. Lessons Learned

---

### DNS and GitHub Pages: the CNAME file is not the DNS record

The CNAME file in your repository tells GitHub what custom domain to serve the site on. It is a GitHub configuration. It has nothing to do with your domain registrar or DNS propagation.

The DNS CNAME record at your registrar is what routes traffic from your domain to GitHub's servers. That's where the actual wait is.

When the custom domain doesn't work after adding the CNAME file: check the registrar, not the repo. Running `dig yourdomain.com` will tell you immediately whether DNS has resolved — if it still shows the registrar's default servers instead of GitHub's IPs, you're waiting on propagation and nothing you do in the repo will change that.

*May 16, 2026*

---

### Write the third-party dependency list before writing the privacy policy

The Sentry section was added to the privacy policy the day after the initial version was published, because the decision to add Sentry came after the policy was drafted. This required a same-day update and created an effective date mismatch.

Better process: before writing the privacy policy, make a complete list of every third-party service the app will use — cloud providers, crash reporting, feedback tools, update checks, analytics. Then write the policy to cover all of them. Updating a privacy policy for a new integration is fine; it's just avoidable extra work.

*May 17, 2026*

---

### Semantic color names make CSS maintainable

Using `--glacial`, `--boreal`, `--dusk`, `--aurora` instead of `--blue-1`, `--blue-2`, `--purple`, `--pink` means you can read the intent of any style rule without looking up the palette. `color: var(--structural)` tells you this is UI chrome at a glance. `color: #5A6080` tells you nothing.

The one rule: semantic names should reflect role, not shade. `--muted` is better than `--gray-3`. If you add a new color, give it a name that describes what it's for, not what it looks like.

*May 16, 2026*

---

### `nextSibling.textContent` beats index-based DOM navigation

The address toggle button updates its label between "Show address" and "Hide address". An earlier version used `parentNode.childNodes[2].nodeValue` to access the text node — this works but is brittle because it depends on the DOM having exactly the right number of nodes in exactly the right order.

The current version uses `btn.querySelector('.toggle-icon').nextSibling.textContent`, which is explicit: "the text node immediately after the toggle icon." This survives whitespace changes and HTML restructuring.

General rule: use the most direct, semantic reference available. Index-based navigation is fragile.

*May 17, 2026*

---

### Vanilla JS for a single UI behaviour — no framework needed

The entire interactive layer of the site is one function, `toggleAddress()`, handling 38 lines of HTML. There is no case for React, Alpine, or any other framework here. The complexity doesn't warrant it.

The threshold for reaching for a framework is when you have multiple pieces of state that need to stay in sync, repeated interactive components, or enough UI logic that vanilla JS becomes hard to read. One toggle button doesn't come close.

*May 16, 2026*

---

### `noindex, nofollow` belongs on legal and policy pages

Search engines indexing your privacy policy can lead to stale cached versions appearing in results, which is confusing and potentially problematic if the policy has changed. The right pattern: link to the policy from the footer so users can always find it, but tell search robots not to index it. The meta tag is two words: `noindex, nofollow`.

*May 16, 2026*

---

### EU Sentry region: make the choice at project creation

Sentry's EU region (`ingest.de.sentry.io`) is selected when you create the project. It cannot be changed after the fact without creating a new project. If privacy or GDPR matters to your product positioning, select EU at creation time — don't assume you can change it later.

*May 17, 2026*

---

### Minidumps contain more than you think

Sentry's native crash minidumps — taken at the moment of a crash — can contain file paths and environment variable names that were in memory at crash time. Sentry processes them to generate a readable crash report, then deletes the raw minidump.

This is fine for our use case, but it's worth knowing. If you're building an app where absolute certainty about what's in a crash report matters (e.g., medical data, law enforcement), you'd want to add a `beforeSend` filter to scrub paths before transmission, or evaluate whether crash reporting is appropriate at all.

*May 17, 2026*

---

## 4. Current State Snapshot

*Last updated: May 17, 2026*

**Site:**
- Live at [bynorthlight.ca](https://bynorthlight.ca)
- GitHub Pages hosting, custom domain working, HTTPS enforced
- Two pages: `index.html` (landing), `vault-privacy.html` (Vault privacy policy)
- Privacy policy effective date: May 17, 2026; Sentry section added same day

**Vault desktop app:**
- In development — not yet shipped
- Windows only at this stage (DPAPI/Keytar for credential storage is Windows-specific)
- Integrates with Google Drive, OneDrive, Dropbox via OAuth
- Crash reporting via Sentry (EU), feedback via ClickUp
- Update checks via GitHub

**Business:**
- Operating as Northlight, sole proprietor (Elizabeth Lemoine)
- Business registration pending, Nova Scotia
- Contact: elizabeth@bynorthlight.ca (general), support@bynorthlight.ca (Vault support)

**Open items:**
- Business registration
- Vault app: finish development and ship initial release
- Mac support: DPAPI is Windows-only; macOS equivalent is Keychain via Keytar (same library, different OS backend — likely straightforward to add)
- When Vault ships: the desktop app codebase will need its own LEARNINGS.md

---

*This document lives in the repo root. Update it at the end of any significant session.*
