import os
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling_core.types.doc import ImageRefMode
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
    TableFormerMode
)
from docling.document_converter import DocumentConverter, PdfFormatOption

from services.PDF_Parsers.pdf_parser import PDF_Parser

class Docling_PDF_Parser(PDF_Parser):
    """
    Docling_PDF_Parser is a sub class of PDF_parser which has a task of parsing PDF documents into different formats (Markdown, HTML, Text etc.) using the Docling API.
    """

    def __init__(self):
        """
        Initialize the object with Docling configuration (OCR Engine, Export type etc.)
        """
        super().__init__()

    def __str__(self):
        """
        Returns a human-readable representation of an object
        """
        return f'Docling PDF Parser'

    def parse_pdf(self, source: str) -> None:
        """
        Parse the given source PDF using the Docling PDF parser

        :param str: The source path containing the the PDF file
        """
        #Check if source path is valid
        assert os.path.isfile(source), f'{source} is not a valid file!'

        #Initialize the Path object
        input_doc_path = Path(source)

        #Configure the Docling PDF Pipeline
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = True
        pipeline_options.do_table_structure = True
        pipeline_options.table_structure_options.do_cell_matching = True
        pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
        pipeline_options.generate_picture_images = True
        pipeline_options.accelerator_options = AcceleratorOptions(num_threads=4, device=AcceleratorDevice.AUTO)

        #Intialize the Docling's Document Converter Object with the Configuration
        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )

        #Parse the Input Document
        self.parsed_data = converter.convert(input_doc_path)
        self.filename = self.parsed_data.input.file.stem

    def export_as_markdown(self, output_dir: str) -> None:
        """
        Export the parsed PDF as a Markdown Document

        :param str output_dir: The output directory to save the exported markdown file
        """
        # Export Markdown format
        with open(f'{output_dir}/{self.filename}.md', 'w', encoding='utf-8') as fp:
            fp.write(self.parsed_data.document.export_to_markdown(image_mode = ImageRefMode.EMBEDDED))

    def export_as_html(self, output_dir: str) -> None:
        """
        Export the parsed PDF as a HTML Document

        :param str output_dir: The output directory to save the exported HTML file
        """
        # Export HTML format
        with open(f'{output_dir}/{self.filename}.html', 'w', encoding='utf-8') as fp:
            fp.write(self.parsed_data.document.export_to_html(image_mode = ImageRefMode.EMBEDDED))

    def export_as_text(self, output_dir: str) -> None:
        """
        Export the parsed PDF as a text Document

        :param str output_dir: The output directory to save the exported text file
        """
        # Export Text format
        with open(f'{output_dir}/{self.filename}.txt', 'w', encoding='utf-8') as fp:
            fp.write(self.parsed_data.document.export_to_text())