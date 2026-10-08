<!-- claude-shared:begin (managed by claude-shared sync; do not edit) -->

@.claude/shared/UNIVERSAL.md
@.claude/shared/NON-CODING.md

<!-- claude-shared:end -->

# CLAUDE.md

> Shared rules for working with Louis are imported at the top of this file (the managed block above, synced from [`louisbaudry/claude-shared`](https://github.com/louisbaudry/claude-shared)). Do not edit the synced copies in `.claude/shared/`; change the rules in `shared/` of `claude-shared`. This file only adds what is specific to this repo.

## Repository-specific conventions

- **This repository is public and shared across unrelated projects.** Nothing
  from any adopting project goes in: no case, lead, client, partner, research
  subject, internal tasking, or "needed by <project>". A need that arises in a
  project is rewritten as one any analyst could have before it is proposed here.
  Examples use invented, neutral subjects.
- **One direction.** Upstream decisions (the UkraineIndependenceWar decision
  records) are cited by number and followed; nothing flows from here to
  upstream without Louis's approval, asked with options.
- **Terms change by decision.** A new term, or a changed meaning, needs Louis's
  approval and a `CHANGELOG.md` entry. Never reuse an identifier with another
  meaning; deprecate instead.
- **Say what was verified.** Every spec carries a provenance block stating what
  was read and checked and what was not. A mapping to a standard is a claim
  until verified against the standard's text.
- **Specs before code.** Machine-readable artefacts (SKOS, SHACL, JSON-LD) are
  added only once the spec they implement is approved.
- A new spec goes into the README's specification table in the same PR.
