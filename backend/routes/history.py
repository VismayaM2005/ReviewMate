from fastapi import APIRouter
from bson import ObjectId
from utils.db import evaluation_collection

router = APIRouter()


def serialize_doc(doc):
    return {
        "id": str(doc["_id"]),
        "company": doc.get("company"),
        "language": doc.get("language"),
        "model": doc.get("model"),
        "code": doc.get("code"),
        "evaluation": doc.get("evaluation"),
        "created_at": doc.get("created_at"),
    }


@router.get("/evaluations")
async def get_evaluations():
    cursor = evaluation_collection.find().sort("created_at", -1).limit(20)
    evaluations = []

    async for doc in cursor:
        evaluations.append(serialize_doc(doc))

    return {
        "success": True,
        "count": len(evaluations),
        "evaluations": evaluations
    }