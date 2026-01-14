from fastapi import APIRouter, Query, HTTPException
from app.database import donors_collection
from bson import ObjectId
from pydantic import BaseModel

class DonorCreate(BaseModel):
    name: str
    blood_group: str
    city: str
    phone: str

router = APIRouter()

# ---------------------------
# GET donors (with filters)
# ---------------------------
@router.get("/donors")
def get_donors(
    blood_group: str | None = Query(default=None),
    city: str | None = Query(default=None)
):
    filter_query = {}

    if blood_group:
        filter_query["blood_group"] = blood_group

    if city:
        filter_query["city"] = city

    donors = []
    for donor in donors_collection.find(filter_query):
        donor["_id"] = str(donor["_id"])
        donors.append(donor)

    return donors
@router.post("/donors")
def add_donor(donor: dict):
    if not donor:
        raise HTTPException(status_code=400, detail="Donor data is required")

    result = donors_collection.insert_one(donor)

    new_donor = donors_collection.find_one({"_id": result.inserted_id})
    new_donor["_id"] = str(new_donor["_id"])

    return new_donor


# ---------------------------
# UPDATE donor
# ---------------------------
@router.put("/donors/{donor_id}")
def update_donor(donor_id: str, updated_data: dict):
    try:
        object_id = ObjectId(donor_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid donor ID")

    result = donors_collection.update_one(
        {"_id": object_id},
        {"$set": updated_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Donor not found")

    donor = donors_collection.find_one({"_id": object_id})
    donor["_id"] = str(donor["_id"])

    return donor


# ---------------------------
# DELETE donor
# ---------------------------
@router.delete("/donors/{donor_id}")
def delete_donor(donor_id: str):
    try:
        object_id = ObjectId(donor_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid donor ID")

    result = donors_collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Donor not found")

    return {"message": "Donor deleted successfully"}



@router.post("/donors")
def add_donor(donor: DonorCreate):
    donor_dict = donor.dict()

    result = donors_collection.insert_one(donor_dict)

    return {
        "_id": str(result.inserted_id),
        **donor_dict
    }
