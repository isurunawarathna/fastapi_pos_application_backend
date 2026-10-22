from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING
from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Boolean, DateTime, func, ForeignKey, Numeric

if TYPE_CHECKING:
    from app.models.order_model import Orders

class OrderItems(Base):

    __tablename__ = "order_items"

    order_item_id : Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False,index=True)
    order_id : Mapped[int] = mapped_column(Integer,ForeignKey("orders.order_id"),nullable=False,index=True)
    product_id : Mapped[int] = mapped_column(Integer,ForeignKey("products.product_id"),nullable=False,index=True)
    quantity : Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    unit_price : Mapped[float] = mapped_column(Numeric(14,2),nullable=False)
    subtotal : Mapped[float] = mapped_column(Numeric(14,2),nullable=False)

    order : Mapped["Orders"] = relationship("Orders", back_populates="order_items")