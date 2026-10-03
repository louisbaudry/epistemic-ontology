# SPEC-002 — Persons and organisations

**Version:** 0.1 (draft) | **Status:** Draft, awaiting owner review
**Supersedes:** — | **Superseded by:** —
**Builds on:** SPEC-001 (core assertion pattern)
**Upstream:** UkraineIndependenceWar DR-0012, DR-0013, DR-0014, DR-0062, DR-0063, DR-0064; its SPEC-0002 (identity and entity resolution)

### Provenance of this draft

Drafted by an AI assistant (Anthropic Claude Code agent session) at the
owner's direction. A draft until the owner approves it.

- **Read in full:** upstream DR-0012, DR-0013, DR-0014, DR-0062, DR-0063,
  DR-0064; upstream SPEC-0002.
- **Read by outline only:** upstream POL-0001 (personal-data policy). It is a
  legal posture specific to that archive, not reviewed by counsel, and is
  deliberately **not** imported here (see §9).
- **Checked against how adopting projects store people:** only one project's
  person-to-organisation affiliation table (role, start, end), which fits §6.
  No other project's model was compared field by field.
- **Verified against the standards' own files (2026-10-03):** CIDOC CRM 7.1.3
  (`E21 Person`, `E74 Group`, `E39 Actor`, `E85 Joining`, `E86 Leaving`,
  `P143`, `P144`, `E15 Identifier Assignment`, `P37 assigned`, `E42
  Identifier`, `E41 Appellation`) and the W3C Organization ontology
  (`org:Membership`, `org:member`, `org:organization`, `org:role`,
  `org:memberDuring`).
- **Not verified:** FollowTheMoney, schema.org and Wikidata mappings; how
  CIDOC CRM models a name assignment (as opposed to an identifier
  assignment). §10 marks each.

---

## 1. Purpose and scope

Persons and organisations are the referents most statements are about and the
ones most easily confused, merged by mistake, or recorded when they should not
be. This specification defines how they are identified, named, related, matched
and, when needed, merged or split, so that a false identification costs less
than a missed one and nothing about a person is recorded by accident.

**In scope:** the two referent kinds `person` and `organisation`; names and
identifiers; referent status; roles and membership over time; matching,
merging and splitting; what a profile must declare about recording persons.

**Out of scope:** places, events and product types or items (later specs);
ownership and control relations (a later relations spec); matcher algorithms
and scoring; any legal posture. The core takes no position on *which* persons
may be recorded; it requires each profile to take and state one (§9).

SPEC-001's terms apply. Every record in this specification is an assertion in
SPEC-001's sense, with a kind, an asserter, a basis and a review state.

## 2. Terms

| Term | Meaning |
|---|---|
| **Agent** | A referent that acts: a person or an organisation. |
| **Person** | A real, living or historical human individual, or one assumed to be, as the sources refer to them. |
| **Organisation** | A company, agency, association, unit or other group that acts collectively. |
| **Name assignment** | An assertion that a name is used for a referent. |
| **Identifier assignment** | An assertion that an identifier from a scheme (a registry number, a domain, an external dataset key) belongs to a referent. |
| **Role event** | An assertion that an agent held a role in an organisation over a period. |
| **Match** | An assertion that two identity bearers refer to the same referent. |
| **Lineage** | The recorded history of merges and splits that produced a referent. |

## 3. Referent kinds

The core defines two kinds: `person` and `organisation`. A profile MAY use
either or both, and MAY add kinds (place, event, product type) without giving
these identifiers another meaning. A referent is identified by an opaque,
immutable `id` that is never reused. It is never identified by a name.

## 4. Names and identifiers are assignments

No bare name or identifier field carries a referent's identity (upstream
DR-0012). Each is an assertion of its own:

| Element | Content | Required |
|---|---|---|
| `value` | The name or identifier exactly as the source gives it. | MUST |
| `type` | For a name: `legal`, `alias`, `transliteration`, `former`, `brand`, `other`. For an identifier: the scheme (a registry, a domain, an external dataset). | MUST |
| `language` | BCP 47 tag; an original and its transliteration carry different tags (`uk`, `uk-Latn`). | MUST for a name |
| `basis` | The excerpt or source it was seen in (SPEC-001 §5.1). | MUST |
| `period` | When it was in use, partial dates allowed. | MAY |
| `status` | The review state of SPEC-001 §10. | MUST |

