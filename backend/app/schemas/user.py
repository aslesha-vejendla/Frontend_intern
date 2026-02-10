from pydantic import BaseModel, EmailStr

# What the client sends when registering or logging in
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# What the API sends back (never include password!)
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
