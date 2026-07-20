from pydantic import BaseModel, ConfigDict, model_validator


class UserList(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str

    model_config = ConfigDict(from_attributes=True)


class UserRegistration(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    id: int
    email: str


class ResetPasswordSchema(BaseModel):
    current_password: str
    new_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.current_password == self.new_password:
            raise ValueError(
                "New password cannot be the same as the current password."
            )
        return self
