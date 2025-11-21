from typing import TypedDict


class ResearcherState(TypedDict, total=False):
    topic: str
    research_results: str


class AnalyzerState(TypedDict, total=False):
    topic: str
    research_results: str
    analysis: str


class ReporterState(TypedDict, total=False):
    topic: str
    research_results: str
    analysis: str
    report: str


class OrchestratorState(TypedDict, total=False):
    topic: str
    research_results: str
    analysis: str
    report: str
    final_output: str
