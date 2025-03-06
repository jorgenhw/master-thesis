from typing import List, Dict
from schemas import Needle, TestResult

class Evaluator:
    @staticmethod
    def evaluate_niah(response: str, needles: List[Needle]) -> TestResult:
        results = {}
        position_accuracy = {}
        
        for needle in needles:
            exact_match = needle.text in response
            partial_match = any(keyword in response for keyword in needle.metadata.get('keywords', []))
            position_accuracy[needle.insertion_position] = exact_match or partial_match
        
        accuracy = sum(position_accuracy.values()) / len(position_accuracy)
        return TestResult(
            accuracy=accuracy,
            details={"position_accuracy": position_accuracy},
            position_accuracy=position_accuracy
        )

    @staticmethod
    def evaluate_multi_hop(response: str, expected_chain: List[str]) -> TestResult:
        # Implementation for multi-hop evaluation
        # ... (omitted for brevity)