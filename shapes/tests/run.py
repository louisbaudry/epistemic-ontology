"""Validate every file in this directory against ../spec-001.ttl.

A file named valid-*.ttl must conform; a file named invalid-*.ttl must not.
Usage: python3 shapes/tests/run.py   (needs pyshacl and rdflib)
"""
import pathlib
import sys

import rdflib
from pyshacl import validate

here = pathlib.Path(__file__).parent
shapes = rdflib.Graph().parse(here.parent / "spec-001.ttl")
failed = 0
for path in sorted(here.glob("*.ttl")):
    conforms, _, text = validate(rdflib.Graph().parse(path), shacl_graph=shapes, inference="none")
    expected = path.name.startswith("valid-")
    ok = conforms == expected
    failed += not ok
    print(("ok   " if ok else "FAIL ") + path.name + ("" if conforms else "  [" + "; ".join(
        sorted({l.split("Message:")[1].strip()[:60] for l in text.splitlines() if "Message:" in l})) + "]"))
sys.exit(1 if failed else 0)
