from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
