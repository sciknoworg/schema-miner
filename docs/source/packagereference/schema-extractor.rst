Schema Mining
*************

The schema extractor is the core three-stage workflow in ``schema-miner``. It
uses a configured LLM to move from an expert-written process specification to a
refined scientific schema, with optional domain-expert feedback between
iterations. Ontology grounding is documented separately in
:doc:`ontology_grounding`.

Configure the provider, process metadata, stage input paths, and output path in
``.env`` before running these commands. See :doc:`../gettingstarted/installation`
for the full configuration template.

Tutorial Demo
=============

The short video below shows a quick run of the first tutorial notebook using the
Hugging Face local GPU setup.

.. raw:: html

   <div style="display:flex; justify-content:center; margin:1.25rem 0 1.5rem;">
     <a href="https://youtu.be/faQMPtWzF2g" target="_blank" rel="noopener" aria-label="Watch a quick demo of the Schema-Miner local GPU tutorial notebook" style="position:relative; display:block; width:min(560px, 100%); line-height:0;">
       <img src="https://img.youtube.com/vi/faQMPtWzF2g/hqdefault.jpg" alt="Quick demo of the Schema-Miner local GPU tutorial notebook" style="width:100%; border:1px solid #d8dee4; border-radius:8px; box-shadow:0 8px 24px rgba(15,23,42,0.12);">
       <span aria-hidden="true" style="position:absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:76px; height:54px; border-radius:14px; background:#ff0000; box-shadow:0 8px 22px rgba(0,0,0,0.28); display:flex; align-items:center; justify-content:center;">
         <span style="width:0; height:0; border-top:13px solid transparent; border-bottom:13px solid transparent; border-left:21px solid #fff; margin-left:5px;"></span>
       </span>
     </a>
   </div>

CLI Options
===========

.. list-table::
   :header-rows: 1
   :widths: 22 24 54

   * - Option
     - Values
     - Description
   * - ``--stage``
     - ``1``, ``2``, or ``3``
     - Runs one schema extraction stage.
   * - ``--schema``
     - Path to ``.json``
     - Required for stages 2 and 3. Points to the schema produced by the
       previous stage or previous refinement iteration.
   * - ``--expert-feedback``
     - Text or path
     - Optional for stages 2 and 3. Accepts inline review text or a path to a
       ``.txt`` or ``.md`` feedback file.
   * - ``--papers``
     - ``N`` or ``all``
     - Optional for stages 2 and 3. Controls the paper batch size. If omitted,
       one paper is processed per batch.

Stage 1: Initial Schema Mining
==============================

Stage 1 generates the first JSON schema from a process specification document.
The specification is usually a compact document written by a domain expert,
listing the key properties researchers repeatedly report for the target
process.

Required input:

* ``STAGE1_SPECS_PATH`` in ``.env`` pointing to a ``.txt``, ``.md``, or
  ``.pdf`` specification document.

Example:

.. code-block:: bash

   schema-miner --stage 1

The extractor reads the process specification, calls the configured LLM, and
writes the initial schema to ``RESULTS_PATH``. In the example data layout, this
corresponds to outputs such as ``data/stage1/schema/<model>.json``.

Stage 2: Preliminary Schema Refinement
======================================

Stage 2 refines the initial schema with a small, curated corpus of
domain-relevant papers and optional expert feedback. This stage is intended to
extend the initial specification into a richer schema while preserving domain
precision.

Required inputs:

* ``STAGE2_PAPERS_PATH`` in ``.env`` pointing to a directory of curated papers.
* ``--schema`` pointing to the Stage 1 JSON schema.

Basic run:

.. code-block:: bash

   schema-miner --stage 2 --schema data/stage1/schema/<model>.json

Run with inline expert feedback:

.. code-block:: bash

   schema-miner --stage 2 --schema data/stage1/schema/<model>.json \
       --expert-feedback "Add units for temperature and pressure fields."

Run with expert feedback from a file:

.. code-block:: bash

   schema-miner --stage 2 --schema data/stage1/schema/<model>.json \
       --expert-feedback data/stage1/feedback/<model>.txt

Run with fixed-size paper batches:

.. code-block:: bash

   schema-miner --stage 2 --schema data/stage1/schema/<model>.json --papers 3

Run all available papers in one batch:

.. code-block:: bash

   schema-miner --stage 2 --schema data/stage1/schema/<model>.json --papers all

When ``--papers N`` is supplied, ``schema-miner`` processes papers in batches of
``N`` and asks for updated expert feedback after each batch. When
``--papers all`` is supplied, all available papers are processed in one run and
the expert feedback provided at the beginning is reused without reprompting
between papers.

Stage 3: Final Schema Refinement
================================

Stage 3 uses a broader, more heterogeneous paper corpus to test schema stability
across different reporting styles, process variants, and edge cases. It starts
from the final Stage 2 schema and follows the same CLI patterns as Stage 2.

Required inputs:

* ``STAGE3_PAPERS_PATH`` in ``.env`` pointing to the broader paper corpus.
* ``--schema`` pointing to the final Stage 2 JSON schema.

Example:

.. code-block:: bash

   schema-miner --stage 3 --schema data/stage2/schema-batch2/<model>.json \
       --papers 5 \
       --expert-feedback data/stage2/feedback-batch2/<model>.txt

The output is a refined schema suitable for ontology grounding and downstream
semantic use.

Python API
==========

The same three-stage workflow can be called directly from Python. These
functions read provider, process, input-path, and output-path settings from the
same ``.env`` configuration used by the CLI.

.. code-block:: python

   from pathlib import Path

   from schema_miner.schema_extractor import (
       extract_schema_stage1,
       extract_schema_stage2,
       extract_schema_stage3,
   )

   # Stage 1: read STAGE1_SPECS_PATH from .env and create the first schema.
   initial_schema = extract_schema_stage1(save_schema=True)

   # Stage 2: refine the schema with expert feedback and one scientific paper.
   refined_schema = extract_schema_stage2(
       initial_schema=Path("data/stage1/schema/<model>.json"),
       expert_review=Path("data/stage1/feedback/<model>.txt"),
       scientific_paper=Path("data/stage2/batch1/Bairagiya_2024.pdf"),
       save_schema=True,
   )

   # Stage 3: continue refinement with the broader corpus.
   final_schema = extract_schema_stage3(
       refined_schema=Path("data/stage2/schema-batch1/<model>.json"),
       expert_review=Path("data/stage2/feedback-batch1/<model>.txt"),
       scientific_paper=Path("data/stage3/batch1/<paper>.pdf"),
       save_schema=True,
   )

``extract_schema_stage1(save_schema=False)``
   Reads the process specification from ``STAGE1_SPECS_PATH`` and returns the
   initial schema as a ``dict``. When ``save_schema=True``, the schema is also
   written to ``RESULTS_PATH/<model>.json``.

``extract_schema_stage2(initial_schema, expert_review, scientific_paper, save_schema=False)``
   Refines a Stage 1 schema using one expert-feedback input and one scientific
   paper. ``initial_schema`` may be a dictionary or JSON file path;
   ``expert_review`` may be inline text or a text/Markdown file path; and
   ``scientific_paper`` may be a PDF or text file path. The function returns the
   updated schema as a ``dict`` and optionally writes it to ``RESULTS_PATH``.

``extract_schema_stage3(refined_schema, expert_review, scientific_paper, save_schema=False)``
   Applies the same refinement pattern to a Stage 2 schema and a broader
   scientific-paper corpus. ``refined_schema`` may be a dictionary or JSON file
   path. The returned dictionary is the final schema used for downstream
   ontology grounding.
