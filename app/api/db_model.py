from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY, ForeignKey, DateTime, TIMESTAMP)

from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+asyncpg://postgres:пдуи@localhost:5433/postgres'
engine = create_async_engine(DATABASE_URL)
metadata = MetaData()
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String(50)),
    Column('password', String(50)),
    Column('username', String(20)),
    Column('is_staff', Integer)
)


