# Tech News

## Contexto

Esse projeto trata-se de consultas em notícias sobre tecnologia. As notícias podem ser obtidas através da raspagem do [blog da Trybe](https://blog.betrybe.com/).

## Técnologias usadas

Aplicação:

> Desenvolvido usando: Python, Pytest, MongoDB, web scraping

## Habilidades

Adquiri essas habilidades ao desenvolver esse projeto:

- Utilizar o terminal interativo do Python

- Escrever seus próprios módulos e importá-los em outros códigos

- Aplicar técnicas de raspagem de dados

- Extrair dados de conteúdo HTML

- Armazenar os dados obtidos em um banco de dado

## Instalando Dependências

- clone o projeto:

  ```bash
  git clone git@github.com:Andreyrvs/36-Tech-News.git
  ```

> Aplicação

1. **Entre no diretório**

   ```bash
   cd 36-Tech-News
   ```

2. **Criar o ambiente virtual**

   ```bash
   python3 -m venv .venv
   ```

3. **Ativar o ambiente virtual**

   ```bash
   source .venv/bin/activate
   ```

4. **Instalar as dependências no ambiente virtual**

   ```bash
   python3 -m pip install -r dev-requirements.txt
   ```

## Executando aplicação

- Para rodar o banco de dados:

   ```bash
   docker-compose up -d mongodb
   ```

- Para rodar a aplicação com menu interativo:

  ```bash
  tech-news-analyzer
  ```
