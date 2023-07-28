from pydantic import BaseModel, Field
from typing import Optional

class Libros(BaseModel):
    id: Optional [int] = None
    name: str = Field(default = "Nuevo libro", min_legth = 5, max_length = 15)
    price: float = Field(default = 0, ge = 0, le = 1000)
    stock: int = Field(default = 0, gt = 0)
        