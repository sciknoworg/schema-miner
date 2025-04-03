import os

from langchain_community.document_loaders import PyPDFLoader

from services.PDF_Parsers.pdf_parser import PDF_Parser

class PyPDF_PDF_Parser(PDF_Parser):
    """
    PyPDF_PDF_Parser is a sub class of PDF_parser which has a task of parsing PDF documents into Text format using the Langchain's PyPDFLoader API.
    """

    def __init__(self):
        """
        Initialize the object with Langchain PyPDFLoader Configuration
        """
        super().__init__()

    def __str__(self):
        """
        Returns a human-readable representation of an object
        """
        return f'Langchain\'s PyPDFLoader PDF Parser'
    
    def parse_pdf(self, source: str) -> None:
        """
        Parse the given source PDF using the Langchain's PyPDFLoader Parser

        :param str: The source path containing the the PDF file
        """
        #Check if source path is valid
        assert os.path.isfile(source), f'{source} is not a valid file!'

        #Loads the Langchain PyPDFLoader Object with the file path
        loader = PyPDFLoader(source)

        #Iterates over each page and append its content to the list
        pages = []
        for page in loader.lazy_load():
            pages.append(page)
        
        #combines the content from each page and return the final text
        self.parsed_data = '\n\n'.join(page.page_content for page in pages)

        #Parse the Input Document
        self.filename, _ = os.path.splitext(source.split('/')[-1])

    def export_as_markdown(self, output_dir: str) -> None:
        """
        Export the parsed PDF as a Markdown Document

        :param str output_dir: The output directory to save the exported markdown file
        """
        raise NotImplementedError('Export as Markdown NOT Support')

    def export_as_html(self, output_dir: str) -> None:
        """
        Export the parsed PDF as a HTML Document

        :param str output_dir: The output directory to save the exported HTML file
        """
        raise NotImplementedError('Export as HTML NOT Support')

    def export_as_text(self, output_dir: str) -> None:
        """
        Export the parsed PDF as a text Document

        :param str output_dir: The output directory to save the exported text file
        """
        # Export Text format
        with open(f'{output_dir}/{self.filename}.txt', 'w', encoding='utf-8') as fp:
            fp.write(self.parsed_data)