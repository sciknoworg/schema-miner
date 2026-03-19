# import os
# import copy
# import json
# from pathlib import Path

# from mineru.cli.common import convert_pdf_bytes_to_bytes_by_pypdfium2, read_fn
# from mineru.utils.enum_class import MakeMode
# from mineru.backend.pipeline.pipeline_analyze import doc_analyze as pipeline_doc_analyze
# from mineru.backend.pipeline.pipeline_middle_json_mkcontent import union_make as pipeline_union_make
# from mineru.backend.pipeline.model_json_to_middle_json import result_to_middle_json as pipeline_result_to_middle_json

# from schema_miner.services.PDF_Parsers.pdf_parser import PDF_Parser

# class MinerU_PDF_Parser(PDF_Parser):
#     """
#     MinerU_PDF_Parser is a sub class of PDF_parser which has a task of parsing PDF documents into different formats (Markdown, HTML, Text etc.) using the MinerU API.
#     """

#     def __init__(self):
#         """
#         Initialize the object with MinerU configuration
#         """
#         super().__init__()

#     def __str__(self):
#         """
#         Returns a human-readable representation of an object
#         """
#         return "MinerU PDF Parser"

#     def parse_pdf(self, source: str) -> None:
#         """
#         Parse the given source PDF using the MinerU PDF parser
#         """
#         # Check if source path is valid
#         assert os.path.isfile(source), f"{source} is not a valid file!"

#         # Initialize the Path object
#         input_doc_path = Path(source)

#         # Extract the filename
#         self.filename = str(input_doc_path.stem)

#         # Read the PDF file as bytes
#         pdf_bytes = read_fn(input_doc_path)

#         # Convert PDF bytes to the format required by pypdfium2
#         new_pdf_bytes = convert_pdf_bytes_to_bytes_by_pypdfium2(pdf_bytes)

#         # Document analyze using MinerU's pipeline
#         infer_results, all_image_lists, all_pdf_docs, lang_list, ocr_enabled_list = pipeline_doc_analyze(pdf_bytes_list=[new_pdf_bytes], lang_list=["en"])

#         # Convert the analyze results to middle JSON format
#         model_json = copy.deepcopy(infer_results[0])

#         # Convert the model JSON to middle JSON format
#         middle_json = pipeline_result_to_middle_json(model_json, all_image_lists[0], all_pdf_docs[0], None, lang_list[0], ocr_enabled_list[0], formula_enabled=True)

#         # Extract PDF info
#         pdf_info = middle_json["pdf_info"]

#         # Extract the markdown content from the middle JSON using the union make mode
#         self.parsed_data = pipeline_union_make(pdf_info, MakeMode.MM_MD, '')

#     def export_as_markdown(self, output_dir: str) -> None:
#         """
#         Export the parsed PDF as a Markdown Document
#         """
#         with open(f"{output_dir}/{self.filename}.md", "w", encoding="utf-8") as fp:
#             fp.write(self.parsed_data)

#     def export_as_html(self, output_dir: str) -> None:
#         """
#         Export the parsed PDF as an HTML Document
#         """
#         raise NotImplementedError("Export as HTML NOT Support")

#     def export_as_text(self, output_dir) -> None:
#         """
#         Export the parsed PDF as a Text Document
#         """
#         with open(f"{output_dir}/{self.filename}.txt", "w", encoding="utf-8") as fp:
#             fp.write(self.parsed_data)