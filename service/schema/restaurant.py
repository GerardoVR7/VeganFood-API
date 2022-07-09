from typing import Optional
from pydantic import BaseModel

class Restaurant(BaseModel):
    idRestaurant: Optional[int]
    name: str
    description: str

