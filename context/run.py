"""Check the JSON-LD context.

1. context/spec-001.jsonld is up to date with core/core.ttl and vocab/*.ttl.
2. Each context/examples/<name>.jsonld expands to the same RDF graph as
   shapes/tests/<name>.ttl.
3. Each example conforms to shapes/spec-001.ttl.

Usage: python3 context/run.py   (needs rdflib and pyshacl)
"""
import pathlib
import subprocess
import sys

import rdflib
from pyshacl import validate
from rdflib.compare import isomorphic

root = pathlib.Path(__file__).resolve().parent.parent
shapes = rdflib.Graph().parse(root / "shapes" / "spec-001.ttl")
failed = 0


def report(ok, text):
    global failed
    failed += not ok
    print(("ok   " if ok else "FAIL ") + text)


report(subprocess.run([sys.executable, str(root / "context" / "build.py"), "--check"]).returncode == 0,
       "spec-001.jsonld is up to date")
for path in sorted((root / "context" / "examples").glob("*.jsonld")):
    data = rdflib.Graph().parse(path, format="json-ld")
    turtle = rdflib.Graph().parse(root / "shapes" / "tests" / (path.stem + ".ttl"))
    report(isomorphic(data, turtle), path.name + " equals shapes/tests/" + path.stem + ".ttl")
    conforms = validate(data, shacl_graph=shapes, inference="none")[0]
    report(conforms, path.name + " conforms to the shapes")
sys.exit(1 if failed else 0)
