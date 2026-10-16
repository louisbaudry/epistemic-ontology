"""Build context/spec-001.jsonld from core/core.ttl and vocab/*.ttl.

Usage: python3 context/build.py          (writes the file)
       python3 context/build.py --check  (exit 1 if the file is out of date)
"""
import json
import pathlib
import sys

import rdflib
from rdflib.namespace import RDF, RDFS, SKOS

root = pathlib.Path(__file__).resolve().parent.parent
CORE = "https://louisbaudry.github.io/epistemic-ontology/core/"
VOCAB = "https://louisbaudry.github.io/epistemic-ontology/vocab/"

# property -> concept scheme whose notations are its values (SPEC-001 3, 5.1, 5.3, 6, 7, 10; SPEC-005 4.3)
SCHEMES = {
    "kind": "assertion-kinds",
    "review": "review-states",
    "stance": "evidence-stances",
    "likelihood": "likelihood-bands",
    "analytic_confidence": "analytic-confidence-levels",
    "absence_state": "absence-states",
    "semantic_type": "quantity-types",
    "factor": "source-quality-factors",
}
# properties whose value is another node, given by IRI
NODE_VALUED = ["subject", "asserter", "recorded_by", "supersedes", "contributed_by",
               "excerpt", "assertion", "assessment", "dependent", "assumption"]


def build():
    core = rdflib.Graph().parse(root / "core" / "core.ttl")
    vocab = rdflib.Graph()
    for f in sorted((root / "vocab").glob("*.ttl")):
        vocab.parse(f)
    ctx = {"@version": 1.1, "core": CORE, "vocab": VOCAB,
           "xsd": "http://www.w3.org/2001/XMLSchema#", "id": "@id", "type": "@type"}
    for cls in sorted(core.subjects(RDF.type, RDFS.Class)):
        ctx[str(cls)[len(CORE):]] = "core:" + str(cls)[len(CORE):]
    for prop in sorted(core.subjects(RDF.type, RDF.Property)):
        name = str(prop)[len(CORE):]
        entry = {"@id": "core:" + name}
        if name in NODE_VALUED:
            entry["@type"] = "@id"
        if name == "asserted_at":
            entry["@type"] = "xsd:dateTime"
        if name in SCHEMES:
            scheme = rdflib.URIRef(VOCAB + SCHEMES[name])
            scoped = {}
            for concept in sorted(vocab.subjects(SKOS.inScheme, scheme)):
                scoped[str(vocab.value(concept, SKOS.notation))] = "vocab:" + str(concept)[len(VOCAB):]
            entry["@type"] = "@vocab"
            entry["@context"] = scoped
        ctx[name] = entry
    return {"@context": ctx}


if __name__ == "__main__":
    text = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    out = root / "context" / "spec-001.jsonld"
    if "--check" in sys.argv:
        sys.exit(0 if out.exists() and out.read_text() == text else 1)
    out.write_text(text)
