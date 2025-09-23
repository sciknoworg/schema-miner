<p align="center">
<img width="450" src="https://github.com/sciknoworg/schema-miner/blob/main/assets/schema-miner-pro-logo.jpg?raw=true" alt="schema-miner pro logo" />
</p>

<div align="center">

[![PyPI - Version](https://img.shields.io/pypi/v/schema-miner)](https://pypi.org/project/schema-miner/)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/schema-miner)](https://pepy.tech/projects/schema-miner)
[![Maintained Yes](https://img.shields.io/badge/maintained-yes-green)](https://github.com/sciknoworg/schema-miner/blob/main/MAINTENANCE.md)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![MIT License](https://img.shields.io/github/license/sciknoworg/schema-miner)](LICENSE)
[![DOI](https://zenodo.org/badge/900734076.svg)](https://doi.org/10.5281/zenodo.14781824)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](https://schema-miner.readthedocs.io/en/latest/)

</div>

<h3 align="center">SCHEMA-MINER<sup>pro</sup>: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow</h3>

Schema-Miner is an open-source framework for scientific schema mining. It combines Large Language Models (LLMs) with human-in-the-loop refinement to extract, and semantically ground schema properties from unstructured text. Schema-Miner Pro extends this framework with an automated ontology-grounding component, aligning the schema with formal ontologies (e.g., [QUDT](https://www.qudt.org/pages/HomePage.html)). Documentation and usage guides are available at [schema-miner.readthedocs.io](https://schema-miner.readthedocs.io/en/latest/).

## 🧪 Installation

Install the package directly from PyPI using ``pip``:

```bash
pip install schema-miner
```

If you are working with the source code directly, install dependencies from [requirements.txt](https://github.com/sciknoworg/schema-miner/blob/main/requirements.txt):


```bash
git clone https://github.com/sciknoworg/schema-miner.git
cd schema-miner
pip install -r requirements.txt
```

## ⚙️ System Requirements
Running with OpenAI models (e.g., [**GPT-4o**](https://platform.openai.com/docs/models#gpt-4o), [**GPT-4-turbo**](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4)) requires no special hardware beyond a basic system with internet access, since inference is API-based. For **open-source models** (e.g., [**Llama 3.1 8B**](https://ai.meta.com/blog/meta-llama-3-1/)), local execution is possible on CPU but slow; for practical performance, a GPU with sufficient VRAM (per model specifications) is strongly recommended.

For more details, please check the documentation: [https://schema-miner.readthedocs.io/en/latest/](https://schema-miner.readthedocs.io/en/latest/).

## 🚀 Quick Start

For a quick start, see the provided example notebooks highlighting the overall workflows of the schema-miner.

<div align="center">

|  | Notebook |
| --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | [Schema Mining With LLMs and expert Example](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_mining_with_LLMs_and_expert_example.ipynb) |
| 2 | [Schema Ontology Grounding Example](https://github.com/sciknoworg/schema-miner/blob/main/tutorials/notebooks/schema_mining_ontology_grounding_example.ipynb) |

</div>

## 📚 Citing this Work

If you use this repository in your research or applications, please cite the appropriate paper(s):

- Schema-Miner (schema discovery/mining only):
  > Sameer Sadruddin, Jennifer D’Souza, Eleni Poupaki, Alex Watkins, Hamed Babaei Giglou, Anisa Rula, Bora Karasulu, Sören Auer, Adrie Mackus, and Erwin Kessels.
  > **LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models.**
  > In *The Semantic Web – ESWC 2025*, Springer, Cham, pp. 244–261.
  > [https://doi.org/10.1007/978-3-031-94578-6_14](https://doi.org/10.1007/978-3-031-94578-6_14)

  ### 📌 BibTeX
  ```bibtex
  @InProceedings{10.1007/978-3-031-94578-6_14,
    author    = {Sadruddin, Sameer and D'Souza, Jennifer and Poupaki, Eleni and Watkins, Alex and Babaei Giglou, Hamed and Rula, Anisa and Karasulu, Bora and Auer, S{\"o}ren and Mackus, Adrie and Kessels, Erwin},
    editor    = {Curry, Edward and Acosta, Maribel and Poveda-Villal{\'o}n, Maria and van Erp, Marieke and Ojo, Adegboyega and Hose, Katja and Shimizu, Cogan and Lisena, Pasquale},
    title     = {LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models},
    booktitle = {The Semantic Web},
    year      = {2025},
    publisher = {Springer Nature Switzerland},
    address   = {Cham},
    pages     = {244--261},
    isbn      = {978-3-031-94578-6},
  }
  ```
- Schema-Miner<sup>pro</sup> (schema mining with QUDT grounding / ontology grounding):
  > Sameer Sadruddin, Jennifer D’Souza, Eleni Poupaki, Alex Watkins, Bora Karasulu, Sören Auer, Adrie Mackus, and Erwin Kessels.
  > **SCHEMA-MINER<sup>pro</sup>: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow.**
  > In *Semantic Web Journal.*
  > [https://www.semantic-web-journal.net/system/files/swj3871.pdf](https://www.semantic-web-journal.net/system/files/swj3871.pdf)

  ### 📌 BibTeX
  ```bibtex
  @InProceedings{10.1007/978-3-031-94578-6_14,
    author    = {Sadruddin, Sameer and D'Souza, Jennifer and Poupaki, Eleni and Watkins, Alex and Karasulu, Bora and Auer, S{\"o}ren and Mackus, Adrie and Kessels, Erwin},
    title     = {SCHEMA-MINERpro: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow},
    journal = {Semantic Web Journal},
    year      = {2025},
  }
  ```

## 👥 Contact & Contributions

We’d love to hear from you!
Whether you're interested in collaborating on `Schema-MinerPro` or have ideas to extend its capabilities, feel free to reach out:

- **Collaboration inquiries:** Contact Jennifer D'Souza at jennifer.dsouza [at] tib.eu

- **Development questions or bug reports:** Please [open an issue](https://github.com/sciknoworg/schema-miner/issues) right here in the repository or get in touch with the lead developer Sameer Sadruddin at sameer.sadruddin [at] tib.eu

Let’s build better schema-mining tools—together!

## 📃 License

This work is licensed under a [MIT License](https://github.com/sciknoworg/schema-miner/blob/main/LICENSE.txt)

## 🔗 Links
Source Code: [https://github.com/sciknoworg/schema-miner](https://github.com/sciknoworg/schema-miner)

Documentation: [https://schema-miner.readthedocs.io/en/latest/](https://schema-miner.readthedocs.io/en/latest/)

Issues: [https://github.com/sciknoworg/schema-miner/issues](https://github.com/sciknoworg/schema-miner/issues)
