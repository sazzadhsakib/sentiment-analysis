from fastapi import FastAPI
from src.presentation.route import sentiment_analyzer_route
from fastapi.middleware.cors import CORSMiddleware

# Create an instance of the FastAPI application
app = FastAPI()

# Configure CORS settings to allow cross-origin requests
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router for the sentiment analyzer
app.include_router(sentiment_analyzer_route.router)
