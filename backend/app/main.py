import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.donors import router as donors_router
from app.routes.auth import router as auth_router

app = FastAPI()

# allow localhost during development; append `RENDER_URL` if set in the environment
origins = ["http://localhost:5173"]
render_url = os.getenv("RENDER_URL")
if render_url:
    origins.append(render_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(donors_router)

@app.get("/")
def health():
    return {"status": "Blood Donation API running"}
