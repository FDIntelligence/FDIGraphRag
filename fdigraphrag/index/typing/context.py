# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

# isort: skip_file
"""A module containing the 'PipelineRunContext' models."""

from dataclasses import dataclass

from fdigraphrag.cache.pipeline_cache import PipelineCache
from fdigraphrag.callbacks.workflow_callbacks import WorkflowCallbacks
from fdigraphrag.index.typing.state import PipelineState
from fdigraphrag.index.typing.stats import PipelineRunStats
from fdigraphrag.storage.pipeline_storage import PipelineStorage


@dataclass
class PipelineRunContext:
    """Provides the context for the current pipeline run."""

    stats: PipelineRunStats
    storage: PipelineStorage
    "Long-term storage for pipeline verbs to use. Items written here will be written to the storage provider."
    cache: PipelineCache
    "Cache instance for reading previous LLM responses."
    callbacks: WorkflowCallbacks
    "Callbacks to be called during the pipeline run."
    state: PipelineState
    "Arbitrary property bag for runtime state, persistent pre-computes, or experimental features."
