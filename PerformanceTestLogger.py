from typing import Dict, Any


class PerformanceTestLogger:
    @staticmethod
    def log_result(result: Dict[str, Any]):
        print(f"Status Code: {result['status_code']}")
        print(f"Response Time: {result['response_time']} seconds")
        print(f"Response Body: {result['body']}")
        print(f"Response Headers: {result['headers']}")
        print("=" * 50)
