from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        extra = "ignore"
        allow_mutations = False
