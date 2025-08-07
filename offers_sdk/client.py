import httpx
from typing import List
from .auth import AuthManager
from .models import Product, Offer
from .exceptions import *

class OffersClient:
    """
    Asynchronous client for interacting with the Offers API.
    """

    def __init__(self, base_url: str, refresh_token: str):
        self.base_url = base_url.rstrip("/")
        self.auth = AuthManager(refresh_token, f"{self.base_url}/auth")

    async def _get_headers(self) -> dict:
        token = await self.auth.get_token()
        return {"Authorization": f"Bearer {token}"}

    async def register_product(self, name: str, description: str) -> Product:
        """
        Registers a new product with the API.
        """
        url = f"{self.base_url}/products"
        headers = await self._get_headers()
        payload = {"name": name, "description": description}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            return Product(**response.json())
        elif response.status_code == 400:
            raise BadRequestError(response.text)
        else:
            raise OffersAPIError(f"Unexpected error: {response.status_code}")

    async def get_offers(self, product_id: str) -> List[Offer]:
        """
        Retrieves all offers for the given product ID.
        """
        url = f"{self.base_url}/products/{product_id}/offers"
        headers = await self._get_headers()

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        if response.status_code == 200:
            offers_data = response.json()
            return [Offer(**offer) for offer in offers_data]
        elif response.status_code == 404:
            raise NotFoundError(f"Product with ID {product_id} not found")
        else:
            raise OffersAPIError(f"Unexpected error: {response.status_code}")
