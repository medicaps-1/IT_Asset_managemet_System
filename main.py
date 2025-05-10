from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, users, assets, asset_types, assignments

app = FastAPI(
    title="IT Asset Management API",
    description="A simple and effective IT Asset Management system",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(assets.router)
app.include_router(asset_types.router)
app.include_router(assignments.router)

@app.get("/")
def root():
    return {"message": "Welcome to the IT Asset Management API"}
