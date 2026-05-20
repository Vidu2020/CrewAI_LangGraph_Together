import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from graph.workflow import build_graph

if __name__ == "__main__":
    topic = input("Enter topic: ")

    graph = build_graph()
    result = graph.invoke({"topic": topic})

    print("\n✅ FINAL OUTPUT:\n")
    print(result)