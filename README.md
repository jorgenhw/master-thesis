# Long Context Accuracy Evaluation

This project aims to measure the long-context accuracy of various LLMs by inserting “needles” (ground truth signals) into long documents and then testing whether the models can accurately retrieve or reason about them. The tests include:

1. **Needle in a Haystack (NIAH)**: Single and multiple needles.
2. **Multi-Hop Tracing**: Chained variable tests across pages.
3. **Aggregation Tasks**: Combining information from various parts of the document.
4. **Advanced Q&A**: Retrieving golden paraphrases from a distracting context.

## Repository Structure
- **src/config.py**: Configuration settings (model names, API keys, file paths, etc.)
- **src/models/llm_runner.py**: Functions to call different LLMs.
- **src/tasks/schema.py**: Definitions of the data schema for needle insertion and task metadata.
- **src/tasks/test_insertion.py**: Code for inserting needles into documents in a context-aware manner.
- **src/tasks/test_retrieval.py**: Code for testing LLM retrieval and reasoning over the inserted needles.
- **src/tasks/metrics.py**: Functions to compute metrics and visualize results.
- **src/utils**: Utility functions for file handling and logging.
- **src/main.py**: Entry point that runs the entire pipeline.

## Getting Started
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
