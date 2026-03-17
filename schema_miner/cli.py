"""
SCHEMA-MINER CLI: A Command-Line Interface for Schema Extraction from Scientific Literature. This CLI allows users to execute different stages of the SCHEMA-MINER pipeline, including initial schema extraction, schema refinement with expert feedback, and ontology grounding. Users can specify the stage to run, provide expert feedback, and choose the ontology grounding method. The CLI also includes a version option to display the current version of the tool.
"""

# Python Standard Library Imports
import logging
from pathlib import Path
import importlib.metadata
from typing import Optional

# Third-Party Library Imports
import typer

# Schema-Miner Module Imports
from schema_miner.config.cliConfig import CLIConfig
from schema_miner.schema_extractor.extract_schema import extract_schema_stage1, extract_schema_stage2, extract_schema_stage3
from schema_miner.ontology_grounding.prompt_qudt_grounding import prompt_based_qudt_grounding
from schema_miner.ontology_grounding.agentic_qudt_grounding import agentic_qudt_grounding

# Initialize the Typer app
app = typer.Typer()

# Initialize the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def version_callback(value: bool) -> None:
    """
    Callback function to display the version of the Schema Miner CLI when the --version option is used.
    Args:
        value (bool): The value of the --version option. If True, the version will be displayed.
    """
    if value:
        # Retrieve the version of the schema-miner package using importlib.metadata
        version = importlib.metadata.version("schema-miner")

        # Display the version to the user and exit the program
        typer.echo(f"Schema Miner CLI Version: {version}")
        raise typer.Exit()

