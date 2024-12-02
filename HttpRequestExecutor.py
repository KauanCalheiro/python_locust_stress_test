import requests
import time
from typing import Dict, Any


class HttpRequestExecutor:
    def __init__(
        self,
        url: str,
        body: Dict[str, Any],
        headers: Dict[str, str],
        method: str = "POST",
    ):
        self.url = url
        self.body = body
        self.headers = headers
        self.method = method

    def execute(self) -> Dict[str, Any]:
        start_time = time.time()

        if self.method.upper() == "POST":
            response = requests.post(self.url, json=self.body, headers=self.headers)

        elif self.method.upper() == "GET":
            response = requests.get(self.url, headers=self.headers)

        else:
            raise ValueError(f"Método {self.method} não suportado")

        end_time = time.time()

        response_time = end_time - start_time
        return {
            "response_time": response_time,
            "status_code": response.status_code,
            "body": response.json() if response.status_code == 200 else response.text,
            "headers": response.headers,
        }
