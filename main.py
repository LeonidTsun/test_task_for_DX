import asyncio
import os
from dotenv import load_dotenv
from offers_sdk.client import OffersClient

# Load variables from .env file
load_dotenv()

async def main():
    base_url = os.getenv("BASE_URL")
    refresh_token = os.getenv("REFRESH_TOKEN")

    if not base_url or not refresh_token:
        raise ValueError("Missing BASE_URL or REFRESH_TOKEN in environment variables")

    client = OffersClient(base_url=base_url, refresh_token=refresh_token)

    product = await client.register_product("Test Product", "Example description")
    offers = await client.get_offers(str(product.id))

    for offer in offers:
        print(offer)

asyncio.run(main())
