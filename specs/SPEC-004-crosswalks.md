# SPEC-004 — Crosswalks to FollowTheMoney, BODS and schema.org

**Version:** 0.1 (draft) | **Status:** Draft, awaiting owner review
**Supersedes:** — | **Superseded by:** —
**Builds on:** SPEC-001 (core assertion pattern), SPEC-002 (persons and organisations), SPEC-003 (sources, captures and excerpts)
**Upstream:** none cited. The mappings here are to external standards, not to upstream decision records.

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction. A draft until the owner approves it. Everything below was
read on 2026-10-04.

- **FollowTheMoney (FtM), read from the source:** the `main` branch schema files
  `Thing`, `Interval`, `Event`, `LegalEntity`, `Person`, `Document`, `Pages`,
  `Page`, `Interest`, `Ownership`, `Membership`, `Note`, `Mention`
  (`followthemoney/schema/*.yaml`), the package version string on that branch
  (`3.8.4`), and the documentation pages "Statements" and the `date` property
  type. A `Documentation` schema file does not exist on that branch (404).
- **BODS v0.4, read from the published documentation** (the standard's
  schema reference, key concepts and changelog pages): the objects Statement,
  Source, Annotation, Identifier, Interest, Name, Address, Publication Details,
  Record Details (relationship) and the opening of Record Details (entity), and
  the codelists Annotation Motivation, Direct Or Indirect, Record Status,
  Record Type, Source Type and Unspecified Reason (the last only in part).
- **schema.org, read from the machine-readable vocabulary file** (the "latest"
  JSON-LD release file) by looking up the definitions of the terms named in §6.
  For most terms only the opening of the definition text was read. The release
  history page lists "Version 30.1" first; the version of the downloaded file
  was not read from the file itself.
- **Not verified:** FtM `Organization`, `Company`, `PublicBody`, `Directorship`,
  `Employment`, `Family`, `Associate`, `Address`, `Value` and `Asset`; FtM
  property types other than `date`; BODS Person and Entity record details in
  full, the `nameType`, `interestType` and `entityType` codelists, the
  modelling and system requirements, and the JSON Schema file itself (not
  retrieved: the paths tried in the source repository returned 404); how any consumer
  (Aleph, OpenSanctions, a BODS validator, a search engine) treats data in
  these shapes; schema.org's rules for partial dates.
- **Not decided here:** file formats, JSON-LD contexts, converters, code. Those
  follow once the specs are approved (`CLAUDE.md`).

---

## 1. Purpose and scope

SPEC-001 §9 promised a crosswalk spec that "records where each loses
information". This is it. The three external standards are widely used for
exchanging records about people, organisations and ownership. None of them was
built around the distinctions the core makes: a source's claim is not an
established finding; evidence has a stance; uncertainty has separate
dimensions; absence is stated. Moving data across the boundary therefore loses
or invents something. This specification says what, for each standard, so that
nobody exports a claim as a fact or imports a record as a conclusion by
accident.

**In scope:** per-standard mappings (term to term), what each mapping loses,
and the rules that apply to every export and import.

**Out of scope:** the conceptual-model mappings already in SPEC-001 §9,
SPEC-002 §11 and SPEC-003 §9 (CIDOC CRM, CRMinf, PROV-O, Web Annotation,
Memento and others); storage and serialisation; machine-readable crosswalk
files; ownership and control relations between organisations (SPEC-002 §10.3
leaves them to a later spec, so §4 maps them only to show the boundary).

Key words follow RFC 2119 and RFC 8174, in capitals only where a conformance
check can follow.

## 2. Terms

| Term | Meaning |
|---|---|
| **Crosswalk** | A documented mapping between a core element and a term of an external standard, with the information the mapping loses. Not a schema. |
| **Export** | Producing data in an external standard's shape from core records. |
| **Import** | Reading data in an external standard's shape into core records. |
| **Strength** | `exact` (same meaning, nothing lost), `partial` (same idea, something lost or added), `none` (no counterpart found in the terms read). |
| **Flattened export** | An export that drops attribution, evidence or assessment because the target cannot carry them (§3.3). |
| **Loss list** | The list of core elements an export left out or reduced (§3.1). |

No core identifier is minted or changed by this specification.

## 3. Rules for every export and import

### 3.1 Say what was lost

1. An export MUST state the external standard and its version, and MUST carry
   or be accompanied by a **loss list**: which core elements (kinds,
   assessments, evidence stance, absence states, dates narrowed, name types)
   the target could not carry.
