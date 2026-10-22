from pydantic import BaseModel, Field, ConfigDict

class ProductBase(BaseModel):
    product_code: str = Field(...,description="Product Code")
    product_name: str = Field(...,description="Product Name")
    unit_price: float = Field(...,description="Product Unit Price")
    available_quantity: int = Field(...,description="Available Quantity")
    active: bool = Field(...,description="Product Active")
    category_id: int = Field(...,description="Product Category Id")


class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductCreate):
    product_id : int = Field(...,description="Product Id")

    model_config = ConfigDict(from_attributes=True)



