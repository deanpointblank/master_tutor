# Streaming Responses

This template does not include streaming by default, but you can easily add it using Server-Sent Events (SSE).

## Implementation

### 1. Install SSE Support

Add to `pyproject.toml`:

```toml
dependencies = [
    # ... existing dependencies
    "sse-starlette>=2.0.0",
]
```

### 2. Create Streaming Endpoint

Add to `app/api/research.py`:

```python
from sse_starlette.sse import EventSourceResponse
from fastapi import Request

@router.post("/research/stream")
async def stream_research(request: Request, body: ResearchRequest):
    async def event_generator():
        orchestrator = create_orchestrator()

        for chunk in orchestrator.stream({"topic": body.topic}):
            if await request.is_disconnected():
                break

            node_name = list(chunk.keys())[0]
            node_output = chunk[node_name]

            yield {
                "event": "update",
                "data": json.dumps({
                    "node": node_name,
                    "output": node_output
                })
            }

        yield {
            "event": "complete",
            "data": json.dumps({"status": "done"})
        }

    return EventSourceResponse(event_generator())
```

### 3. Frontend Example

```javascript
const eventSource = new EventSource('/api/research/stream', {
  method: 'POST',
  body: JSON.stringify({ topic: 'AI' })
});

eventSource.addEventListener('update', (e) => {
  const data = JSON.parse(e.data);
  console.log(`${data.node}: ${data.output}`);
});

eventSource.addEventListener('complete', () => {
  eventSource.close();
});
```

## LangGraph Streaming Modes

LangGraph supports three streaming modes:

- `stream()` - Stream node outputs as they complete
- `stream_tokens()` - Stream LLM tokens in real-time (requires LLM support)
- `stream_events()` - Stream all graph events for detailed monitoring

See [LangGraph docs](https://langchain-ai.github.io/langgraph/how-tos/stream-tokens/) for details.
