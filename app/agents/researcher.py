from typing import cast

from langgraph.graph import END, StateGraph

from app.llm import LLMProviderFactory
from app.prompts.research import researcher_prompt
from app.state import ResearcherState


def research_node(state: ResearcherState) -> dict[str, str]:
    topic = state["topic"]

    provider = LLMProviderFactory.get_default_provider()
    llm = provider.get_chat_model()

    if llm is None:
        return {
            "research_results": f"[Simulated research results for: {topic}] "
            "This is placeholder content when LLM is not configured."
        }

    prompt = researcher_prompt()
    chain = prompt | llm

    response = chain.invoke({"topic": topic})
    return {"research_results": str(response.content)}


def create_researcher() -> StateGraph:
    workflow = StateGraph(ResearcherState)
    workflow.add_node("research", research_node)
    workflow.set_entry_point("research")
    workflow.add_edge("research", END)

    return workflow.compile()


graph = create_researcher()
