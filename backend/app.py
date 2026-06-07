from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.evaluate import router as evaluate_router
from routes.history import router as history_router

app = FastAPI(title="AI Interview Evaluator", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(evaluate_router)
app.include_router(history_router)

@app.get("/")
def home():
    return {"message": "AI Interview Evaluator API Running"}