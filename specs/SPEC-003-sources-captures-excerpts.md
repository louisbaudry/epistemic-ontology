# SPEC-003 — Sources, captures and excerpts

**Version:** 0.1 | **Status:** Approved by the owner, 2026-10-13
**Supersedes:** — | **Superseded by:** —
**Builds on:** SPEC-001 (core assertion pattern), SPEC-002 (persons and organisations)

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction. Approved by the owner on 2026-10-13, after the mapping checks
and open-point decisions recorded in the CHANGELOG; the text is otherwise
unchanged by the approval.

- **Read in full:** fifteen earlier decision records, none cited here
  (CHANGELOG, 2026-10-19); this repository's SPEC-001 and SPEC-002.
- **Read by section only:** one earlier specification (the holding bridge and
  the object family inventory), not cited here.
- **Verified against the standards' own text (2026-10-03 and 2026-10-11):**
  - RFC 7089 (Memento): the definitions of Original Resource, Memento,
    TimeGate and TimeMap, and the `Memento-Datetime` header (2026-10-03).
  - The PROV-O and Web Annotation terms of SPEC-001 §9 (2026-10-03).
  - Web Annotation vocabulary (W3C, `annotation-vocab`), 2026-10-11:
    `oa:hasState`, `oa:State`, `oa:TimeState`, `oa:cachedSource`,
    `oa:sourceDate`.
  - LRMoo 1.0 and 1.1.1 (cidoc-crm.org class and property declarations),
    2026-10-11: the names and superclasses of `F1`, `F2`, `F3`, `F5` and the
    domain and range of `R3`, `R4`, `R7`. Scope-note wording was read through
    a summarising fetch and is not verified verbatim; the first 100,000
    characters of each page were read, which held all of these.
  - PREMIS Data Dictionary 3.0 (PDF, text extracted), 2026-10-11:
    `objectCategory`, `eventType`, `eventDateTime`, `eventOutcomeInformation`,
    `linkingAgentIdentifier`, and the glossary entries Capture, Fixity Check,
    Representation, Intellectual Entity, Event, Agent.
  - WARC 1.1 (IIPC publication of the standard), 2026-10-11: the eight record
    types, `WARC-Date`, and the `response` and `revisit` definitions.
- **How the 2026-10-11 reads were made:** web pages were read through a
  summarising fetch, so quoted phrases from the Web Annotation vocabulary,
  LRMoo and WARC come from that summary and not from a verbatim copy of the
  page; PREMIS was read from the extracted PDF text.
- **Not verified:** the PREMIS `eventType` controlled vocabulary at
  id.loc.gov (the fetch returned 403), so whether it lists `capture` or
  `fixity check` is unknown; OCFL; the text of ISO 28500 itself (the IIPC page
  is read, not the ISO document, and states no ISO number for 1.1); LRMoo
  scope-note wording; and any statement about how a particular web archive
  behaves. §9 marks each.
- **Not decided here:** storage layout, file formats and tooling. WARC, OCFL
  and fixity cadence are mentioned as context only (§2, §9).

---

## 1. Purpose and scope

SPEC-001 says an excerpt supports or contradicts an assertion and that an
excerpt keeps its passage verbatim. This specification defines what an excerpt
points at, so that "what exactly did this assertion rest on?" stays answerable
after the live source has changed, moved or disappeared.

**In scope:** the layers of a documentary source; what is held and how
completely; captures and capture series; third-party captures; the anchoring
rule; excerpts, quotations and their derivations; declared dependence between
sources; what a source record carries at minimum.

**Out of scope:** storage layout and file formats; fixity schedules; rights and
access policy beyond an explicit `unknown` value; collection scheduling;
source triage grading; vocabularies as data; argument structure.

Key words follow RFC 2119 and RFC 8174, in capitals only where a conformance
check can follow.

## 2. Terms

