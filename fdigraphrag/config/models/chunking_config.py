# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Parameterization settings for the default configuration."""

from pydantic import BaseModel, Field

from fdigraphrag.config.defaults import fdigraphrag_config_defaults
from fdigraphrag.config.enums import ChunkStrategyType


class ChunkingConfig(BaseModel):
    """Configuration section for chunking."""

    size: int = Field(
        description="The chunk size to use.",
        default=fdigraphrag_config_defaults.chunks.size,
    )
    overlap: int = Field(
        description="The chunk overlap to use.",
        default=fdigraphrag_config_defaults.chunks.overlap,
    )
    group_by_columns: list[str] = Field(
        description="The chunk by columns to use.",
        default=fdigraphrag_config_defaults.chunks.group_by_columns,
    )
    strategy: ChunkStrategyType = Field(
        description="The chunking strategy to use.",
        default=fdigraphrag_config_defaults.chunks.strategy,
    )
    encoding_model: str = Field(
        description="The encoding model to use.",
        default=fdigraphrag_config_defaults.chunks.encoding_model,
    )
    prepend_metadata: bool = Field(
        description="Prepend metadata into each chunk.",
        default=fdigraphrag_config_defaults.chunks.prepend_metadata,
    )
    chunk_size_includes_metadata: bool = Field(
        description="Count metadata in max tokens.",
        default=fdigraphrag_config_defaults.chunks.chunk_size_includes_metadata,
    )
