"""Configuration manager for dirganize."""

import logging
import os
from typing import Dict

import yaml

CONFIG_FILE = ".dirganize.yml"


def get_mapping() -> Dict[str, str]:
    """Parse the .dirganize.yml file and return mapping of extension -> folder."""
    structure = {"Documents": ["pdf", "docx"]}
    mapping = {}

    if os.path.isfile(CONFIG_FILE):
        with open(CONFIG_FILE) as stream:
            structure.update(yaml.safe_load(stream))

    logging.info(structure)

    for folder, extensions in structure.items():
        for ext in extensions:
            mapping[ext] = folder

    logging.info(mapping)

    return mapping
