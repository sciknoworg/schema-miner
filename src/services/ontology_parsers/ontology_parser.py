from rdflib import Graph

class Ontology_Parser:

    def __init__(self):
        super().__init__()

        self.ontology_text = None

    def load(self, url: str) -> None:
        g = Graph()
        g.parse(url, format = 'turtle')
        self.ontology_text = g.serialize(format = 'turtle')

    