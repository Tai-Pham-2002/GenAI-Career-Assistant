from langgraph.graph import StateGraph, END, START
from state import State
from categorization import categorize, handle_learning_resource, handle_interview_preparation
from handlers import job_search, handle_resume_making, ask_query_bot, tutorial_agent, interview_topics_questions, mock_interview
from routing import route_query, route_interview, route_learning

def create_workflow():
    workflow = StateGraph(State)
    
    # Add nodes
    workflow.add_node("categorize", categorize)
    workflow.add_node("handle_learning_resource", handle_learning_resource)
    workflow.add_node("handle_resume_making", handle_resume_making)
    workflow.add_node("handle_interview_preparation", handle_interview_preparation)
    workflow.add_node("job_search", job_search)
    workflow.add_node("mock_interview", mock_interview)
    workflow.add_node("interview_topics_questions", interview_topics_questions)
    workflow.add_node("tutorial_agent", tutorial_agent)
    workflow.add_node("ask_query_bot", ask_query_bot)
    
    # Define edges
    workflow.add_edge(START, "categorize")
    workflow.add_conditional_edges(
        "categorize",
        route_query,
        {
            "handle_learning_resource": "handle_learning_resource",
            "handle_resume_making": "handle_resume_making",
            "handle_interview_preparation": "handle_interview_preparation",
            "job_search": "job_search"
        }
    )
    workflow.add_conditional_edges(
        "handle_interview_preparation",
        route_interview,
        {
            "mock_interview": "mock_interview",
            "interview_topics_questions": "interview_topics_questions",
        }
    )
    workflow.add_conditional_edges(
        "handle_learning_resource",
        route_learning,
        {
            "tutorial_agent": "tutorial_agent",
            "ask_query_bot": "ask_query_bot",
        }
    )
    workflow.add_edge("handle_resume_making", END)
    workflow.add_edge("job_search", END)
    workflow.add_edge("interview_topics_questions", END)
    workflow.add_edge("mock_interview", END)
    workflow.add_edge("ask_query_bot", END)
    workflow.add_edge("tutorial_agent", END)
    
    # Set entry point
    workflow.set_entry_point("categorize")
    
    # Compile workflow
    return workflow.compile()