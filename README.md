# Pip Module
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/gadc1996/python-workspace)
[![Actions Status](https://github.com/gadc1996/python-workspace/workflows/Lint/badge.svg)](https://github.com/gadc1996/python-workspace/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python package index(pypi) ready template for module development

## Setting Up
### Prerequisites

Before you begin, make sure you have the following:

- [Docker](https://www.docker.com/) installed on your system.
- [Visual Studio Code](https://code.visualstudio.com/) installed.

## Installation
1. Clone repository
```
git clone https://github.com/gadc1996/pip-module.git
```

2. Copy env file
```
cp .env.example .env
```

3. Update workspace name in `.devcontainer/devcontainer.json`

## Secrets
Add the following secrets to the repository to use deployment to [pypi](https://pypi.org/) and [test-pypi](https://test.pypi.org/) respectively:

- PYPI_API_TOKEN 
- TEST_PYPI_API_TOKEN 