from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from common.models.service import Service
from common.serializer.serviceSerializer import AddService

from ..database import get_bd

route = APIRouter(prefix='/service')


@route.post('/add')
def add_service(request: AddService = Request, db: Session = Depends(get_bd)):
    service = Service(email=request.email, name=request.name)
    db.add(service)
    db.commit()
    db.refresh(service)
    return {'status': 'ok', 'message': 'New Service Add Successfully'}
