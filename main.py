import os
import json
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import errors

load_dotenv()
chave = os.getenv("GEMINI_API_KEY")
avaliacoes = [
    "A comida chegou quente e super rápido, adorei!",
    "O pedido veio errado e o entregador foi grosseiro",
    "Pizza ok, nada de especial",
]


client = genai.Client(api_key=chave)

def analisar(avaliacao):
    pedido = f"""Analise esta avaliação de um cliente de delivery.
Responda em JSON com duas chaves:
"sentimento": "positivo", "negativo" ou "neutro"
"resumo": uma frase curta

Avaliação: {avaliacao}"""
    
    for tentativa in range(3):
        try:
            resposta = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=pedido,
                config=types.GenerateContentConfig(response_mime_type="application/json"),
            )
            return json.loads(resposta.text)
        except errors.ServerError:
            print("Servidor ocupado, tentando de novo...")
            time.sleep(5)
    raise RuntimeError("O servidor continuou ocupado depois de 3 tentativas.")   

contagem = {"positivo": 0, "negativo": 0, "neutro": 0}
for avaliacao in avaliacoes:
    resultado = analisar(avaliacao)
    print(avaliacao)
    print("Sentimento:", resultado["sentimento"])
    print("Resumo:", resultado["resumo"])
    print()
    contagem[resultado["sentimento"]] += 1
print("Resumo geral:")
print("Positivas:", contagem["positivo"])
print("Negativas:", contagem["negativo"])
print("Neutras:", contagem["neutro"])