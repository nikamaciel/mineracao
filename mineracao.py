from dotenv import load_dotenv
import os

# Carregar as variáveis do ambiente
load_dotenv()

SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_STORE_URL = os.getenv("SHOPIFY_STORE_URL")

print(f"Conectando à loja: {SHOPIFY_STORE_URL}")