| Term | Meaning |
|---|---|
| **Source** | A document, page, record, recording or other artefact that says something (SPEC-001 §2). A source is an intellectual thing, not a file. |
| **Work, expression, manifestation, item** | The four documentary layers (§3). |
| **Holding** | The statement "this custodian possesses this item, in these preserved representations, at this completeness" (§4). |
| **Representation** | One preserved form of a holding: the original bytes as acquired, or a derivative of them (OCR text, transcript, normalised copy, translation). |
| **Capture** | An event in which a custodian acquired a state of an original resource and produced a holding (§5). |
| **Capture series** | The holdings produced by successive captures of the same original resource (§5.2). |
| **Truncated** | A flag on a holding whose capture was cut short (§4.6). Not the same as the completeness value `fragment`. |
| **Custodian** | The agent that holds a copy. Not necessarily the project. |
| **Locator** | The address of an original resource at capture time (for example a URL). Context, never an anchor (§6). |
| **Anchor** | The pinned representation an excerpt targets (§6). |
| **Quotation, paraphrase, summary** | Three distinct kinds of excerpt-like record (§7). |

## 3. Documentary layers

A source is never collapsed into "a file". Four layers stay distinct:

| Layer | Meaning | Example (invented) |
|---|---|---|
| **Work** | The intellectual creation. | A town council's annual report. |
| **Expression** | A particular realisation of the work: a language, a version, a text. | The English text of the 2031 edition. |
| **Manifestation** | A published or embodied form of an expression. | The PDF the council published; the web page that displays it. |
| **Item** | One individual copy of a manifestation. | The copy a custodian holds. |

1. An identifier, hash or URL identifies at most one layer. A record MUST say
   which.
2. A **translation, OCR output, transcript or excerpt is an expression derived
   from another**, with its own provenance (method, agent, time, input). It is
   never the original and is never evidence in place of it (SPEC-001 §5.1.3).
3. Creation and publication are events carrying agents and typed roles. Stated
   author, actual author, signer, publisher and issuing authority are distinct
   roles; a record MUST NOT merge them into one "author" field. An agent is a
   person or organisation as in SPEC-002.
4. A social-media post is a manifestation; an account is an identifier assigned
   to an actor, not the actor (SPEC-002 §4); reply, forward, quote and thread
   membership are typed relations between sources, captured where they are
   cheap to capture.
5. A source's lifecycle (published, revised, withdrawn, deleted, moved) is a
   series of dated events on its manifestations, each evidenced by a capture
   (§5) or by a statement with its own source. Absence of a later capture is
   not a deletion event (SPEC-001 §7).

## 4. Holdings and completeness

A holding links **exactly one item** to **one or more representations** and
carries a **completeness** value:

`original` · `archival-copy` · `derivative` · `screenshot` · `transcript` ·
`fragment` · `metadata-only`

1. Completeness is stated, never implied. A holding that is not `original` or
   `archival-copy` MUST NOT be presented as the document.
2. A copy held by another custodian is a holding too, with that `custodian` and
   no representation link. Possession is never assumed from a citation.
3. A holding's original representation is immutable. Adding a derivative adds a
   representation; it never alters an existing one. A correction is a new
   representation with a derivation link.
4. Each representation SHOULD carry a digest recorded at ingestion. A fixity
   check is a dated event with an outcome, failures included. A matching digest
   is a bit-level statement only: it says nothing about authenticity or truth.
5. Different captures of the same locator are **different holdings** (§5.2).
6. **`fragment` and `truncated` are different things.** `fragment` is a
   completeness value: the holding is deliberately only a part of the item, such
   as an excerpted section. `truncated` is a flag any holding may carry: its
   capture was cut short, so the representation is less than what the original
   resource served. A truncated holding records the captured length and, whatever
   its completeness value, MUST NOT be presented as the document. The flag keeps
   a truncated copy of an otherwise complete document distinguishable from a
   deliberate excerpt.

## 5. Captures

### 5.1 The capture event

A capture records: the original resource's locator; the **capturing agent**;
the **original capture time** (when the state was acquired); the
**retrieval time** (when this custodian obtained the holding), which differs
from the first when the capturing agent is a third party; the **archive record
locator** where the holding came from a third-party archive; the method; the
outcome; and the completeness (§4).

1. A **failed** capture is recorded with its outcome and reason. It is never
   silently retried into invisibility.
2. A **partial** capture (for example a truncated payload) is admitted as a
   holding carrying the `truncated` flag (§4.6), with the captured length
   recorded. It is never treated as the complete page, and is not refused merely
   for being incomplete.

### 5.2 Capture series

Successive captures of one locator form a **capture series**, ordered by
original capture time. Each is its own holding. The series is a relation among
holdings, not a version history inside one of them.

"What did this page say on date D?" is answered from the series, whoever made
the captures, with the capturing agent visible on each.

