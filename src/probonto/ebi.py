from ebi.ols.api.client import OlsClient

client = OlsClient()
ontology = client.ontology("probonto")


class Distribution:
    def human_names(self):
        pass

    def preferred_human_name(self):
        pass

    def codename(self):
        pass

    def pdf(self):
        pass

    def cdf(self):
        pass

    def mean(self):
        pass

    def mode(self):
        pass

    def median(self):
        pass

    def variance(self):
        pass

    def variate(self):
        pass

    def support(self):
        pass

    def parameters(self):
        pass


class CDF:
    pass


class PDF:
    pass


class Reparametrization:
    pass
