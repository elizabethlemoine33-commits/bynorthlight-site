#!/usr/bin/env node
// .github/scripts/blog-checks/run.js — the deterministic pre-publish checks on the post files given.
//   node .github/scripts/blog-checks/run.js blog/some-post.md [more.md ...]
// Writes a markdown report to blog-checks-report.md (for the PR comment), prints it, and exits 1
// when any check fails. No model call, no network, no secrets. Only posts (layout: post) are checked.
const fs = require('fs');
const path = require('path');
const { checkMarkdown, parseFrontMatter, formatChecks } = require('./blog-checks');

const files = process.argv.slice(2).filter(f => /\.md$/i.test(f));
const out = [];
let failing = 0, checked = 0;

for (const file of files) {
  if (!fs.existsSync(file)) continue;   // deleted in this change
  const md = fs.readFileSync(file, 'utf8');
  const parsed = parseFrontMatter(md);
  if (!parsed || parsed.fm.layout !== 'post') continue;
  checked++;
  const slug = path.basename(file).replace(/\.md$/, '');
  const r = checkMarkdown(md, { slug });
  if (!r.ok) failing++;
  const bad = r.checks.filter(c => c.status === 'fail' || c.status === 'warn');
  out.push(`### ${r.ok ? '✅' : '❌'} \`${file}\`${r.ok ? ' passes' : ` — ${r.failures.length} failing`}`);
  if (bad.length) out.push('', formatChecks(bad).split('\n').map(l => `- ${l}`).join('\n'));
  out.push('');
}

const head = failing
  ? `## Blog checks: ${failing} of ${checked} post(s) failing\n\nFix the ❌ items and push again. ⚠️ items are warnings and do not fail the job.\n`
  : `## Blog checks: ${checked} post(s) passing\n`;
const report = `${head}\n${out.join('\n')}\n_Deterministic checks only (no quality rating). The quality rating for code-written posts is still a manual \`/quality-rating\` run._\n`;
fs.writeFileSync('blog-checks-report.md', report);
console.log(report);
process.exit(failing ? 1 : 0);
