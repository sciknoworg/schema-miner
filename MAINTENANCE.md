# Schema-miner Maintenance Plan

This document outlines the maintenance and sustainability plan for **Schema-miner**, a tool for extracting schema properties from scientific literature. The goal is to ensure the long-term availability, usability, and extensibility of the project.

## Future Maintenance Plans

* **Incorporation of Agentic AI Workflows:**
Integrating agentic workflows to automate JSON validation processes and ensure accurate grounding of measurement ontologies.

* **Enhancing Domain-Agnostic Functionality:**
Refactor the system to accept role or domain parameters in prompts, enabling applicability across various knowledge domains.

* **Additional Use Cases:**
Applying Schema-miner to new scenarios beyond its initial scope, demonstrating its versatility and broadening its impact.

* **Creating Comprehensive Documentation**
Create and maintaining a dedicated [documentation](https://schema-miner.readthedocs.io/en/latest/) page that provides in-depth instructions on utilizing Schema-miner across various use cases and configurations. In general, the guide will include:
    * **Use Case Scenarios:** Detailed examples demonstrating how to apply Schema-miner in different contexts.
    * **Code Explanation:** Comprehensive and in-depth explanations of the Schema-miner codebase.
    * **Tutorials**: Guided walkthroughs to assist users in setting up and effectively using the tool.

## Repository Sustainability

* The **Schema-miner** codebase is hosted on GitHub under the [**MIT License**](LICENSE.txt) allowing open-source contributions and long-term access.
* A persistent **DOI** is assigned via [**Zenodo**](https://doi.org/10.5281/zenodo.14781824) to ensure permanent referencing of the latest stable release.
* Releases will be tagged on GitHub, with versioning to track major, minor, and patch updates.

## Security Measures

* **Regular Security Audits**: We will conduct periodic security audits to identify and address vulnerabilities promptly.
* **Dependency Management**: A regular update of dependencies to their latest stable versions to mitigate risks associated with known vulnerabilities.

## Maintenance Responsibilities

* The primary maintainer of this repository is [Sameer Sadruddin](https://github.com/SameerSamji)
* Ongoing maintenance includes:
    * Fixing reported bugs and issues.
    * Reviewing and merging community pull requests.
* Issues and PRs will be reviewed within 2 - 3 days to ensure timely reponses.

## Update and Support Schedule

* Based on community feedbacks, planned improvements will be discussed in GitHub Issues and internal organization, and will be implemented in scheduled updates.
* Libraries used by **Schema-miner** will be reviewed and updated **at least every 6 months** to ensure stability and security.

## Community Contributions

* Contributions from the community are highly encouraged through **GitHub Issues** (for reporting bugs and suggesting features) and **Pull Requests** (for code contributions).
* Contribution guidelines are outlined in [CONTRIBUTING.md](CONTRIBUTING.md), detailing code standards, testing requirements and PR submission processes.

## Long-Term Preservation

* The repository is archived on [**Zenodo**](https://doi.org/10.5281/zenodo.14781824), allowing users to cite **Schema-miner** using a **DOI**.
* In the event that maintainers are unable to continue development, the repository will be marked as **Archived** on GitHub.

Maintainers can be contacted at [sameer.sadruddin@tib.eu](mailto:sameer.sadruddin@tib.eu) for inquiries regarding sustainability and long-term support.
