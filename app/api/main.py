from fastapi import APIRouter, Header, HTTPException, Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.db_model import AsyncSessionLocal
from app.api.db_manegar import update_user
from app.api.model import UserIn,UserOut,UserUpdate
from app.api import db_manegar, db_model

app = FastAPI()




async def get_db():
    async_db = AsyncSessionLocal()
    try:
        yield async_db
    finally:
        await async_db.close()


@app.get('/', response_model=list[UserOut])
async def get_all_(db: AsyncSession = Depends(get_db)):
    return await db_manegar.get_all_user(db)


@app.get('/{id}', response_model=UserIn)
async def get_one(id: int, db: AsyncSession = Depends(get_db)):
    return await db_manegar.get_user(id, db)


@app.post('/')
async def add(performances: UserIn, db: AsyncSession = Depends(get_db)):
    db_per = db_model.Table()
    await db_manegar.add_user(performances, db)
    await db.commit()
    for instance in db:
        await db.refresh(instance)

    return {'message': "performance add"}


@app.put('/{id}', response_model=UserIn)
async def update(id: int, performances: UserUpdate, db: AsyncSession = Depends(get_db)):
    perfo = await db_manegar.get_user(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="Not found")

    await update_user(id, performances.dict(exclude_unset=True), db)

    await db.commit()
    return await db_manegar.get_user(id, db)




@app.delete('/{id}')
async def delete(id: int, db: AsyncSession = Depends(get_db)):
    perfo = await db_manegar.get_user(id, db)
    if not perfo:
        raise HTTPException(status_code=404, detail="not found")

    await db_manegar.delete_user(id, db)

    await db.commit()
    for instance in db:
        await db.refresh(instance)
    return {'message': 'performance delete'}