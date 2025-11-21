import pytest

from app.agents.orchestrator import create_orchestrator


def test_orchestrator_basic_flow() -> None:
    orchestrator = create_orchestrator()
    result = orchestrator.invoke({"topic": "artificial intelligence"})

    assert "topic" in result
    assert "research_results" in result
    assert "analysis" in result
    assert "report" in result
    assert "final_output" in result
    assert result["topic"] == "artificial intelligence"
    assert len(result["research_results"]) > 0
    assert len(result["final_output"]) > 0


def test_orchestrator_preserves_topic() -> None:
    orchestrator = create_orchestrator()
    test_topic = "machine learning frameworks"
    result = orchestrator.invoke({"topic": test_topic})

    assert result["topic"] == test_topic
