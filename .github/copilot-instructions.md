--
Repository: Portfolio (static personal website)
Purpose: concise, actionable guidance for automated coding agents editing this repo
--

Summary
- This repo is a static portfolio website composed of many individual HTML pages (e.g. `index.html`, `Portfolio.html`, `Resume.html`) plus global assets `script.js` and `style.css` and asset directories `Photos/` and `Videos/`.
- There is no frontend build system or framework: pages are standalone HTML files that reference assets directly. Many mass-edits are done with small Python helpers in the repo root (see list below).

Quick contract for automated edits
- Input: small, idempotent change to one or a handful of files (HTML, CSS, JS, or helper script).
- Output: updated HTML/CSS/JS/asset references with no broken links and preserved relative paths.
- Safety: don't rename or move files in `Photos/` or `Videos/` unless you also update every referencing HTML or run the URL-update scripts.

Important files & patterns (read before editing)
- `index.html`, `Portfolio.html`, `Resume.html`: canonical pages; copy their structure when adding pages.
- `script.js`, `style.css`: single shared JS/CSS. Prefer adding small scoped CSS rules rather than large rewrites.
- `Photos/`, `Videos/`: canonical asset stores. Filenames are referenced directly from pages (case-sensitive). Backups and alternate exports live in `BU/` and nested subfolders.
- Python helpers: `fix_r2_urls.py`, `switch-to-jsdelivr.py`, `update_html_urls.py`, `update-video-urls.py`, `fix-mobile-videos.py`, `restore-original.py`. These perform repo-wide string/URL transformations—inspect before running.
- `CNAME`: indicates GitHub Pages custom domain; deploys use the repo root contents.

Developer workflows an agent should follow
- Local preview: run a static server from the repo root to validate pages and relative links:
  - python3 -m http.server 8000  # browse http://localhost:8000
- Run-only URL transformations: inspect the Python helper before executing. Use `python3 <script>.py --help` where available. Prefer dry-run modes if present.
- Asset changes: if you add or replace images/videos, update the HTML(s) that reference them. For many pages, the references are inline in the HTML—search for the filename.

Project-specific conventions and gotchas
- Pages are mostly hand-authored HTML (not templated). Reuse blocks by copying examples from existing pages rather than trying to infer a global template.
- Filenames are literal and often contain underscores and mixed case. Treat paths as case-sensitive.
- There are several ad-hoc scripts for switching CDN paths (jsDelivr/R2). The repo expects these scripts to be the canonical source for mass URL updates instead of manual global search-and-replace.
- Avoid sweeping reformatting of HTML files; keep whitespace and structure to minimize diff noise and avoid breaking relative asset paths.

Integration points & deployment notes
- GitHub Pages: This repository appears configured to publish the repository root (presence of `CNAME`). Pushing to the `main` branch will normally update the site—verify repository Pages settings in the GitHub UI.
- CDN switching: `switch-to-jsdelivr.py` and similar scripts rewrite asset URLs across pages. Use them when changing asset serving strategy.

Examples (concrete edits)
- Add a new project page: copy `SCADxNYC.html`, rename, update title/meta, update nav links in `index.html`/`Portfolio.html` and test locally.
- Replace an image used on many pages: (1) add new image to `Photos/`, (2) run `update_html_urls.py` or edit each referencing HTML, (3) preview via `python3 -m http.server`.

Checks before committing
- Serve the site locally and open the changed pages. Verify images and videos load and console has no 404s.
- If you changed CDN paths, run the appropriate helper script and do a local search for any remaining old URLs.

If something is missing
- If a reusable pattern isn't obvious (header/footer copy, navigation changes), open the main pages listed above (`index.html`, `Portfolio.html`) and follow existing structure.

Questions for maintainers (ask before large changes)
- Are any of the Python helpers expected to be run in CI or with specific Python versions/flags?
- Is the `CNAME` still valid for live deployments?

--
Please review — I can iterate this guidance to include more examples or to merge into an existing instructions file if you have one. 