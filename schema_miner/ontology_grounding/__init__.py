# Copyright 2025 Scientific Knowledge Organization (SciKnowOrg) Research Group.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Ontology Grounding subpackage.
Contains modules and utilities for grounding JSON Schema with QUDT Ontology Using Either Simple LLM Prompting or Agent-based Workflow
"""
from .agentic_qudt_grounding import agentic_qudt_grounding
from .prompt_qudt_grounding import prompt_based_qudt_grounding

__all__ = ["prompt_based_qudt_grounding", "agentic_qudt_grounding"]
