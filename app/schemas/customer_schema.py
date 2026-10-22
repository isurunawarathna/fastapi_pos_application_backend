from datetime import datetime
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr,field_validator


def validate_sl_phone(value: Optional[str]) -> Optional[str]:
    if value is None:
        return value
    value = value.strip()
    if not value:
        return None
    pattern = r"^(07\d{8}|\+947\d{8})$"
    if not re.fullmatch(pattern, value):
        raise ValueError("Phone number must be a valid Sri Lankan mobile number.")
    return value

class CustomerBase(BaseModel):
    customer_id: int = Field(...,description="Customer ID")
    mobile_number: str = Field(...,description="Mobile Number")
    full_name: str = Field(...,description="Full Name")
    email: EmailStr = Field(...,description="Email Address")
    loyalty_points: int = Field(...,description="Loyalty Points")

    @field_validator("mobile_number")
    @classmethod
    def mobile_number_validator(cls, v):
        return validate_sl_phone(v)

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerCreate):
    registered_at: datetime = Field(...,description="Registered At")

