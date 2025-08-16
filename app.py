from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="D2R Traderie Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",                # vita local dev
        "https://ducst0vfguwb2.cloudfront.net/" # deployed frontend
    ],
    allow_credentials=False, # no user data
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
