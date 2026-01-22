from fastapi import FastAPI
from scheme import *
from fastapi import Depends
from datebase import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from lifespan import lifespan
import models, crud

app = FastAPI(
    title="Todo List",
    lifespan=lifespan
)


@app.post("/api/v1/advert", response_model=CreateAdvResponse)
async def create_advert(adv: CreateAdvRequest, session: AsyncSession = Depends(get_session)):
    adv_dict = adv.model_dump(exclude_unset=True)
    adv_obj = models.Advert(**adv_dict)
    await crud.add_item(session=session, item=adv_obj)
    return {"id": adv_obj.id}

@app.get("/api/v1/advert/{id}", response_model=GetAdvResponse)
async def get_advert(id: int, session: AsyncSession = Depends(get_session)):
    adv_obj = await crud.get_item_by_id(session=session, orm_cls=models.Advert, item_id=id)
    return adv_obj
    # return adv_obj.dict


@app.patch("/api/v1/advert/{id}", response_model=UpdateAdvResponse)
async def update_advert(id: int, adv_data: UpdateAdvRequest, session: AsyncSession = Depends(get_session)):
    adv_dict = adv_data.model_dump(exclude_unset=True)
    adv_db_obj =  await crud.get_item_by_id(item_id=id, orm_cls=models.Advert, session=session)
    
    for field, val in adv_dict.items():
        setattr(adv_db_obj, field, val)
    await crud.add_item(session=session, item=adv_db_obj)
    return {"status" : "success"}


@app.delete("/api/v1/advert/{id}", response_model=DeleteAdvResponse)
async def delete_advert(id: int, session: AsyncSession = Depends(get_session)):
    adv_db_obj = await crud.get_item_by_id(session=session, orm_cls=models.Advert, item_id=id)
    await crud.delete_item(session=session, item=adv_db_obj)
    return {"status" : "success"}


@app.get("/api/v1/advert", response_model=SearchAdvResponse)
async def search_advert(
    session: AsyncSession = Depends(get_session),
    title: str | None = None,
    description: str | None = None,
    author: str | None = None,
    price: int | None = None,
    release_date: datetime.datetime | None = None,
    ):
    adverts = await crud.search_adverts(
        session=session,
        title=title,
        description=description,
        author=author,
        price=price,
    )

    return { "result": [adv.dict for adv in adverts] }
    



