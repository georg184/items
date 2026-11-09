# Item publication instructions

- Read [README.md](README.md) and [DEVELOPMENT.md](DEVELOPMENT.md) before
  exporting or publishing an item. They own the export commands and the
  verification and GitHub Pages workflow respectively.
- Keep author content in the canonical MuWeave library. Repository wrappers
  select existing items; creating a wrapper does not allocate a new item ID.
- Use the item's appropriate semantic block kind and inspect its dependencies.
  Keep general appearance settings at MuWeave defaults unless requested.
- Regenerate `N/index.html` with `scripts/export.py`; never hand-edit that
  generated document or recreate its graphics in another implementation.
- Preserve existing user changes. Commit only this repository's files.
- Apply the library's
  [standing item-publication authorization](../../../Python/ggpackages/muweave_library/AGENTS.md#automatic-item-publication).
  Complete verified item changes with commit, push, deployment and public
  verification without another confirmation. Honour explicit local-only
  limits and publish only the affected items and related publication files.
