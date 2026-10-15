# SPEC-005 — Mapping to the IC Analytic Standards (ICD 203)

**Version:** 0.1 | **Status:** Decisions 1 to 5 approved by the owner, 2026-10-15; decision 6 (ICD 206) open
**Supersedes:** — | **Superseded by:** —
**Builds on:** SPEC-001 (core assertion pattern), SPEC-003 (sources, captures and excerpts)
**Upstream:** none cited. The mapping is to an external directive, not to upstream decision records.

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction, on 2026-10-15. The owner decided §7 decisions 1 to 5 on the
same day, each as recommended; decision 6 stays open until an ICD 206 text is
supplied. The recommendations were implemented in the same change: SPEC-001
(§3, §5.3, §5.4, §11), the vocabularies, the core terms, the shapes and the
JSON-LD context. Those machine-readable files were run (22 shape tests and the
context checks pass under pyshacl and rdflib); they were checked against this
text, not against any second tool.

- **Read in full:** Intelligence Community Directive (ICD) 203, *Analytic
  Standards*, signed 2 January 2015, from the text layer of the copy kept in
  the ODNI archive. That copy also carries two technical amendments (one signed
  21 January 2022, a later one that cites a memorandum of August 2022). Sections
  read: the purpose and policy (D.1 to D.6), the five Analytic Standards, the
  nine Analytic Tradecraft Standards (D.6.e(1) to (9)), including the two rules
  on expressing likelihood and confidence (D.6.e(2)(a) and (b)), and the
  responsibilities (E). Quotations below are verbatim from that text.
- **Compared:** the seven likelihood terms and their order in
  [`vocab/likelihood-bands.ttl`](../vocab/likelihood-bands.ttl) against the
  table in D.6.e(2)(a). The seven terms of the first row match, in order.
- **Not verified:**
  - **ICD 206**, *Sourcing Requirements for Disseminated Analytic Products*.
    The PDF retrieved is an image scan with no text layer and was not read.
    Everything this spec says about ICD 206 is what ICD 203 says about it.
    No ICD 206 requirement is mapped here.
  - The ODNI evaluation rating criteria that ICD 203 refers to (E.1.b(1)); any
    IC element's supplemental standards (D.1); amendments to ICD 203 later than
    the copy read; how any agency applies the standards in practice.
  - That the ICD 203 percentage ranges are meant as the only reading of the
    terms. The directive prints them in the same table as the terms.

---

## 1. Purpose and scope

SPEC-001 §5.3 and the likelihood vocabulary already use ICD 203's likelihood
bands. The core is also commonly described as meeting intelligence-community
standards. This specification tests that description term by term: for each
requirement of ICD 203, what the core carries, what it only partly carries, and
what is missing.

**ICD 203 is a standard for analytic products, not a data model.** Most of what
it asks is a property of a finished piece of analysis (a clear main message, an
effective graphic), not of a record. A set of records cannot be "ICD 203
compliant". What a record can do is carry the elements a product-level check
needs. This specification lists those elements and the gaps.

**In scope:** a mapping of the five Analytic Standards and the nine Analytic
Tradecraft Standards to core elements; the gaps; candidate decisions to close
them.

**Out of scope:** ICD 206 (unread, see the provenance block); any source
reliability or information credibility grading scale; alignment with a formal
top-level or mid-level ontology; classification and dissemination markings;
anything about a project's own products.

Key words follow RFC 2119 and RFC 8174, in capitals only where a conformance
check can follow.

## 2. Terms

| Term | Meaning |
|---|---|
| **Strength** | `carried` (the core has an element with the same purpose), `partly` (it covers some of what the standard asks), `not carried` (no counterpart), `product-level` (the requirement is a property of a finished product, not of a record). |
| **Assumption** | As ICD 203 defines it (D.6.e(3)): "suppositions used to frame or support an argument". They "affect analytic interpretation of underlying intelligence information". |
| **Judgment** | As ICD 203 defines it (D.6.e(3)): "conclusions based on underlying intelligence information, analysis, and assumptions". |
| **Indicator** | ICD 203 uses the word ("indicators that, if detected, would alter judgments") and does not define it in the text read. §4.2 proposes a reading. |

