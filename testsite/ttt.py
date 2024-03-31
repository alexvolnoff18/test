import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
DOMAIN = os.getenv("DOMAIN")

print(TOKEN)
print(DOMAIN)