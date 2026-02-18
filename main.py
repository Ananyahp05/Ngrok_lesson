import logging
from fastapi import FastAPI
from routes import user_routes
from db import engine, Base

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create tables in the database
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")

app = FastAPI()

app.include_router(user_routes.router, prefix="/user", tags=["User"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Login/Signup Project"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
