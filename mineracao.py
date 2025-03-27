import os
from dotenv import load_dotenv  # Adicionando dotenv para carregar as variáveis

import requests

# Carregar variáveis do arquivo .env
load_dotenv()  # Isso vai carregar as variáveis para o ambiente

# Agora você pode acessar a variável de ambiente
SHOPIFY_ACCESS_TOKEN = os.getenv("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")
SHOPIFY_STORE_URL = "https://enigmafemme.com/"
SHOPIFY_API_VERSION = "2023-01"

# URL da API para criar produtos
url = f"{SHOPIFY_STORE_URL}/admin/api/{SHOPIFY_API_VERSION}/products.json"

# Cabeçalhos com autenticação correta
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN  # Usando o token da variável de ambiente
}

# Dados de um produto de teste
data = {
    "product": {
        "title": "Legging Teste",
        "vendor": "Kaisan",
        "product_type": "Fitness",
        "variants": [{"price": "99.90"}]
    }
}

# Fazendo a requisição
response = requests.post(url, json=data, headers=headers)

# Verificando se funcionou
print(response.status_code, response.json())

