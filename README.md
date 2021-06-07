# dirganize

Declutter you folders and get peace of mind.
A command-line tool to organize files into category directories.

[![Tests](https://github.com/aahnik/dirganize/actions/workflows/test.yml/badge.svg)](https://github.com/aahnik/dirganize/actions/workflows/test.yml)
[![Code Quality](https://github.com/aahnik/dirganize/actions/workflows/quality.yml/badge.svg)](https://github.com/aahnik/dirganize/actions/workflows/quality.yml)
[![codecov](https://codecov.io/gh/aahnik/dirganize/branch/main/graph/badge.svg?token=2SRYMBMAHH)](https://codecov.io/gh/aahnik/dirganize)

## Installation

```shell
pip install dirganize
```

## Usage

Dirganize has an ultra simple command-line interface.
Just move into the directory you want to organize, and run `dirganize`.

You can also specify which folder to organize by using the `path` option.

```shell
dirganize --path ~/Downloads
```

If no path is specified, dirganize works on the current directory.

## Configuration

By default `dirganize` determines the destination folder for a particular file by
guessing its type from its extension.
The
[`guess_type`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type)
function of python's inbuilt module
[`mimetypes`](https://docs.python.org/3/library/mimetypes.html)
is used for this purpose.

> ***NOTE*** Dotfiles are not affected by dirganize.

You can put a `.dirganize.yml` file ( inside the folder you want to dirganize )
to provide a custom configuration.

```yaml
# .dirganize.yml
# folder: [ext1,ext2, ...]
Animations: [gif]
Binaries: [bin,dat]
```

Basically you have the folder name,
mapped to the list of file types to put in that folder.

Dirganize will first try to determine the destination directory from the `.dirganize.yml`.
When the yaml configuration file is absent or
the folder for an encountered file type is not defined in the configuration,
`dirganize` will fallback to the default technique.
