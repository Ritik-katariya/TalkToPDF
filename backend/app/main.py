from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import question  # Adjust this import based on your directory structure

app = FastAPI()




# Include the router for ask endpoint
app.include_router(question.router, prefix="/api")



# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
from app.routers import upload
app.include_router(upload.router, prefix="/api")
