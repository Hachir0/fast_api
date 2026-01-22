from fastapi import HTTPException
from models import ORM_CLS, ORM_OBJ, Advert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


# async def add_item(session: AsyncSession, item: ORM_OBJ):
#     session.add(item)
#     try:
#         await session.commit()
        
#     except IntegrityError as err:
#         raise HTTPException(409, "Item Already exists!")

async def add_item(session: AsyncSession, item: ORM_OBJ):
    session.add(item)
    try:
        await session.commit()
        await session.refresh(item)
        return item
    except IntegrityError:
        await session.rollback()
        raise HTTPException(409, "Item already exists")
    
    
async def get_item_by_id(session: AsyncSession, orm_cls: ORM_CLS, item_id: int):
    orm_obj = await session.get(orm_cls, item_id)
    if orm_obj is None:
        raise HTTPException(404, "Item not found")
    return orm_obj


async def delete_item(session: AsyncSession, item: ORM_OBJ):
    await session.delete(item)
    await session.commit()

async def search_adverts(session: AsyncSession, title: str, description: str, author: str, price: int):
    stmt = select(Advert)
    
    if title:
        stmt = stmt.where(Advert.title.ilike(f"%{title}%"))

    if description:
        stmt = stmt.where(Advert.description.ilike(f"%{description}%"))

    if author:
        stmt = stmt.where(Advert.author.ilike(f"%{author}%"))

    if price is not None:
        stmt = stmt.where(Advert.price == price)

    result = await session.execute(stmt)
    return result.scalars().all()
