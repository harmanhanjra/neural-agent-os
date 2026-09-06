from fastapi import FastAPI
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
app = FastAPI()
@app.get("/health")
def health(): return {"status":"defensive-active","score":82,"routing":"free"}
@app.get("/agent")
def agent(q="hello"): return {"agent":"agent","reply":"[offline/fallback] "+q,"usage":0}
@app.get("/docs")
def docs(): return {"endpoints":["/health","/agent","/docs"],"security":"defensive"}
