import httpx
from typing import Any, Dict, Optional

class RestClient:
    """
    A simple REST client for making HTTP requests(GET and POST) to a specified base URL.
    """
    
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: int = 10):
        """
        Initializes the REST client with the specified base URL, API key, and timeout.
        Args:
            base_url (str): The base URL for the REST API.
            api_key (str, optional): The API key for authentication. Defaults to None.
            timeout (int, optional): The timeout for requests in seconds. Defaults to 10.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.client = httpx.AsyncClient(base_url=base_url, timeout=timeout)

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Sends a GET request to the specified endpoint with optional query parameters.
        Args:
            endpoint (str): The API endpoint to send the GET request to.
            params (dict, optional): Query parameters for the GET request. Defaults to None.
        Returns:
            dict: The JSON response from the API.
        Raises:
            httpx.HTTPError: If an error occurs during the request.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        response = await self.client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    
    async def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> httpx.Response:
        """
        Sends a POST request to the specified endpoint with optional JSON data.
        Args:
            endpoint (str): The API endpoint to send the POST request to.
            data (dict, optional): JSON data to include in the POST request. Defaults to None.
        Returns:
            dict: The JSON response from the API.
        Raises:
            httpx.HTTPError: If an error occurs during the request.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        response = await self.client.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    async def close(self) -> None:
        """
        Closes the underlying HTTP client session.
        """
        await self.client.aclose()