<p align="center">
<img width="450" src="https://github.com/sciknoworg/schema-miner/blob/main/assets/schema-miner-logo.png?raw=true" alt="schema-miner logo" />
</p>

<div align="center">

![Maintained Yes](https://img.shields.io/badge/maintained-yes-green)
[![MIT License](https://img.shields.io/github/license/sciknoworg/schema-miner)](LICENSE)
[![DOI](https://zenodo.org/badge/900734076.svg)](https://doi.org/10.5281/zenodo.14781824)
[![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](https://schema-miner.readthedocs.io/en/latest/)

</div>

**LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models**

This is an open-source implementation of Schema-miner.

## 📋 Schema-miner Overview

Schema-miner (LLMs4SchemaDiscovery) is novel framework that leverages Large Language Models (LLMs) and continuous human feedback to automate and enhance schema mining task. Through an iterative process, the framework uses LLMs to extract and organize properties from unstructured text, refine schemas with expert input, and incorporate domain-specific ontologies to add semantic knowledge. A comprehensive documentation for schema-miner, including detailed guides and examples, is available at [schema-miner.readthedocs.io](https://schema-miner.readthedocs.io/en/latest/).

## ⚙️ System Requirements

The computational requirements for running this project vary depending on the model being used. If utilizing OpenAI models such as [**GPT-4o**](https://platform.openai.com/docs/models#gpt-4o) and [**GPT-4-turbo**](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), no specialized hardware is needed since inference is performed via API calls. A basic system with a stable internet connection is sufficient for executing API-based workflow.

For users opting to run **open-source models** such as [**Llama 3.1 8B**](https://ai.meta.com/blog/meta-llama-3-1/) or other large-scale transformer-based models, local execution demands significantly higher computational resources. While these models can be executed on a CPU, inference times will be considerably longer. However, for efficient execution, a dedicated GPU with VRAM (specified by the model's documentation) is strongly recommended.

While the hardware configuration can be adjusted based on the model size and performance needs, using a GPU significantly accelerates inference processes, reducing execution time drastically compared to CPU-only setups.

## 🧪 Installation

Install the package directly from PyPI:

```bash
pip install -i https://test.pypi.org/simple/ schema-miner
```

If you are working with the source code directly, install dependencies from [requirements.txt](requirements.txt):


```bash
pip install -r requirements.txt
```

For more details, please check the documentation [here](https://schema-miner.readthedocs.io/en/latest/).

## 📚 Citing this Work

If you use `schema-miner` in your research or applications, please cite the following paper:

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

## 👥 Contact & Contributions

We’d love to hear from you!
Whether you're interested in collaborating on `schema-miner` or have ideas to extend its capabilities, feel free to reach out:

- **Collaboration inquiries:** Contact Jennifer D'Souza at jennifer.dsouza [at] tib.eu

- **Development questions or bug reports:** Please [open an issue](https://github.com/sciknoworg/schema-miner/issues) right here in the repository or get in touch with the lead developer Sameer Sadruddin at sameer.sadruddin [at] tub.eu

Let’s build better schema-mining tools—together!

## 📃 License

This work is licensed under a [MIT License](https://github.com/sciknoworg/schema-miner/blob/main/LICENSE.txt)