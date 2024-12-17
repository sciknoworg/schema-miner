import os
import pandas as pd
from utils.utils import pdf_loader, write_text_file

def pdf_text_extractor(source_filepath: str, filename: str, destination_filepath: str):
    """
    Extracts the text from a PDF file and save it in a text file

    :param str source_filepath: The file path of the source directory
    :param str filename: PDF file name
    :param str destination_filepath: The file path of the destination directory
    """
    print(f'\nExtracting text from the PDF: {filename}')
    #Extracting the text from the PDF file
    complete_file_path = f'{source_filepath}/{filename}'
    pdf_text = pdf_loader(complete_file_path)

    #Saving the text in a text file
    filename = ''.join(filename.split('.')[:-1])
    complete_dest_file_path = f'{destination_filepath}/{filename}.txt'
    filesaved = write_text_file(complete_dest_file_path, pdf_text)
    print(f'Text file saved successfully: {filesaved}')

def all_pdf_text_extraction(source_filepath: str, destination_filepath: str):
    """
    Extracts text from all the PDF's in the source directory

    :param str source_filepath: The file path of the source directory
    :param str destination_filepath: The file path of the destination directory
    """
    print(f'\nExtracting text from all PDF\'s from the directory: {source_filepath}')
    for filename in os.listdir(source_filepath):
        #Checking for the PDF file
        if not filename.endswith('.pdf'): continue

        #Extracting the text
        pdf_text_extractor(source_filepath, filename, destination_filepath)

def read_csv_file(source_filepath: str, filename: str, columns_to_return: list, return_rows: int = None):
    """
    Reads a CSV file and return the content as a DataFrame Object

    :param str source_filepath: The file path of the source directory
    :param str filename: CSV file name
    :param list columns_to_return: The list of column names to return in the final DataFrame
    :param int return_rows: If not None, the total rows to be returned from the DataFrame
    :return DataFrame: The DataFrame
    """
    #Reading the CSV file with the appropiate encoding
    data = pd.read_csv(f'{source_filepath}/{filename}', encoding='ISO-8859-1')

    #Extracting rows where the value of the specified columns are not empty
    mask = data[columns_to_return].apply(lambda col: col != '-', axis = 0).all(axis = 1)
    data = data[mask]
    data = data[columns_to_return]

    #Checking for returning rows
    if return_rows: 
        data = data.sample(return_rows)
    
    #Returning the final dataframe
    return data.reset_index(drop = True)

if __name__ == "__main__":

    print('\nLLMs4SchemaDiscovery Framework -- A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models ')
    print('Formatting Knowledge Base - Converting PDF Documents to Text Files')

    print('\nPlease input the directory location containing the PDF documents')
    source_dir_path = input('Directory Path> ')

    print('\nPlease input the directory Location to store the converted text files')
    destination_dir_path = input('Directory Path> ')

    #Executing PDF to text conversion
    all_pdf_text_extraction(source_dir_path, destination_dir_path)

    print('\nPDF documents successfully convert to text format!')