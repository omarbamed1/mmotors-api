from fastapi import FastAPI

app = FastAPI(title="API M-Motors")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API backend de M-Motors !"}

@app.get("/health")
def health_check():
    return {"status": "OK", "infrastructure": "AWS ECS & PostgreSQL prêts"}
