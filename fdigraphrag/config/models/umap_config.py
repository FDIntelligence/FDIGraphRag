# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Parameterization settings for the default configuration."""

from pydantic import BaseModel, Field

from fdigraphrag.config.defaults import fdigraphrag_config_defaults


class UmapConfig(BaseModel):
    """Configuration section for UMAP."""

    enabled: bool = Field(
        description="A flag indicating whether to enable UMAP.",
        default=fdigraphrag_config_defaults.umap.enabled,
    )
