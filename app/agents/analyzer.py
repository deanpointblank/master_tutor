from langgraph.graph import END, StateGraph

from app.llm import LLMProviderFactory
from app.prompts.research import analyzer_prompt
from app.state import AnalyzerState


def analyze_node(state: AnalyzerState) -> dict[str, str]:
    topic = state["topic"]
    research_results = state["research_results"]

    provider = LLMProviderFactory.get_default_provider()
    llm = provider.get_chat_model()

    if llm is None:
        return {
            "analysis": f"[Simulated analysis for: {topic}] "
            "This is placeholder content when LLM is not configured."
        }

    prompt = analyzer_prompt()
    chain = prompt | llm

    response = chain.invoke({"topic": topic, "research_results": research_results})
    return {"analysis": str(response.content)}


def create_analyzer() -> StateGraph:
    workflow = StateGraph(AnalyzerState)
    workflow.add_node("analyze", analyze_node)
    workflow.set_entry_point("analyze")
    workflow.add_edge("analyze", END)

    return workflow.compile()


graph = create_analyzer()
