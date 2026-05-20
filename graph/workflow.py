from langgraph.graph import StateGraph
from crew.crew_setup import build_crew

# Shared state type
State = dict


def run_crew(state: State):
    topic = state["topic"]

    crew = build_crew(topic)
    result = crew.kickoff()

    return {"report": str(result)}


# ✅ Human in the loop
def human_review(state: State):
    print("\n--- GENERATED REPORT ---\n")
    print(state["report"])

    decision = input("\nApprove? (yes/no): ")

    return {"approved": decision.lower() == "yes"}


def build_graph():
    builder = StateGraph(State)

    builder.add_node("crew_execution", run_crew)
    builder.add_node("review", human_review)

    builder.set_entry_point("crew_execution")

    builder.add_edge("crew_execution", "review")

    builder.add_conditional_edges(
        "review",
        lambda s: "END" if s["approved"] else "crew_execution"
    )

    return builder.compile()