### 5.3 Third-party captures

A capture made by an archive that is not the custodian (a public web archive,
another institution, a colleague) is a capture in the same series, not a
derivative of the custodian's own captures and not a new series.

1. The capturing agent MUST be recorded and MUST NOT be the custodian unless
   the custodian made the capture.
2. The record MUST NOT read as if the custodian made a capture it did not.
   Wording shown to readers names the capturing agent and the original capture
   time.
3. **Custody wording.** A record documents custody history: acquisition,
   transfers, handling. It MUST NOT assert "chain of custody" as a status of a
   holding. The phrase is allowed only when reporting what another party
   asserts, or inside a history explicitly labelled as documented custody
   history.
4. The origin source's rights and access defaults govern a third-party capture.
   The archive is the capturing agent, not the publisher of the content.
5. A third-party capture and the custodian's own capture of the same page are
   two observations of what a server sent, at different times by different
   means. Whether they count as independent for corroboration is decided under
   SPEC-001 §5.2, never by default.
6. **Qualifying archives are a profile matter.** Which third-party archives a
   project accepts, and on what conditions (for example that the archive
   supplies the original response record, does no new crawling and leaves
   rights with the publisher), is stated in the profile. The core sets no such
   criteria; it requires only the recording rule of item 1.

## 6. The anchoring rule

An excerpt (and any other evidential annotation) MUST target a **preserved
representation** held by a custodian, version-pinned. It MUST NOT target a live
locator alone.

1. If the material is not yet preserved, **preservation precedes annotation.**
2. The live locator MAY be recorded as context on the anchor.
3. A target SHOULD carry redundant selectors where the medium allows: a text
   quote with prefix and suffix, plus a text position. Position selectors hold
   only against the exact representation they were made on, which is why the
   anchor is a pinned representation.
4. For non-text media the selector is a media fragment (audio, video
   interval), a region (image, page) or a structural path (structured
   documents). The pinning rule is the same.
5. An anchor resolves to bytes through the holding. "What exactly did this
   point at?" is then answerable without the live source.

## 7. Excerpts

An excerpt is an annotation on an anchor (§6). Three kinds stay distinct and
are never silently converted into one another:

| Kind | Content |
|---|---|
| **Quotation** | The exact passage, verbatim, in the original language. |
| **Paraphrase** | A restatement in the recorder's words, labelled as such. |
| **Summary** | A condensed account of a larger passage, labelled as such. |

A quotation MUST carry:

1. the **exact passage**, verbatim, in the original language;
2. the **anchor** (§6) and the **locus** within it (page, paragraph, interval);
3. **marked omissions**: any elision inside the passage is shown as an
   elision, never closed up;
4. **derivation** where the text passed through OCR or transcription: the
   step, its agent and method, and that the passage is the output of it;
5. **linked translations** where present, each an expression with its own
   method and agent (§3.2), shown beside the original and never in place of it;
6. **editorial context** where it changes how the passage reads.

A quotation MUST NOT be created from a paraphrase or a summary. A paraphrase
is not upgraded to a quotation by being found to match; the quotation is made
from the anchor.

Where text passed through an automated step, the excerpt is marked AI-assisted
as in SPEC-001 §10 and a person decides before it counts as evidence.

## 8. Source records and dependence

A source record carries at minimum: an identifier, a type, the roles of §3.3
where known, its original language, its rights position (with `unknown` as an
explicit value, never a blank) and its lifecycle events.

1. **Declared dependence.** Known republishing and syndication between sources
   MAY be stated once at the source level, using the typed relations of
   SPEC-001 §5.2. Items inherit that as a **hypothesis of dependence**, not a
   conclusion; independence remains a researched conclusion.
2. A triage grade, where a profile keeps one, is for ordering work only. It is
   not evidence and MUST NOT be used as a stance, a likelihood or a confidence.
