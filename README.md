<div align="center">

<img src="https://raw.githubusercontent.com/ivnvxd/ivnvxd/master/img/h_gendiff.png" alt="logo" width="270" height="auto" />
<h1>Difference Generator</h1>

<p>
Calculate the difference between two files
</p>

[![Actions Status](https://github.com/venyxD/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/venyxD/python-project-50/actions)
![Lint and test check](https://github.com/venyxd/python-project-50/actions/workflows/lint-and-test.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/e72f2ffcdbb2ab78dea7/maintainability)](https://codeclimate.com/github/venyxD/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e72f2ffcdbb2ab78dea7/test_coverage)](https://codeclimate.com/github/venyxD/python-project-50/test_coverage)

<p>
<a href="#about">About</a> •
<a href="#installation">Installation</a> •
<a href="#usage">Usage</a> •
<a href="#demo">Demo</a> •
<a href="#additionally">Additionally</a> 
</p>
</div>

<details><summary style="font-size:larger;"><b>Table of Contents</b></summary>

* [About](#about)
  * [Features](#features)
  * [Built With](#built-with)
* [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Package](#package)
* [Usage](#usage)
* [Demo](#demo)
  * [Stylish format](#stylish-format)
  * [Plain format](#plain-format)
  * [JSON format](#json-format)
* [Additionally](#additionally)
  * [Dependencies](#dependencies)
  * [Dev Dependencies](#dev-dependencies)
  * [Makefile Commands](#makefile-commands)
  * [Project Tree](#project-tree)

</details>

## About

Difference Generator is a tool that determines the difference between two data structures. This is a popular task, for which there are many online services, such as http://www.jsondiff.com/.

Such a mechanism, for example, is used when outputting tests or when automatically tracking changes in configuration files.

Example:

```bash
gendiff --format plain filepath1.json filepath2.yml

Setting "common.setting4" was added with value: False
Setting "group1.baz" was updated. From 'bas' to 'bars'
Section "group2" was removed
```

### Features:

* [X] Supported file formats: JSON, YAML.
* [X] Output as plain text, structured text or JSON.
* [X] Can be used as CLI tool or external library.

### Built With

* Python
* Poetry
* PyYAML
* JSON
* Pytest
* flake8
* argparse

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.8.0+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

### Package

To use the package, you need to clone the repository to your computer. This is done using the ```git clone``` command. Clone the project:

```bash
>> git clone https://github.com/venyxD/python-project-50.git
```

Then you have to build the package and install it:

```bash
>> cd python-project-50
```

```bash
>> poetry build
>> python3 -m pip install --user dist/*.whl
```

---

## Usage

Difference Generator can be used as CLI tool or as an external library.

### As external library

```python
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2, file_format)
```

### As CLI tool

The general usage is (both absolute and relative paths to files are supported):

```bash
>> gendiff [-f file_format] file_path1 file_path2
```

Difference Generator provides help command as well:

```bash
>> gendiff --help

usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (default: 'stylish')
```

## Demo

### _Stylish format_

If no format option is provided, output will be provided in _stylish_ format.

The difference is based on how the files have changed relative to each other, the keys are rendered in alphabetical order.

The absence of a plus or minus indicates that the key is in both files, and its values coincide. In all other situations, the value of the key is either different, or the key is only in one file.

```bash
>> gendiff file_path1.json file_path2.json

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

#### :diamonds: Compare two flat JSON and/or YAML files: _stylish_ format

<a href="https://asciinema.org/a/540234" target="_blank"><img src="https://asciinema.org/a/540234.svg" width="300"/></a>

#### :diamonds: Compare two nested JSON and/or YAML files: _stylish_ format

<a href="https://asciinema.org/a/540237" target="_blank"><img src="https://asciinema.org/a/540237.svg" width="300"/></a>

### _Plain format_

_Plain_ format reflects the situation as if we had combined the second object with the first one.

* If the new value of the property is a complex value, ```[complex value]``` is provided.
* If the property is nested, then the entire path to the root is displayed, not just including the parent.

```bash
>> gendiff --format plain file_path1.json file_path2.json

Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```

#### :diamonds: Compare two flat JSON and/or YAML files: _plain_ format

<a href="https://asciinema.org/a/540238" target="_blank"><img src="https://asciinema.org/a/540238.svg" width="300"/></a>

#### :diamonds: Compare two nested JSON and/or YAML files: _plain_ format

<a href="https://asciinema.org/a/540239" target="_blank"><img src="https://asciinema.org/a/540239.svg" width="300"/></a>

### _JSON format_

In addition to an unstructured output (as a text), often an output in a structured format, such as JSON, is needed.

JSON (JavaScript Object Notation) is a standard text format for representing structured data based on JavaScript object syntax. It is usually used to transfer data in web applications (e.g. sending some data from the server to the client so that it can be displayed on a web page or vice versa).

```bash
>> gendiff --format json file_path1.json file_path2.json

{
    "follow": {
        "value": false,
        "type": "removed"
    },
    "host": {
        "value": "hexlet.io",
        "type": "unchanged"
    },
    "proxy": {
        "value": "123.234.53.22",
        "type": "removed"
    },
    "timeout": {
        "value": 50,
        "new value": 20,
        "type": "updated"
    },
    "verbose": {
        "value": true,
        "type": "added"
    }
}
```

#### :diamonds: Compare two flat JSON and/or YAML files: _JSON_ format

<a href="https://asciinema.org/a/Q06wRrClwU6BoZrzda5RMjJWX" target="_blank"><img src="https://asciinema.org/a/Q06wRrClwU6BoZrzda5RMjJWX.svg" width="300"/></a>

#### :diamonds: Compare two nested JSON and/or YAML files: _JSON_ format

<a href="https://asciinema.org/a/540241" target="_blank"><img src="https://asciinema.org/a/540241.svg" width="300"/></a>

---

## Additionally

### Dependencies

* python = "^3.10"
* PyYAML = "^6.0"

### Dev Dependencies

* flake8 = "^5.0.4"
* pytest = "^7.2.0"
* pytest-cov = "^4.0.0"

### Makefile Commands

<dl>
    <dt><code>make build</code></dt>
    <dd>Build the Poetry package.</dd>    
    <dt><code>make package-install</code></dt>
    <dd>Install the package in the user's environment.</dd>
    <dt><code>make package-reinstall</code></dt>
    <dd>Reinstall the package in the user's environment.</dd>
    <dt><code>make lint</code></dt>
    <dd>Check code with flake8 linter.</dd>
    <dt><code>make test</code></dt>
    <dd>Run tests.</dd>
    <dt><code>make check</code></dt>
    <dd>Validate structure of <code>pyproject.toml</code> file, check code with tests and linter.</dd>
</dl>

---

<a name="project-tree"></a>
<details><summary style="font-size:larger;"><b>Project Tree</b></summary>

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
│   │   ├── render.py
│   │   ├── render_json.py
│   │   ├── render_plain.py
│   │   └── render_stylish.py
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
    │   │   └── ...
    │   ├── result
    │   │   └── ...
    │   └── yaml
    │       └── ...
    ├── test_cli_parse.py
    └── test_gendiff.py
```

</details>

---

:octocat: This is the second training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@ivnvxd](https://github.com/ivnvxd) &nbsp;&middot;&nbsp;
> LinkedIn [@Andrey Ivanov](https://www.linkedin.com/in/abivanov/)