No core identifier is minted or changed by this specification.

## 3. The nine Analytic Tradecraft Standards

Numbers follow ICD 203 D.6.e. The "asks" column paraphrases the directive.
The strengths are those found when the specification was drafted; §4 records
what each decision of 2026-10-15 changed.

| ICD 203 standard | What it asks | Core element | Strength | What is missing |
|---|---|---|---|---|
| (1) Describes quality and credibility of sources, data and methodologies | Identify the underlying sources and methods. Describe the factors that affect source quality: "accuracy and completeness, possible denial and deception, age and continued currency of information, and technical elements of collection as well as source access, validation, motivation, possible bias, or expertise". Use source summary statements (strongly encouraged) for "a holistic assessment of the strengths or weaknesses in the source base". | Source, holding, capture and completeness (SPEC-003); independence of origin and the seven dependence relations (SPEC-001 §5.2); `supports` / `contradicts` stance (§5.1) | partly | The quality factors are not carried (§4.3). Holding completeness (SPEC-003 §4) is about a copy of a source, not the accuracy or completeness of what the source says. There is no source summary statement (§4.3). |
| (2) Expresses and explains uncertainty | State the likelihood of an event or development and the analyst's confidence in the basis, using the terms of one table row. Note the causes of uncertainty and "how uncertainties affect analysis". Identify "indicators that would alter the levels of uncertainty". | Likelihood bands and analytic confidence, each with a rationale (SPEC-001 §5.3); absence states for knowledge gaps (§6) | carried for the two dimensions; partly for the rest | Indicators (§4.2). The same-sentence rule (§4.5). The percentage ranges and the second row of terms (§4.4). |
| (3) Distinguishes information from assumptions and judgments | Separate statements of underlying information from statements of assumption or judgment. State assumptions "explicitly when they serve as the linchpin of an argument or when they bridge key information gaps", and "explain the implications for judgments if assumptions prove to be incorrect". | `claim` and `finding` (information) are separate kinds from `assessment` (judgment); a `claim` is never a `finding` (SPEC-001 §3) | partly | There is no way to record an assumption (§4.1). |
| (4) Incorporates analysis of alternatives | "Identify and assess plausible alternative hypotheses", their assumptions and likelihood, and the indicators that would affect them. | `hypothesis`, an optional kind (SPEC-001 §3) | partly | Nothing groups the hypotheses that compete to explain one thing, or records that one was assessed against another (§4.6). |
| (5) Demonstrates customer relevance and addresses implications | Provide insight on issues relevant to the customer and say what follows. | None in the core. Relevance is a profile-defined dimension (SPEC-001 §5.3). | product-level; carried by a profile that defines relevance | None in the core, by an earlier decision. |
| (6) Uses clear and logical argumentation | A main message up front; every judgment supported by relevant information and coherent reasoning; "acknowledge significant supporting and contrary information". | `basis` (evidence links and prose reasoning, SPEC-001 §4); stance `contradicts` | partly | The main message and the internal consistency of a text are product-level. A record can show that contrary evidence is linked, and that it is not hidden. |
| (7) Explains change to or consistency of judgments | Say whether a judgment is consistent with, or a change from, earlier analysis, or is initial coverage. | Append-only `supersedes`; `asserted_at` apart from `valid_time` (SPEC-001 §4, §8) | carried | The sentence that explains the change is product-level. |
| (8) Makes accurate judgments and assessments | Express judgments "as clearly and precisely as possible", "addressing the likelihood, timing, and nature of the outcome or development". | Likelihood band; partial `valid_time` (SPEC-001 §4, §8) | product-level | Whether a judgment later proved accurate is not recorded (no outcome record exists). |
| (9) Incorporates effective visual information | Use tables, charts and images where they clarify. | None | product-level | — |

