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
- Decision: likelihood has no `not-assessed` value; a likelihood that is not
  given records why with a SPEC-001 §6 absence state, such as `not-applicable`
  (SPEC-001 §5.3, §12 item 5; owner, 2026-10-04).
- Decision: a profile-defined assessment dimension's identifier carries the
  profile's own prefix, `<profile>:<name>`; the core defines no values for it
  (SPEC-001 §5.3, §12 item 6; owner, 2026-10-04). Existing profiles that name
  novelty or relevance without a prefix have not adopted this yet and follow it
  when they next change or exchange.
- Decision: SPEC-001 and SPEC-002 approved as 0.1 by the owner on 2026-10-04.
  SPEC-003 remains a draft with three open points. Before 1.0 a term may still
  change, by a recorded decision.
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
- SPEC-003 mappings checked on 2026-10-11 against LRMoo 1.0 and 1.1.1
  (class and property declarations), PREMIS 3.0 (data dictionary), WARC 1.1
  (IIPC text) and the Web Annotation vocabulary (`oa:hasState`,
  `oa:TimeState`). Findings: LRMoo `F5 Item` is a physical class, so a digital
  copy does not clearly map to it; a PREMIS `Representation` is a complete
  rendition, so a `fragment` or `metadata-only` holding does not map to it;
  `capture` is a PREMIS glossary term and not a listed `eventType` example;
  the PREMIS `eventType` vocabulary could not be read. No core term minted or
  changed; SPEC-003 stays a draft with its three open points.
- SPEC-004 mappings checked on 2026-10-12 against FtM schema files and
  documentation, BODS v0.4's schema reference (codelists read in full) and
  schema.org pages. Findings: the BODS `unspecifiedReason` codelist has seven
  values and all are mapped; BODS `nameType`, `interestType` and `entityType`
  now mapped (a group without legal personality has no BODS counterpart;
  `entityType` and FtM `Organization` both assume legal personality); FtM
  `Directorship` and `Employment` added as role-event targets; schema.org's
  `Quotation` page says "new" and `translationOfWork` "bib", not "pending", so
  the wording of SPEC-004 §6.2 and decision 4 may be stale. Whether schema.org
  accepts partial dates is still unresolved. No core term minted or changed;
  SPEC-004 stays a draft.
- Decision: SPEC-004's loss-list rule for `Quotation` and `translationOfWork`
  names each term with the schema.org section its page gives and the version
  checked (version 30.1: `Quotation` "new", `translationOfWork` "bib"), instead
  of calling them pending; exports may still use both (SPEC-004 §6.1, §6.2,
  §10.4; owner, 2026-10-13). Replaces the wording of the 2026-10-04 decision;
  its substance (allowed, listed) is unchanged.
- Decision: `fragment` stays a completeness value for a deliberately partial
  holding, and a new `truncated` flag, with the captured length, marks a capture
  cut short; a truncated holding is never presented as the document (SPEC-003
  §4.6, §5.1, §10, §11 item 1; owner, 2026-10-13). New term: `truncated`.
- Decision: qualifying criteria for third-party archives belong in profiles; the
  core keeps only the rule that the capturing agent is recorded (SPEC-003 §5.3
  item 6, §11 item 2; owner, 2026-10-13).
- Decision: the core names WARC as an acceptable capture format and commits to
  no format (SPEC-003 §9, §11 item 3; owner, 2026-10-13). No text change.
- Decision: SPEC-003 and SPEC-004 approved as 0.1 by the owner on 2026-10-13, after the
  mapping checks and open-point decisions recorded above. Their provenance
  blocks keep the lists of what was not verified. Before 1.0 a term may still
  change, by a recorded decision.
- Decision: `assessment` keeps both senses, the assertion kind (SPEC-001 §3) and
  the likelihood and analytic confidence attached to another assertion
  (SPEC-001 §5.3), and the glossary says so; no spec text and no term changes
  (GLOSSARY.md; owner, 2026-10-13).
- Vocabularies drafted as SKOS (`vocab/`): 17 concept schemes, 84 concepts, one
  Turtle file per scheme, covering the controlled values of SPEC-001 to
  SPEC-004. Definitions only where the specifications give them. No core term
  minted or changed. Open for the owner: the namespace base (GitHub Pages,
  unconfirmed) and whether a separate licence is wanted for these first schema
  files (see the 0.1.0 licence decision).
  The SKOS terms used were checked against the W3C SKOS Reference on 2026-10-14
  (SPEC-001 §9 still lists the SKOS mapping as not verified; its text is
  unchanged).
- Shapes drafted (`shapes/`): SHACL for the SPEC-001 §11 rules a single record
  can show, with 17 example files tested under pyshacl 0.40.1. Rules about a
  system over time (kind never changed, required kinds supported, original left
  unchanged on correction) are listed as not checked. EDTF in `valid_time` and
  profile dimensions are not checked either.
