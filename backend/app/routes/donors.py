from fastapi import APIRouter
from backend.app.database import users_collection

router = APIRouter(prefix="/donors", tags=["Donors"])

@router.post("/")
def create_donor(donor: dict):
    result = users_collection.insert_one(donor)
    return {"id": str(result.inserted_id)}

@router.get("/")
def list_donors():
    donors = []
    for d in users_collection.find():
        d["_id"] = str(d["_id"])
        donors.append(d)
    return donors
