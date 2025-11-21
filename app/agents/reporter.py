from langgraph.graph import END, StateGraph

from app.llm import LLMProviderFactory
from app.prompts.research import reporter_prompt
from app.state import ReporterState


def report_node(state: ReporterState) -> dict[str, str]:
    topic = state["topic"]
    research_results = state["research_results"]
    analysis = state["analysis"]

    provider = LLMProviderFactory.get_default_provider()
    llm = provider.get_chat_model()

    if llm is None:
        return {
            "report": f"# Report: {topic}\n\n"
            "[Simulated report when LLM is not configured]\n\n"
            f"Research: {research_results[:100]}...\n\n"
            f"Analysis: {analysis[:100]}..."
        }

    prompt = reporter_prompt()
    chain = prompt | llm

    response = chain.invoke({
        "topic": topic,
        "research_results": research_results,
        "analysis": analysis,
    })
    return {"report": str(response.content)}


def create_reporter() -> StateGraph:
    workflow = StateGraph(ReporterState)
    workflow.add_node("report", report_node)
    workflow.set_entry_point("report")
    workflow.add_edge("report", END)

    return workflow.compile()


graph = create_reporter()
