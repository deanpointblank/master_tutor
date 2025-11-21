from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agents import create_orchestrator

router = APIRouter()


class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=1, description="The topic to research")


class ResearchResponse(BaseModel):
    topic: str
    research_results: str
    analysis: str
    report: str
    final_output: str


@router.post("/research", response_model=ResearchResponse)
async def conduct_research(request: ResearchRequest) -> ResearchResponse:
    orchestrator = create_orchestrator()
    result = orchestrator.invoke({"topic": request.topic})

    return ResearchResponse(
        topic=result["topic"],
        research_results=result["research_results"],
        analysis=result["analysis"],
        report=result["report"],
        final_output=result["final_output"],
    )


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy"}
