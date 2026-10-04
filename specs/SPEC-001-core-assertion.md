# SPEC-001 — Core assertion pattern

**Version:** 0.1 (draft) | **Status:** Draft, awaiting owner review
**Supersedes:** — | **Superseded by:** —
**Upstream:** UkraineIndependenceWar DR-0024, DR-0025, DR-0026, DR-0028, DR-0029, DR-0030, DR-0065; its SPEC-0001 §2.1

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction. A draft until the owner approves it.

- **Read in full:** upstream DR-0024, DR-0025, DR-0026, DR-0028, DR-0029,
  DR-0030, DR-0031, DR-0062; the band table of DR-0065 (identifiers match the
  upstream registry); upstream SPEC-0001 §1–§2.1; one adopting project's
  profile of this model.
- **Verified against the standards' own texts (2026-10-03):** the CRMinf 1.2.1
  class and property definitions used in §9; the PROV-O ontology file (domain,
  range and subproperty of each property used); the Web Annotation vocabulary
  file (each class and property used). Fetched from cidoc-crm.org and w3.org.
- **Not verified:** the CIDOC CRM time-span mapping, the SKOS mapping, the
  wording of the ICD 203 bands beyond DR-0065's table, and EDTF and BCP 47
  themselves. §9 marks each.

---

## 1. Purpose and scope

This specification defines the one pattern every statement of knowledge
follows, so that "what a source says", "what was established" and "what an
analyst concludes" are never confused, and so that uncertainty and absence
are recorded explicitly.

**In scope:** the assertion, its kinds, its basis in evidence, the separate
assessments attached to it, absence, quantities, revision, and the recording
of automated assistance.

**Out of scope:** persons and organisations (a later spec); sources, captures
and excerpts beyond what an evidence link needs; vocabularies as data;
argument structure (upstream's sixth layer, DR-0024; schemes and defeaters,
DR-0032 to DR-0037); physical schema, storage and interchange formats.
The pattern here covers upstream's layers 2 to 5: documentary assertions,
evidence relations, project assertions and assessments.

The key words MUST, MUST NOT, SHOULD and MAY are used as in RFC 2119 and
RFC 8174, and only where a conformance check can follow.

## 2. Terms

| Term | Meaning |
|---|---|
| **Referent** | Anything a statement can be about: a person, organisation, place, event, product type, document. |
| **Source** | A document, page, record, recording or other artefact that says something. |
| **Excerpt** | A short passage of a source, quoted verbatim with a locator. |
| **Assertion** | A recorded statement about a referent, with a kind, a holder, a basis and its uncertainty. |
| **Evidence link** | A relation from an excerpt to an assertion, with a stance. |
| **Assessment** | A judgment attached to an assertion: likelihood, analytic confidence, and any profile-defined dimension. |
| **Asserter** | The agent who holds an assertion: a person, a source, an organisation or a process. |

"Fact" is a word of ordinary speech, not a stored kind (decision recorded in
CHANGELOG 0.1.0). It is a **display label**, derived and never stored:

1. The label "fact" MAY be shown for an assertion of kind `finding` that has at
   least one active supporting evidence link (§5.1).
2. It MUST be computed when shown. If the last supporting link is withdrawn,
   the label disappears with it; nothing is migrated.
3. A profile MAY apply a stricter rule (for example, a minimum number of
   independent origins, §5.2, or a `reviewed` state). It MUST state that rule
   in the profile, and MUST NOT show the label for assertions that fail the
   rule in rule 1.
4. No stored field, identifier or export uses `fact` as a kind.

## 3. Assertion kinds

Every assertion carries exactly one kind. The identifiers are upstream's
epistemic vocabulary v1 (DR-0025) and keep upstream's meaning.

| Identifier | Meaning |
|---|---|
| `observation` | A direct record of what was perceived or measured, by a named observer, with the instrument or method. |
| `claim` | A proposition asserted by a source or actor, held by them, recorded with attribution. Recording a claim does not establish it. |
| `assessment` | An evaluative judgment by a named assessor on a stated basis. |
| `hypothesis` | A proposition put forward for testing, with no commitment that it is true. |
| `finding` | A conclusion of a defined investigation, with its scope and method. |
| `project-conclusion` | A conclusion the project as a whole adopts after review. |

