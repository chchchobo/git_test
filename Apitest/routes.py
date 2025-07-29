# routes.py
from fastapi import APIRouter
from schemas import ShipmentUpdate
from services.pcc import post_tracking_update

router = APIRouter()

@router.post("/update-status")
def update_status(payload: ShipmentUpdate):
    return post_tracking_update(payload.dict())
