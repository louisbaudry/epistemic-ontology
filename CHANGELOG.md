# Changelog

Versions follow the specification set as a whole. Before 1.0, any minor
version may change a term; after 1.0, a change to a term's meaning is a major
version and the old term is deprecated, not removed.

## 0.1.0 — unreleased

- Repository created.
- SPEC-001 (core assertion pattern) drafted.
- Decision: `fact` is a derived display label for a `finding` with at least one
  active supporting evidence link, not a stored kind (owner, 2026-10-03).
- Decision: `finding`, `claim` and `assessment` are required kinds;
  `observation`, `hypothesis` and `project-conclusion` are optional, with a rule
  for receiving an unsupported kind (owner, 2026-10-03).
- Decision: `not-assessed` is a core analytic-confidence value, a state and not
  a level, dropped (never mapped to `low`) when exchanging with a three-level
  system (owner, 2026-10-03).
