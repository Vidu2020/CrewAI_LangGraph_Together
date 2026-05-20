from fastapi import FastAPI
from graph.workflow import build_graph

app = FastAPI()
graph = build_graph()


@app.get("/")
def home():
    return {"message": "LLM Factory API Running ✅"}


@app.post("/generate")
def generate(topic: str):
    result = graph.invoke({"topic": topic})
    return {"result": result}