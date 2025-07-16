from fastapi import APIRouter
from src.api.v1.endpoints import predict, auth, arquivos

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(predict.router, prefix="/predict", tags=["predict"])
router.include_router(arquivos.router, prefix="/arquivos", tags=["arquivos"])