# backend/app/database.py
import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI environment variable not set")

client = MongoClient(MONGO_URI)

db = client["blood_donation_db"]

users_collection = db["users"]
