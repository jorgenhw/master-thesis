"""
This file is used to define the structure of the data that is being sent to the API and the data that is being received from the API
"""
from pydantic import BaseModel
from typing import List, Dict, Any

class Needle(BaseModel):
    text: str
    insertion_position: int
    test_type: str
    metadata: Dict[str, Any]
    expected_answer: str

class TestResult(BaseModel):
    model_name: str
    test_type: str
    accuracy: float
    details: Dict[str, Any]
    position_accuracy: Dict[int, bool]