from dotenv import load_dotenv

from langgraph.graph import StateGraph, END

from graph.consts import EVALUATE_ANSWER, GENERATE_ANSWER, WEB_SEARCH
from graph.nodes import evaluate_answer, generate_answer, web_search
from graph.state import GraphState

load_dotenv()


def decide_to_continue(state: GraphState) -> bool:
    return state["confidence_score"] > 0.6

graph = StateGraph(GraphState)

graph.add_node(GENERATE_ANSWER, generate_answer)
graph.add_node(WEB_SEARCH, web_search)
graph.add_node(EVALUATE_ANSWER, evaluate_answer)

graph.set_entry_point(WEB_SEARCH)
graph.add_edge(WEB_SEARCH, GENERATE_ANSWER)
graph.add_edge(GENERATE_ANSWER, EVALUATE_ANSWER)
graph.add_conditional_edges(EVALUATE_ANSWER, decide_to_continue, {
    False: GENERATE_ANSWER,
    True: END
})

app = graph.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")