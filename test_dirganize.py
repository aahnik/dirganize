#!/usr/bin/env python

# pylint: skip-file

import logging
import os
import shutil

import click
import pytest

from dirganize import cli


def create_files(folder, *files):
    cwd = os.getcwd()
    os.chdir(folder)

    for file in files:
        with open(file, "w"):
            pass

    os.chdir(cwd)


def test_dirganize():
    sb = "sandbox"

    try:
        shutil.rmtree(sb)
    except:
        pass
    os.makedirs(sb)

    files = [
        "a.mp4",
        "b.mp3",
        "c.png",
        "d.py",
        ".dotfile",
        "what",
        "e.gif",
        ".dirganize.yml",
    ]
    create_files(sb, *files)

    with open(os.path.join(sb, ".dirganize.yml"), "w") as file:
        file.write("Animations: [gif]")

    with pytest.raises(click.exceptions.Exit):
        cli.version_callback(value=True)

    cli.verbosity_callback(value=True)

    assert set(os.listdir(sb)) == set(files)

    cli.main(sb)  # cwd changes to sb

    assert set(os.listdir()) == set(
        [
            ".dirganize.yml",
            ".dotfile",
            "Images",
            "Others",
            "Videos",
            "Audios",
            "Texts",
            "Animations",
        ]
    )
    assert set(os.listdir("Others")) == set(["what"])
    assert set(os.listdir("Animations")) == set(["e.gif"])
    assert set(os.listdir("Audios")) == set(["b.mp3"])


if __name__ == "__main__":
    test_dirganize()