2. A round trip (export, then import) is not promised to be lossless. An
   implementation MUST NOT describe an exchange as lossless unless the loss
   list is empty.

### 3.2 Exports never upgrade

1. A `claim` MUST be exported as a claim, a source's statement or an
   attributed record, never as an unattributed property value of the referent.
   Where the target has no way to say "attributed", the export is a flattened
   export (§3.3).
2. The display label "fact" (SPEC-001 §2) is never exported as a type or value.
3. An assertion in state `draft` MUST NOT be exported as if reviewed. A target
   with no review concept gets the loss list entry, or the assertion is not
   exported.
4. A likelihood or confidence is never converted to a number to fit a target's
   scale (SPEC-001 §5.3). Where the target takes only a number, the assessment
   is left out and listed.

### 3.3 Flattened exports

A target such as an entity-and-property model may be wanted without per-value
attribution (for a search index, a graph view). That is allowed if the export
is declared flattened, carries a pointer from each value back to the core
assertion `id`, and states that the values are claims. It MUST NOT be offered
as the record of what is known.

### 3.4 Imports enter as proposals

1. Every imported record becomes a `claim` held by the exporting party
   (dataset, publisher or declarant), recorded by the importing process, in
   review state `draft` (SPEC-001 §10). An import never creates a `finding`, a
   `canonical` referent or a confirmed match (SPEC-002 §7).
2. A "verified", "approved" or "reviewed" marker in the source data is itself a
   claim by the exporter about its own process. It is kept as such and never
   sets the review state (§5.2).
3. An identifier or a deduplication key from the exporting system is an
   identifier assignment attributed to that system (SPEC-002 §4.4). A
   cluster or canonical id the exporter computed is a suggested match: it
   enters as a `draft` match with `suggested-match` as the role of the
   process (SPEC-001 §10), never as an `id` of the referent.
4. A translation, OCR output or transcript found on an imported document is
   split off as a derived expression (SPEC-003 §3.2). It does not replace the
   original text as evidence.

### 3.5 Dates

Partial dates are kept as given (SPEC-001 §8). Where a target requires a full
date, an export MAY round, but it MUST say so in the loss list and, where the
target has a place for it, annotate the rounded value. On import, a full date
whose precision the source does not state is stored as given, with precision
`unknown`. The importer MUST NOT assume it was exact.

## 4. FollowTheMoney (FtM)

Basis: the schema files and the two documentation pages listed in the
provenance block. FtM's primary unit is an entity with typed properties. A
separate statement-based form adds metadata per property value.

### 4.1 Mapping

