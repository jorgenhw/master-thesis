import random
from schemas import Needle

class NeedleInHaystack:
    def __init__(self, context_aware_llm):
        self.context_aware_llm = context_aware_llm
    
    def insert_needle(self, document: str, test_variant: str, num_needles: int = 1) -> tuple:
        if test_variant == "single":
            return self._insert_single_needle(document)
        elif test_variant == "multiple":
            return self._insert_multiple_needles(document, num_needles)
    
    def _insert_single_needle(self, document: str) -> tuple:
        # Generate context-aware needle using LLM
        prompt = f"Generate a relevant fact to insert into this legal document:\n{document[:1000]}..."
        needle = self.context_aware_llm.generate(prompt, "")
        
        # Insert at random position
        sections = document.split('\n\n')
        insert_pos = random.randint(0, len(sections)-1)
        sections.insert(insert_pos, needle)
        
        return '\n\n'.join(sections), Needle(
            text=needle,
            insertion_position=insert_pos,
            test_type="single_niah",
            metadata={"variant": "single"},
            expected_answer=needle
        )
    
    def _insert_multiple_needles(self, document: str, num_needles: int) -> tuple:
        # Similar logic with multiple needles and distractors
        # ... (implementation omitted for brevity)