def _get_total_papers(stage: int) -> int:
    """
    Get the total number of papers available in the dataset for the specified stage.
    Args:
        stage (int): The stage of schema extraction to execute (1, 2, or 3).
    Returns:
        int: The total number of papers available in the dataset for the specified stage.
    """
    # For stage 2 and stage 3, determine the papers path based on the stage and validate that it is set in the environment variables
    papers_path = CLIConfig.STAGE2_PAPERS_PATH if stage == 2 else CLIConfig.STAGE3_PAPERS_PATH
    if not papers_path:
        typer.secho(f"Missing papers path for stage {stage}. Please set the appropriate environment variable for the papers path.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Validate that the papers path is a valid directory
    papers_dir = Path(papers_path)
    if not papers_dir.is_dir():
        typer.secho(f"Papers path for stage {stage} is not a valid directory: {papers_path}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Validate that path contains any papers in text or markdown format
    paper_files = list(papers_dir.glob("*.txt")) + list(papers_dir.glob("*.md"))
    if not paper_files:
        typer.secho(f"No paper files found in the specified papers path for stage {stage}: {papers_path}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Return the total number of papers available in the dataset for the specified stage
    return len(paper_files)

def _validate_input_arguments(stage: int, schema: Optional[str], expert_feedback: Optional[str], papers: Optional[int]) -> None:
    """
    Validate the input arguments for the specified stage of schema-miner.
    Args:
        stage (int): The stage of schema miner to execute (1, 2, or 3).
        schema (Optional[str]): Path to the initial schema for stage 2 and refined schema for stage 3
        expert_feedback (Optional[str]): Expert feedback as text or path to a text file.
        papers (Optional[int]): The number of scientific papers to use in batches for stage 2 and stage 3.
    """

    # Check 1: Validate the stage argument - It should be either 1, 2, or 3
    if stage not in [1, 2, 3]:
        typer.secho("Invalid stage specified. Please choose 1, 2, or 3.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Check 2: For stage 1, check if specification document exists at the specified path and is a valid text file
    if stage == 1:
        if not Path(CLIConfig.STAGE1_SPECIFICATION_PATH).is_file():
            typer.secho(f"Specification document not found at path: {CLIConfig.STAGE1_SPECIFICATION_PATH}", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)
        if not CLIConfig.STAGE1_SPECIFICATION_PATH.endswith(('.txt', '.md')):
            typer.secho("Specification document should be a text file with .txt or .md extension.", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)

    # Check 3: For stage 2 and stage 3, validate the schema_path
    if stage in [2, 3]:
        if not schema:
            typer.secho(f"Schema is required for stage {stage}. Please provide the path to the schema using --schema.", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)
        if not Path(schema).is_file():
            typer.secho(f"Schema file not found at path: {schema}", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)
        if not schema.endswith('.json'):
            typer.secho("Schema file should be a JSON file with .json extension.", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)

    # Check 4: For stage 2 and stage 3, validate the expert_feedback which is optional but if provided should be either a text string or a valid text file path
    if stage in [2, 3] and expert_feedback:
        if Path(expert_feedback).is_file():
            if not expert_feedback.endswith(('.txt', '.md')):
                typer.secho("Expert feedback file should be a text file with .txt or .md extension.", fg=typer.colors.RED, bold=True)
                raise typer.Exit(code=1)
        else:
            # If it's not a file, it should be a non-empty string
            if not isinstance(expert_feedback, str) or not expert_feedback.strip():
                typer.secho("Expert feedback should be a non-empty string or a valid text file path.", fg=typer.colors.RED, bold=True)
                raise typer.Exit(code=1)

    # Check 5: For stage 2 and stage 3, validate the number of papers provided to process in batch should be less than or equal to the total number of papers available in the dataset
    if stage in [2, 3] and papers is not None:
        if papers <= 0:
            typer.secho("Number of papers should be a positive integer.", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)
        total_papers = _get_total_papers(stage)
        if papers > total_papers:
            typer.secho(f"Number of papers to process in batch ({papers}) exceeds the total number of papers available in the dataset for stage {stage} ({total_papers}).", fg=typer.colors.RED, bold=True)
            raise typer.Exit(code=1)

def _run_stage_expert_feedback(stage: int, schema: str, expert_feedback: Optional[str], papers: Optional[int]) -> None:
    """
    Run the stage (2 or 3) of schema-miner in batches with the provided expert feedback.
    Args:
        stage (int): The stage of schema extraction to execute (2 or 3).
        schema (str): Path to the initial schema for stage 2 and refined schema for stage 3.
        expert_feedback (Optional[str]): Expert feedback as text or path to a text file.
        papers (Optional[int]): The number of scientific papers to use in batches for stage 2 and stage 3.
    """
    # Collect the papers path based on the stage
    papers_path = CLIConfig.STAGE2_PAPERS_PATH if stage == 2 else CLIConfig.STAGE3_PAPERS_PATH
    papers_dir = Path(papers_path)
    paper_files = list(papers_dir.glob("*.txt")) + list(papers_dir.glob("*.md"))

    # If papers argument is not provided, set it to the total number of papers available in the dataset for the specified stage
    batch_size = papers if papers is not None else len(paper_files)
    batches = [paper_files[i:i + batch_size] for i in range(0, len(paper_files), batch_size)]

    # Initialize the Path object for the schema
    schema = Path(schema)

    # Extract function for schema-miner stage 2 and stage 3
    extract_schema_fn = extract_schema_stage2 if stage == 2 else extract_schema_stage3
    stage_label = "Preliminary Schema Refinement" if stage == 2 else "Finalize Schema Refinement"

    # Process each batch of papers with the provided expert feedback
    typer.echo(f"Running SCHEMA-MINER -- Stage {stage}: {stage_label}")
    typer.echo(f"Total papers: {len(paper_files)} | Batch size: {batch_size} | Total batches: {len(batches)}\n")

    for batch_num, batch in enumerate(batches):
        typer.echo(f"Batch {batch_num + 1}/{len(batches)}:")
        for paper_idx, paper_file in enumerate(batch):
            global_idx = batch_num * batch_size + paper_idx + 1
            typer.echo(f"Processing paper {global_idx}/{len(paper_files)}: {paper_file}")
            schema = extract_schema_fn(schema, expert_feedback or "", paper_file, save_schema=True)
            if not schema:
                typer.secho(f"Schema extraction failed for paper: {paper_file}", fg=typer.colors.RED, bold=True)
                raise typer.Exit(code=1)
        typer.secho(f"Completed batch {batch_num + 1}/{len(batches)}\n", fg=typer.colors.GREEN, bold=True)

        # After every batch except the last one, pause and prompt the user for feedback
        if batch_num < len(batches) - 1:
            typer.echo("─" * 50)
            feedback_input = typer.prompt("Enter expert feedback for the next batch (or press Enter to continue without feedback)", default="", show_default=False)
            if feedback_input.strip():
                expert_feedback = feedback_input.strip()
            typer.echo("")

    typer.secho(f"Stage {stage} completed. Refined schemas saved to {CLIConfig.RESULTS_PATH}", fg=typer.colors.GREEN, bold=True)

def _run_stage(stage: int, schema: Optional[str], expert_feedback: Optional[str], papers: Optional[int]) -> None:
    """
    Run the specified stage of SCHEMA-MINER with the optional expert feedback.
    Args:
        stage (int): The stage of schema extraction to execute (1, 2, or 3).
        schema (Optional[str]): Path to the initial schema for stage 2 and refined schema for stage 3
        expert_feedback (Optional[str]): Expert feedback as text or path to a text file.
        papers (Optional[int]): The number of scientific papers to use in batches for stage 2 and stage 3.
    """
    # Validate the input arguments for the specified stage
    _validate_input_arguments(stage, schema, expert_feedback, papers)

    # Run the specified stage
    if stage == 1:
        typer.echo("Running SCHEMA-MINER -- Stage 1: Initial Schema Extraction")
        extract_schema_stage1(save_schema=True)
        typer.secho(f"Stage 1 completed. Initial schema saved to {CLIConfig.RESULTS_PATH}", fg=typer.colors.GREEN, bold=True)
    # For stage 2 and stage 3, run the stage in batches with the provided expert feedback
    else:
        _run_stage_expert_feedback(stage, schema, expert_feedback, papers)

def _run_ontology_grounding(ontology_grounding_method: str, schema: str) -> None:
    """
    Run the specified Ontology Grounding method with the provided process schema.
    Args:
        ontology_grounding_method (str): The ontology grounding method to use: 'prompt' or 'agentic'.
        schema (str): Path to the process schema to be grounded.
    """
    # Validate the ontology grounding method
    if ontology_grounding_method not in ['prompt', 'agentic']:
        typer.secho("Invalid ontology grounding method specified. Please choose 'prompt' or 'agentic'.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Validate the schema path
    if not schema:
        typer.secho("Schema path is required for ontology grounding. Please provide the path to the schema using --schema.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    if not Path(schema).is_file():
        typer.secho(f"Schema file not found at path: {schema}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    if not schema.endswith('.json'):
        typer.secho("Schema file should be a JSON file with .json extension.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Initialize the Path object for the schema
    schema = Path(schema)

    # Run the specified ontology grounding method
    ontology_grounding_fn = prompt_based_qudt_grounding if ontology_grounding_method == 'prompt' else agentic_qudt_grounding
    ontology_grounding_fn(schema, save_schema=True)
    typer.secho(f"Ontology grounding completed using {ontology_grounding_method} method. Grounded schema saved to {CLIConfig.RESULTS_PATH}", fg=typer.colors.GREEN, bold=True)

@app.command()
def main(
    stage: Optional[int] = typer.Option(None, "--stage", help="Specify the stage of schema extraction to execute (1, 2, or 3)."),
    ontology_grounding: Optional[str] = typer.Option(None, "--ontology-grounding", help="Ontology grounding method: 'prompt' or 'agentic'"),
    schema: Optional[str] = typer.Option(None, "--schema", help="Path to the initial schema for stage 2 and refined schema for stage 3, or process schema for ontology grounding."),
    expert_feedback: Optional[str] = typer.Option(None, "--expert-feedback", help="Expert feedback as text or path to a text file (stages 2 & 3 only)."),
    papers: Optional[int] = typer.Option(None, "--papers", help="Number of scientific papers to use in batches for stage 2 and stage 3."),
    version: Optional[bool] = typer.Option(None, "--version", callback=version_callback, is_eager=True, help="Show the version of the Schema Miner CLI and exit.")
):
    """
    SCHEMA-MINER CLI: A Command-Line Interface for Schema Extraction from Scientific Literature. This CLI allows users to execute different stages of the SCHEMA-MINER pipeline, including initial schema extraction, schema refinement with expert feedback, and ontology grounding. Users can specify the stage to run, provide expert feedback, and choose the ontology grounding method. The CLI also includes a version option to display the current version of the tool.
    """

    # Guard 1: Validate that at least one of stage or ontology_grounding is provided
    if not stage and not ontology_grounding:
        typer.secho("Please specify either a stage to run using --stage or an ontology grounding method using --ontology-grounding.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Guard 2: If both stage and ontology_grounding are provided, show an error as only one of them can be executed at a time
    if stage and ontology_grounding:
        typer.secho("Please specify only one of --stage or --ontology-grounding at a time. To run a stage, use --stage. To run ontology grounding, use --ontology-grounding.", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # If stage is provided, run the specified stage of schema extraction
    if stage:
        _run_stage(stage, schema, expert_feedback, papers)

    # If ontology_grounding is provided, run the specified ontology grounding method
    if ontology_grounding:
        _run_ontology_grounding(ontology_grounding, schema)

if __name__ == "__main__":
    app()
