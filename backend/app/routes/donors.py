from fastapi import APIRouter, Depends, HTTPException, Query
from app.database import donors_collection
from app.auth import verify_token
from bson import ObjectId

router = APIRouter()

@router.get("/donors", dependencies=[Depends(verify_token)])
def get_donors(
    blood_group: str | None = Query(None),
    city: str | None = Query(None)
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


@router.post("/donors", dependencies=[Depends(verify_token)])
def add_donor(donor: dict):
    result = donors_collection.insert_one(donor)
    return {
        "message": "Donor added",
        "id": str(result.inserted_id)
    }


@router.put("/donors/{donor_id}", dependencies=[Depends(verify_token)])
def update_donor(donor_id: str, updated_data: dict):
    result = donors_collection.update_one(
        {"_id": ObjectId(donor_id)},
        {"$set": updated_data}
    )
    if result.matched_count == 0:
        raise HTTPException(404, "Donor not found")

    return {"message": "Donor updated"}


@router.delete("/donors/{donor_id}", dependencies=[Depends(verify_token)])
def delete_donor(donor_id: str):
    result = donors_collection.delete_one({"_id": ObjectId(donor_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, "Donor not found")

    return {"message": "Donor deleted"}
