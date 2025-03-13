# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Root package for description summarization."""

from fdigraphrag.index.operations.summarize_descriptions.summarize_descriptions import (
    summarize_descriptions,
)
from fdigraphrag.index.operations.summarize_descriptions.typing import (
    SummarizationStrategy,
    SummarizeStrategyType,
)

__all__ = [
    "SummarizationStrategy",
    "SummarizeStrategyType",
    "summarize_descriptions",
]
