# services/pcc.py
import requests
import logging
from fastapi import HTTPException
from auth import get_access_token
from config import TRACKING_URL

def post_tracking_update(payload: dict):
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(TRACKING_URL, headers=headers, json=payload)
        if res.status_code == 204:
            return {"result": "✅ PCC 상태 업데이트 성공"}
        else:
            return {
                "result": "❌ 실패",
                "status_code": res.status_code,
                "body": res.text
            }
    except Exception as e:
        logging.error("PCC API 호출 실패: %s", e)
        raise HTTPException(status_code=500, detail="PCC 호출 실패")
