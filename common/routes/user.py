from fastapi import APIRouter, HTTPException
from fastapi import Depends
from common.database import get_bd
from common.models.user import User
from common.serializer.userSerializer import (
    UserList as UserSerializer,
    UserRegistration,
    UserLogin,
    LoginResponse,
    ResetPasswordSchema
)
from sqlalchemy.orm import Session
from typing import List
from fastapi.requests import Request
from common.helpers.password import make_password, check_password
from common.helpers.jwt import JWT

route = APIRouter(prefix="/users", tags=["Users"])


@route.get("/list", response_model=List[UserSerializer])
def UserList(db: Session = Depends(get_bd)):
    return db.query(User).all()


@route.post("/register")
def Register(request: UserRegistration = Request, db: Session = Depends(get_bd)):
    user = User(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number,
        password=make_password(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"status": "ok", "message": "User created successfully"}


@route.post("/login")
def Login(request: UserLogin = Request, db: Session = Depends(get_bd)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="No User Found")
    checkPassword = check_password(request.password, user.password)
    if not checkPassword:
        raise HTTPException(status_code=401, detail="Incorrect Password")
    login_response = LoginResponse(
        id = user.id,
        email = user.email
    )
    token = JWT().EncodeJwt(login_response.model_dump())
    return {
        "token" : token,
        "token_type" : "bearer"
    }

@route.post('/password/reset')
def ResetPassword(request : ResetPasswordSchema = Request , db :Session = Depends(get_bd)):
    current_user = db.query(User).filter(User.id == 1).first()
    if not current_user:
        raise HTTPException(status_code=403,detail="no user found")
    current_user.password = make_password(request.new_password)
    db.commit()
    db.refresh(current_user)

    return {
        "status" : 200, "message" : "password reset successfully"
    }