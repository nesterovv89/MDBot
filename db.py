import aiosqlite
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Profile(Base):
    __tablename__ = 'profile'

    user_id = Column(String, primary_key=True)
    name = Column(String)
    surname = Column(String)

class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    name = Column(String)
    age = Column(String)
    method = Column(String)
    contact = Column(String)

async def createtables():
    async with aiosqlite.connect('bot.sqlite3') as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS profile (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                surname TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS request (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                name TEXT,
                age TEXT,
                method TEXT,
                contact TEXT
            )
        """)
        await db.commit()

async def profile(user_id, name, surname):
    engine = create_async_engine('sqlite+aiosqlite:///bot.sqlite3')
    async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        user = await session.get(Profile, user_id)
        if not user:
            user = Profile(user_id=user_id, name=name, surname=surname)
            session.add(user)
        await session.commit()

async def request(user_id, name, age, method, contact):
    engine = create_async_engine('sqlite+aiosqlite:///bot.sqlite3')
    async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        try:
            request = Request(user_id=user_id, name=name, age=age, method=method, contact=contact)
            session.add(request)
            await session.commit()
            return True
        except:
            return False

async def users():
    engine = create_async_engine('sqlite+aiosqlite:///bot.sqlite3')
    async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        result = await session.execute(select(Profile.user_id))
        users = result.scalars().all()
        return [user for user in users]


