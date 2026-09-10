# Item publication development

Audience: maintainers and AI agents publishing canonical MuWeave items.

Read [README.md](README.md) for the source boundary and exact export commands.
In the sibling `software/Python/ggpackages/` workspace, the canonical entry
is `muweave-suite/docs/AGENT_AUTHORING.md`; detailed author operations are in
`muvocab/docs/AUTHORING.md` and their exact signatures in
`muvocab/docs/AUTHOR_API.md`. Resource ownership is documented in
`muweave_library/README.md`.

## Publish another item — agent workflow

1. Read this repository's `AGENTS.md`, the MuWeave authoring guide, the
   applicable MuVocab reference, the complete canonical item, included items,
   and any context it relies on. Select only items requested for publication.
2. Create `N.muweave` using the existing numeric identity. Add title and
   language directives and the appropriate semantic placement. Use
   `µblock.text(item=N)` for text, `µblock.problem(item=N)` for a problem, or
   another documented block kind when appropriate. Native applets use
   `µblock.applet(item=N)` with their item-owned `description` part and initial
   `µ! --config applet.base_url=https://georg184.github.io/items/`. Keep shared
   teaching definitions outside the applet; Item 88 also includes Item 107.
   The typed placement overrides the item's default kind; do not turn every item into text.
3. Include a companion solution only when intended, using
   `µblock.solution(item=N)`. Other parts, external references, source-defined
   variables, required configuration, and dependent items may need explicit
   context in the wrapper. A context-dependent item is not necessarily a
   one-line export. Resolve that context semantically; do not suppress broken
   references or copy backend markup. Canonical resources remain explicit.
4. Run `scripts/export.py N`; multiple IDs may be supplied in one call.
   Keep normal appearance defaults unless the publication request specifies
   an override. The helper always uses `--publish` and retains embedded AI.
5. Inspect the whole rendered page and exercise its interactions. Check
   mathematical rendering, links, browser errors, offline startup, and the
   embedded AI content to the extent relevant to the item. For Item 88 test
   both sliders, equal times, both endpoints, and a reversed interval. Compare
   the diagram and content with its normal MuWeave rendering. Do not change a
   consumer course document as an integration fixture. If author content
   changes, also perform its normal LaTeX/HTML/AI and PDF visual checks.
6. Add a relative `N/` link with a readable title to the root `index.html`.
   Keep the item's numeric URL stable. The index is ordinary maintained HTML;
   `N/index.html` is always generated.
7. Review the diff and confirm publication authorization. Commit only the
   wrapper, verified export, intended index change, and related project files
   in this repository. Never include learner `.work` files or the complete
   private library. Follow the publication procedure below.

Each item page is one self-contained HTML artifact. It has no separately
cached application CSS, JavaScript, fonts, or MathJax files that could become
mixed across releases. Preserve this publication boundary and do not add
service workers or split its runtime into manually maintained assets.

## Commit and deployment

An explicit request to publish authorizes the commit, push, and deployment
needed for that request. Otherwise obtain publication authorization after
preparing and verifying the concrete result.

```bash
git status --short
git diff --check
git diff --stat
git add 88.muweave 88/index.html index.html
git commit -m "Publish item 88"
git push origin main
gh run list --workflow deploy-pages.yml --commit "$(git rev-parse HEAD)"
gh run watch RUN_ID --exit-status
```

Substitute the selected paths and returned run ID. On the first repository
setup, also commit its README, DEVELOPMENT, agent instructions, exporter, workflow,
`.nojekyll`, and `.gitignore`. Never force-push over existing history.

After the workflow succeeds, fetch the canonical URL and compare its SHA-256
with the local `N/index.html`. Use a fresh browser to verify the public page,
sliders, and links as well as `/items/`. If propagation still serves old
bytes, keep monitoring until the intended artifact is public. Deployment
success alone does not finish publication.

Use `gh api user --jq .login` to check API authentication separately from
`git ls-remote --heads origin` for Git's SSH transport. Run as the normal
owning user with actual network access, without changing credentials or using
`sudo`. A network failure is not an authentication failure.
