from pydantic import BaseModel


class Translit(BaseModel):
    id: int
    text: str
    text_translit: str

    class Config:
        orm_mode = True