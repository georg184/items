# MuWeave items

This repository publishes selected MuWeave items as independent interactive
pages at <https://georg184.github.io/items/>. Item 88 is available at
<https://georg184.github.io/items/88/>.

The maintained content lives in the canonical
`ggpackages/muweave_library/items/` collection. Each `N.muweave` here is a
small standalone wrapper. Its generated `N/index.html` is a complete PyHTML
document with embedded fonts, mathematics, graphics, and browser runtime.
The repository contains generated publication snapshots, not a second
implementation of the items. A source change goes online only after export
and publication.

## Item 88

The complete wrapper is:

```text
µ! --title "Momentangeschwindigkeit"
µ! --language de-CH

µblock.text(item=88)
```

The two initial directives provide page metadata. The only content operation
selects the existing item. General typography, margins, themes, and other
appearance settings use the installed MuWeave defaults; explicit choices
inside the item remain effective. PyHTML's normal worksheet controls are
retained. Publication mode hides author working indicators.

## Export locally

Run these commands from this repository, normally
`/mnt/data/sync/software/HTML/ggprojects/items/`:

```bash
/mnt/data/sync/software/Python/ggpackages/pythonvenv1_dbg/bin/python \
  scripts/export.py 88
```

The helper invokes the installed `python -m pyhtml` frontend without modifying
its output. It creates a temporary source under `/tmp`, so a course's inherited
`.mu` settings do not affect the publication, and passes the canonical item,
image, and interactive-module roots explicitly. The wrapper's own initial
directives still apply. Every requested build must succeed before any existing
export is replaced; each HTML replacement is atomic through `ggpaths`.

The default library is the sibling
`software/Python/ggpackages/muweave_library`. Override it on another machine:

```bash
python scripts/export.py 88 --library /path/to/muweave_library
```

Use a Python 3.13+ environment containing MuWeave/PyHTML and `ggpaths`.
In the workspace, use the existing mirrored environment; do not install or
update packages there. GitHub Actions only publishes the checked-in exports
and does not need the local toolchain or the canonical library.

To create a disposable preview while keeping the current export:

```bash
/mnt/data/sync/software/Python/ggpackages/pythonvenv1_dbg/bin/python \
  scripts/export.py 88 --output-root /tmp/muweave-items-preview
```

Open `/tmp/muweave-items-preview/88/index.html` in a fresh browser profile.
Existing browser work and view preferences are learner state, not author
defaults, and must not be copied into a publication.

## GitHub Pages publication


The repository is `georg184/items`, branch `main`, remote
`git@github.com:georg184/items.git`. GitHub Pages uses **GitHub Actions**.
The workflow packages the root index and every numeric wrapper's
`N/index.html`, preserving those bytes and directories. Source wrappers,
scripts, and agent instructions are not included in the website artifact.
The workflow fails if a registered wrapper has no generated page.

The agent workflow for additional items, verification, commits and deployment
is documented in [DEVELOPMENT.md](DEVELOPMENT.md).
