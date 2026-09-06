from fastapi import FastAPI
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import agent_core
app = FastAPI()
@app.get("/health")
def health(): return {"status":"defensive-active","score":82,"routing":"free"}
@app.get("/agent")
def agent(q: str="hello"): return agent_core.run(q)
