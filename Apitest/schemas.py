# schemas.py
from pydantic import BaseModel

class ShipmentUpdate(BaseModel):
    dealerCode: str
    documentNumber: str
    documentStatus: str
    fulfillment: dict  # 추후 Dict[str, Any] 또는 custom 모델로 확장 가능