Rules:

1. Names are never merged into one field and never normalised in place. A
   normalised form MAY be stored beside the original, as derived data.
2. Renaming never changes a referent's `id`.
3. Two referents MAY carry the same name. Equal names are not identity.
4. An identifier assignment from an external scheme is a claim by that scheme,
   attributed to it. It does not establish identity on its own.
5. An implementation MUST NOT fetch an external dataset to resolve or enrich an
   identifier unless the adopting profile allows it. The core fetches nothing.

## 5. Referent status

Every referent carries one status (upstream DR-0062):

| Status | Meaning |
|---|---|
| `canonical` | Treated as a real, distinct referent. |
| `candidate` | Provisionally distinct, not yet consolidated. A lead enters here. |
| `fabricated` | Concluded never to have referred to a real, distinct referent: an invented persona or identity. |
| `disproved` | Shown to be a duplicate or an error, pointing to what replaced it. |

1. A new referent starts as `candidate`. Promoting it to `canonical` needs the
   evidence a match needs (§7), not a name.
2. `fabricated` and `disproved` referents are kept, never deleted: claims about
   them exist and stay citable.
3. A status change is an assertion with a basis, attributed to someone, like any
   other.

## 6. Roles and membership

Membership, office and role are **temporal events** (upstream DR-0013), never a
field on the person.

| Element | Content | Required |
|---|---|---|
| `agent` | The person or organisation holding the role. | MUST |
| `organisation` | The organisation it is held in. | MUST |
| `role` | The role as the source writes it, in its original language. | MAY |
| `qualifier` | `acting`, `interim`, `de-facto`, `disputed`, or none. | MAY |
| `start`, `end` | Partial dates; either may be unknown. | MAY |
| `basis` | Excerpt or source. | MUST |

1. A role event is an ordinary assertion. Two sources that disagree about who
   held a role both stay, each with its evidence; nothing averages them.
2. A `disputed` or `de-facto` role is an attributed claim by its source; whether
   it is true is a separate assessment (SPEC-001 §5.3).
3. Presence, participation and responsibility are different things. A role
   event says that an agent held a role, never that the agent is responsible
   for anything the organisation did.
4. Attributes of a person never silently encode an organisational capacity:
   "spokesperson for X" is a role event, not a person attribute.

## 7. Matching

A match proposes that two identity bearers (a candidate and a canonical
referent, a listed name and a referent, an account and an actor, an
external-dataset entity and a referent) refer to the same referent (upstream
DR-0063).

1. **States:** `proposed`, `under-review`, `confirmed`, `rejected`, and
   `withdrawn` for a proposer's retraction. A state change is a superseding
   assertion with an asserter and a basis.
2. **Automated matchers and models MAY create `proposed` matches only**, each
   recording the features it matched on. They MUST NOT confirm.
3. **Confirmation is a human decision on discriminating evidence**: at least one
   basis beyond name or transliteration similarity, such as a shared strong
   identifier, a documented relationship, or a registry entry that gives the
   same identifying data. **Name similarity alone never confirms**, for any
   referent and at any level of review.
4. **A rejection is kept**, with its reason, and a matcher MUST consult rejected
   matches before re-proposing one.
5. **A confirmed match takes effect by assertion, not mutation.** The two
   records stay distinct; the link is a further assertion.
6. When in doubt the referents stay separate and the match stays `proposed`. A
   false merge costs more than a missed one.

A profile MAY require stricter confirmation for some uses (for example a second
reviewer for a link that supports a legal conclusion). It MUST state the rule.

## 8. Merging and splitting

Merge and split are events (upstream DR-0064).

1. A **merge** designates a successor referent and marks the predecessors
   `disproved` as distinct, with permanent redirects so every published
   identifier keeps resolving.
2. A **split** designates a successor set, records a disposition for each
   assertion attached to the original, and redirects to a disambiguation record.
3. **Every assertion attached to a predecessor is re-pointed explicitly or
   flagged for review, never moved in bulk**, because some of them may have
   belonged only to the error.
4. **Lineage is permanent and queryable**: what merges and splits produced a
   referent, decided by whom, on what evidence.

## 9. Recording persons: what a profile must declare

