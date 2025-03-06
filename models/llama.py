from transformers import AutoTokenizer, AutoModelForCausalLM
from .base_model import BaseLLM

class LlamaModel(BaseLLM):
    def __init__(self, model_size: str):
        self.model_sizes = {
            '3B': 'meta-llama/Llama-3-3B',
            '8B': 'meta-llama/Llama-3-8B',
            '20B': 'meta-llama/Llama-3-20B'
        }
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_sizes[model_size])
        self.model = AutoModelForCausalLM.from_pretrained(self.model_sizes[model_size])
    
    def generate(self, prompt: str, context: str) -> str:
        full_input = f"Context: {context}\n\nQuestion: {prompt}\nAnswer:"
        inputs = self.tokenizer(full_input, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    def get_context_window(self) -> int:
        return 8192  # Adjust based on actual model