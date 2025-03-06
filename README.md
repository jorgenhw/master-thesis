project-root/
│
├── config/
│   ├── __init__.py
│   ├── paths.py          # File paths configuration
│   └── model_config.py   # Model parameters
│
├── data/
│   ├── __init__.py
│   ├── cuad_loader.py    # CUAD dataset handling
│   └── document_processor.py  # Document preprocessing
│
├── models/
│   ├── __init__.py
│   ├── base_model.py     # Base model interface
│   ├── llama.py          # LLaMA implementations
│   ├── deepseek.py       # Deepseek implementation
│   └── openai.py         # OpenAI implementations
│
├── testing/
│   ├── __init__.py
│   ├── needle_testing.py # NIAH test implementations
│   ├── multi_hop.py      # Multi-hop tracing tests
│   ├── aggregation.py    # Aggregation tests
│   └── qa_tests.py       # Q&A tasks
│
├── evaluation/
│   ├── __init__.py
│   ├── metrics.py        # Evaluation metrics
│   └── visualizations.py # Accuracy visualization
│
├── schemas.py            # Data schemas/Pydantic models
├── main.py               # Main execution script
└── requirements.txt
