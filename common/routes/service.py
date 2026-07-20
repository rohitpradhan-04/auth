from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from ..database import get_bd
from common.models.service import Service
from common.serializer.serviceSerializer import AddService

route = APIRouter(prefix="/service")


@route.post("/add")
def addService(request: AddService = Request, db: Session = Depends(get_bd)):
    service = Service(email=request.email, name=request.name)
    db.add(service)
    db.commit()
    db.refresh(service)
    return {"status": "ok", "message": "New Service Add Successfully"}
