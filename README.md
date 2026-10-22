# epistemic-ontology

A shared ontology for **what is known, how it is known, and who it is about**:
facts and findings, attributed claims, analyst assessments, the sources and
evidence behind them, and the people and organisations they concern.

It is written once, as a common core, and adopted by several independent
projects through short **profiles** that each declare the subset they use.
It is built from established standards rather than invented terms.

**Status:** version 0.1. SPEC-001 to SPEC-004 are approved; SPEC-005 is approved; ICS 206-01 is mapped and its text is filed in [references/](references/). Before 1.0 any term may still change by a recorded decision; see
[CHANGELOG.md](CHANGELOG.md).

## Why a common core

Research projects keep rediscovering the same distinctions: "the source says
X" is not "X is true"; a quotation is not the document it came from; a name
is not the thing named; confidence in a judgment is not the probability of the
event. Writing them down once, with the standard each one comes from, lets
different projects exchange work without translating it.

## Layers

```
Standards            CIDOC CRM · CRMinf · PROV-O · W3C Web Annotation · SKOS · ISO 11179 · ICD 203
   ↓ grounds
Common core          specs/ in this repository
   ↓ narrowed by
Project profiles     one short document per adopting project, kept in that project
```

- **Common core** (this repo): the terms, patterns and rules every adopter
  shares. It contains no project-specific material and never names a case, a
  client or a partner.
- **Profiles** (in each adopting project): which kinds, relations and
  vocabularies the project uses, any stricter rules it applies, and any term
  it adds. A profile may leave out part of the core and may add terms of its
  own; it may not give a core identifier a different meaning.

## Specifications

| Spec | Subject | Status |
|---|---|---|
| [SPEC-001](specs/SPEC-001-core-assertion.md) | The core assertion pattern: findings, claims, assessments, evidence, uncertainty, absence | Approved 0.1 |
| [SPEC-002](specs/SPEC-002-persons-and-organisations.md) | Persons and organisations: names and identifiers as assignments, status, roles over time, matching, merge and split, the person policy a profile must declare | Approved 0.1 |
| [SPEC-003](specs/SPEC-003-sources-captures-excerpts.md) | Sources, captures and excerpts: documentary layers, holdings and completeness, capture series, third-party captures, the anchoring rule, quotations and their derivations, declared dependence | Approved 0.1 |
| [SPEC-004](specs/SPEC-004-crosswalks.md) | Crosswalks to FollowTheMoney, BODS and schema.org: term-by-term mappings, what each loses, and the rules for exports and imports | Approved 0.1 |
| [SPEC-005](specs/SPEC-005-icd-203-tradecraft.md) | Mapping to the IC Analytic Standards (ICD 203) and Sourcing Requirements (ICD 206): what the core carries of each, the gaps found (assumptions, indicators, source-quality factors) and the owner's decisions on them. ICS 206-01 (open-source citation) mapped, with a `note` on the evidence link and a `process_note` on an automated contribution. | Approved 0.1 (decisions 1 to 5, 7 and 8) |

Vocabularies as SKOS: approved 0.1 in [vocab/](vocab/), 18 concept schemes for
the controlled values the specifications define. SHACL shapes for the SPEC-001
conformance rules, approved 0.1, in [shapes/](shapes/), with the RDF names they
use in [core/](core/) (approved 0.1). A JSON-LD context for the SPEC-001 record
elements, approved 0.1, in [context/](context/). Reference texts of standards
the specifications cite, kept as supplied (any change is stated in the file), in [references/](references/): they
are third-party documents, not this repository's work, and are outside its
licence (see Licence).

## Standards used

| Need | Standard |
|---|---|
| Things in the world: actors, places, events | CIDOC CRM (ISO 21127), conceptually |
| Beliefs and arguments over evidence | CRMinf |
| Provenance: who asserted what, derived from what | W3C PROV-O |
| Pointing at a passage in a preserved copy | W3C Web Annotation (text quote and position selectors) |
| Controlled vocabularies | SKOS, with the ISO/IEC 11179 registry pattern |
| Probability wording; analytic tradecraft | ICD 203 likelihood bands; the nine tradecraft standards; ICD 206 sourcing requirements (both mapped in SPEC-005) |
| Partial dates | ISO 8601, with EDTF where uncertainty must be expressed |
| Languages and scripts | BCP 47 |
| Interchange | FollowTheMoney, BODS, schema.org (crosswalks, not the model) |

## Conventions

- **Terms are decided, not drifted.** A new term, or a change to an existing
  one, is a recorded decision in the changelog, not a quiet edit.
- **Identifiers never change meaning.** A retired term is deprecated and kept.
- **Public by construction.** Everything here is public. Examples use invented,
  neutral subjects.
- **Specifications use RFC 2119 / RFC 8174 wording** (MUST, SHOULD, MAY) in
  capitals only where a conformance test can follow.

## Contributing

This is a personal working standard. Issues and comments from people who work
on ontologies are welcome, in particular on whether a mapping to a standard is
right.

## Licence

Everything in this repository, except the third-party texts in
[references/](references/), is licensed under
[Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may
share and adapt it, including commercially, if you credit it. If code or schema
files are added later, a separate code licence may be added for them (see the
CHANGELOG).
