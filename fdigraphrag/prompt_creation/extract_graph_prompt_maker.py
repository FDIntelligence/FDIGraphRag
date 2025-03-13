# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file explaining how to create a extract graph prompt"""

SUMMARIZE_PROMPT = """
You are a helpful assistant responsible for generating a comprehensive prompt file which will be used by GPT to extract a graph from data.
Given a list of possible entity types, the input text data and a sample extract claims prompt file.
Please use the sample extract graph prompt to create a new, comprehensive prompt of a similar style, incorporating the entity types you are given and some examples using samples you will take from the input text data.
Ensure the prompt emphasises that all relationships must be obtained.
Make sure it is written in third person, and include the entity names so we have the full context.
Ensure that you leave the CONTINUE_PROMPT and LOOP_PROMPT intact at the end of the prompt.

#######
-Data-
Entity Types: {entity_name}
Input Text: {input_text}
Sample Extract Graph Prompt: {extract_claims_prompt}
#######
Output:
"""
