import requests

# 🔹 Substitua pelos seus dados do Shopify
SHOPIFY_API_KEY = "S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"
SHOPIFY_STORE_URL = "https://enigmafemme.com/"
SHOPIFY_API_VERSION = "2023-01"

# 🔹 URL da API do Shopify para criar produtos
url = f"{SHOPIFY_STORE_URL}/admin/api/{SHOPIFY_API_VERSION}/products.json"

# 🔹 Cabeçalhos com a API Key
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_API_KEY  # Aqui vai a API Key!
}

# 🔹 Dados do produto de teste
data = {
    "product": {
        "title": "Legging Teste",
        "body_html": "<strong>Legging Confortável</strong>",
        "vendor": "Kaisan",
        "product_type": "Fitness",
        "variants": [{"price": "99.90"}]
    }
}

# 🔹 Enviando a requisição
response = requests.post(url, json=data, headers=headers)

# 🔹 Verificando o resultado
print(response.status_code, response.json())
