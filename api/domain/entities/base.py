from pydantic import BaseModel


class Base(BaseModel):
    class Config:
        extra = "ignore"
        allow_mutations = False

    def __getitem__(self, item):
        return getattr(self, item)
