from typing import List, TypedDict

class GraphState(TypedDict):
    question: str
    generation: str
    web_search: str
    feedback: str 
    confidence_score: float
    documents: List[str]