import logging
import os

from schema_miner.services.PDF_Parsers.docling_pdf_parser import Docling_PDF_Parser
from schema_miner.services.PDF_Parsers.pdf_parser import PDF_Parser


def pdf_text_extractor(source_filename: str, destination_filepath: str | None = None, pdf_parser: PDF_Parser = Docling_PDF_Parser(), return_text: bool = False) -> None | str:
    """
    Extract text content from a PDF file and optionally save it to a Markdown file.

    This function parses a given PDF document using the provided or default parser. The extracted content is saved as a Markdown file in the specified destination directory. Optionally, the extracted text can also be returned.

    :param str source_filename: Path to the source PDF file to be processed.
    :param str destination_filepath: Path to the destination directory where the extracted text will be saved.
    :param PDF_Parser pdf_parser: A PDF parser instance. If None, a default parser (Docling_PDF_Parser) is used.
    :param bool, optional return_text: If True, returns the extracted text in addition to saving it. Defaults to False.
    :returns None | str: Extracted text content if ``return_text`` is True, otherwise None.
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)

    # Extract the filename from the source filepath
    filename = os.path.basename(source_filename)

    # Validate file type
    if not filename.endswith(".pdf"):
        raise ValueError(f"Invalid file type: {filename}. Expected a PDF file.")

    logger.info(f"\nExtracting text from the PDF: {filename}")

    # Parse the PDF Document
    pdf_parser.parse_pdf(source_filename)
    logger.info("PDF parsed successfully")

    # Optionally, Export/Save the PDF Document as a Markdown File
    if destination_filepath:
        pdf_parser.export_as_markdown(destination_filepath)

    # Optionally Return the content of the file
    if return_text:
        return pdf_parser.parsed_data.document.export_to_markdown()

    # Return None if return_text is False
    return None


def all_pdf_text_extraction(source_filepath: str, destination_filepath: str, pdf_parser: PDF_Parser = Docling_PDF_Parser()) -> None:
    """
    Extract text content from all PDF files in a source directory and save them as Markdown files.

    Each PDF file in the source directory is parsed using the provided parser (or the default ``Docling_PDF_Parser`` if none is supplied). The extracted content is saved as individual Markdown files in the specified destination directory.

    :param str source_filepath: Path to the directory containing PDF files.
    :param str destination_filepath: Path to the directory where extracted Markdown files will be saved.
    :param PDF_Parser pdf_parser: A PDF parser instance. If None, a default parser (Docling_PDF_Parser) is used.
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)

    logger.info(f"\nExtracting text from all PDF's from the directory: {source_filepath}")

    # Iterate over each file and save as a markdown file
    for filename in os.listdir(source_filepath):
        # Check for the PDF file
        if not filename.endswith(".pdf"):
            continue

        # Concatenate the source filepath and filename to get the complete path of the PDF file
        pdf_file_path = os.path.join(source_filepath, filename)

        # Extract the text and save as markdown file
        pdf_text_extractor(pdf_file_path, destination_filepath, pdf_parser, return_text=False)
