# SPEC-005 — Mapping to the IC Analytic Standards (ICD 203) and Sourcing Requirements (ICD 206)

**Version:** 0.1 | **Status:** Decisions 1 to 5 approved by the owner, 2026-10-15; ICD 206 mapped (§3.2); ICS 206-01 open (§7, decision 7)
**Supersedes:** — | **Superseded by:** —
**Builds on:** SPEC-001 (core assertion pattern), SPEC-003 (sources, captures and excerpts)
**Upstream:** none cited. The mapping is to an external directive, not to upstream decision records.

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction, on 2026-10-15. The owner decided §7 decisions 1 to 5 on the
same day, each as recommended. The owner then supplied a text of ICD 206 and
decision 6 became the mapping in §3.2. The recommendations were implemented in the same change: SPEC-001
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
- **Read (ICD 206, supplied by the owner on 2026-10-15):** *Sourcing
  Requirements for Disseminated Analytic Products*, as a .docx converted from a
  scan. It holds the signature block of 2 January 2015 (the technical amendment
  in the same file says "signed 22 January 2015"; the two dates are as read and
  not reconciled), the amendment adding Intelligence Community Standard 206-01,
  the directive and its glossary. The conversion left artefacts (garbled stamp
  text) and the paragraph numbers of the directive's own list are unreliable, so
  quotations below may carry transcription errors, and ICD 206 is cited by
  mechanism (D.3.a to D.3.d, the sections its own cross-references give) and
  topic, not by paragraph number.
- **Read (ICD 710, 2026-10-16):** *Classification Management and Control
  Markings System*, 21 June 2013, from the ODNI copy: purpose, applicability,
  policy D.1 and D.2 and implementation E.1 to E.5. The rest of the directive
  was not read, and later revisions were not checked.
- **Not verified:**
  - **ICS 206-01**, *Citation and Reference for Publicly Available Information,
    Commercially Available Information, and Open Source Intelligence*, which
    ICD 206 names as the rule for citing open sources. It was not supplied or
    read; it is the standard most relevant to open-source work (§7, decision 7).
  - **ICD 501** (discovery and dissemination or retrieval), named by ICD 206.
    The full text could not be downloaded; only a search-engine summary of the
    2009 text was seen. The CAPCO Register and Manual that ICD 710 relies on was
    not read.
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

**Out of scope:** ICS 206-01 (unread); any source
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

### 3.2 Sourcing requirements (ICD 206)

ICD 206 sets what a disseminated analytic product must say about its sources.
Like ICD 203 it governs products. Its four presentation mechanisms (D.3.a to
D.3.d) are ways of printing source information, so most of what it asks is
rendering. The table maps what a record can supply.

| ICD 206 mechanism or rule | What it asks | Core element | Strength | What is missing |
|---|---|---|---|---|
| Source reference citation (SRC), D.3.a | A numbered endnote each time a source is directly cited, or "a specific aspect of analysis (i.e., judgment, assessment, estimate, alternative hypothesis or view, confidence level) depends on a source". | Evidence link from an excerpt to an assertion, with a stance (SPEC-001 §5.1) | carried | The link joins an excerpt to an assertion, not to the assertion's confidence level in particular. Endnote numbering is rendering. |
| SRC: "the most original source that presents the relevant information" | Cite the original, not a copy. | Typed dependence relations; declared dependence on a source record (SPEC-001 §5.2, SPEC-003 §8) | partly | Choosing the most original source is the analyst's judgment. The core records the chain once the analyst states it. |
| SRC elements: originator, unambiguous identifier, title, date of issuance, publication or posting (date of online access if posting date unknown), page | Enough to "locate and retrieve" the source. | Source record (identifier, type, roles of creation and publication, SPEC-003 §3.3, §8); capture with original capture time and retrieval time (§5.1); excerpt locus (§7) | carried | Nothing needed beyond a rendering. The "date of online access" corresponds to the capture time. |
| SRC elements: portion marking, classification of the extracted information, overall classification | Classification markings (ICD 710). | None | not carried | By design: the core is for public-source material and carries no marking scheme. ICD 710 was not read. |
| Relevance of a source | Apparent from the cited source, "otherwise the product text shall explain why the source pertains". | Excerpt, anchor and locus show where the passage is (SPEC-003 §6, §7) | partly | There is no prose field on an evidence link saying why the source pertains. |
| Appended reference citation (ARC), D.3.b | Supplementary or background sources that do not "expressly affect or support a specific aspect or outcome of analysis", listed apart, with "a succinct explanation for why the ARC is being included". | Evidence link with stance `contextualizes` (SPEC-001 §5.1) | partly | The succinct explanation (same gap as the line above). |
| Source descriptor, D.3.c | "A brief, narrative exposition of factors that affect or indicate the quality or credibility of a single source". The factors (glossary): "accuracy and completeness, possible denial and deception, age and continued currency of information, and technical elements of collection as well as source access, validation, motivation, possible bias, or expertise". Also used "when the time of pertinent information in a source is significantly different from the time of publication of the source". | Source-quality judgments (§4.3): an assessment of kind `assessment` about a source, one `factor` each, reasoning in `basis` | carried | A descriptor is a rendering of the judgments that are germane to a judgment of the product. The time difference between information and publication is partly carried by `valid_time` and the source's dates. For intelligence sources a descriptor is derived from the source document; that does not apply to open sources. |
| Source summary statement, D.3.d | "Strongly encouraged"; a holistic assessment of sourcing: "strengths and weaknesses of the source base, which sources are most important to key judgments, what sources are meaningfully corroborative or conflicting", and the "specific subject matter expertise used". | Strengths and weaknesses: the source-quality judgments. Corroboration: independent origins (SPEC-001 §5.2). Conflict: `contradicts` links. | product-level; partly supplied | "Which sources are most important to key judgments" and "subject matter expertise used" have no counterpart. See §4.3. |
| Preserve dynamic or ephemeral sources | A record of a source that is dynamic (an internet posting), ephemeral or not systematically stored must be preserved for at least one year, five years or the time horizon for estimates. | Holding and capture (SPEC-003 §4, §5) | carried | The retention period is an organisation's policy and belongs to a profile. |
| Keep the product with its sourcing as a document of record; re-issue within 30 days if sourcing was omitted; exemptions | Process duties of IC elements. | None | product-level | — |
| Sourcing removed from publicly released versions (D.3 on downgraded or sanitised copies) | Remove sourcing information on public release. | None | product-level | No conflict with the repository's rule that exports cite sources inline: that is a choice for deliverables of a project, not for the core. |

