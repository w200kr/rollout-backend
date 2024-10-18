from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.entrypoints.routes.health_check import router as health_check_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(health_check_router)