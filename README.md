[![python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)
[![spark](https://img.shields.io/badge/Spark-2.4.5-red)](https://spark.apache.org/)

# Repositório destinado a criação de pequenas soluções utilizando Pyspark

O objetivo desse repositório é disponibilizar algumas soluções simples, mas que facilitam o desenvolvimento de um código utilizando Python e Spark.


## Soluções já disponíveis 

- [X] Como adicionar um arquivo .py ao sparkcontext para disponibiliza-lo aos seus executores. Isso foi feito através da criação de uma classe para tratamento de textos.
- [X] Contém exemplos de UDF (função definida pelo usuário).
- [X] Presença de testes unitários.
- [ ] Como se conectar a um banco de dados.  


## Instalação

Ao executar os comandos abaixo, você irá configurar um ambiente virtual e instalar as dependências necessárias:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements-dev.txt
```

## Testes e cobertura

Para rodar os testes e vizualizar o relatório de cobertura, execute:

```bash
$ pytest -x --cov=nlp --cov-report=term-missing --cov-report=html:htmlcov
```

> Status do Projeto: Em desenvolvimento :construction:
