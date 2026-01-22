from contextlib import asynccontextmanager

from fastapi import FastAPI
from datebase import init_orm, close_orm


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Start")
    await init_orm()
    yield
    await close_orm()
    print("Finish")
    
    