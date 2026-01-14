from fastapi import APIRouter, Query
from app.database import donors_collection

from bson import ObjectId
from fastapi import HTTPException

router = APIRouter()

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


@router.put("/donors/{donor_id}")
def update_donor(donor_id: str, updated_data: dict):
    result = donors_collection.update_one(
        {"_id": ObjectId(donor_id)},
        {"$set": updated_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Donor not found")

    donor = donors_collection.find_one({"_id": ObjectId(donor_id)})
    donor["_id"] = str(donor["_id"])
@router.put("/donors/{donor_id}")
def update_donor(donor_id: str, updated_data: dict):
    result = donors_collection.update_one(
        {"_id": ObjectId(donor_id)},
        {"$set": updated_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Donor not found")

    return {"message": "Donor updated successfully"}
    return donor
@router.delete("/donors/{donor_id}")
def delete_donor(donor_id: str):
    result = donors_collection.delete_one({"_id": ObjectId(donor_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Donor not found")

    return {"message": "Donor deleted successfully"}

