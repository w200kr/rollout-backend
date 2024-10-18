from fastapi import APIRouter
from dependency_injector.wiring import inject

router = APIRouter()

@router.get("/health")
@inject
async def health_check() -> str:
    return "ok"