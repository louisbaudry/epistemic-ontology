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
- Decision: novelty, relevance and any other project-dependent assessment
  dimension are defined in profiles, not in the core (owner, 2026-10-03).
- Decision: licence is CC BY 4.0 for everything; revisit a separate code
  licence when the first code or schema files are added (owner, 2026-10-03).
- SPEC-001 verified against upstream DR-0024, 0028, 0030, 0031 and the
  standards' own texts. Corrections: quantity types now include `greater-than`
  and `fewer-than`, uncertainty and derivation method (DR-0030); source
  dependence uses upstream's seven typed relations (DR-0028); `basis` maps to
  the CRMinf I1/I5/I7 pattern, not to a property of the belief; the
  excerpt-to-source link is `prov:wasQuotedFrom`; `oa:exact` is normalised, so
  the verbatim excerpt is kept in its own field; CRMinf 1.2.1 has no evidence
  stance property.
- SPEC-002 (persons and organisations) drafted: names and identifiers as
  assignments, referent status, roles as temporal events, the match lifecycle,
  merge and split lineage, and a person policy each profile must declare. Four
  candidate decisions open (SPEC-002 §13).
- Decision: the core ships no default person policy; each profile that records
  persons declares its own (SPEC-002 §9; owner, 2026-10-03).
