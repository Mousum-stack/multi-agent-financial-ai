
from typing import TypedDict

from langgraph.graph import StateGraph, START, END


# 1. Define the state schema
class FinancialState(TypedDict):
    company: str
    revenue: float
    analysis: str


# 2. Define the first node
def research_node(state: FinancialState) -> dict:
    print("Research node is running...")

    company = state["company"]

    return {
        "analysis": f"Research completed for {company}."
    }


# 3. Define the second node
def analysis_node(state: FinancialState) -> dict:
    print("Analysis node is running...")

    research_result = state["analysis"]

    return {
        "analysis": research_result + " Basic analysis completed."
    }


# 4. Create the graph builder
graph_builder = StateGraph(FinancialState)


# 5. Register the nodes
graph_builder.add_node("research", research_node)
graph_builder.add_node("analysis", analysis_node)


# 6. Define the execution path
graph_builder.add_edge(START, "research")
graph_builder.add_edge("research", "analysis")
graph_builder.add_edge("analysis", END)


# 7. Compile the graph
graph = graph_builder.compile()


# 8. Create a reusable function
def run_financial_graph(company: str, revenue: float) -> dict:
    initial_state: FinancialState = {
        "company": company,
        "revenue": revenue,
        "analysis": ""
    }

    return graph.invoke(initial_state)


# 9. Execute demonstration only when this file is run directly
if __name__ == "__main__":

    initial_state: FinancialState = {
        "company": "NVIDIA",
        "revenue": 100.0,
        "analysis": ""
    }

    print("\n--- INVOKE ---")

    result = graph.invoke(initial_state)

    print("\nFinal result:")
    print(result)

    print("\n--- STREAM: NODE UPDATES ---")

    for update in graph.stream(initial_state, stream_mode="updates"):
        print(update)
