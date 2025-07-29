# main.py
from fastapi import FastAPI
from routes import router

app = FastAPI()

# 라우터 등록
app.include_router(router)

# 테스트용 루트 엔드포인트
@app.get("/")
def root():
    return {"message": "PCC API Server is running"}