Persons are the one referent kind where recording can itself do harm. The core
does not decide who may be recorded: that depends on a project's purpose, its
legal basis and its audience, and a rule written for one would be wrong for
another. It requires each profile that uses `person` to **declare a person
policy** covering:

1. **Who** may be recorded as a person (for example, only people in a public
   role) and who never may.
2. **What** is recorded about them, and what is never structured, whatever the
   source says.
3. **How an allegation is recorded:** as an attributed `claim` (SPEC-001 §3),
   never as a `finding` about the person without evidence the analyst can cite.
4. **How a person or a record made in error is removed**, including what happens
   to history that would otherwise preserve it.
5. **How automated output about a person is held:** as `draft` until a human
   adopts it (SPEC-001 §10).

The core states these minimums, which no profile may relax:

- A person's record contains only what the profile's policy allows, however much
  more a source says.
- A claim about a person that the source attributes to someone else stays
  attributed to that someone.
- No automated process creates a person referent as `canonical`.

The core ships no default policy (decided; see the end of this spec).

## 10. Organisations

1. An organisation's address, such as a registered office, is the organisation's
   attribute, not a person's.
2. A legal entity and a group that acts without legal personality are both
   `organisation`. A profile that needs to tell them apart does so with a
   type of its own, defined in the profile.
3. Ownership, control and funding between organisations are relations, not
   covered here.

## 11. Mappings to standards

Verified means checked on 2026-10-03 against the standard's own published file.

| This spec | Standard | Mapping | Status |
|---|---|---|---|
| `person`, `organisation` | CIDOC CRM 7.1.3 | `E21 Person` and `E74 Group`, both subclasses of `E39 Actor`. CIDOC's own note on `E21` says that where doubt exists whether several persons are identical, several instances may be created and related: this is §7's "stay separate". | Verified |
| Role event, joining | CIDOC CRM 7.1.3 | `E85 Joining` (an `E39 Actor` becoming a member of an `E74 Group`, `P143 joined`, `P144 joined with`) and `E86 Leaving`. CIDOC says it implies no initiative by either party. | Verified |
| Identifier assignment | CIDOC CRM 7.1.3 | `E15 Identifier Assignment`, `P37 assigned` an `E42 Identifier`. | Verified |
| Name | CIDOC CRM 7.1.3 | An `E41 Appellation` exists. How a name assignment is modelled, as opposed to an identifier assignment, was not checked. | Partly verified |
| Role event, membership | W3C Organization ontology | `org:Membership`, an n-ary relation between an agent (`org:member`), an organisation (`org:organization`) and a role (`org:role`), with an optional interval (`org:memberDuring`). The ontology has no qualifier for acting, interim, de facto or disputed; `qualifier` is an extension. | Verified |
| Person, organisation | schema.org, FollowTheMoney, Wikidata | `Person` and `Organization` types and external identifiers, as an export. | Not verified |

## 12. Conformance

An implementation conforms to this specification if, for every person and
organisation it stores:

1. identity is carried by an opaque `id`, and names and identifiers are
   assignments with a basis;
2. status is one of §5, a new referent starts as `candidate`, and `fabricated`
   and `disproved` referents are kept;
3. roles are temporal events, not person attributes;
4. no automated process confirms a match or creates a `canonical` person, and
   name similarity alone never confirms;
5. a rejected match is kept and consulted;
6. merges and splits leave redirects and lineage, with explicit re-pointing;
7. any profile that records persons declares the policy of §9.

## 13. Candidate decisions for the owner

Items 1 to 3 are decided; the last is open.

1. ~~**A shared default person policy.**~~ Decided: no default. The core
   requires each profile that records persons to declare a policy (§9), and
   gives none of its own. Recorded in CHANGELOG 0.1.0.
2. ~~**Review levels.**~~ Decided: one rule in the core (§7), and a profile may
   be stricter if it states the rule. Upstream's three tiers are not adopted.
   Recorded in CHANGELOG 0.1.0.
3. ~~**Name types.**~~ Decided: a starting list in the spec (§4); a SKOS
   vocabulary follows once the specs are approved. Recorded in CHANGELOG 0.1.0.
4. **Minors.** The core is silent. One upstream interim ruling (2026-10-01, not yet in a
   decision record) holds that no named minor is entered as a person until a
   further decision. Alternative: make that a
   core minimum in §9.
