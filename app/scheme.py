from pydantic import BaseModel
from typing import Literal
import datetime

class SuccessResponse(BaseModel):
    status: Literal["success"]
    
class IdResponse(BaseModel):
    id: int

class CreateAdvRequest(BaseModel):
    title: str
    description: str
    price: int 
    author: str
    release_date: datetime.datetime

class CreateAdvResponse(IdResponse):
    pass

class UpdateAdvResponse(SuccessResponse):
    pass

class UpdateAdvRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None
    author: str | None = None
    release_date: datetime.datetime | None = None
    done: bool | None = None

class GetAdvResponse(BaseModel):
    title: str
    description: str
    price: int 
    author: str
    release_date: datetime.datetime
    
    class Config:
        from_attributes = True
    
class DeleteAdvResponse(SuccessResponse):
    pass

class SearchAdvResponse(BaseModel):
    result: list[GetAdvResponse]
