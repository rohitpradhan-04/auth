from pydantic import BaseModel, ConfigDict


class AddService(BaseModel):
    email: str
    name: str

    model_config = ConfigDict(from_attributes=True)