Rules:

1. A kind MUST NOT be changed on an existing assertion. A claim that is later
   established is a new `finding` that cites the claim; the claim remains.
2. A `finding` MUST have at least one active supporting evidence link (§5).
   A profile that cannot meet this MUST NOT use the kind.
3. An attributed claim and a finding with the same wording are different
   assertions. "The company says X" and "X" are never the same record.
4. `finding`, `claim` and `assessment` are **required**: every conforming
   profile supports them. `observation`, `hypothesis` and `project-conclusion`
   are **optional**: a profile uses them only if it needs them, and a profile
   MUST NOT give any of the six identifiers another meaning.
5. A profile MUST NOT add a kind without a recorded decision in this
   repository.
6. **Receiving an unsupported kind.** When assertions are exchanged and the
   receiver does not support a kind, it MUST NOT silently drop the assertion or
   convert it to another kind. It MUST either store it with its original
   kind identifier, marked unsupported and held as `draft` (§10), or reject it
   with a stated reason.

## 4. The assertion record

An assertion carries the following elements. This is the upstream assertion
pattern (SPEC-0001 §2.1) made implementation-neutral.

| Element | Content | Required |
|---|---|---|
| `id` | Opaque, immutable, never reused. | MUST |
| `kind` | One of §3. | MUST |
| `subject` | The referent the assertion is about. | MUST |
| `content` | The proposition: a typed relation, a value with a quantity (§7), a status, or an absence (§6). | MUST |
| `valid_time` | When the proposition holds in the world. Partial dates allowed (§8). May be unknown. | MAY |
| `asserted_at` | When the assertion entered the record. | MUST |
| `asserter` | Who holds it (§2). For a `claim`, the source or actor making it, not the recorder. | MUST |
| `recorded_by` | Who entered it. | MUST |
| `basis` | Evidence links (§5) and, for judgments, the reasoning in prose. | MUST for `finding` and `assessment` |
| `assessment` | Likelihood and confidence where assessed (§5.3). | MAY |
| `review` | `draft`, `unreviewed` or `reviewed` (§10). | MUST |
| `supersedes` | The assertion(s) this one replaces (§8). | MAY |

Two times are always kept apart: **`valid_time`** is about the world;
**`asserted_at`** is about the record. "What did we believe on a given date"
filters on the second; "what was true of a given period" filters on the first.

## 5. Evidence and assessment

### 5.1 Evidence links

An evidence link joins one excerpt to one assertion with a **stance**:
`supports`, `contradicts` or `contextualizes`.

1. Stance belongs to the link, not to the excerpt. The same excerpt may
   support one assertion and contradict another.
2. A link MAY be withdrawn with a reason. It MUST NOT be deleted. An assertion
   whose last supporting link is withdrawn MUST be flagged for review, not
   silently left standing.
3. An excerpt MUST keep the passage verbatim in its original language. A
   translation is stored beside it, with its method, and is never evidence in
   place of the original.

### 5.2 Independence of origin

Corroboration counts **independent origins**, not documents. Five reports
repeating one release are one origin. Where it matters, a source's dependence on
another is recorded as a typed relation, from this list (upstream DR-0028):
`cites`, `reposts`, `syndicates`, `derives-from`,
`shares-underlying-document`, `shares-underlying-witness`,
`common-evidentiary-origin`. An implementation SHOULD be able to report how
many independent origins support an assertion. Independence is a researched
conclusion, the established absence of dependence, never a default assumption.
A profile MAY record only an untyped "derived from" link, and then MUST NOT
count origins as independent from it alone.

### 5.3 Assessments

Uncertainty has separate dimensions and they MUST NOT be collapsed into one
number (upstream DR-0026):

| Dimension | Meaning | Values |
|---|---|---|
| **Likelihood** | How probable the proposition is. | The ICD 203 bands, stored by identifier, never as a number: `almost-no-chance`, `very-unlikely`, `unlikely`, `roughly-even-chance`, `likely`, `very-likely`, `almost-certain` (upstream DR-0065). |
| **Analytic confidence** | How good the basis for the judgment is: evidence quality, independence of origin, strength of reasoning. | `low`, `moderate`, `high`, or `not-assessed`. |

