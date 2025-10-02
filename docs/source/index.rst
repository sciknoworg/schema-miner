.. Schema-Miner documentation master file, created by
   sphinx-quickstart on Tue Feb  4 21:49:19 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: img/schema-miner-pro-logo.jpg
   :align: center
   :width: 450px
   :alt: Schema miner pro Logo

.. raw:: html

   <div style="text-align: center;">
        <a href="https://pypi.org/project/schema-miner/">
            <img src="https://img.shields.io/pypi/v/schema-miner" alt="PYPI Version">
        </a>
        <a href="https://pepy.tech/projects/schema-miner">
            <img src="https://img.shields.io/pepy/dt/schema-miner" alt="PYPI Total Downloads">
        </a>
        <a href="https://github.com/sciknoworg/schema-miner/blob/main/MAINTENANCE.md">
            <img src="https://img.shields.io/badge/maintained-yes-green" alt="Maintained">
        </a>
        <a href="https://github.com/pre-commit/pre-commit">
            <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit" style="max-width:100%;">
        </a>
        <a href="https://github.com/PyCQA/bandit">
            <img src="https://img.shields.io/badge/security-bandit-yellow.svg" alt="security: bandit">
        </a>
        <a href="https://github.com/sciknoworg/schema-miner/blob/main/LICENSE.txt">
            <img src="https://img.shields.io/github/license/sciknoworg/schema-miner" alt="License">
        </a>
        <a href="https://doi.org/10.5281/zenodo.14781824">
            <img src="https://zenodo.org/badge/900734076.svg" alt="DOI">
        </a>
        <a href="https://test.pypi.org/project/schema-miner/">
            <img src="https://img.shields.io/badge/TestPyPI-2.0.0-blue" alt="TestPyPI Package">
        </a>
    </div>
   <br>

SCHEMA-MINER :sup:`Pro`: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow
************************************************************************************************************************************

Schema-Miner is a novel framework that leverages Large Language Models (LLMs) and continuous human feedback to automate and enhance the schema mining task. Through an iterative process, the framework uses LLMs to extract and organize properties from unstructured text and refines schemas with expert input. Schema-Miner :sup:`pro` extends Schema-Miner with an ontology grounding component powered by agentic AI. It performs multi-step reasoning using lexical heuristics and semantic similarity search, and grounds schema elements in formal ontologies (e.g., `QUDT <https://www.qudt.org/pages/HomePage.html>`_).

Below is the workflow diagram of Schema-Miner.

.. figure:: img/LLM4SchemaMining-Workflowdesign.svg
   :align: center
   :width: 80%
   :alt: Schema-miner Workflow

   **Figure 1.** Overview of the LLMs4SchemaDiscovery workflow implemented in schemaminer. Stage 1 (gray box) generates an initial schema from domain specifications. Stage 2 (orange box) refines the schema using a small, expert-curated set of papers and optional feedback. Stage 3 (red box) finalizes the schema with a larger, non-curated collection of papers. The workflow iteratively updates the schema and concludes by grounding schema properties to ontologies.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :glob:
   :hidden:

   gettingstarted/installation
   gettingstarted/quickstart

.. toctree::
   :maxdepth: 2
   :caption: Package Reference
   :glob:
   :hidden:

   packagereference/schema-extractor
   packagereference/ontology_grounding
   packagereference/pdf_extractor

Citing this Work
****************

If you use this repository in your research or applications, please cite the following paper(s):

**LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models**
--------------------------------------------------------------------------------------------------------------

Sameer Sadruddin, Jennifer D’Souza, Eleni Poupaki, Alex Watkins, Hamed Babaei Giglou, Anisa Rula, Bora Karasulu, Sören Auer, Adrie Mackus, and Erwin Kessels.
**LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Mining with Large Language Models.**
In *The Semantic Web – ESWC 2025*, Springer, Cham, pp. 244–261.
`https://doi.org/10.1007/978-3-031-94578-6_14 <https://doi.org/10.1007/978-3-031-94578-6_14>`_


BibTeX
------

.. code-block:: text

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

**SCHEMA-MINERpro: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow**
-----------------------------------------------------------------------------------------------------------------------------

Sameer Sadruddin, Jennifer D’Souza, Eleni Poupaki, Alex Watkins, Bora Karasulu, Sören Auer, Adrie Mackus, and Erwin Kessels.
**SCHEMA-MINERpro: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow.**
In *Semantic Web Journal.*
`https://www.semantic-web-journal.net/system/files/swj3871.pdf <https://www.semantic-web-journal.net/system/files/swj3871.pdf>`_

BibTeX
------

.. code-block:: text

    @InProceedings{10.1007/978-3-031-94578-6_14,
    author    = {Sadruddin, Sameer and D'Souza, Jennifer and Poupaki, Eleni and Watkins, Alex and Karasulu, Bora and Auer, S{\"o}ren and Mackus, Adrie and Kessels, Erwin},
    title     = {SCHEMA-MINERpro: Agentic AI for Ontology Grounding over LLM-Discovered Scientific Schemas in a Human-in-the-Loop Workflow},
    journal = {Semantic Web Journal},
    year      = {2025},
    }

License
**********

This project is open source and distributed under the terms of the **MIT License**.

The full license text is available in the `MIT License <https://github.com/sciknoworg/schema-miner/blob/main/LICENSE.txt>`_ file in the repository.
