# Discoverability playbook

Most people who accelerate discovery for niche technical work do five things repeatedly: tighten on-platform metadata, publish one strong explainer elsewhere that links home, consolidate entity signals (same person, same projects), refresh the repo on a sane cadence, and avoid waiting for viral moments.

Research synthesis (what tends to shorten the wait)

1. Treat GitHub metadata as headline plus tags. Readable names, descriptive About blurbs, topics, an honest README headline, plus activity all improve both GitHub Search and outbound snippets when Google cites the README.
2. Ship one crawlable landing page outside the Markdown-only view when you care about assistants and richer snippets. GH Pages served from `/docs` on `username.github.io/reponame` adds HTML, canonical URL, structured data.
3. Build the same knot everywhere: identical spelling of your name, links among profile, repos, LinkedIn, and posts so search builds an entity bundle instead of orphaned pages.
4. Earn a handful of reputable inbound links sooner rather than chasing hundreds of weak ones: one substantive dev.to piece, Show HN, or a Reddit thread with detail beats silent perfectionism.
5. Expect honest latency. Exact-name queries resolve faster than contested phrases like optical computing head terms. Competitive keywords compound over quarters, not afternoons.

Already implemented in HoloWeights (copy these files when you sync the repo)

- `CITATION.cff` for citation indexes and citation-style discovery.
- `llms.txt` pointing crawlers at the concise graph of docs.
- `docs/index.html`, `docs/sitemap.xml`, `docs/robots.txt` for GitHub Pages after you flip one switch in repo settings.

What you enable once on GitHub (about two minutes each)

Settings → Pages → Build and deployment → Source: Deploy from branch, folder `/docs`, branch `main`. After the first publish, optional: add property `mprahboamey.github.io` in Google Search Console and request indexing for `/holoweights/`.

Optional outbound draft for dev.to or your blog

Title idea: Packing LLM weights like a hologram stack still lives on RAM (and that is fine)

Paste and adapt HoloWeights `README.md` lead plus one figure or table from `RESULTS.md`, end with hard links to the GitHub repo, PHOTEX-clean, LinkedIn profile, and this Pages URL once live. Cross-post lightly to X with the same wording so every mention reinforces the knot.
