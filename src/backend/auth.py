from fastapi import FastAPI, Request
app = FastAPI()
@app.get("/audit")
def audit(): return {"log":"persistent","layer":"defensive"}
