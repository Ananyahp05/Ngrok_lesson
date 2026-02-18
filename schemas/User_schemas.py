from pydantic import BaseModel

# Schema for creating a user (input)
class UserCreate(BaseModel):
    email: str
    password: str

# Schema for returning user data (output) - mirrors SQLAlchemy User model
class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True  # Allows reading from SQLAlchemy model instances

# Keep UserSchema as alias for backward compatibility
UserSchema = UserCreate
