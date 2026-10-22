from typing import TYPE_CHECKING
from decimal import Decimal
from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, Numeric, ForeignKey

if TYPE_CHECKING:
   from app.models.category_model import Category

class Product(Base):

    __tablename__ = "products"

    product_id : Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True,index=True,nullable=False)
    product_code : Mapped[str] = mapped_column(String(50),index=True,unique=True)
    product_name : Mapped[str] = mapped_column(String(50),index=True)
    unit_price : Mapped[Decimal] = mapped_column(Numeric(14,2),default=0,nullable=False)
    available_quantity : Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    active : Mapped[bool] = mapped_column(Boolean,nullable=False)
    category_id : Mapped[int] = mapped_column(Integer,ForeignKey("categories.category_id",ondelete="CASCADE"),nullable=False)

    category : Mapped["Category"] = relationship("Category", back_populates="products",lazy="selectin")