`not-assessed` is a state, not a level: it records that nobody has yet judged
the basis, so it is never ordered between or compared with `low`, `moderate`
and `high`. It is an addition to upstream's three-level scale (DR-0026); an
exchange with a system that has only the three levels MUST drop the dimension,
not map it to `low`.

Each assessment that has a level MUST carry a short rationale;
`not-assessed` needs none.

Likelihood has no `not-assessed` value. An assessment whose likelihood is not
given, where the gap matters, records why with an absence state from §6
(for example `not-applicable` for an assessment of a capability, or
`not-researched`); it does not use a likelihood value.

Likelihood and analytic confidence are the only assessment dimensions in the
core. A dimension that depends on something a project owns, such as a baseline
of what is already known (novelty) or an agreed research question (relevance),
is defined **in the profile that uses it**, not here. A profile that adds one
MUST define its values and meaning in the profile, MUST NOT reuse a core
identifier for it, MUST NOT combine it with any other dimension into a score,
and MUST NOT average contradictory assessments.

## 6. Absence

A missing value never means "no". Where a gap matters it is recorded with one
of the absence states (upstream DR-0029):

`unknown`, `not-researched`, `no-evidence-found`, `unavailable`, `withheld`,
`redacted`, `lost-or-destroyed`, `not-applicable`, `indeterminate`.

"No evidence found" is a `finding` with its scope and method, not an empty
field. An explicit negative ("X did not occur") is an ordinary assertion:
attributed, dated and evidenced.

## 7. Quantities

A number taken from a source keeps its **original expression** as written
(in the original language where relevant), together with its semantic type
(`exact`, `approximate`, `at-least`, `at-most`, `range`, `greater-than`,
`fewer-than`), value or values and unit, stated precision, any uncertainty the
source gives, and, for a computed value, its derivation method. A converted or
normalised value is derived data, stored beside the original and never in place
of it. Aggregation respects the semantic type: a sum of `at-least` values is an
`at-least`. (Upstream DR-0030.)

## 8. Dates, language and revision

- Dates a source gives MAY be partial: ISO 8601 text (`2026`, `2026-09`,
  `2026-09-29`). A date MUST NOT be padded to a day the source did not give.
  Where uncertainty or approximation must be expressed, EDTF MAY be used.
- Language is a BCP 47 tag. An original and its transliteration carry
  different tags (`uk` and `uk-Latn`).
- Assertions are append-only. A correction is a new assertion with `supersedes`
  naming the one it replaces; the earlier one stays readable. Removal of
  material that must not be kept is a governed exception recorded outside the
  assertion, not an edit.

## 9. Mappings to standards

Verified means checked on 2026-10-03 against the standard's own published
definitions (CRMinf 1.2.1, the PROV-O ontology file, the Web Annotation
vocabulary file). They are conceptual mappings, as upstream adopts them
(DR-0010, DR-0031), not a schema.

