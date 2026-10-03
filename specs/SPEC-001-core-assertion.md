# SPEC-001 — Core assertion pattern

**Version:** 0.1 (draft) | **Status:** Draft, awaiting owner review
**Supersedes:** — | **Superseded by:** —
**Upstream:** UkraineIndependenceWar DR-0024, DR-0025, DR-0026, DR-0028, DR-0029, DR-0030, DR-0065; its SPEC-0001 §2.1

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction. A draft until the owner approves it.

- **Read in full:** upstream DR-0025, DR-0026, DR-0029, DR-0062; the band
  table of DR-0065 (identifiers match the upstream registry); upstream
  SPEC-0001 §1–§2.1; one adopting project's profile of this model.
- **Read by title only:** upstream DR-0024, DR-0028, DR-0030, DR-0031. Their
  content is used here as stated in that profile and must be checked against
  the records before approval.
- **Not verified:** every mapping in §9 against the text of CRMinf, PROV-O
  and the Web Annotation Data Model. They are indicative.

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
physical schema, storage and interchange formats.

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
repeating one release are one origin. A source MAY record what it derives from
(`derived-from`), and an implementation SHOULD be able to report how many
independent origins support an assertion. Independence is a researched
conclusion, never a default. (Upstream DR-0028.)

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

A number taken from a source keeps its **original expression** as written,
together with its type (`exact`, `approximate`, `at-least`, `at-most`,
`range`), unit and stated precision. A converted or normalised value is
derived and stored beside the original, never in place of it. (Upstream
DR-0030.)

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

## 9. Mappings to standards (indicative, unverified)

| This spec | Standard | Mapping |
|---|---|---|
| Assertion | CRMinf | A belief held by the asserter in a proposition (conceptually `I2 Belief` over an `I4 Proposition Set`); `basis` as the belief's grounds. |
| Assertion, excerpt, source | PROV-O | Assertion as a `prov:Entity`; `asserter` as `prov:wasAttributedTo` an agent; `recorded_by` and the recording activity as `prov:wasGeneratedBy`; `supersedes` as `prov:wasRevisionOf`; excerpt as `prov:wasDerivedFrom` its source. |
| Excerpt locator | W3C Web Annotation | An excerpt is an annotation whose target is a preserved copy, selected by a text quote selector (exact text with prefix and suffix) and, where stable, a text position selector. |
| Vocabularies (kinds, stances, bands, absence) | SKOS | Each as a concept scheme, identifiers as concept notations. |
| `valid_time` | CIDOC CRM | A time-span on the event or state the proposition is about. |

These mappings are claims until checked against each standard's text; the
planned crosswalk spec will verify them and record where they lose information.

## 10. Review and automated assistance

`review` takes one of: `draft` (proposed, not adopted; the starting state of
anything a process proposed), `unreviewed` (entered by the analyst, not yet
checked by anyone else), `reviewed`.

Output from a language model or other automated process MUST NOT become
evidence, and MUST NOT enter as anything but `draft`. Where a process
contributed to an assertion, the record MUST carry, fixed at creation: the
process or model identifier, its role (for example `extraction`, `translation`,
`suggested-match`) and the date. A reviewer's adoption is a separate, attributed
act.

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

Items 1 to 4 are decided; the rest are open and each changes what this spec says.

1. ~~**`fact` as a kind.**~~ Decided: not a stored kind; a derived display
   label (§2). Recorded in CHANGELOG 0.1.0.
2. ~~**`observation`, `hypothesis`, `project-conclusion`.**~~ Decided:
   optional in the core; `finding`, `claim` and `assessment` required; receivers
   follow §3 rule 6. Recorded in CHANGELOG 0.1.0.
3. ~~**`not-assessed` confidence.**~~ Decided: a core value, as a state and
   not a level (§5.3). Recorded in CHANGELOG 0.1.0.
4. ~~**Where profile-level assessment dimensions live** (novelty,
   relevance).~~ Decided: in profiles only (§5.3). Recorded in CHANGELOG 0.1.0.
5. **Likelihood without a value.** `not-assessed` exists for confidence only.
   Whether likelihood needs the same state, or an absent likelihood is
   enough, is open; the question follows from item 3 and the no-silent-nulls
   principle (§6).
6. **Naming of profile dimensions.** Two profiles may each define "relevance"
   differently. Whether the core should require a naming convention for
   profile-defined dimensions (for example a profile prefix), without defining
   their values, is open.
