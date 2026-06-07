import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "interview_ai")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "evaluations")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]
evaluation_collection = db[COLLECTION_NAME]