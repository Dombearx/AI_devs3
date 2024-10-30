from pydantic import BaseModel


class PoligonResponse(BaseModel):
    code: int
    message: str
