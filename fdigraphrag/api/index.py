# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""
Indexing API for fdigraphrag.

WARNING: This API is under development and may undergo changes in future releases.
Backwards compatibility is not guaranteed at this time.
"""

import logging

from fdigraphrag.callbacks.reporting import create_pipeline_reporter
from fdigraphrag.callbacks.workflow_callbacks import WorkflowCallbacks
from fdigraphrag.config.enums import IndexingMethod
from fdigraphrag.config.models.graph_rag_config import fdigraphragConfig
from fdigraphrag.index.run.run_pipeline import run_pipeline
from fdigraphrag.index.run.utils import create_callback_chain
from fdigraphrag.index.typing.pipeline_run_result import PipelineRunResult
from fdigraphrag.index.typing.workflow import WorkflowFunction
from fdigraphrag.index.workflows.factory import PipelineFactory
from fdigraphrag.logger.base import ProgressLogger
from fdigraphrag.logger.null_progress import NullProgressLogger

log = logging.getLogger(__name__)


async def build_index(
    config: fdigraphragConfig,
    method: IndexingMethod = IndexingMethod.Standard,
    is_update_run: bool = False,
    memory_profile: bool = False,
    callbacks: list[WorkflowCallbacks] | None = None,
    progress_logger: ProgressLogger | None = None,
) -> list[PipelineRunResult]:
    """Run the pipeline with the given configuration.

    Parameters
    ----------
    config : fdigraphragConfig
        The configuration.
    method : IndexingMethod default=IndexingMethod.Standard
        Styling of indexing to perform (full LLM, NLP + LLM, etc.).
    memory_profile : bool
        Whether to enable memory profiling.
    callbacks : list[WorkflowCallbacks] | None default=None
        A list of callbacks to register.
    progress_logger : ProgressLogger | None default=None
        The progress logger.

    Returns
    -------
    list[PipelineRunResult]
        The list of pipeline run results
    """
    logger = progress_logger or NullProgressLogger()
    # create a pipeline reporter and add to any additional callbacks
    callbacks = callbacks or []
    callbacks.append(create_pipeline_reporter(config.reporting, None))

    workflow_callbacks = create_callback_chain(callbacks, logger)

    outputs: list[PipelineRunResult] = []

    if memory_profile:
        log.warning("New pipeline does not yet support memory profiling.")

    pipeline = PipelineFactory.create_pipeline(config, method)

    workflow_callbacks.pipeline_start(pipeline.names())

    async for output in run_pipeline(
        pipeline,
        config,
        callbacks=workflow_callbacks,
        logger=logger,
        is_update_run=is_update_run,
    ):
        outputs.append(output)
        if output.errors and len(output.errors) > 0:
            logger.error(output.workflow)
        else:
            logger.success(output.workflow)
        logger.info(str(output.result))

    workflow_callbacks.pipeline_end(outputs)
    return outputs


def register_workflow_function(name: str, workflow: WorkflowFunction):
    """Register a custom workflow function. You can then include the name in the settings.yaml workflows list."""
    PipelineFactory.register(name, workflow)
