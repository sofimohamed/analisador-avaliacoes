# Analisador de Avaliações com IA

Esse é um projeto feito em Python que utiliza a inteligência artificial do Google Gemini para analisar avaliações de clientes de delivery.

A ideia é fazer com que o programa consiga identificar se uma avaliação é positiva, negativa ou neutra. Além disso, ele gera um pequeno resumo de cada avaliação e, no final, mostra quantas avaliações existem em cada categoria.

## Como funciona

1. Primeiro, o programa recebe uma lista com avaliações de clientes.
2. Depois, envia cada avaliação para a IA do Gemini, pedindo para identificar o sentimento e criar um pequeno resumo.
3. A resposta da IA vem em formato JSON, que o Python transforma em dados para conseguir organizar e contar os resultados.
4. No final, o programa mostra a análise de cada avaliação e a quantidade total de avaliações positivas, negativas e neutras.

Também implementei um tratamento para quando a API apresenta erro 503. Nesse caso, o programa tenta fazer a solicitação novamente, até 3 vezes.

## Tecnologias utilizadas

- Python, para desenvolver o programa.
- Google Gemini, para fazer a análise das avaliações.
- `google-genai`, biblioteca utilizada para acessar a API.
- `python-dotenv`, para guardar a chave da API em um arquivo separado.
- Git e GitHub, para controlar as versões e armazenar o projeto.

## Como rodar

1. Instale as bibliotecas:

   ```
   python -m pip install -r requirements.txt
   ```

2. Crie um arquivo `.env` na pasta do projeto com a sua chave da API do Gemini:

   ```
   GEMINI_API_KEY=sua_chave_aqui
   ```

3. Rode o programa:

   ```
   python main.py
   ```

## O que aprendi

- Como usar uma API de inteligência artificial a partir do Python, enviando um pedido (prompt) e recebendo a resposta.
- Como escrever o prompt para que a IA responda em JSON e como transformar essa resposta em dados que o programa consegue contar.
- Como proteger a chave da API usando um arquivo `.env` e o `.gitignore`, para que ela nunca vá para o GitHub.
- Como usar um ambiente virtual (`.venv`) para isolar as bibliotecas do projeto.
- Como lidar com erros do servidor usando `try` e `except`, tentando de novo automaticamente.

## Próximos passos

- Ler as avaliações de um arquivo CSV, em vez de uma lista escrita no código.
- Testar com mais avaliações e comparar a classificação da IA com a de uma pessoa.
- Mostrar os resultados em um gráfico ou em uma planilha.