| This spec | Standard | Mapping | Status |
|---|---|---|---|
| Assertion | CRMinf | An `I2 Belief` held by the asserter, `J4 that` an `I4 Proposition Set`, with `J5 holds to be` an `I6 Belief Value`. | Verified |
| How an assertion came about (`basis`) | CRMinf | The belief is concluded (`J2 concluded that`) by an `I1 Argumentation`. For a `finding` or `assessment` that is an `I5 Inference Making`, whose premises are beliefs (`J1 used as premise`). For adopting what a source says it is an `I7 Belief Adoption`, which rests on trust in the source and is `J7 based on evidence from` an `E73 Information Object`, and yields an `I12 Adopted Belief`. A reviewer adopting an automated proposal (§10) is an `I7`. | Verified |
| Evidence stance (`supports`, `contradicts`, `contextualizes`) | CRMinf | No stance property was found in CRMinf 1.2.1's property list; `J7` and `J1` say only that something is evidence or a premise. Stance is an extension, as upstream's evidence-relation layer (DR-0024, layer 3) treats it. | Verified: gap |
| Assertion, asserter, recording | PROV-O | The assertion as a `prov:Entity`; `prov:wasAttributedTo` an agent (domain Entity, range Agent); `prov:wasGeneratedBy` the recording activity (domain Entity, range Activity). | Verified |
| `supersedes` | PROV-O | `prov:wasRevisionOf` (Entity to Entity, a subproperty of `prov:wasDerivedFrom`), where the new assertion revises the old; otherwise `prov:wasDerivedFrom`. | Verified |
| Excerpt to source | PROV-O | `prov:wasQuotedFrom` (a subproperty of `prov:wasDerivedFrom`); PROV-O says the more specific subproperty should be used where it applies. | Verified |
| Excerpt locator | Web Annotation | An annotation whose target (`oa:hasTarget`) is a `oa:SpecificResource` with `oa:hasSource` the preserved copy and `oa:hasSelector` a `oa:TextQuoteSelector` (`oa:exact`, `oa:prefix`, `oa:suffix`) and, where stable, a `oa:TextPositionSelector` (`oa:start`, `oa:end`, 0-based). | Verified |
| Verbatim excerpt text | Web Annotation | `oa:exact` is defined as the selected text "after normalization", so it is not guaranteed verbatim. The excerpt therefore keeps the verbatim passage in its own field and uses the selector only to locate it. Position selectors hold only against the exact preserved copy they were made on, which is why upstream anchors to captures (DR-0018). | Verified: caveat |
| Vocabularies (kinds, stances, bands, absence) | SKOS | Each as a concept scheme, identifiers as concept notations. | Not verified |
| `valid_time` | CIDOC CRM | A time-span on the event or state the proposition is about. | Not verified |

The planned crosswalk spec will extend these and record where each loses
information.

## 10. Review and automated assistance

`review` takes one of: `draft` (proposed, not adopted; the starting state of
anything a process proposed), `unreviewed` (entered by the analyst, not yet
checked by anyone else), `reviewed`.

Output from a language model or other automated process MUST NOT become
evidence, and MUST NOT enter as anything but `draft`. Where a process
contributed to an assertion, the record MUST carry, fixed at creation: the
process or model identifier, its role (for example `extraction`, `translation`,
`suggested-match`) and the date. A reviewer's adoption is a separate, attributed
act. Until then the assertion is a belief held by the automated agent, not by
the project (upstream DR-0031).

## 11. Conformance

An implementation conforms to this core if, for every assertion it stores:

1. exactly one kind from §3, never changed, and the three required kinds
   supported;
2. a `finding` has an active supporting evidence link, and the last one's
   withdrawal flags it;
3. stance lives on the evidence link;
4. no single score combines likelihood, confidence or any profile dimension;
5. quantities, dates and original-language text are kept as the source gave
   them;
6. corrections supersede and never overwrite;
7. automated output enters as `draft` with its marker.

Machine-readable conformance tests (SHACL shapes) are planned and not yet
written.

## 12. Candidate decisions for the owner

Items 1 to 5 are decided; the rest are open and each changes what this spec says.

1. ~~**`fact` as a kind.**~~ Decided: not a stored kind; a derived display
   label (§2). Recorded in CHANGELOG 0.1.0.
2. ~~**`observation`, `hypothesis`, `project-conclusion`.**~~ Decided:
   optional in the core; `finding`, `claim` and `assessment` required; receivers
   follow §3 rule 6. Recorded in CHANGELOG 0.1.0.
3. ~~**`not-assessed` confidence.**~~ Decided: a core value, as a state and
   not a level (§5.3). Recorded in CHANGELOG 0.1.0.
4. ~~**Where profile-level assessment dimensions live** (novelty,
   relevance).~~ Decided: in profiles only (§5.3). Recorded in CHANGELOG 0.1.0.
5. ~~**Likelihood without a value.**~~ Decided: no new likelihood value; a
   likelihood that is not given records why with a §6 absence state (§5.3).
   Recorded in CHANGELOG 0.1.0.
6. **Naming of profile dimensions.** Two profiles may each define "relevance"
   differently. Whether the core should require a naming convention for
   profile-defined dimensions (for example a profile prefix), without defining
   their values, is open.
