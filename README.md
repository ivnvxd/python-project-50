# Difference Generator
[![Actions Status](https://github.com/venyxD/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/venyxD/python-project-50/actions)
![Lint and test check](https://github.com/venyxd/python-project-50/actions/workflows/lint-and-test.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/e72f2ffcdbb2ab78dea7/maintainability)](https://codeclimate.com/github/venyxD/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e72f2ffcdbb2ab78dea7/test_coverage)](https://codeclimate.com/github/venyxD/python-project-50/test_coverage)
## Description

## Installation

## Usage
<a href="https://asciinema.org/a/2WDBOZQzATpAFpJPL9EXtQJGo" target="_blank"><img src="https://asciinema.org/a/2WDBOZQzATpAFpJPL9EXtQJGo.svg"  width="200"/></a>

## Project tree
```bash
.
├── Makefile
├── README.md
├── coverage.xml
├── gendiff
│   ├── __init__.py
│   ├── constants.py
│   ├── diff.py
│   ├── file_handler.py
│   ├── find_diff.py
│   ├── formatters
│   │   ├── plain.py
│   │   ├── render.py
│   │   └── stylish.py
│   ├── parse_cli.py
│   └── scripts
│       ├── __init__.py
│       └── gendiff.py
├── poetry.lock
├── pyproject.toml
├── setup.cfg
└── tests
    ├── fixtures
    │   ├── json
    │   │   ├── file1_flat.json
    │   │   ├── file1_nested.json
    │   │   ├── file2_flat.json
    │   │   └── file2_nested.json
    │   ├── result
    │   │   ├── plain_flat.txt
    │   │   ├── plain_nested.txt
    │   │   ├── stylish_flat.txt
    │   │   └── stylish_nested.txt
    │   └── yaml
    │       ├── file1_flat.yaml
    │       ├── file1_flat.yml
    │       ├── file1_nested.yaml
    │       ├── file1_nested.yml
    │       ├── file2_flat.yaml
    │       ├── file2_flat.yml
    │       ├── file2_nested.yaml
    │       └── file2_nested.yml
    └── test_gendiff.py
```
---

This is the second training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)