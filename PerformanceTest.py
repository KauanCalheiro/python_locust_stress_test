from typing import List, Dict, Any
from PerformanceTestInterface import PerformanceTestInterface
from HttpRequestExecutor import HttpRequestExecutor
from PerformanceTestLogger import PerformanceTestLogger
import time
import aiohttp
import asyncio


class PerformanceTest(PerformanceTestInterface):
    def __init__(
        self,
        url: str,
        body: Dict[str, Any],
        headers: Dict[str, str],
        num_requests: int,
        duration: int,
        method: str = "POST",
        show_logs: bool = True,
    ):
        self.url = url
        self.body = body
        self.headers = headers
        self.num_requests = num_requests
        self.duration = duration
        self.method = method
        self.executor = HttpRequestExecutor(url, body, headers, method)
        self.logger = PerformanceTestLogger()
        self.show_logs = show_logs

    def execute_request(self) -> Dict[str, Any]:
        result = self.executor.execute()
        if self.show_logs:
            self.logger.log_result(result)
        return result

    async def execute_test(self) -> List[Dict[str, Any]]:

        async def fetch(session):
            async with session.request(
                self.method, self.url, json=self.body, headers=self.headers
            ) as response:
                result = await response.json()
                if self.show_logs:
                    self.logger.log_result(result)
                return result

        start_time = time.time()
        results = []

        async with aiohttp.ClientSession() as session:
            tasks = []
            while time.time() - start_time < self.duration:
                for _ in range(self.num_requests):
                    tasks.append(fetch(session))

            results = await asyncio.gather(*tasks)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Running time: {elapsed_time:.2f} seconds")

        return results
