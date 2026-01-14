from fastapi import FastAPI
from app.routes.donors import router as donors_router
from app.auth import auth_router  # JWT login route

app = FastAPI(title="Blood Donation API")

# Routers
app.include_router(auth_router)
app.include_router(donors_router)

@app.get("/")
def home():
    return {"status": "Blood Donation API running"}

@app.get("/test-db")
def test_db():
    from app.database import donors_collection
    donors_collection.insert_one({"test": "connection"})
    return {"status": "MongoDB connected"}
