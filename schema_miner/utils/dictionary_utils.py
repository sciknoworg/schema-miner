import pandas as pd

def convert_dict_to_df(dictionary: dict):
    """
    Converts the dictionary containing the schema's evaluation into the DataFrame

    :param dict dictionary: The dictionary containing the schema's evaluation
    :return DataFrame: The DataFrame containing the schema's evaluation
    """
    #Initializing a list to store dataframe rows
    df = []

    #Iterating over each reference and comparsion models
    for ref_model, ref_value in dictionary.items():
        for comp_model, metrics in ref_value.items():
            #Formatting the row containing the models and metrics
            row = {"Reference": ref_model, "Comparison": comp_model}
            row.update(pd.json_normalize(metrics, sep = '_').to_dict(orient='records')[0])
            df.append(row)
    
    #Returning the DataFrame
    return pd.DataFrame(df)

def delete_dictionary_keys(dictionary: dict, keys_to_delete: list):
    """
    Deletes a list of keys from the provided dictionary recursively and returns the updated dictionary.

    :param dict dictionary: The dictionary containing the keys to delete
    :param list keys_to_delete: The list of keys to be deleted from the dictionary
    :return dict: The updated dictionary
    """
    #Extracting the keys from the dictionary
    dict_keys = list(dictionary.keys())

    #Iterating over the dictionary keys
    for key in dict_keys:
        #Deleting the key if present in the keys to delete list
        if key in keys_to_delete:
            dictionary.pop(key)
        #Recursively calling the function for nested dictionary
        elif isinstance(dictionary[key], dict):
            delete_dictionary_keys(dictionary[key], keys_to_delete)
    
    #Returning the updated dictionary
    return dictionary

def get_schema_leaf_keys(d: dict, parent_key: str = "") -> list[tuple[str, str | None]]:
    """
    Recursively collect all leaf keys from a nested dictionary representing a schema. If a key has a "description", include it with the leaf key. Keys are returned as (flattened_key, description).

    :param dict d: Input dictionary (possibly nested).
    :param str parent_key: Accumulated parent keys (for recursion).
    :return list[tuple[str, str|None]]: List of (key_path, description).
    """
    keys = []
    for k, v in d.items():
        new_key = f"{parent_key} {k}".strip()
        
        if isinstance(v, dict):
            # Extract description if present
            description = v.get("description")
            
            # If dict has 'properties', go deeper
            if "properties" in v:
                keys.extend(get_schema_leaf_keys(v["properties"], new_key))
            else:
                # Leaf dict with description
                if description:
                    keys.append((new_key, description))
        else:
            # Primitive leaf (no description)
            keys.append((new_key, None))
    return keys