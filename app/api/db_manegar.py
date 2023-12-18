from sqlalchemy.ext.asyncio import AsyncSession

from app.api.model import UserIn
from app.api.db_model import users
# model for performance


async def add_user(per: UserIn, db: AsyncSession):
    return await db.execute(users.insert().values(**per.dict()))


async def get_all_user(db: AsyncSession):
    return (await db.execute(users.select())).all()

    #return await database.fetch_all(query=performances.select())


async def get_user(id: int, db: AsyncSession):
    return (await db.execute(users.select(users.c.id == id))).fetchone()


async def delete_user(id: int, db: AsyncSession):
    query = users.delete().where(users.c.id == id)
    return await db.execute(query)


async def update_user(id: int, per: users, db: AsyncSession):

    return await db.execute(users
                            .update()
                            .where(users.c.id == id)
                            .values(**per))