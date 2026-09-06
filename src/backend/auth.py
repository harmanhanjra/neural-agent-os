from fastapi import FastAPI
app = FastAPI()
@app.get("/audit")
def audit(): return {"layer":"defensive","log":"persistent"}
