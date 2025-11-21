# LangGraph Multi-Agent Template

A production-ready template for building multi-agent applications using LangGraph and LangChain.

## Features

- **Multi-agent orchestration** with LangGraph
- **Multiple LLM providers** (OpenAI, Anthropic, Google Gemini)
- **FastAPI** REST API with CORS
- **Type-safe** state management with TypedDict
- **Retry logic** with exponential backoff
- **Token counting** and cost estimation utilities
- **LangSmith integration** for observability
- **LangGraph Studio** support for visual debugging

## Quick Start

### 1. Install Dependencies

Using UV (recommended):

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
DEFAULT_LLM_PROVIDER=openai
OPENAI_API_KEY=your-key-here

# Optional: LangSmith for tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your-langsmith-key
```

### 3. Run the API

```bash
python -m app.main
```

API will be available at `http://localhost:8000`

## Usage

### API Endpoint

```bash
curl -X POST http://localhost:8000/api/research \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence"}'
```

### Python SDK

```python
from app.agents import create_orchestrator

orchestrator = create_orchestrator()
result = orchestrator.invoke({"topic": "quantum computing"})

print(result["final_output"])
```

## Project Structure

```
app/
├── agents/          # LangGraph agent definitions
├── api/             # FastAPI routes
├── llm/             # LLM provider abstraction
├── prompts/         # Prompt templates
├── state/           # State type definitions
└── utils/           # Utility functions

tests/               # Test suite
docs/                # Additional documentation
```

## Development

### Run Tests

```bash
pytest
```

### Code Quality

```bash
ruff check .         # Linting
ruff format .        # Formatting
mypy .               # Type checking
```

### LangGraph Studio

Open this project in [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio) for visual debugging.

## Customization

This template uses a **Research Assistant** as an example. To adapt for your use case:

1. **Define your state** in `app/state/types.py`
2. **Create custom prompts** in `app/prompts/`
3. **Build your agents** in `app/agents/`
4. **Update the orchestrator** to coordinate your agents
5. **Modify API routes** in `app/api/` to match your workflow

## Documentation

- [Streaming Responses](docs/STREAMING.md) - How to add SSE streaming

## License

MIT