**Findings.**

1. ICD 206's source descriptor lists the same factors as ICD 203 D.6.e(1). The
   ten factors of the `source-quality-factors` scheme (decision 3) are now
   confirmed by both directives, and both describe the descriptor as narrative.
   **Neither directive read prescribes a letter-and-number reliability or
   credibility grade.** Whether any IC element adopts one in its supplemental
   standards, or in ICS 206-01, is not established here.
2. A source reference citation maps cleanly to what the core already holds. The
   gaps are two small ones: a prose reason why a cited source pertains, and
   anything for classification markings (not wanted).
3. The source summary statement needs no stored element (§4.3).

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

**Source summary statement.** ICD 203 calls it "strongly encouraged"; ICD 206
(D.3.d) says what it covers (§3.2). It is a holistic statement about the whole
source base, so it belongs to a product or a body of analysis, not to a source
or an assertion, and the core has no object for either (see §1). With ICD 206
read, the conclusion is that **no stored element is needed**: a statement is
written for a product from records the core already holds (the source-quality
judgments, the independent origins of each assertion, the `contradicts` links)
plus what the analyst adds (which sources matter most to the key judgments, the
expertise used). A statement a process drafts is an automated contribution and
enters as `draft` (SPEC-001 §10); it never becomes a reviewed statement without
a person.

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
- **ICS 206-01.** The open-source citation standard that ICD 206 names; not
  read (decision 7).
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
6. ~~**ICD 206.**~~ Done: the owner supplied a text copy on 2026-10-15 and it is
   mapped in §3.2. It confirmed the factor list of decision 3 and changed
   nothing decided.
7. **ICS 206-01 and a "why this source pertains" note.** Open, and the owner's
   to supply: a text of ICS 206-01, *Citation and Reference for Publicly
   Available Information, Commercially Available Information, and Open Source
   Intelligence*, if it can be obtained. It is the rule for citing open
   sources, so it may fix citation elements that the core does not yet carry.
   Options for the one small gap found in §3.2 (a prose note on an evidence link
   saying why the source pertains, also used for an appended reference): (A) add
   an optional `note` to the evidence link; (B) leave it to the excerpt's
   editorial context (SPEC-003 §7); (C) wait for ICS 206-01. *Recommended: C*,
   because the standard may define the citation fields and A could be redone.

## 8. Deferred: handling labels and discovery metadata (ICD 710, ICD 501)

Status: **deferred** to a later version (owner, 2026-10-16: "version 1 or 2").
Nothing here is adopted, and no term, vocabulary or shape is added.

**What the two directives are.** ICD 710 governs classification and control
markings for intelligence information: a marking on every portion (title and
metadata included), dissemination controls, carry-forward of controls into any
new format, and the lifecycle of classification. ICD 501 (as summarised, not
read in full) requires IC elements to make information discoverable by
automated means to authorised personnel. They concern protecting and sharing
inside the IC. They add nothing to the epistemic model of §3.

**Why real markings are not for the core.** Under ICD 710 only designated
original classification authorities, or derivative classifiers working from
source documents, may classify. A project outside that system applying a real
marking would invent authority. The markings themselves live in the CAPCO
Register, which the IC controls. The core therefore never defines IC markings;
a profile that receives markings from a counterparty carries them as given.

**Trigger for building anything.** Work starts only when one of these holds:

1. a named recipient requires markings or discovery metadata;
2. a project must store material that is not public-source;
3. different users need different access to the same record.

**No-regret habits** (apply now, cost nothing):

1. Keep one handling position per excerpt (the portion of this core), and do
   not merge text with different handling into one excerpt.
2. Keep derivation links complete (SPEC-001 §5.2, `supersedes`, dependencies),
   because a derived item inherits the strictest handling of its sources
   (ICD 710 D.1.d).
3. Record handling and rights as fields with an explicit `unknown`
   (SPEC-003 §8), never as free text in a note.
4. Route every export through one allowlist, so a handling filter can later go
   in one place.
5. Keep markings out of the shared core; they are a profile term.
6. Store no nonpublic material. Retrofitting handling onto stored material is
   the hard part, and removal is a governed exception (SPEC-001 §8).

**Proposed sequence** (a proposal, not a decision).

| Stage | Work |
|---|---|
| Before v1 | Record the trigger and habits above. Draft a proposal for a small handling vocabulary, owned by a profile. |
| v1 | Handling on source and excerpt; an export filter; a strictest-wins inheritance rule; a test that an export never contains anything above its recipient's clearance. |
| v2, only with a counterparty | A mapping from the project's labels to the counterparty's markings, supplied by the counterparty; a catalogue export for discovery. |

**To obtain, if the trigger occurs:** the current CAPCO Register (not public as
far as is known), the full text of ICD 501, ICS 206-01 (decision 7), and the
counterparty's format requirements.
