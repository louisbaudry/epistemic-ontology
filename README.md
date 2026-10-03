# epistemic-ontology

A shared ontology for **what is known, how it is known, and who it is about**:
facts and findings, attributed claims, analyst assessments, the sources and
evidence behind them, and the people and organisations they concern.

It is written once, as a common core, and adopted by several independent
projects through short **profiles** that each declare the subset they use.
It is built from established standards rather than invented terms.

**Status:** draft, version 0.1. Nothing here is stable yet; see
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
Upstream decisions   UkraineIndependenceWar decision records (public), cited by DR number
   ↓ generalised by
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
- **Upstream**: the [UkraineIndependenceWar](https://github.com/louisbaudry/UkraineIndependenceWar_dot_org)
  archive settled most of this model through numbered Decision Records. This
  repository cites them rather than restating their reasoning, and follows
  them where it adopts a term. If an upstream record is superseded, the core
  follows by a new version, not an edit.

## Specifications

| Spec | Subject | Status |
|---|---|---|
| [SPEC-001](specs/SPEC-001-core-assertion.md) | The core assertion pattern: findings, claims, assessments, evidence, uncertainty, absence | Draft |
| [SPEC-002](specs/SPEC-002-persons-and-organisations.md) | Persons and organisations: names and identifiers as assignments, status, roles over time, matching, merge and split, the person policy a profile must declare | Draft |

Planned, not yet written: sources, captures and excerpts; vocabularies as SKOS with SHACL validation and JSON-LD
contexts; crosswalks to FollowTheMoney, BODS and schema.org.

## Standards used

| Need | Standard |
|---|---|
| Things in the world: actors, places, events | CIDOC CRM (ISO 21127), conceptually |
| Beliefs and arguments over evidence | CRMinf |
| Provenance: who asserted what, derived from what | W3C PROV-O |
| Pointing at a passage in a preserved copy | W3C Web Annotation (text quote and position selectors) |
| Controlled vocabularies | SKOS, with the ISO/IEC 11179 registry pattern |
| Probability wording | ICD 203 likelihood bands |
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

Everything in this repository is licensed under
[Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may
share and adapt it, including commercially, if you credit it. If code or schema
files are added later, a separate code licence may be added for them (see the
CHANGELOG).
