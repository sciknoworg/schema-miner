import evaluate
from transformers import AutoTokenizer
    
def rouge_score(references: list, predictions: list):
    """
    Calculate the ROUGE-N scores between the reference output and the predicted output

    :param list references: The list of reference outputs
    :param list predictions: The list of predicted outputs
    :return dict: The ROUGE score
    """
    rouge = evaluate.load('rouge')
    return rouge.compute(predictions = predictions, references = references)

def bleu_score(references: list, predictions: list):
    """
    Calculate the BLEU scores between the reference output and the predicted output

    :param list references: The list of reference outputs
    :param list predictions: The list of predicted outputs
    :return dict: The BLEU score
    """
    bleu = evaluate.load('bleu')
    return bleu.compute(predictions = predictions, references = references)

def split_into_chunks(text: str, tokenizer: object, max_length: int = 512):
    """
    Split text into chunks of max length tokens, ensuring truncation

    :param str text: The text to be splitted
    :param object tokenizer: The tokenizer for the specified embedding model
    :param int max_length: The maximum length of tokens in a split
    :return list: The list of splitted texts
    """
    tokens = tokenizer.encode(text, add_special_tokens = False)
    chunks = [tokens[i: i + max_length - 4] for i in range(0, len(tokens), max_length - 4)]
    return [tokenizer.decode(chunk, skip_special_tokens = False) for chunk in chunks]

def bert_score(references: list, predictions: list, embedding_model: str, max_length: int = 512):
    """
    Calculate the BERT score between the reference output and the predicted output using the specified embedding model

    :param list references: The list of reference outputs
    :param list predictions: The list of predicted outputs
    :param str embedding_model: The BERT embedding model used for calculating bert score
    :param int max_length: The maximum length of tokens in a split
    :return dict: The BERT score
    """
    #Loading the BERT score and Embedding model from HuggingFace
    bertscore = evaluate.load('bertscore')
    tokenizer = AutoTokenizer.from_pretrained(embedding_model)
    
    #Intializing dictionary for storing intermediate scores
    scores = {'precision': [], 'recall': [], 'f1': []}
    
    #Iterating each reference and prediction pair
    for pred, ref in zip(predictions, references):
        pred_chunks = split_into_chunks(pred, tokenizer, max_length)
        ref_chunks = split_into_chunks(ref, tokenizer, max_length)

        #Calculating bert score for each chunk separately
        for p_chunk, r_chunk in zip(pred_chunks, ref_chunks):
            result = bertscore.compute(predictions = [p_chunk], references = [r_chunk], model_type = embedding_model, lang = 'en')
            scores['precision'].append(result['precision'][0])
            scores['recall'].append(result['recall'][0])
            scores['f1'].append(result['f1'][0])
        
        #Aggregating the scores - average across chunks
        scores = {
            'precision': sum(scores['precision'])/len(scores['precision']),
            'recall': sum(scores['recall'])/len(scores['recall']),
            'f1': sum(scores['f1'])/len(scores['f1'])
        }
        return scores

def evaluation_summary(llm_models: list, schemas: dict, embedding_model: str):
    """
    Calculated the evaluation metrics summary with different measure in a formatted dictionary

    :param list llm_models: The list of Language Models
    :param dict schemas: The dictionary containing the JSON schema's from different Language Models
    :param str embedding_model: The BERT embedding model used for calculating bert score
    :return dict: The evaluation summary
    """
    #Initializing dictionary for evaluation summary
    schema_evaluation = {}

    #Iterating over each model as the reference
    for reference_model in llm_models:
        reference_output = schemas[reference_model]
        schema_evaluation[reference_model] = {}

        #Comparing reference with all other models
        for comp_model in llm_models:
            #Skipping if there is self-comparison
            if reference_model == comp_model: continue
            comparison_output = schemas[comp_model]
            
            #Calculating the ROUGE score
            score = rouge_score([str(reference_output)], [str(comparison_output)])
            
            #Calculating the BLEU Score
            bleu = bleu_score([str(reference_output)], [str(comparison_output)])
            score['bleu'] = bleu

            #Calculating the BERT score
            bertscore = bert_score([str(reference_output)], [str(comparison_output)], embedding_model)
            score['bert'] = bertscore

            #Updating the evaluation summary
            schema_evaluation[reference_model][comp_model] = score
    
    return schema_evaluation