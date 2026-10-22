from datetime import datetime
from typing import TYPE_CHECKING
from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime,func

if TYPE_CHECKING:
    from app.models.order_model import Orders

class LoyaltyCustomers(Base):

    __tablename__ = "loyalty_customers"

    customer_id : Mapped[int] = mapped_column(Integer, primary_key=True,index=True,autoincrement=True)
    mobile_number : Mapped[str] = mapped_column(String(20),unique=True,nullable=False)
    full_name : Mapped[str] = mapped_column(String(100),nullable=False)
    email : Mapped[str] = mapped_column(String(100),nullable=False)
    loyalty_points : Mapped[int] = mapped_column(Integer,nullable=False,default=0)
    registered_at : Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())

    orders : Mapped[list["Orders"]] = relationship("Orders", back_populates="customer",lazy="selectin")