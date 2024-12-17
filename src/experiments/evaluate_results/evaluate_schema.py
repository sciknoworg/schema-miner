import os

from utils.evaluation import convert_dict_to_df, evaluation_summary
from utils.utils import read_json_file, save_json_file, delete_dictionary_keys

if __name__ == "__main__":
    
    #LLM Models
    llm_models = ['gpt-4-turbo', 'gpt-4o', 'meta-llama-3.1-8b-instruct']

    #Initializing dictionary for JSON Schemas
    schemas = {}
    
    #List of Keys to be removed from the schema for calculating evaluation metrics
    keys_to_remove = ['type', 'requried', 'items', 'enum', 'minItems', 'maxItems', 'default']

    #Bert Embedding model
    bert_embedding_model = 'allenai/scibert_scivocab_uncased'
    
    #Reading JSON Schema's
    schema_path = 'results/stage-3/simulation-schema/Experiment-4'
    for filename in os.listdir(schema_path):
        if os.path.isdir(f'{schema_path}/{filename}'): continue
        model_name, _ = os.path.splitext(filename)
        
        #Reading the JSON file and removing some keys for evaluation metrics
        schema = read_json_file(f'{schema_path}/{filename}')
        schema = delete_dictionary_keys(schema, keys_to_remove)

        #Updating the dictionary with the JSON schema
        schemas[model_name] = schema

    #Calculating evaluation summary
    schema_evaluation = evaluation_summary(llm_models, schemas, bert_embedding_model)
    
    #Converting Dictionary to Pandas DataFrame
    schema_evaluation_df = convert_dict_to_df(schema_evaluation)
    
    #Saving the results in a JSON format
    results_path = f'{schema_path}/evaluation'
    file_saved = save_json_file(results_path, 'quantitative_evaluation.json', schema_evaluation)
    if file_saved: print('Evaluation Metrics Summary Saved Successfully in JSON Format!')

    #Saving the results in a CSV format
    schema_evaluation_df.to_csv(f'{results_path}/quantitative_evaluation.csv', index = False)
    print('Evaluation Metrics Summary Saved Successfully in CSV Format!')