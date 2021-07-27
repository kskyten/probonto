#!/usr/bin/env python3

from owlready2 import *

onto = get_ontology("file://probonto.nt")
onto.load()


# def get_classes():
#     return list(onto.classes())


# def get_props():
#     return list(onto.data_properties())


# def get_obj_props():
#     return list(onto.object_properties())


def render_using_label(entity):
    return entity.label.first() or entity.name


set_render_func(render_using_label)

# onto.data_properties
# has_R_expr = http://www.probonto.org/ontology#PROB_c0000083


def get_prop(entity, prop_name):
    prop = {render_using_label(prop): prop for prop in entity.get_properties()}.get(
        prop_name
    )
    if prop:
        return getattr(entity, prop.name)[0]


# def has_property(entity, prop):
#     return prop in entity.get_properties()


def process_distribution(distn):
    codename = get_prop(distn, "has code name")
    name = get_prop(distn, "has name")
    mean = get_prop(distn, "distribution has mean")
    mode = get_prop(distn, "distribution has mode")
    median = get_prop(distn, "distribution has median")
    variance = get_prop(distn, "distribution has variance")
    pmf = get_prop(distn, "distribution has PMF")
    hf = get_prop(distn, "distribution has HF")
    sf = get_prop(distn, "distribution has SF")
    pdf = get_prop(distn, "distribution has PDF")
    cdf = get_prop(distn, "distribution has CDF")
    if pmf is not None:
        pmf_code = get_prop(pmf, "has R code expression")
        pmf_latex = get_prop(pmf, "has Latex expression")
    if cdf is not None:
        cdf_code = get_prop(cdf, "has R code expression")
        cdf_latex = get_prop(cdf, "has Latex expression")

    return Distribution(
        codename=codename,
        name=name,
        mean=mean,
        mode=mode,
        median=median,
        variance=variance,
        pmf=pmf,
        hf=hf,
        sf=sf,
        pdf=pdf,
        cdf=cdf,
    )


def get_distributions(onto):
    dist = onto.search(label="probability distribution")[0]
    return dist.instances()


class Distribution:
    def __init__(self, **kwrgs):
        pass


class DiscreteDistribution:
    def __init__(self, codename, density, support, variate):
        pass


class ContinuousDistribution:
    def __init__(self, codename, density, support, variate):
        pass
