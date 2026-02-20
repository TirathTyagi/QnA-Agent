from typing import Dict, Any
from graph.state import GraphState
from graph.chains.answer_evaluator import eval_chain

def evaluate_answer(state: GraphState) -> Dict[str, Any]:
    print("--- Evaluating Answer ---")
    question = state["question"]
    generation = state["generation"]
    documents = state["documents"]
    cc = eval_chain.invoke({"question": question, "generation": generation, "documents": documents})
    return {"confidence_score": cc.confidence_score, "question": question, "generation": generation, "documents": documents, "feedback": cc.feedback}