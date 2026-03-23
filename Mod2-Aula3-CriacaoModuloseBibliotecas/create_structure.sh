#!/bin/bash

# Verifica se um nome foi fornecido
if [ -z "$1" ]; then
    echo "Uso: $0 nome_da_estrutura"
    exit 1
fi

# Nome da estrutura
STRUCTURE_NAME=$1

# Cria a estrutura de diretórios e arquivos
mkdir -p $STRUCTURE_NAME/$STRUCTURE_NAME
touch $STRUCTURE_NAME/$STRUCTURE_NAME/__init__.py

# Adiciona o código da biblioteca no core.py
cat <<EOL > $STRUCTURE_NAME/$STRUCTURE_NAME/core.py
# $STRUCTURE_NAME/core.py

def hello_world():
    return "Hello, World!"
EOL

mkdir -p $STRUCTURE_NAME/tests

# Adiciona um teste basico no test_core.py
cat <<EOL > $STRUCTURE_NAME/tests/test_core.py
from curses import echo

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from $STRUCTURE_NAME.core import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"
EOL

# Cria o setup.py com a configuração do pacote
cat <<EOL > $STRUCTURE_NAME/setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="${STRUCTURE_NAME}-package",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    description="Uma biblioteca de exemplo chamada $STRUCTURE_NAME",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Seu Nome",
    author_email="",
    license="MIT",
    url='https://github;com/tadrianinet/${STRUCTURE_NAME}-package',
)
EOL

# Cria o README.md com uma descrição básica
cat <<EOL > $STRUCTURE_NAME/README.md
# $STRUCTURE_NAME

Este é um exemplo de biblioteca Python chamada $STRUCTURE_NAME. Ela contém uma função simples que retorna "Hello, World!".

## Instalação

\`\`\`sh
pip install ${STRUCTURE_NAME}-package
\`\`\`

## Usage

\`\`\`python
from $STRUCTURE_NAME import hello_world

print(hello_world())
\`\`\`
EOL

echo "Estrutura de diretórios e arquivos para $STRUCTURE_NAME criada com sucesso!"