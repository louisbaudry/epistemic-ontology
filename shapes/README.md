# Shapes

SHACL shapes for the conformance rules of [SPEC-001 §11](../specs/SPEC-001-core-assertion.md).
**Version 0.1, first draft:** a draft until the owner approves it. The
specification is the authority; each shape message cites the rule it checks.

| File | Content |
|---|---|
| [spec-001.ttl](spec-001.ttl) | The shapes |
| [../core/core.ttl](../core/core.ttl) | The RDF names the shapes use, one per record element of SPEC-001 §4, §5.1, §5.3, §7, §10 (approved 0.1, see CHANGELOG) |
| [tests/](tests/) | Example data: files named `valid-*` must conform, files named `invalid-*` must not |

Run the tests with `python3 shapes/tests/run.py` (needs `pyshacl` and `rdflib`).
The shapes are self-contained: the concept IRIs are listed in `sh:in`, so no
vocabulary graph needs loading.

## Rules checked

| SPEC-001 §11 | Checked |
|---|---|
| 1. exactly one kind | one kind, from the six of §3. "Never changed" and "the three required kinds supported" are properties of a system over time, not of a record: not checked |
| 2. a `finding` has an active supporting link | a link counts when its stance is `supports` and it has no `withdrawn_reason`. The flagging on withdrawal is the system's job: not checked |
| 3. stance on the link | one stance per link; none on an excerpt |
| 4. no single score | a number on an assessment fails; likelihood, confidence and absence state are one of their listed values |
| 5. values as given | `valid_time` is a typed date; an excerpt's text is language-tagged; a quantity keeps its original expression and one semantic type |
| 6. corrections supersede | `supersedes` is an IRI and not the record itself. That the earlier record stays unchanged is not checked |
| 7. automated output is `draft` | a record with `contributed_by` has the review state `draft`; the marker has process, role and date |

Also checked from SPEC-001 §4: the required elements, and a `basis` on a
`finding` or an `assessment`.

## Provenance of this draft

- **Read:** SPEC-001 §3, §4, §5.1, §5.3, §6, §7, §8, §10, §11 and the
  vocabularies in [../vocab/](../vocab/).
- **Checked:** both Turtle files parse; every concept IRI in the shapes exists
  in `vocab/`; the 17 files in `tests/` give the expected result under pyshacl
  0.40.1, each invalid file failing for its intended rule (the output names it).
- **Not checked:**
  - the shapes against the SHACL Recommendation's text beyond what pyshacl
    accepts, and against any second SHACL engine;
  - EDTF values in `valid_time` (only `xsd:gYear`, `xsd:gYearMonth` and
    `xsd:date` are accepted, so an EDTF value fails and a profile that uses
    EDTF needs its own shape);
  - profile dimensions (rule 4 names them): a profile adds its own shapes;
  - checks across records (history, redirects), which need the whole store;
  - the IRIs themselves: the namespace base is unconfirmed until GitHub Pages
    is enabled.
- **Examples** use invented, neutral subjects.
