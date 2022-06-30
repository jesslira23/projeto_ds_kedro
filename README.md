# projeto_ds_kedro

## Overview
Esse é um projeto com o objetivo de construir um pipeline de machine learning utilizando Kedro que permite a previsão dos resultados da eleição portuguesa de 2019. 

Segue o link para obtenção do [dataset](https://archive.ics.uci.edu/ml/datasets/Real-time+Election+Results%3A+Portugal+2019).
## Rules and guidelines
Dentro do projeto_ds_kedro há uma pasta escrita "project_ds_kedro", onde está todo o projeto da previsão eleitoral usando Kedro. Para isso, vá para a pasta:

```
cd project_ds_kedro
```

## How to install dependencies
Declare quaisquer dependências em `src/requirements.txt` para instalação do `pip`.
Instale todas, run:
```
pip install -r src/requirements.txt
```

## How to add raw_dataset?
Você deve seguir os seguintes passos para adicionar o conjunto de dados no projeto Kedro:
1) Ir no local onde está o [dataset](https://archive.ics.uci.edu/ml/datasets/Real-time+Election+Results%3A+Portugal+2019);
2) Baixar o arquivo "ElectionData.csv";
3) Salvar o arquivo na pasta data>01_raw.

## How to run your Kedro pipeline

Você pode executar seu projeto Kedro com:
```
kedro run
```
