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
- Decision: match confirmation is one rule in the core (a human, on
  discriminating evidence); a profile may be stricter. Upstream's three review
  tiers are not adopted (SPEC-002 §7; owner, 2026-10-03).
- Decision: name types stay a starting list in SPEC-002 §4; a SKOS vocabulary
  follows after the specs are approved (owner, 2026-10-03).
- Decision: no named minor is recorded as a person unless the profile's policy
  explicitly allows it and says why (SPEC-002 §9; owner, 2026-10-03).
- SPEC-003 (sources, captures and excerpts) drafted: the four documentary
  layers, holdings and completeness, capture series, third-party captures and
  custody wording, the anchoring rule, quotations with omissions and
  derivation, declared dependence. Three candidate decisions open (SPEC-003
  §11). Verified against RFC 7089; LRMoo, PREMIS and WARC mappings not
  verified.
- Decision: the upstream archive has no profile of the core and does not name
  it; the core cites upstream decision records and follows them, and nothing
  flows back (owner, 2026-10-04).
- SPEC-004 (crosswalks to FollowTheMoney, BODS and schema.org) drafted:
  term-by-term mappings with what each loses, and rules for every export and
  import (loss list, no upgrade of a claim, flattened exports, imports enter
  as `draft` claims held by the exporter). No core term minted or changed.
  Verified on 2026-10-04 against
  FtM's schema files and documentation, BODS v0.4's published schema
  reference, and schema.org's vocabulary file; FtM schemas, BODS codelists
  and schema.org date rules not read are listed in its provenance block.
- Decision: imports from an external standard enter as `draft` claims held by
  the exporter; both directions are mapped; a BODS export rounds a partial
  date and annotates it; schema.org pending terms (`Quotation`,
  `translationOfWork`) are allowed in exports and named in the loss list
  (SPEC-004 §3.4, §3.5, §6.2, §10; owner, 2026-10-04).
