from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CodeSentinel AI",
    description="API d'analyse de code et conformité DevSecOps",
    version="0.1.0"
)

class HealthCheck(BaseModel):
    status: str
    version: str

@app.get("/health", response_model=HealthCheck, tags=["System"])
def health_check():
    return HealthCheck(status="ok", version="0.1.0")