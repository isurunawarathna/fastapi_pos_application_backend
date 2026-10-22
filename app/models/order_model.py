from datetime import datetime
from enum import StrEnum
from decimal import Decimal
from app.core import Base
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, func, Numeric, ForeignKey

if TYPE_CHECKING:
    from app.models.order_items_model import OrderItems
    from app.models.loyalty_customers_model import LoyaltyCustomers

class OrderStatus(StrEnum):
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"

class Orders(Base):
    __tablename__ = "orders"

    order_id : Mapped[int] = mapped_column(Integer,nullable=False,primary_key=True)
    customer_id : Mapped[int] = mapped_column(Integer,ForeignKey("loyalty_customers.customer_id"),nullable=False,index=True)
    order_date_time : Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False,server_default=func.now())
    order_status : Mapped[str] = mapped_column(String(50),default=OrderStatus.PROCESSING,nullable=False)
    total_amount : Mapped[Decimal] = mapped_column(Numeric(14,2),nullable=False)
    loyalty_points_earned : Mapped[int] = mapped_column(Integer,default=0,nullable=False)

    order: Mapped[list["OrderItems"]] = relationship("OrderItems", back_populates="order",lazy="selectin")
    customer: Mapped["LoyaltyCustomers"] = relationship("LoyaltyCustomers", back_populates="orders",lazy="selectin")
