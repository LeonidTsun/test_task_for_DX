import httpx
import time
import asyncio
from typing import Optional
from .exceptions import AuthenticationError

class AuthManager:
    """
    Handles token-based authentication and automatic token refresh.
    """

    def __init__(self, refresh_token: str, auth_url: str):
        self.refresh_token = refresh_token
        self.auth_url = auth_url
        self._access_token: Optional[str] = None
        self._expires_at: Optional[float] = None
        self._lock = asyncio.Lock()

    async def get_token(self) -> str:
        """
        Returns a valid access token, refreshing it if necessary.
        """
        async with self._lock:
            if not self._access_token or time.time() >= self._expires_at:
                await self._refresh_token()
            return self._access_token

    async def _refresh_token(self):
        """
        Refreshes the access token using the refresh token.
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.auth_url}/token",
                json={"refresh_token": self.refresh_token}
            )

        if response.status_code != 200:
            raise AuthenticationError("Failed to refresh access token")

        data = response.json()
        self._access_token = data["access_token"]
        self._expires_at = time.time() + data["expires_in"] - 60
