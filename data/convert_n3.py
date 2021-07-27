#!/usr/bin/env python3

import rdflib
import tempfile

path = "probonto-v2.5.owl"

with open(path) as f:
    contents = f.read()
    contents.replace("^^<en>", "")
    tmp = tempfile.NamedTemporaryFile("w")
    tmp.write(contents)
    g = rdflib.Graph()
    g.load(tmp.name, format="n3")
    g.serialize("probonto.nt", format="nt")
