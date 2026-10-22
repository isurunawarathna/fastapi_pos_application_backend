
from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String, Text, Boolean

from app.models import Product


class Category(Base):

    __tablename__ = 'categories'

    category_id : Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True,index=True)
    category_code : Mapped[str] = mapped_column(String(),unique=True,index=True,nullable=False)
    category_name : Mapped[str] = mapped_column(String,index=True,nullable=False)
    description : Mapped[str] = mapped_column(Text,nullable=False)
    active: Mapped[bool] = mapped_column(Boolean,nullable=False)

    products: Mapped[list["Product"]] = relationship("Product",back_populates="category",lazy="selectin")