### 3.1 The five Analytic Standards

D.6 requires every product to be objective, independent of political
consideration, timely, based on all available sources, and to exhibit the
tradecraft standards. These describe the analyst's conduct and the product's
timing. A record cannot show them. One element is checkable: the fourth ("based
on all available sources") asks analysts to "identify and address critical
information gaps". The core carries that gap as an absence state, such as
`not-researched` or `no-evidence-found` (SPEC-001 §6), which is `carried`.

## 4. Gaps and decisions

Each subsection states the gap, the options, the recommendation and, for
decisions 1 to 5, the decision (owner, 2026-10-15).

### 4.1 Assumptions (ICD 203 standard 3)

**Gap.** The core has no way to record an assumption. An assumption is not a
`claim` (nobody asserted it as true of the world, and it is held by the
analyst), not a `finding` (no investigation concluded it), not an `assessment`
(it is not a conclusion), and not a `hypothesis` (a hypothesis is put forward
for testing, SPEC-001 §3, whereas an assumption is held so that an argument can
proceed).

**What a record would need.** The assumption itself; the judgments that depend
on it; whether it is a linchpin or bridges a gap; and what follows for those
judgments if it is wrong.

**Options.**

- **A. Add a kind `assumption`** with a `depends-on` relation from each
  dependent assertion. Clear and checkable. Needs a recorded decision to add a
  kind (SPEC-001 §3 rule 5) and touches the six-kind vocabulary, the SHACL
  shapes and the JSON-LD context.
- **B. Stay inside the existing kinds:** record the assumption in the `basis`
  prose of the dependent assessment. Costs nothing. Not checkable, and the
  assumption cannot be found, reused or reviewed on its own.
- **C. A profile adds it,** following the profile rules (SPEC-001 §3 rule 5
  forbids adding a kind without a decision in this repository, so this reduces
  to A or B).

**Recommendation: A**, as an optional kind (like `observation`), with the
dependent assertion required to name it. It is the one gap in standard 3 that
cannot be closed without a new element.

**Decided: A** (owner, 2026-10-15). Written up in SPEC-001 §3 and §5.4. The open
question was settled as a routine call: the implication if the assumption is
wrong is required text on the **dependency** (one record per dependent), because
it differs between judgments that rest on the same assumption. A dependency is
not required of every assertion, because whether a judgment rests on an
unrecorded assumption cannot be checked (SPEC-001 §5.4 rule 6). The kind is the
core's own addition: upstream's epistemic vocabulary (DR-0025) does not define
it.

### 4.2 Indicators (ICD 203 standards 2, 3 and 4)

**Gap.** ICD 203 asks three times for indicators that "would alter judgments",
"would alter the levels of uncertainty" or "would affect the likelihood of
identified alternatives". The core has nowhere to record one.

**Proposed reading.** An indicator is an observable condition that, if detected,
would change a stated assertion. The text read gives no further definition.

**Options.**

- **A. A prose field** on an assessment, naming what would change it.
- **B. A structured element:** an assertion about a future observable, with a
  relation to the assertion it would change and the direction of the change.

**Recommendation: A.** B invites a monitoring and warning workflow that the core
does not need, and the directive asks only that products identify them.
Revisit B if an adopter needs to track whether an indicator occurred.

**Decided: A** (owner, 2026-10-15). `indicators` is optional prose on an
assessment (SPEC-001 §5.3).

### 4.3 Source-quality factors and the source summary (ICD 203 standard 1)

**Gap.** ICD 203 lists factors that affect source quality and credibility
(quoted in §3, row 1). The core records independence of origin and the
completeness of a holding. It records nothing about a source's possible denial
and deception, its motivation or bias, its access, its validation or its
expertise. These are the factors most relevant to open-source work.

**Constraints that already hold.** SPEC-001 §5.3 forbids collapsing assessment
dimensions into one number and forbids reusing a core identifier for a profile
dimension. A source-quality factor is not project-dependent, so by the rule
that sends only project-dependent dimensions to profiles, it could live in the
core.

**Options.**

- **A. A core, optional record of source-quality factors:** per source, any of a
  fixed list of factor identifiers (the ICD 203 list), each with a short stated
  rationale and the date it was judged. No factor has a level; nothing is
  combined into a grade or score; a factor not judged is `not-assessed`.
- **B. Leave to profiles.** Each profile defines its own.
- **C. Do nothing;** rely on the `basis` prose.

**Recommendation: A**, because ICD 203 names the factors and a shared list
lets projects exchange them. Two cautions: a factor judgment is an assessment
by a named assessor (SPEC-001 §3) and so carries `recorded_by`, a rationale and
a review state; and a letter-and-number reliability grade is a separate
question (see §4.7).

**Decided: A** (owner, 2026-10-15). Normative rules:

1. A source-quality judgment is an assertion of kind `assessment` whose subject
   is the source (a referent, SPEC-001 §2) and that carries `factor`, one
   concept of the `source-quality-factors` scheme (`vocab/`): `accuracy`,
   `information-completeness`, `denial-and-deception`, `currency`,
   `collection-technical`, `access`, `validation`, `motivation`, `bias`,
   `expertise`. The list is ICD 203 D.6.e(1)'s, in the directive's words; no
   definition is added. `information-completeness` is not the `completeness`
   of a holding (SPEC-003 §4).
2. It has the usual elements of an assessment (SPEC-001 §4): a `basis` stating
   what was found, `recorded_by`, a review state, `asserted_at`. It carries no
   level, grade, letter or number for the factor, and an implementation MUST
   NOT combine factor judgments into one value.
3. One factor per assertion. A factor nobody has judged has no record: the core
   holds no empty one. This replaces option A's idea of a `not-assessed` factor
   (a routine call: `not-assessed` is a confidence level, SPEC-001 §5.3, and
   reusing it here would give the identifier a second meaning). Where it
   matters that a factor was looked at and nothing could be determined, the
   `basis` says so.
4. A letter-and-number reliability or credibility grade is not part of this
   decision (§4.7). A judgment of one factor is never converted to one.

**Source summary statement.** ICD 203 calls it "strongly encouraged". It is a
holistic statement about the whole source base and "which sources are most
important to key analytic judgments". It belongs to a product or a body of
analysis, not to a source or an assertion. The core has no object for either
(see §1). This specification proposes no element for it, and defers to a
reading of ICD 206 (§7, decision 6).

### 4.4 Likelihood: ranges and alternative terms (ICD 203 standard 2(a))

**Gap.** ICD 203 prints, in one table, three things for each of the seven
likelihood bands: a first row of terms, a second row of alternative terms
(`remote`, `highly improbable`, `improbable`, `roughly even odds`, `probable`,
`highly probable`, `nearly certain`) and a percentage range (01–05%, 05–20%,
20–45%, 45–55%, 55–80%, 80–95%, 95–99%, as printed, so the boundary values
appear in two ranges). It says products "must use one of the following sets of
terms" and are "strongly encouraged not to mix terms from different rows"; a
product that mixes them "must include a disclaimer".
The vocabulary today records only the first row and states that "no numeric
ranges" are added.

**Options.**

- **A. Keep as is:** no ranges, no alternative terms.
- **B. Document, do not store:** add the second row as `skos:altLabel` and quote
  the printed ranges in the concept's scope note, saying that they come from
  ICD 203 and are not a value an assessment carries.
- **C. Store the ranges as machine-readable properties** on the concept.

**Recommendation: B.** It records what the directive says a term means, so the
identifiers are not read more loosely than they were defined, and it keeps the
rule that an assessment never carries a number (SPEC-001 §5.3). C risks a
consumer reading an assessment as a probability. Whether to add the ranges
needs the owner because the existing vocabulary states that none are added.

**Decided: B** (owner, 2026-10-15). The second row is `skos:altLabel`, and each
concept's scope note quotes the range ICD 203 prints for it, as documentation
(`vocab/likelihood-bands.ttl`). No range is a value an assessment carries; the
shapes still refuse a number on an assessment. The first-row terms remain the
identifiers.

### 4.5 The same-sentence rule (ICD 203 standard 2(b))

**Gap.** ICD 203 says a product that uses a confidence level "must not combine a
confidence level and a degree of likelihood, which refers to an event or
development, in the same sentence". SPEC-001 §5.3 keeps the two dimensions
apart in the record and conformance item 4 forbids one combined score. It does
not say how they are written out. An adopter may write "very likely, with high
confidence" in one sentence and still conform.

**Proposal.** Add a rendering rule to SPEC-001 §5.3: a text generated from
assertions MUST NOT state a likelihood band and an analytic confidence level in
one sentence. Adopters already applying the rule in their profile would move it
to the core.

**Recommendation: adopt.** It is a one-sentence rule with a clear test, and the
directive is explicit.

**Decided: adopt** (owner, 2026-10-15). SPEC-001 §5.3 (rendering) and §11 item 9.
The shapes cannot check it: it concerns generated text, not a record.

### 4.6 Competing hypotheses (ICD 203 standard 4)

**Gap.** `hypothesis` exists (optional). Nothing says which hypotheses compete
to explain the same thing, or how each fared against the same evidence.

**Options.** (A) A relation `alternative-to` between hypotheses; (B) a
structured evidence-by-hypothesis matrix; (C) defer.

**Recommendation: C.** A relation can follow when an adopter uses `hypothesis`
in earnest. A matrix is a method, and the core does not prescribe methods.

**Not among the six decisions;** left at the recommendation (C, defer). Nothing
changed.

### 4.7 What is not proposed

- **Reliability and credibility grading scales** (letter-and-number schemes used
  in allied military doctrine). ICD 203 does not prescribe one. They are a
  separate decision with their own trade-offs and are not treated here.
- **Source summary statement and ICD 206 sourcing rules** until ICD 206 has been
  read (decision 6).
- **Formal-ontology alignment.** Not a tradecraft matter; a separate
  specification if wanted.

## 5. What may be claimed

1. An implementation or profile MAY say that it carries the ICD 203 elements
   listed as `carried` in §3.
2. It MUST NOT say that the core, a profile or its records conform to or comply
   with ICD 203. ICD 203 applies to IC analytic products and comes with a review
   programme this repository does not run (ICD 203 D.2, E.1.b).
3. Nothing here is an endorsement by, or an affiliation with, any government
   body.

## 6. Maintaining this specification

A later amendment to ICD 203 is a new verification, not an edit. The mapping
stays at the text read; the provenance block records which text. Reading ICD
206 is a new round of the same kind.

## 7. Decisions

Decided by the owner on 2026-10-15, each as recommended in the section cited.

1. ~~**Assumptions (§4.1).**~~ Decided: an optional kind `assumption` with a
   dependency record that states what follows if it is wrong (SPEC-001 §3, §5.4).
2. ~~**Indicators (§4.2).**~~ Decided: an optional prose field on an assessment
   (SPEC-001 §5.3).
3. ~~**Source-quality factors (§4.3).**~~ Decided: an optional core record, an
   assessment with a `factor` from the ICD 203 list, no levels, no combining
   (§4.3 rules 1 to 4).
4. ~~**Likelihood ranges and alternative terms (§4.4).**~~ Decided: alternative
   labels and the printed ranges as documentation; no stored number.
5. ~~**Same-sentence rule (§4.5).**~~ Decided: in the core, as a rendering rule
   (SPEC-001 §5.3, §11 item 9).
6. **ICD 206.** Open. The owner supplies a text copy of ICD 206 (the retrievable
   PDF is an image scan), after which a further pass maps its source
   descriptors and source summary statement. Recommended before any further
   source-quality element is built, since ICD 206 may define the descriptors
   that §4.3 takes from ICD 203.
