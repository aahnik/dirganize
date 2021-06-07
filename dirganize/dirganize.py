"""Dirganize your directory."""

import logging
import os
from mimetypes import guess_type
from typing import Dict

from rich.progress import track

from dirganize.conf import get_mapping


def _guess_type(filename) -> str:
    try:
        return guess_type(filename)[0].split("/")[0].title() + "s"  # type: ignore
    except:  # pylint: disable=bare-except
        return "Others"


def _get_dir(filename: str, mapping: Dict[str, str]) -> str:
    ext = filename.split(".")[-1]
    folder = mapping.get(ext)
    if not folder:
        folder = _guess_type(filename)
    return folder


def dirganize(path: str):
    """Organizes files into folders."""
    os.chdir(path)
    mapping = get_mapping()
    logging.info("Current working directory is %s", os.getcwd())
    all_files = [file for file in os.listdir() if os.path.isfile(file)]
    logging.info(all_files)

    for file in track(all_files, description="Moving files "):
        if file.startswith("."):
            continue
        new_parent_dir = _get_dir(file, mapping)
        if new_parent_dir:
            new_file = os.path.join(new_parent_dir, file)
            if not os.path.isdir(new_parent_dir):
                os.makedirs(new_parent_dir)
            os.rename(file, new_file)
            logging.info("%s renamed to %s", file, new_file)
    return os.walk(".")