3. Registry changes (a source's rights, scope, declared dependence) are
   recorded as dated changes, not silent edits.

## 9. Mappings and verification status

| Need | Standard | Mapping | Status |
|---|---|---|---|
| Work, expression, manifestation, item | LRMoo | `F1 Work` (E89 Propositional Object), `F2 Expression` (E73 Information Object), `F3 Manifestation` (E73 Information Object), `F5 Item` (E24 Physical Human-Made Thing). `R3 is realised in` (F1 to F2), `R4 embodies` (F3 to F2) and `R7 exemplifies` (F5 to F3) match §3's chain. | Verified: class names, superclasses, `R3`/`R4`/`R7` (LRMoo 1.0 and 1.1.1). Caveat: `F5` is a physical object class, so a digital copy held by a custodian is not clearly an `F5` (a summary of the 1.0 scope note lists "files" among its examples and the 1.1.1 summary does not; not reconciled). Scope-note wording not verified |
| Translation, OCR, transcript as derived expression | PROV-O | A new entity `prov:wasDerivedFrom` the original, generated by an activity with its agent. | Verified (PROV-O, as in SPEC-001 §9) |
| Excerpt to source | PROV-O | `prov:wasQuotedFrom`. | Verified (SPEC-001 §9) |
| Excerpt locator | Web Annotation | `oa:SpecificResource` with `oa:hasSource` the pinned representation and `oa:hasSelector` text-quote and text-position selectors. | Verified (SPEC-001 §9) |
| Version pinning of the target | Web Annotation | `oa:hasState` (domain `oa:ResourceSelection`, of which `oa:SpecificResource` is a subclass; range `oa:State`) to an `oa:TimeState`, whose `oa:cachedSource` is "a copy of the Source resource's representation" and whose `oa:sourceDate` (`xsd:dateTime`) is the time the source is to be read as applicable. The pinned representation is the `oa:cachedSource`. | Verified |
| Original resource, prior state, series | Memento (RFC 7089) | Original Resource = the live locator; Memento = a state of it; `Memento-Datetime` = the original capture time; TimeMap = a list of the series. A capture series corresponds to a TimeMap. | Verified (RFC 7089 definitions) |
| Preserved bytes, events, fixity | PREMIS 3.0 | `File` for preserved bytes; Event with `eventType`, `eventDateTime`, `eventOutcomeInformation` and `linkingAgentIdentifier` for ingestion and fixity checks. `capture` is a PREMIS glossary term (the process by which a repository actively obtains digital objects, preceding ingest), not a listed example of `eventType`. | Verified: the structure. Partial: a PREMIS `Representation` is "the set of stored Files and Structural Metadata needed to provide a complete rendition of the Intellectual Entity", so §4's `fragment` and `metadata-only` holdings, and any `truncated` holding, are not PREMIS Representations. Not verified: the `eventType` vocabulary |
| Web capture record | WARC (ISO 28500) | One acceptable capture format for web pages. A `response` record block "should contain the full HTTP response received over the network, including headers" (so headers and payload as served); `WARC-Date` is "the instant that data capture for record creation began", the original capture time. A `revisit` record notes content already archived, so a repeat capture may be stored without its bytes (§5.2 still treats it as its own holding). | Verified against the IIPC text of WARC 1.1; the ISO text itself is not read |
| Capturing agent, custodian | PROV-O | `prov:Agent`; the capture is a `prov:Activity`. | Verified (PROV-O) |

## 10. Conformance summary

An implementation conforms if it can show that:

1. no identifier is used for more than one documentary layer without saying so;
2. no translation, OCR output or transcript replaces its original as evidence;
3. every excerpt targets a pinned preserved representation, and none targets a
   live locator alone;
4. successive captures of one locator are separate holdings in one series, each
   with its capturing agent and original capture time;
5. no record claims a capture the custodian did not make, or a "chain of
   custody" status;
6. no quotation derives from a paraphrase or summary, and omissions and
   derivation steps are shown;
7. a holding states its completeness, a truncated capture carries the
   `truncated` flag and is not presented as the document, and no holding
   implies possession it does not have;
8. a source's rights position is stated, with `unknown` where it is.

## 11. Open points for the owner

All three are decided (owner, 2026-10-13), each as recommended. Recorded in
CHANGELOG 0.1.0.

1. ~~**Whether `fragment` should be a completeness value or a flag.**~~ Decided:
   both. `fragment` stays a completeness value for a deliberately partial
   holding; a `truncated` flag, with the captured length, marks a capture cut
   short (§4.6, §5.1).
2. ~~**Third-party archive qualifying criteria.**~~ Decided: in profiles. The
   core keeps only the rule that the capturing agent is recorded (§5.3).
3. ~~**Format commitments.**~~ Decided: the core names WARC as acceptable and
   commits to no format (§9).
