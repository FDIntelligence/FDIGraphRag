#!/usr/bin/env python3
"""
This script updates the default entity types for ExtractGraphDefaults.
It reads a list of entity types from the command line and updates the
default in the configuration (fdigraphrag_config_defaults.extract_graph).

Usage:
    python update_entity_types.py Person Organization Location
"""

import argparse
from config.defaults import fdigraphrag_config_defaults

def update_default_entity_types(new_entity_types: list[str]):
    """
    Update the default entity types for ExtractGraphDefaults.

    Parameters:
        new_entity_types (list[str]): A list of strings representing the new entity types.
    """
    fdigraphrag_config_defaults.extract_graph.entity_types = new_entity_types
    print("Default entity types updated to:")
    for et in fdigraphrag_config_defaults.extract_graph.entity_types:
        print(" -", et)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update the default entity types in the configuration."
    )
    parser.add_argument(
        "entity_types",
        nargs="+",
        help="New entity types (space separated list) to replace the current default."
    )
    args = parser.parse_args()
    update_default_entity_types(args.entity_types)
