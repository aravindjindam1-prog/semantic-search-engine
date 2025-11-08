from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Semantic Search Engine API")
app.include_router(router)

# Run: uvicorn backend.main:app --reload
