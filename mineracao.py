import requests

# 🔗 Dados da Loja Shopify
SHOPIFY_API_URL = "https://enigmafemme.myshopify.com/admin/api/2023-10/products.json"  # URL correta da API
SHOPIFY_API_KEY = "1be2adc3e9404ec827aea369428189bd"  # Chave de API
SHOPIFY_API_PASSWORD = "8bfdc1a58652f167b9341cddfadffaef"  # Chave Secreta da API (Senha de API)

# 🔍 Simulando a extração de produtos do site Kaisan
produtos_extraidos = [
    {"title": "Legging Fitness Preta", "price": "79.90", "sku": "KAISAN-001"},
    {"title": "Top Esportivo Branco", "price": "49.90", "sku": "KAISAN-002"}
]

# 🔍 Verificando se os produtos foram extraídos corretamente
print("🔍 Produtos extraídos do site Kaisan:")
for produto in produtos_extraidos:
    print(f"📦 Produto: {produto['title']} - Preço: R${produto['price']} - SKU: {produto['sku']}")

# 🚀 Enviando os produtos para o Shopify
for produto in produtos_extraidos:
    payload = {
        "product": {
            "title": produto["title"],
            "body_html": f"<strong>{produto['title']}</strong>",  # Descrição do produto
            "vendor": "Kaisan",
            "product_type": "Fitness",
            "variants": [
                {
                    "price": produto["price"], 
                    "sku": produto["sku"],
                    "inventory_management": "shopify",
                    "inventory_quantity": 100  # A quantidade inicial em estoque
                }
            ]
        }
    }
    
    headers = {
        "Content-Type": "application/json",
    }

    # Autenticando com Chave de API e Senha da API
    response = requests.post(SHOPIFY_API_URL, json=payload, auth=(SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD))

    # 📝 Verificando a resposta do Shopify
    print(f"📤 Enviando produto '{produto['title']}' para o Shopify...")
    print("📝 Resposta do Shopify:", response.status_code, response.text)

print("✅ Processo finalizado!")

