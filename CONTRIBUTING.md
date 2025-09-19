# Contributing to Schema-miner

Thank you for showing your interest in contributing to **Schema-miner!** We welcome all contributions, whether it's bug reports, feature request, documentation improvement, or code enhancements.

## How to Contribute

**Reporting Issues**

If you encounter a bug or have a suggestion for improvement, please open an [issue](https://github.com/sciknoworg/schema-miner/issues) on github. When reporting an issue, please include the following:

1. A clear description of the problem
2. Steps to reproduce the issue (if applicable)
3. Any relevant error messages or logs

**Feature Requests**

The ideas for improving **Schema-miner** are really appreciated! If you have a feature in mind, please follow these steps:

1. Before submitting a new feature request, check the [issue](https://github.com/sciknoworg/schema-miner/issues) to see if similar request already exist. If an existing issue covers your idea, consider commenting on it, instead of opening a new one.
2. To open a new feature request, please provide the following details:
    * **Title:** A short and clear description of the feature.
    * **Problem Statement:** Explain the problem that this feature solves or what limitation it addresses.
    * **Proposed Solution:** Describe how this feature should work.

## Submitting a Pull Request (PR)

If you would like to contribute in the code, please follow these steps:

**Step 1: Fork and Clone the Repository**

1. First "Fork" the [**Schema-miner**](https://github.com/sciknoworg/schema-miner) repository
2. Clone the fork repository
```bash
git clone https://github.com/sciknoworg/schema-miner.git
cd schema-miner
```

**Step 2: Create a Feature Branch**

Create a new branch for your changes and push your commits to your forked branch:
```bash
git checkout -b feature-name
#Do your changes
git add .
git commit -m "Add brief description of your changes"
git push origin feature-name
```

**Step 3: Open a Pull Request**

Submit your pull request by providing a clear description of your changes. Ensure that your code follows the project guidelines properly.

## Code Guidelines

To maintain the quality and consistency in the code, please follow these guidelines:

1. **Code Style:** Follow the Python best practices [(PEP 8)](https://peps.python.org/pep-0008/)
2. **Modularization:**
    * Structure your code using **classes and objects** where appropriate
    * Keep functions **small and focused** to improve readability and maintainability
    * Avoid large monolithic scripts, instead break code into meaningful modules.
3. **Commenting and Documentation:**
    * Add **docstring** to all public functions and classes following the [(PEP 257)](https://peps.python.org/pep-0257/) convention.
    * Use inline comments to explain non-trivial logic.
    * If your code introduces a new feature, update the relevant section in the [README.md](README.md)

## Questions?

If you have any questions, feel free to open an issue or contact me at [sameer.sadruddin@tib.eu](mailto:sameer.sadruddin@tib.eu).
