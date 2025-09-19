import importlib.resources as pkg_resources
import json

from schema_miner import schemas


class SchemaManager:
    """
    A utility class for loading and managing JSON schemas packaged within the `schema_miner.schemas` module.
    """

    @staticmethod
    def get_schema(schema_filename: str) -> dict:
        """
        Load a JSON schema from the internal `schemas` package.

        :param str schema_filename: The filename of the schema located inside the `schema_miner/schemas/` directory.
        :returns dict: A Python dictionary representing the loaded JSON schema.
        """
        # Open the schema file located in the schema_miner.schemas package
        with pkg_resources.open_text(schemas, schema_filename) as f:
            # Parse and return the JSON content as a dictionary
            return json.load(f)