| Core | FtM term | Strength | What is lost or added |
|---|---|---|---|
| `person` | `Person` (extends `LegalEntity`, extends `Thing`) | exact | None for the kind. FtM has no referent status. |
| `organisation` | `LegalEntity`, or `Organization` / `Company` / `PublicBody` | partial | `LegalEntity` is described as used when "raw data does not specify if something is a person or company". The legal-versus-no-legal-personality split of SPEC-002 §10.2 has no counterpart in the terms read. |
| Referent status (`canonical`, `candidate`, `fabricated`, `disproved`) | none | none | Export: `fabricated` and `disproved` referents MUST NOT be exported as ordinary entities. They are left out and listed. |
| Name assignment, type `alias` | `Thing.alias` | exact | Basis and period are lost in the entity form (kept in the statement form's dataset and times). |
| Name, type `former` | `Thing.previousName` | exact | Period lost. |
| Name, preferred form | `Thing.name` | partial | The core has no "preferred" flag. An export chooses one name for `name` and says which rule it used. |
| Names of type `legal`, `transliteration`, `brand`, `other` | `Thing.name` or `Thing.alias` | partial | The type is lost. |
| FtM `weakAlias` (import) | name of type `other` | partial | FtM marks it as not used for matching; the core has no such flag, so the reduced reliability is lost. |
| Name language (BCP 47) | statement `lang` | partial | The statement table's `lang` is a 3-letter code. Script and region subtags (`uk-Latn`) cannot be carried. |
| Identifier assignment | Typed properties: `registrationNumber`, `idNumber`, `taxNumber`, `licenseNumber`, `vatCode`, `leiCode`, `wikidataId`, and others on `LegalEntity` and `Thing` | partial | The scheme is the property name. The issuing authority is a separate entity-level property (`jurisdiction`), so an entity with several numbers cannot say which authority issued which. Identifier assignments with no matching property have no FtM home. |
| Role event | `Membership` (`member`, `organization`; role and status from `Interest`; dates from `Interval`) | partial | The qualifier (`acting`, `interim`, `de-facto`, `disputed`) can only travel inside the free `role` or `status` text. The event has no `proof` link: `proof` is defined on `Thing`, and `Interval` does not extend `Thing` in the files read. It has `sourceUrl`, `publisher` and `retrievedAt`. |
| Ownership or control relation | `Ownership` (`owner`, `asset`, `percentage` and others) | out of scope | SPEC-002 §10.3 leaves these to a later spec. |
| Event (SPEC-002 §3, profile-added kind) | `Event` (`Interval`, with `involved`, `organizer`) | partial | Only mapped for profiles that add the kind. |
| Partial dates | `date` property type | exact | FtM carries date prefixes (`2021`, `2021-08`) and uses them as precision. Approximate dates and ranges are stated as not yet supported. EDTF is not carried. |
| Original expression | statement `original_value` | exact | Only in the statement form. |
| Assertion, `claim` | One statement (row: `entity_id`, `prop`, `value`, `lang`, `original_value`, `dataset`, `origin`, `first_seen`, `last_seen`, `external`, `canonical_id`) | partial | A statement is one property value by one dataset. It carries no kind, no basis, no stance and no assessment. |
| `asserter` | statement `dataset` (with `origin`) | partial | A dataset is an exporter, not necessarily the agent who made the claim. |
| `asserted_at` | statement `first_seen` | partial | FtM's own text says it records only values seen since July 2021. It is a pipeline observation, not the time the assertion entered a record, and is never `valid_time`. |
| `valid_time` | `Interval.startDate` / `endDate` on edges; `birthDate`, `deathDate`, `incorporationDate`, `dissolutionDate` on entities | partial | Only for the properties that have such dates. A property value has no validity period in the entity form. |
| Review state `draft` | statement `external` | partial | `external` marks "suggested additions to a dataset, pending human-in-the-loop approval". `unreviewed` and `reviewed` have no counterpart. |
| Evidence link (excerpt supports an assertion) | `Thing.proof` (to a `Document`; reverse `proven`) | partial | No stance, no passage, no locator. It says "derived from this document" and nothing else. |
| Excerpt | `Page.bodyText` (page of a `Pages` document), `Document.bodyText` | partial | Page text, not a verbatim passage with a selector. The locator is the page index. |
| Detected name in a document | `Mention` (`document`, `resolved`, `name`) | partial | A process output. On import it is a `draft` (§3.4), never a quotation. |
| Free note on a document or entity | `Note` | none | Free text. No core element. |
| Derived expression | `Document.translatedText`, `translatedLanguage` | partial | FtM keeps the translation as a property of the same record. Exports of derived expressions follow SPEC-003 §3.2; imports split them (§3.4.4). |
| Digest | `Document.contentHash` | exact | A bit-level statement only (SPEC-003 §4.4). |
| Capture | `retrievedAt`, `crawler`, `processingAgent`, `processedAt` | partial | No original capture time, capture series, completeness or failed-capture record. |
| Likelihood, analytic confidence | none | none | Left out and listed (§3.2.4). |
| Absence states | none | none | An empty or missing property cannot say `unknown` rather than `not-researched`. On export, an absence is left out and listed; it is never exported as an empty string. |

### 4.2 Notes

1. FtM's statement form is the closest fit to the core assertion: it keeps
   dataset, origin, language, the original value and times for each value. A
   core-to-FtM export SHOULD use it. The entity form is a flattened export
   (§3.3).
2. FtM `canonical_id` is a deduplication result. It follows §3.4.3.

## 5. Beneficial Ownership Data Standard (BODS) v0.4

Basis: the BODS documentation pages listed in the provenance block. BODS is
the closest of the three to the core in spirit. Its key-concepts page says each
Statement "represents a claim made by a source at a particular point in time",
that statements can conflict and overlap, and that statements are immutable:
an update is a new Statement with the same `recordId`.

### 5.1 Mapping

| Core | BODS term | Strength | What is lost or added |
|---|---|---|---|
| `claim` | A Statement | exact for `claim`; none for the other kinds | Every BODS Statement is a claim. `observation`, `hypothesis`, `finding`, `assessment` and `project-conclusion` have no counterpart. A `finding` exported as a Statement loses its kind and is read as a source's claim. The export MUST say so (§3.2.1). |
| Referent `person` | Person record (`recordType: person`) | partial | Referent status is lost. Only persons that are beneficial owners or related officials belong in the BODS scope. |
| Referent `organisation` | Entity record (`recordType: entity`) | partial | The `entityType` codelist was not read. |
| Assertion `id` | `statementId` (32 to 64 characters, persistent, globally unique) | partial | Core ids are opaque and need not meet the length rule; the export maps them reversibly. |
| Referent `id` | `recordId` | partial | `recordId` groups the Statements about one record over time. It is a publisher-local id. |
| Supersession (`supersedes`) | A new Statement with the same `recordId`, `recordStatus: updated` | exact | The earlier Statement stays published. This is the same append-only rule as SPEC-001 §8. |
| (none) | `recordStatus: closed` | none | "Closed" means the last Statement published for that record. It does not mean the interest ended. An export MUST NOT set `endDate` from it, and an import MUST NOT read it as an end of validity. |
| `asserter` | `source.assertedBy` (`name`, `uri`) | exact | The agents providing the information, including a declarant or an agent on their behalf. |
| Source type | `source.type`: `selfDeclaration`, `officialRegister`, `thirdParty`, `primaryResearch`, `verified` | partial | A coarse classification. The core records the source and its roles (SPEC-003 §3.3). `verified` is a claim about the publisher's own process (§3.4.2). |
| Source location and retrieval | `source.url`, `source.retrievedAt` | partial | No capture series, completeness or original capture time (SPEC-003 §5). |
| `asserted_at` | `publicationDetails.publicationDate` | partial | The publication date of the Statement, not the date the importer or exporter recorded it. |
| Date the source made the declaration | `statementDate` | none | The core's `asserted_at` is recording time (SPEC-001 §4). `statementDate` is the declaration time. It belongs to the source or excerpt it came from, not to `asserted_at`. An import MUST store it on the source side. |
| Recorder (`recorded_by`) | `publicationDetails.publisher`, `annotations[].createdBy` | partial | The publisher of the statement is not necessarily the recorder. |
| Role event / interest | `Interest` in a Relationship record (`type`, `directOrIndirect`, `details`, `startDate`, `endDate`, `share`) | partial | Only for interests in an entity. Roles in an organisation that are not interests have no Statement shape in the terms read. |
| Beneficial ownership or control flag | `Interest.beneficialOwnershipOrControl` | none in the core | A classification under a jurisdiction's definition. It is a profile term. The core gives it no meaning. |
| Name | `Name` (`type`, `fullName`, `familyName`, `givenName`, `patronymicName`) | partial | `Name` is for persons. The `nameType` codelist was not read, so the type mapping is open. |
| Identifier assignment | `Identifier` (`id`, `scheme`, `schemeName`, `uri`) | exact | `scheme` is an org-id.guide code for entities, or `{JURISDICTION}-{TYPE}` for persons. This is the best fit among the three: scheme and value stay together. |
| Partial dates | `startDate`, `endDate` (full `YYYY-MM-DD`) | partial | BODS says an unknown month or day "may be rounded to the first day" with the rounding noted in guidance. An export follows §3.5 and adds an annotation (below). An import cannot tell exact from rounded. |
| Quantities (`share`) | `Interest.share` (exact, or `minimum` / `maximum` and exclusive forms) | partial | Maps `exact` and `range`. The semantic types `approximate`, `at-least`, `at-most`, `greater-than`, `fewer-than` have no named counterpart; some can be expressed with a bound. Original expression is lost. |
| Absence: unspecified interested party | `UnspecifiedRecord` with `reason` | partial | See §5.2. |
| Output notes, corrections, transformations | `Annotation` (`statementPointerTarget` as RFC 6901 pointer, `motivation`, `description`, `transformedContent`, `url`, `createdBy`) | partial | Carries the loss list entries for rounded dates and other transformations (motivation `transformation`). No core equivalent for the other motivations. |
| Evidence link, excerpt, stance | none | none | A Statement points to a source, not to a passage, and has no stance. Left out and listed. |
| Likelihood, analytic confidence | none | none | Left out and listed. |
| Review state | none | none | `verified` in `source.type` is not a review state (§3.4.2). |
| Referent status | none | none | As for FtM. |

### 5.2 Absence

BODS can state why an interested party is not given. The reasons read were
mapped as follows. This is a judgement, because an `UnspecifiedRecord` is a
declaration by a publisher about a network, not an absence state of a field.

| BODS reason | Core |
|---|---|
| `noBeneficialOwners` | Not an absence state. An explicit negative assertion (SPEC-001 §6), attributed to the declarant, scoped to "according to the rules under which the statement is made". |
| `subjectUnableToConfirmOrIdentifyBeneficialOwner`, `interestedPartyHasNotProvidedInformation` | `withheld` or `unknown`, attributed to the declarant. An importer cannot tell which and MUST use `unknown` unless the source says. |
| `subjectExemptFromDisclosure`, `interestedPartyExemptFromDisclosure` | `not-applicable`, with the exemption as the stated reason. |
| `unknown`, `informationUnknownToPublisher` | `unknown` |

The codelist was read only in part. Reasons not listed here MUST NOT be
mapped until read.

### 5.3 Worked example (invented)

The core holds a `claim` held by "Harbourside Registry", dated `2019-06`, that
"Alder Holdings Ltd holds at least 25% of Birch Trading Ltd", with the original
wording kept. The export to BODS:

- one Relationship Statement; `source.assertedBy` names Harbourside Registry;
- `startDate` `2019-06-01`, with an `Annotation` (`transformation`) on
  `/recordDetails/interests/0/startDate` saying the month was given and the day
  was filled;
- `share` expressed with a `minimum` of 25, with the loss list noting that
  "at least" and the original wording are not carried by name;
- the loss list notes that no evidence link, assessment or review state travelled.

## 6. schema.org

Basis: definitions looked up in the vocabulary file (provenance block).
schema.org is a general web vocabulary. It is widely published and consumed,
but it has no assertion model. Its `Claim` class is the nearest term.

### 6.1 Mapping

| Core | schema.org term | Strength | What is lost or added |
|---|---|---|---|
| `claim` | `Claim` (a `CreativeWork`; `text`, `appearance`, `firstAppearance`, `claimInterpreter`) | partial | `Claim` is "a specific, factually-oriented claim that could be the `itemReviewed` in a `ClaimReview`". It names where the claim appears, not who holds it, as a first-class property. |
| `asserter` of a claim | `author` or `creator` of the work where it appears, `claimInterpreter` | partial | Authorship of the work is not holding of the claim. An export MUST NOT set `author` unless the asserter is the author of the work. |
| Other kinds | `Statement` (a `CreativeWork`: "a statement about something, for example a fun or interesting fact"), or none | none | `Statement` invites the reading "this is a fact". An export MUST NOT use it for a `claim` or `hypothesis` (§3.2.1). Not used for other kinds. |
| `assessment` of a claim | `ClaimReview` (a `Review`; `claimReviewed`, `itemReviewed`, `reviewRating`) | partial | A review of a claim. A `Rating` takes `ratingValue` as a number or text, and `reviewAspect` names a facet. The core's two dimensions can each be a `Rating` with a text value (the band identifier) and a distinguishing `reviewAspect`. This is valid in the vocabulary. How consumers treat a non-numeric `ratingValue` was not checked. |
| Evidence link | `citation`, `isBasedOn`, `appearance` | partial | None carries a stance or a passage. |
| Excerpt (a quotation) | `Quotation` (use `isBasedOn` to link to the origin) | partial | `Quotation` is in the pending area of schema.org. It has no selector. The verbatim passage can go in `text`; the locator cannot be expressed. |
| Source: work and expression | `CreativeWork`, `exampleOfWork`, `workExample`, `inLanguage` (BCP 47) | partial | The four layers of SPEC-003 §3 are not separate classes. |
| Source: web page, document, dataset | `WebPage`, `DigitalDocument`, `Dataset`, `ArchiveComponent` | partial | A choice of class, not a layer. |
| Translation | `translator`, `translationOfWork` | partial | `translationOfWork` is in the pending area. |
| Derivation | `isBasedOn` (`isBasedOnUrl` is superseded by it) | partial | One undifferentiated relation. SPEC-001 §5.2's seven dependence relations collapse to it. |
| Holding, digest, location | `sha256`, `contentUrl`, `encodingFormat`, `archivedAt`, `license` | partial | `archivedAt` says a page or link is "involved in archival". It has no original capture time, no series and no completeness. |
| Person | `Person` (`birthDate`, `deathDate`, `taxID`, `vatID`) | exact for the kind | No referent status. |
| Organisation | `Organization` (`legalName`, `foundingDate`, `dissolutionDate`, `leiCode`, `iso6523Code`, `parentOrganization`) | exact for the kind | No referent status. |
| Names | `name`, `alternateName`, `legalName` | partial | Name types and languages per value are lost (`alternateName` is untyped). |
| Identifier assignment | `identifier` (text, URL or `PropertyValue`), `sameAs`, and typed ones such as `leiCode`, `taxID`, `vatID` | partial | `PropertyValue` can pair a value with a scheme name. Use it rather than bare text. `sameAs` is "a reference page that unambiguously indicates the item's identity": an exporter MUST NOT emit it for a candidate match (§3.4.3, SPEC-002 §7). |
| Role event | `Role` (`roleName`, `startDate`, `endDate`) carried on `member`, `memberOf` or `worksFor` | partial | `Role` is the schema.org n-ary pattern. The qualifier and basis are lost. |
| Likelihood, confidence (as ratings) | `Rating` | partial | See `assessment`. |
| Absence states | none found in the terms read | none | Left out and listed. |
| Review state | none | none | Left out and listed. |
| Partial dates | `Date` values | not verified | Whether partial ISO 8601 dates are valid values was not checked. An exporter keeps them and lists the uncertainty. |

### 6.2 Notes

1. The pending-area terms (`Quotation`, `translationOfWork`) MAY be used in
   exports (§10.4). The loss list MUST name them as pending terms.
2. schema.org is primarily an export target. §3.4 applies to anything imported
   from it.

## 7. Where each standard loses what

`Carried` means a counterpart was found in the terms read. `Partly` means the
idea exists but not the core's rule. `No` means none was found in the terms
read. It is not a claim about the standard as a whole.

| Core element | FtM | BODS | schema.org |
|---|---|---|---|
| Assertion kinds | No | Partly (claims only) | Partly (`Claim`) |
| Asserter | Partly (dataset) | Carried | Partly |
| Basis, evidence stance | No | No | No |
| Verbatim excerpt and locator | Partly (page text) | No | Partly (`Quotation`, pending) |
| Likelihood and confidence, kept apart | No | No | Partly (`Rating`) |
| Absence states | No | Partly (unspecified party) | No |
| Partial dates | Carried | No (rounding) | Not verified |
| Original expression | Carried (statement form) | Partly (annotation) | No |
| Review state | Partly (`external`) | No | No |
| Append-only supersession | Partly (times) | Carried | No |
| Referent status | No | No | No |
| Name types and per-value language | Partly | Partly | No |
| Identifier with scheme | Partly | Carried | Partly (`PropertyValue`) |
| Capture series and completeness | No | No | No |

## 8. Conformance

An implementation that exports to, or imports from, one of these standards
conforms to this specification if it can show that:

1. every export names the standard and version and has a loss list (§3.1);
2. no export presents a `claim`, `draft` or `hypothesis` as established, and no
   assessment is converted to a number (§3.2);
3. a flattened export is declared as such and points back to the assertion
   ids (§3.3);
4. every imported record is a `claim` held by the exporter, in `draft`, and no
   import creates a `finding`, a `canonical` referent or a confirmed match
   (§3.4);
5. an exporter's cluster or canonical id is stored as a suggested match, not as
   the referent's `id` (§3.4.3), and `sameAs` is never emitted for a
   candidate (§6.1);
6. a rounded date is listed and annotated where the target allows (§3.5), and
   BODS `closed` is never read as an end date (§5.1);
7. no BODS unspecified-party reason is mapped beyond §5.2 until its text has
   been read.

## 9. Maintaining this specification

A new version of any of the three standards is a new verification, not an
edit. A mapping stays at the version it was checked against. The provenance
block records the date and the version, and a change of strength or loss is
a changelog entry.

## 10. Candidate decisions for the owner

All four are decided (owner, 2026-10-04), each as recommended. Recorded in
CHANGELOG 0.1.0.

1. ~~**Starting state of an import.**~~ Decided: `draft` (§3.4.1).
2. ~~**Direction.**~~ Decided: both directions are mapped; the import rules stay
   minimal.
3. ~~**BODS dates.**~~ Decided: an export rounds a partial date and annotates it
   (§3.5).
4. ~~**Pending schema.org terms.**~~ Decided: `Quotation` and `translationOfWork`
   are allowed in exports and are listed in the loss list as pending terms
   (§6.2).
