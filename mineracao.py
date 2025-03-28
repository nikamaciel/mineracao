import requests

# 🔗 Dados da Loja Shopify
SHOPIFY_API_URL = "https://enigmafemme.myshopify.com/admin/api/2023-10/products.json"  # URL correta da API
SHOPIFY_ACCESS_TOKEN = "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"  # Seu token de acesso

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
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
        
    }
    
    print(f"📤 Enviando produto '{produto['title']}' para o Shopify...")

    response = requests.post("https://www.kaisan.com.br/produtos", auth=("fe651dbae88b7513021c8461fabff8c4Y", "617d6bfbf8622c9c731a8e6f7177724d"), json=data)


    # 📝 Verificando a resposta do Shopify
    print("📝 Resposta do Shopify:", response.status_code, response.text)

print("✅ Processo finalizado!")
