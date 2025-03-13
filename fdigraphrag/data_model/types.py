# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Common types for the fdigraphrag knowledge model."""

from collections.abc import Callable

TextEmbedder = Callable[[str], list[float]]
