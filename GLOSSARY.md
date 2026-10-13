# Glossary

The words this repository uses with a fixed meaning. Read it before naming
anything; change it only by a recorded decision (see `CLAUDE.md` and
[CHANGELOG.md](CHANGELOG.md)). The specs in `specs/` are the authority; each
row cites the spec section it comes from. A row marked `unconfirmed` is a
reading by the drafter that the owner has not yet confirmed.

| Term | Definition | Avoid | Source |
|---|---|---|---|
| absence state | One of nine values (`unknown`, `not-researched`, `no-evidence-found`, `unavailable`, `withheld`, `redacted`, `lost-or-destroyed`, `not-applicable`, `indeterminate`) that records why a value is missing. | A blank or null read as "no". | SPEC-001 §6 |
| agent | A referent that acts: a person or an organisation. | | SPEC-002 §2 |
| analytic confidence | How good the basis for a judgment is, taken as `low`, `moderate`, `high` or the state `not-assessed`. | "Confidence" alone; a single score. | SPEC-001 §5.3 |
| anchor | The pinned preserved representation an excerpt targets. | A live locator used as the target. | SPEC-003 §6 |
| `asserted_at` | When an assertion entered the record. | Using it for when the proposition holds. | SPEC-001 §4 |
| assertion | A recorded statement about a referent, with a kind, a holder, a basis and its uncertainty. | `Statement` outside a crosswalk. | SPEC-001 §2 |
| asserter | The agent who holds an assertion; for a `claim`, the source or actor making it, not the recorder. | "Recorder" (that is `recorded_by`). | SPEC-001 §4 |
| assessment | A judgment by a named assessor on a stated basis, used in two related senses: the assertion kind `assessment`, and the likelihood and analytic confidence attached to another assertion. | Treating it as a score; mixing the two senses in one sentence. | SPEC-001 §2, §3, §5.3 |
| candidate | The referent status of a provisionally distinct, not yet consolidated referent; a lead enters here. | | SPEC-002 §5 |
| canonical | The referent status of a referent treated as real and distinct. | | SPEC-002 §5 |
| capture | An event in which a custodian or another party acquired a state of an original resource and produced a holding. | | SPEC-003 §5 |
| capture series | The holdings produced by successive captures of one locator, ordered by original capture time, each its own holding. | A version history inside one holding. | SPEC-003 §5.2 |
| `claim` | An assertion kind: a proposition held by a source or actor and recorded with attribution; recording it does not establish it. | Treating "the company says X" as "X". | SPEC-001 §3 |
| common core | The terms, patterns and rules in `specs/` that every adopting project shares. | | README |
| completeness | A holding's stated degree of fullness: `original`, `archival-copy`, `derivative`, `screenshot`, `transcript`, `fragment` or `metadata-only`. | Leaving it implied. | SPEC-003 §4 |
| crosswalk | A documented mapping between a core element and a term of an external standard, with the information the mapping loses; not a schema. | | SPEC-004 §2 |
| custodian | The agent that holds a copy; not necessarily the project. | "Chain of custody" as a status. | SPEC-003 §2, §5.3 |
| `disproved` | The referent status of a referent shown to be a duplicate or an error, pointing to what replaced it. | Deleting it. | SPEC-002 §5 |
| evidence link | A relation from one excerpt to one assertion, carrying a stance. | Putting the stance on the excerpt. | SPEC-001 §5.1 |
| excerpt | A passage of a source, kept verbatim with a locator, annotated on an anchor. | A paraphrase or summary called a quote. | SPEC-001 §2, SPEC-003 §7 |
| expression | A particular realisation of a work: a language, a version, a text. | | SPEC-003 §3 |
| export | Producing data in an external standard's shape from core records. | | SPEC-004 §2 |
| `fabricated` | The referent status of a referent concluded never to have referred to a real, distinct referent. | | SPEC-002 §5 |
| fact | A display label, computed when shown, for a `finding` with at least one active supporting evidence link; never a stored kind. | A kind `fact`; a stored field, identifier or export value `fact`. | SPEC-001 §2 |
| `finding` | An assertion kind: a conclusion of a defined investigation, with its scope and method, needing an active supporting evidence link. | "Fact" as a kind. | SPEC-001 §3 |
| flattened export | An export that drops attribution, evidence or assessment because the target cannot carry them. | | SPEC-004 §3.3 |
| `fragment` | A completeness value for a holding that is deliberately only a part of the item, such as an excerpted section. | Using it for a capture cut short (that is `truncated`). | SPEC-003 §4 |
| holding | The statement that a custodian possesses one item, in one or more preserved representations, at a stated completeness. | Assuming possession from a citation. | SPEC-003 §4 |
| identifier assignment | An assertion that an identifier from a scheme belongs to a referent. | Identifying a referent by an identifier alone. | SPEC-002 §2, §4 |
| import | Reading data in an external standard's shape into core records; it enters as `draft` claims held by the exporter. | | SPEC-004 §2, §3.4 |
| independent origin | A unit of corroboration counted by its ultimate origin, not by document; independence is a researched conclusion, never a default. | Counting documents. | SPEC-001 §5.2 |
| item | One individual copy of a manifestation. | | SPEC-003 §3 |
| likelihood | How probable a proposition is, stored as one of seven ICD 203 band identifiers, never as a number. | A numeric probability. | SPEC-001 §5.3 |
| lineage | The recorded history of merges and splits that produced a referent; permanent and queryable. | | SPEC-002 §2, §8 |
| locator | The address of an original resource at capture time, such as a URL; context, never an anchor. | | SPEC-003 §2 |
| loss list | The list of core elements an export left out or reduced. | | SPEC-004 §3.1 |
| manifestation | A published or embodied form of an expression. | | SPEC-003 §3 |
| match | An assertion that two identity bearers refer to the same referent, in one of the states `proposed`, `under-review`, `confirmed`, `rejected` or `withdrawn`. | A merge; confirming on name similarity alone. | SPEC-002 §7 |
| merge | An event that designates a successor referent and marks its predecessors `disproved` as distinct, with permanent redirects. | Moving assertions in bulk. | SPEC-002 §8 |
| name assignment | An assertion that a name is used for a referent. | Identifying a referent by its name. | SPEC-002 §2, §4 |
| organisation | A company, agency, association, unit or other group that acts collectively, with or without legal personality. | | SPEC-002 §2, §10 |
| paraphrase | A restatement in the recorder's words, labelled as such. | "Quote". | SPEC-003 §7 |
| person | A real, living or historical human individual, or one assumed to be, as the sources refer to them. | | SPEC-002 §2 |
| person policy | The declaration each profile using `person` makes of who may be recorded, what, how allegations are recorded, how errors are removed and how automated output is held. | A default policy in the core. | SPEC-002 §9 |
| profile | A short document in an adopting project declaring the subset of the core it uses, any stricter rules and any terms it adds; it never gives a core identifier another meaning. | | README, SPEC-001 §3 |
| quotation | The exact passage of a source, verbatim, in its original language. | Normalised text called verbatim. | SPEC-003 §7 |
| referent | Anything a statement can be about: a person, organisation, place, event, product type, document. | Identifying one by a name. | SPEC-001 §2 |
| referent status | One of `canonical`, `candidate`, `fabricated` or `disproved`, carried by every referent. | | SPEC-002 §5 |
| representation | One preserved form of a holding: the original bytes as acquired, or a derivative of them. | Altering an existing one. | SPEC-003 §2, §4 |
| review state | One of `draft`, `unreviewed` or `reviewed` on every assertion; anything a process proposed starts as `draft`. | | SPEC-001 §10 |
| role event | An assertion that an agent held a role in an organisation over a period. | | SPEC-002 §2, §6 |
| source | A document, page, record, recording or other artefact that says something; an intellectual thing, not a file. | "File". | SPEC-001 §2, SPEC-003 §2 |
| split | An event that designates a successor set of referents, records a disposition for each assertion, and redirects to a disambiguation record. | | SPEC-002 §8 |
| stance | The relation an evidence link has to an assertion: `supports`, `contradicts` or `contextualizes`. | | SPEC-001 §5.1 |
| strength | The rating of a crosswalk row: `exact`, `partial` or `none`. | | SPEC-004 §2 |
| summary | A condensed account of a larger passage, labelled as such. | "Quote". | SPEC-003 §7 |
| `supersedes` | The element naming the earlier assertion a correction replaces; the earlier one stays readable. | Editing or overwriting. | SPEC-001 §4, §8 |
| `truncated` | A flag on a holding whose capture was cut short, recorded with the captured length; whatever its completeness value, it is not presented as the document. | Marking a cut-short capture `fragment`. | SPEC-003 §4, §5.1 |
| upstream | The UkraineIndependenceWar archive's numbered decision records, cited by DR number and followed; nothing flows back. | | README |
| `valid_time` | When a proposition holds in the world, partial dates allowed. | Using it for when the record was made. | SPEC-001 §4 |
| work | The intellectual creation, the first of the four documentary layers. | | SPEC-003 §3 |
