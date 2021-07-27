#!/usr/bin/env python3

import rdflib
from rdflib.namespace import RDF, OWL, XSD, RDFS
from rdflib import URIRef

path =  "../data/probonto.owl"

# CODENAME = "http://www.probonto.org/ontology#PROB_c0000029"
# DISTRIBUTION = "http://www.probonto.org/ontology#PROB_c0000020"

# dstn = URIRef(DISTRIBUTION)
# name = URIRef(CODENAME)

# g = rdflib.Graph()
# g.load(path, format="n3")

# def print_names():
#     for d in g.subjects(None, dstn):
#         for n in g.objects(d, name):
#             print(n)

def get_distributions(graph=None):
    if graph is None:
        graph = rdflib.Graph()
        graph.load(path, format="n3")

    DISTRIBUTION = "http://www.probonto.org/ontology#PROB_c0000020"
    for distribution in graph.subjects(None, URIRef(DISTRIBUTION)):
        yield Distribution(graph, distribution)

def predicate_by_name(graph, name):
    pass


class Distribution:
    def __init__(self, graph, uri):
        self.graph = graph
        self.uri = uri

    @property
    def label(self):
        return self.graph.label(self.uri)

    @property
    def name(self):
        pass

    @property
    def codename(self):
        CODENAME = URIRef("http://www.probonto.org/ontology#PROB_c0000029")
        return self.value(CODENAME)

    @property
    def pdf(self):
        pass

    def julia_struct(self):
        return f"""
        struct {self.codename}{{PT}}
            parameters :: PT
        end
        """

    def value(self, predicate, object=None, **kwargs):
        return self.graph.value(subject=self.uri, predicate=predicate, object=object, **kwargs)


    def predicates(self, obj=None):
        for pred in self.graph.predicates(self.uri, obj):
            yield pred

    def objects(self, predicate=None):
        for obj in self.graph.objets(self.uri, predicate):
            yield obj

    def __repr__(self):
        return f"Distribution({self.label})"
