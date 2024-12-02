from typing import List, Dict, Any


class PerformanceTestInterface:
    def execute_test(self) -> List[Dict[str, Any]]:
        raise NotImplementedError
