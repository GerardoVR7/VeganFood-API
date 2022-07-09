from typing import Optional
from pydantic import BaseModel

class Type(BaseModel):
    id: Optional[int]
    type: str
