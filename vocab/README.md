# Vocabularies

SKOS concept schemes for the controlled values the approved specifications
define. **Version 0.1, approved by the owner on 2026-10-15.**

One Turtle file per concept scheme, 17 schemes and 84 concepts in all. Each
concept's `skos:notation` is the identifier the specification uses, so
`:assertion-kinds-finding` carries the notation `"finding"`.

| File | Scheme | Specification |
|---|---|---|
| [assertion-kinds.ttl](assertion-kinds.ttl) | Assertion kinds | SPEC-001 §3 |
| [evidence-stances.ttl](evidence-stances.ttl) | Evidence stances | SPEC-001 §5.1 |
| [source-dependence-relations.ttl](source-dependence-relations.ttl) | Source dependence relations | SPEC-001 §5.2 |
| [likelihood-bands.ttl](likelihood-bands.ttl) | Likelihood bands (ordered) | SPEC-001 §5.3 |
| [analytic-confidence-levels.ttl](analytic-confidence-levels.ttl) | Analytic confidence levels | SPEC-001 §5.3 |
| [absence-states.ttl](absence-states.ttl) | Absence states | SPEC-001 §6 |
| [quantity-types.ttl](quantity-types.ttl) | Quantity semantic types | SPEC-001 §7 |
| [review-states.ttl](review-states.ttl) | Review states | SPEC-001 §10 |
| [referent-kinds.ttl](referent-kinds.ttl) | Referent kinds | SPEC-002 §3 |
| [name-types.ttl](name-types.ttl) | Name types | SPEC-002 §4 |
| [referent-statuses.ttl](referent-statuses.ttl) | Referent statuses | SPEC-002 §5 |
| [role-qualifiers.ttl](role-qualifiers.ttl) | Role qualifiers | SPEC-002 §6 |
| [match-states.ttl](match-states.ttl) | Match states | SPEC-002 §7 |
| [documentary-layers.ttl](documentary-layers.ttl) | Documentary layers | SPEC-003 §3 |
| [completeness-values.ttl](completeness-values.ttl) | Holding completeness values | SPEC-003 §4 |
| [excerpt-kinds.ttl](excerpt-kinds.ttl) | Excerpt kinds | SPEC-003 §7 |
| [crosswalk-strengths.ttl](crosswalk-strengths.ttl) | Crosswalk strengths | SPEC-004 §2 |

## Provenance

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction, on 2026-10-14. Everything below is a claim about what was
checked.

- **Source:** the text of SPEC-001 to SPEC-004 as approved. The specification
  is the authority; where a file and a specification differ, the specification
  is right and the file is a bug.
- **Checked:** every file parses as Turtle (rdflib 7.6.0); each scheme has one
  `skos:ConceptScheme`, and each concept has a unique notation, an `inScheme`
  link and a `prefLabel`; every notation appears in the specifications.
- **Definitions** (`skos:definition`) are given only where the specification
  gives definition text, copied from it. Where it gives none (for example the
  nine absence states, the stances, the likelihood bands), the scheme says so
  and no definition is invented. Adding definitions is a specification change,
  not a vocabulary edit.
- **Order:** the likelihood bands and the three analytic confidence levels are
  ordered collections (`skos:OrderedCollection`) in the order the specification
  lists them. `not-assessed` is in no order, as SPEC-001 §5.3 requires. The
  bands carry no numeric ranges.
- **SKOS terms checked** on 2026-10-14 against the W3C SKOS Reference
  (`ConceptScheme`, `Concept`, `inScheme`, `hasTopConcept`, `topConceptOf`,
  `notation`, `prefLabel`, `definition`, `scopeNote`, `OrderedCollection`,
  `member`, `memberList`; first 100,000 characters of the page, read through a
  summarising fetch). It found one integrity condition the first draft broke:
  every item of a `skos:memberList` must also be a `skos:member`. The two
  ordered collections now declare both, and the check above covers it.
  `skos:notation` is given as a plain literal; the Reference says its datatype
  is by convention tied to a notation system, and none is defined here.
- **Not checked:** that the ICD 203 band wording matches ICD 203 itself (the
  specification does not verify it either); SKOS validation beyond parsing
  (no SHACL or `skosify` run); rendering.
- **Not decided here:** JSON-LD contexts for the other specifications. The
  SPEC-001 context in [../context/](../context/) and the SHACL shapes in
  [../shapes/](../shapes/) use these concept IRIs and are checked against them,
  but do not validate the vocabularies.

## Open points for the owner

1. **Namespace base.** The IRIs use
   `https://louisbaudry.github.io/epistemic-ontology/vocab/`. They resolve
   only if GitHub Pages is enabled for the repository, which is a repository
   setting. Until then the base is `unconfirmed`. Changing it is a mechanical
   edit of the `@prefix :` line in each file.
2. **Licence.** The files are published under CC BY 4.0 like the rest of the
   repository (`dcterms:license` in each scheme). The changelog says a separate
   licence for code or schema files is to be revisited when the first such
   files are added; these are the first. Whether data files like these need
   one is the owner's call.
3. **Concept IRIs.** A concept's IRI is the scheme slug plus the notation
   (`vocab/assertion-kinds-finding`), not a nested path. Identifiers never
   change meaning (README, Conventions); a retired concept is deprecated, not
   deleted.
