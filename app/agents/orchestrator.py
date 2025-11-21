from langgraph.graph import END, StateGraph

from app.agents.analyzer import create_analyzer
from app.agents.reporter import create_reporter
from app.agents.researcher import create_researcher
from app.state import OrchestratorState


def invoke_researcher(state: OrchestratorState) -> dict[str, str]:
    researcher = create_researcher()
    result = researcher.invoke({"topic": state["topic"]})
    return {"research_results": result["research_results"]}


def invoke_analyzer(state: OrchestratorState) -> dict[str, str]:
    analyzer = create_analyzer()
    result = analyzer.invoke({
        "topic": state["topic"],
        "research_results": state["research_results"],
    })
    return {"analysis": result["analysis"]}


def invoke_reporter(state: OrchestratorState) -> dict[str, str]:
    reporter = create_reporter()
    result = reporter.invoke({
        "topic": state["topic"],
        "research_results": state["research_results"],
        "analysis": state["analysis"],
    })
    return {"report": result["report"]}


def finalize_output(state: OrchestratorState) -> dict[str, str]:
    return {"final_output": state["report"]}


def create_orchestrator() -> StateGraph:
    workflow = StateGraph(OrchestratorState)

    workflow.add_node("researcher", invoke_researcher)
    workflow.add_node("analyzer", invoke_analyzer)
    workflow.add_node("reporter", invoke_reporter)
    workflow.add_node("finalize", finalize_output)

    workflow.set_entry_point("researcher")
    workflow.add_edge("researcher", "analyzer")
    workflow.add_edge("analyzer", "reporter")
    workflow.add_edge("reporter", "finalize")
    workflow.add_edge("finalize", END)

    return workflow.compile()


graph = create_orchestrator()
