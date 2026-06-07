from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

from services.prompt_service import build_evaluation_prompt
from services.llm_service import evaluate_with_llm
from utils.parse_evaluation import parse_evaluation_response
from utils.db import evaluation_collection

router = APIRouter()


class EvaluateRequest(BaseModel):
    code: str
    language: str
    company: str
    model: str | None = None


@router.post("/evaluate")
async def evaluate_code(payload: EvaluateRequest):
    prompt = build_evaluation_prompt(
        company=payload.company,
        language=payload.language,
        code=payload.code
    )

    llm_response = evaluate_with_llm(prompt, model=payload.model)
    parsed = parse_evaluation_response(llm_response)

    evaluation_doc = {
        "company": payload.company,
        "language": payload.language,
        "model": payload.model,
        "code": payload.code,
        "evaluation": parsed,
        "created_at": datetime.utcnow()
    }

    result = await evaluation_collection.insert_one(evaluation_doc)

    return {
        "success": True,
        "evaluation_id": str(result.inserted_id),
        "company": payload.company,
        "language": payload.language,
        "model": payload.model,
        "evaluation": parsed
    }