- Decision (proposed, owner approval pending): the core mints RDF terms in
  `core/core.ttl`, named exactly after the record elements of SPEC-001 (`kind`,
  `subject`, `content`, `valid_time`, `asserted_at`, `asserter`, `recorded_by`,
  `basis`, `assessment`, `review`, `supersedes`) and the classes `Assertion`,
  `EvidenceLink`, `Excerpt`, `Assessment`, `Quantity`, `Automation`. Added
  beyond the spec's element names, only to make rules checkable: `contributed_by`
  (links an assertion to its automation marker), `excerpt`, `assertion`,
  `withdrawn_reason`, `text` and the Automation and Assessment fields. The
  namespace base is still unconfirmed.
- Decision: the core RDF terms in `core/core.ttl`, as proposed in the entry
  above, are approved as 0.1: the classes `Assertion`, `EvidenceLink`,
  `Excerpt`, `Assessment`, `Quantity`, `Automation`, the properties named after
  the SPEC-001 record elements, and the added `contributed_by`, `excerpt`,
  `assertion`, `withdrawn_reason`, `text` and the Automation and Assessment
  fields (owner, 2026-10-14). The shapes in `shapes/` stay a draft. The
  namespace base is still unconfirmed. Before 1.0 a term may still change by a
  recorded decision.
- JSON-LD context drafted (`context/`): one JSON-LD 1.1 context for the SPEC-001
  record elements, generated from `core/core.ttl` and `vocab/*.ttl`, with four
  examples checked against the Turtle test files and the shapes. No core term
  minted or changed. Controlled values are written by notation and read within
  their own property. Contexts for SPEC-002 to SPEC-004 wait for their RDF
  terms. Open for the owner: approval of the context; the namespace base.
- Decision: the SHACL shapes for SPEC-001 §11 (`shapes/spec-001.ttl`) and the
  JSON-LD context for the SPEC-001 record elements (`context/spec-001.jsonld`)
  are approved as 0.1 (owner, 2026-10-15). Their provenance blocks keep the
  lists of what was not checked. The vocabularies in `vocab/` they read remain
  a first draft; a change to a concept IRI would change both. Before 1.0 a term
  may still change by a recorded decision.
- Decision: the 17 SKOS concept schemes in `vocab/` (84 concepts) are approved as
  0.1 (owner, 2026-10-15). Their provenance block keeps the list of what was not
  checked (the ICD 203 band wording, SKOS validation beyond parsing). The core
  terms, shapes and JSON-LD context that read their concept IRIs are approved
  as well, so the whole machine-readable set is now 0.1. Open for the owner: the
  namespace base (GitHub Pages) and a separate licence for the schema files.
  Before 1.0 a term may still change by a recorded decision.
- SPEC-005 (mapping to the IC Analytic Standards, ICD 203) drafted
  (2026-10-15). Read for it: the text of ICD 203 (ODNI archive copy, with its
  2022 technical amendments). Not read: ICD 206 (the retrievable PDF is an
  image scan). Finding: the core carries the likelihood bands, analytic
  confidence, evidence stance and append-only revision that ICD 203 asks for,
  partly carries source quality and alternatives, and had no way to record
  assumptions or indicators. The seven likelihood terms were checked against
  ICD 203's table and match.
- Decision: SPEC-005 decisions 1 to 5, each as recommended (owner, 2026-10-15):
  1. a seventh assertion kind, `assumption`, optional, with a dependency record
     that states what follows if it is wrong (SPEC-001 §3, §5.4). It is the
     core's own addition: upstream's epistemic vocabulary (DR-0025) does not
     define it;
  2. `indicators`, optional prose on an assessment (SPEC-001 §5.3);
  3. source-quality factors: an assessment about a source carrying one `factor`
     of ten taken from ICD 203 D.6.e(1), no level, grade or number (SPEC-005
     §4.3; new scheme `source-quality-factors`);
  4. the second row of ICD 203's likelihood terms as `skos:altLabel` and its
     printed percentage ranges in the scope notes, as documentation only;
  5. the rule that a generated text never states a likelihood band and a
     confidence level in one sentence (SPEC-001 §5.3, §11 item 9).
  Routine calls inside these: the implication if wrong sits on the dependency,
  not on the assumption; an unjudged factor has no record and `not-assessed` is
  not reused for it; `core:withdrawn_reason` no longer declares a domain, since
  it now applies to evidence links and dependencies. Machine-readable files
  updated to match: `core/core.ttl`, `vocab/assertion-kinds.ttl`,
  `vocab/likelihood-bands.ttl`, `vocab/source-quality-factors.ttl` (18 schemes,
  95 concepts), `shapes/spec-001.ttl` (22 test files pass under pyshacl),
  `context/spec-001.jsonld` (rebuilt). SPEC-001 is amended in place; its status
  line says so. Decision 6 stays open: the owner supplies an ICD 206 text.
  Adopting profiles that list their kinds need to add `assumption` if they use it.
