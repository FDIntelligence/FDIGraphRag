# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Parameterization settings for the default configuration."""

from pydantic import BaseModel, Field

from fdigraphrag.config.defaults import fdigraphrag_config_defaults


class EmbedGraphConfig(BaseModel):
    """The default configuration section for Node2Vec."""

    enabled: bool = Field(
        description="A flag indicating whether to enable node2vec.",
        default=fdigraphrag_config_defaults.embed_graph.enabled,
    )
    dimensions: int = Field(
        description="The node2vec vector dimensions.",
        default=fdigraphrag_config_defaults.embed_graph.dimensions,
    )
    num_walks: int = Field(
        description="The node2vec number of walks.",
        default=fdigraphrag_config_defaults.embed_graph.num_walks,
    )
    walk_length: int = Field(
        description="The node2vec walk length.",
        default=fdigraphrag_config_defaults.embed_graph.walk_length,
    )
    window_size: int = Field(
        description="The node2vec window size.",
        default=fdigraphrag_config_defaults.embed_graph.window_size,
    )
    iterations: int = Field(
        description="The node2vec iterations.",
        default=fdigraphrag_config_defaults.embed_graph.iterations,
    )
    random_seed: int = Field(
        description="The node2vec random seed.",
        default=fdigraphrag_config_defaults.embed_graph.random_seed,
    )
    use_lcc: bool = Field(
        description="Whether to use the largest connected component.",
        default=fdigraphrag_config_defaults.embed_graph.use_lcc,
    )
