from rdflib import Graph

class Ontology_Parser:
    """
    Utility class for loading and serializing ontologies using RDFLib.

    This class provides a flexible interface for parsing ontologies and returning them either as an RDFLib Graph or as a serialized string in the desired format.
    """
    @staticmethod
    def load(url: str, input_format: str = 'turtle', output_format: str = 'turtle', return_as_graph: bool = False) -> str | Graph:
        """
        Load an ontology from a given URI and return either:
        - an RDFLib Graph (if `return_as_graph=True`), or
        - a serialized string in the specified output format.
        
        :param str url: URI to the ontology file.
        :param str input_format: Format of the input data. Default is "turtle".
        :param str output_format: Format for serialization if returning as string. Default is "turtle".
        :param bool return_as_graph: If True, return an RDFLib Graph object instead of a serialized string. Default is False.
        :returns str | Graph: Serialized ontology string or RDFLib Graph.
        """
        g = Graph()
        g.parse(url, format = input_format)
        return g if return_as_graph else g.serialize(format = output_format)