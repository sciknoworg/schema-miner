from abc import ABC, abstractmethod


class PDF_Parser(ABC):
    """
    PDF_Parser is an Abstract class for parsing data(Including text, images, tables etc.) from a PDF document.
    """

    def __init__(self):
        """
        Initializes the Object
        """

        # The parsed PDF data
        self.parsed_data = None

        # The PDF file name
        self.filename = None

    @abstractmethod
    def parse_pdf(self, source: str) -> None:
        pass

    @abstractmethod
    def export_as_markdown(self, output_dir: str) -> None:
        pass

    @abstractmethod
    def export_as_html(self, output_dir: str) -> None:
        pass

    @abstractmethod
    def export_as_text(self, output_dir) -> None:
        pass
