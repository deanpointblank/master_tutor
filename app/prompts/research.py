from langchain_core.prompts import ChatPromptTemplate


def researcher_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a research assistant that gathers comprehensive information on topics.",
            ),
            (
                "human",
                "Research the following topic and provide detailed findings: {topic}",
            ),
        ]
    )


def analyzer_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an analytical expert who examines research and provides insights.",
            ),
            (
                "human",
                "Analyze this research on {topic}:\n\n{research_results}\n\n"
                "Provide key insights, patterns, and conclusions.",
            ),
        ]
    )


def reporter_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a report writer who creates clear, well-structured summaries.",
            ),
            (
                "human",
                "Create a comprehensive report on {topic}.\n\n"
                "Research findings:\n{research_results}\n\n"
                "Analysis:\n{analysis}\n\n"
                "Format as a professional report with sections.",
            ),
        ]
    )
