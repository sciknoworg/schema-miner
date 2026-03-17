import os

from dotenv import load_dotenv

from schema_miner.config.processConfig import ProcessConfig


class CLIConfig:

    # Loading the environment file
    load_dotenv()

    # Process Configuration
    PROCESS_NAME = os.getenv("PROCESS_NAME", "")
    PROCESS_DESCRIPTION = os.getenv("PROCESS_DESCRIPTION", "")

    # Update ProcessConfig
    ProcessConfig.Process_name = PROCESS_NAME
    ProcessConfig.Process_description = PROCESS_DESCRIPTION

    # Data Paths
    STAGE1_SPECIFICATION_PATH = os.getenv("STAGE1_SPECS_PATH", "")
    STAGE2_PAPERS_PATH = os.getenv("STAGE2_PAPERS_PATH", "")
    STAGE3_PAPERS_PATH = os.getenv("STAGE3_PAPERS_PATH", "")

    # Result Paths
    RESULTS_PATH = os.getenv("RESULTS_PATH", "")

    @staticmethod
    def validate_process_config() -> bool:
        """
        Validate that essential process configuration parameters are set, else raise a clear error.
        """
        if not CLIConfig.PROCESS_NAME:
            raise ValueError("Missing PROCESS_NAME. Please set it in your environment:\n")
        if not CLIConfig.PROCESS_DESCRIPTION:
            raise ValueError("Missing PROCESS_DESCRIPTION. Please set it in your environment:\n")
        return True

    @staticmethod
    def validate_result_paths() -> bool:
        """
        Validate that results path is set, else raise a clear error.
        """
        if not CLIConfig.RESULTS_PATH:
            raise ValueError("Missing RESULTS_PATH. Please set it in your environment:\n")
        return True
