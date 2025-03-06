"""
This is the base class for all language models. It defines the methods that all language models should implement.
"""

from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str, context: str) -> str:
        pass

    @abstractmethod
    def get_context_window(self) -> int:
        pass