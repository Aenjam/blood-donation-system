from fastapi import FastAPI
from app.database import donors_collection
from app.routes.donors import router as donors_router


from pydantic import BaseModel
app = FastAPI()

app.include_router(donors_router)

@app.get("/")
def home():
    return {"message": "Blood Donation project started"}

@app.get("/test-db")
def test_db():
    users_collection.insert_one({"test": "connection"})
    return {"status": "MongoDB connected"}
@app.get("/donors")
def get_donors():
    donors = list(users_collection.find({}, {"_id": 0}))
    return donors


class Donor(BaseModel):
    name: str
    blood_group: str
    city: str
@app.post("/donors")
def add_donor(donor: Donor):
    users_collection.insert_one(donor.model_dump())
    return {"message": "Donor added successfully"}
@app.get("/donors")
def get_donors():
    donors = []
    for donor in users_collection.find():
        donor["_id"] = str(donor["_id"])
        donors.append(donor)
    return donors


