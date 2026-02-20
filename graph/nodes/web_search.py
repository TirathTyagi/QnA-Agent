from typing import Dict, Any
from graph.state import GraphState
from langchain_tavily import TavilySearch
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

web_search_tool = TavilySearch()

def web_search(state: GraphState) -> Dict[str, Any]:
    print("--- Performing web search ---")
    query = state["question"]
    docs = state.get("documents", [])

    search_results = web_search_tool.invoke({"query": query})
    final_results = "\n".join([result["content"] for result in search_results['results']])
    web_results = Document(page_content=final_results)

    if docs is not None:
        docs.append(web_results)
    else:
        docs = [web_results]

    return {"documents": docs, "question": query}