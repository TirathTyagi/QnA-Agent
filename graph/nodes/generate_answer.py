from typing import Dict, Any
from graph.state import GraphState
from graph.chains.answer_generator import answer_chain


def generate_answer(state: GraphState) -> Dict[str, Any]:
    print("--- Generating Answer ---")
    question = state["question"]
    documents = state["documents"]
    answer = answer_chain.invoke({"question": question, "documents": documents, "feedback": state.get("feedback", ""), "generation": state.get("generation", "")})
    return {"question": question, "generation": answer, "documents": documents}