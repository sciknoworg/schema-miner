from rdflib import Graph

from .ontology_parser import Ontology_Parser


class OntologyManager:
    """
    Manages the loading and access of a single ontology from a URL.

    Supports lazy loading and can return the ontology either as an RDFLib Graph or as a serialized string in a specified RDF format.
    """

    def __init__(self, url: str, input_format: str = "turtle"):
        self.url = url
        self.input_format = input_format
        self.ontology: str | Graph = None

    def _read_ontology(self, output_format: str = "turtle", return_as_graph: bool = False) -> None:
        """
        Load the ontology from the URL and store it in the instance cache.

        :param str output_format: Serialization format if returning as string.
        :param bool return_as_graph: If True, store as RDFLib Graph. Else store as string.
        """
        self.ontology = Ontology_Parser.load(
            self.url, self.input_format, output_format, return_as_graph
        )

    def get(self, output_format: str = "turtle", return_as_graph: bool = False) -> str | Graph:
        """
        Retrieve the ontology, loading it if it has not been loaded yet.

        :param str output_format: Serialization format if returning as string.
        :param bool return_as_graph: If True, store as RDFLib Graph. Else store as string.
        :returns str | Graph: Loaded ontology.
        """
        if not self.ontology:
            self._read_ontology(output_format, return_as_graph)
        return self.ontology
