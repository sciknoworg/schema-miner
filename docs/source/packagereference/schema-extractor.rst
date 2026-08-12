Schema Extractor
****************

The schema extractor is the core three-stage workflow in ``schema-miner``. It
uses a configured LLM to move from an expert-written process specification to a
refined scientific schema, with optional domain-expert feedback between
iterations. Ontology grounding is documented separately in
:doc:`ontology_grounding`.

For complete command-line setup, see the repository
`README <https://github.com/sciknoworg/schema-miner#readme>`_.

Shared Configuration
====================

Before running any extraction stage, configure the provider and process context
in ``.env``:

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Variable
     - Purpose
   * - ``LLM_PROVIDER``
     - Selects the inference backend, for example ``OPENAI``, ``SAIA``,
       ``OPENROUTER``, ``OLLAMA``, or ``HUGGINGFACE``.
   * - ``LLM_MODEL``
     - Selects the model used for schema extraction and refinement.
   * - ``PROCESS_NAME``
     - Names the scientific process being mined.
   * - ``PROCESS_DESCRIPTION``
     - Gives the model short domain context for interpreting the process,
       papers, feedback, and schema properties.
   * - ``RESULTS_PATH``
     - Directory where each stage writes generated schemas, logs, and
       intermediate outputs.

The provider-specific credential variables, such as ``OPENAI_API_KEY``,
``SAIA_API_KEY``, ``OPENROUTER_API_KEY``, or
``HuggingFace_Access_Token``, are also read from ``.env``. Use
``.env.example`` in the repository as the starting template.

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

The same workflow is implemented by the functions below.

.. automodule:: schema_miner.schema_extractor
   :members:
   :undoc-members:
   :show-inheritance:
