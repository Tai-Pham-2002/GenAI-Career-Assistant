import os
from dotenv import load_dotenv
from typing import Dict
from workflow import create_workflow
from IPython.display import display, Image
from langchain_core.runnables.graph import MermaidDrawMethod
from langchain_ollama import ChatOllama


def run_user_query(query: str) -> Dict[str, str]:
    """Process a user query through the LangGraph workflow.

    Args:
        query (str): The user's query

    Returns:
        Dict[str, str]: A dictionary containing the query's category and response
    """
    app = create_workflow()
    results = app.invoke({"query": query})
    return {
        "category": results["category"],
        "response": results["response"]
    }

# Visualize the workflow graph
def visualize_workflow():
    app = create_workflow()
    display(
        Image(
            app.get_graph().draw_mermaid_png(
                draw_method=MermaidDrawMethod.API,
            )
        )
    )

if __name__ == "__main__":
    # Example test cases
    test_cases = [
        "I want to learn Langchain and langgraph.With usage and concept. Also give coding example implementation for both.Create tutorial for this.",
        "I am confused between Langgraph and CrewAI when to use what for Agent Creation?"
    ]
    
    for query in test_cases:
        print(f"\nRunning test case: {query}")
        result = run_user_query(query)
        print(result)
    
    # Visualize the workflow
    visualize_workflow()