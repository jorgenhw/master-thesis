from models import LlamaModel, DeepseekModel, OpenAIModel
from data import cuad_loader
from testing import NeedleInHaystack, MultiHopTest
from evaluation import Evaluator
from schemas import TestResult

def main():
    # Initialize models
    test_llm = LlamaModel('8B')
    context_aware_llm = OpenAIModel('gpt-4')
    
    # Load dataset
    contracts = cuad_loader.load_dataset()
    
    # Prepare tests
    niah_tester = NeedleInHaystack(context_aware_llm)
    multi_hop_tester = MultiHopTest(context_aware_llm)
    
    results = []
    
    for contract in contracts:
        # Test 1: Needle in Haystack
        modified_doc, needles = niah_tester.insert_needle(contract.text, "single")
        response = test_llm.generate("What is the most important clause in this document?", modified_doc)
        results.append(Evaluator.evaluate_niah(response, [needles]))
        
        # Test 2: Multi-hop tracing
        modified_doc, variables = multi_hop_tester.insert_variables(contract.text)
        response = test_llm.generate("What is the value of variable_3?", modified_doc)
        results.append(Evaluator.evaluate_multi_hop(response, variables))
    
    # Generate visualizations
    generate_accuracy_plots(results)

if __name__ == "__main__":
    main()