from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
