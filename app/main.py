from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.research import router as research_router
from app.config import settings

app = FastAPI(
    title="LangGraph Agent Template",
    description="Multi-agent research assistant using LangGraph and LangChain",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research_router, prefix="/api", tags=["research"])


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "LangGraph Agent Template API",
        "docs": "/docs",
        "health": "/api/health",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True,
    )
