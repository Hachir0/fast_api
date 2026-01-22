
from sqlalchemy import String, Integer, Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from datebase import Base
    

class Advert(Base):
    __tablename__ = "advert"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(Text)
    author: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    release_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    
    @property
    def dict(self): 
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author": self.author,
            "price": self.price,
            "release_date": self.release_date,
            "done": self.done
        }
        

ORM_OBJ = Advert
ORM_CLS = type[Advert]
    
    