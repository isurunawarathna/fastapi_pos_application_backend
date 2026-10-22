from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.exceptions.products_exception import DuplicateProductCode
from app.models import Product
from app.repository.products_repository import ProductRepository
from app.schemas import ProductCreate, ProductResponse


class ProductService:

    def __init__(self,repo: ProductRepository):
        self.repo = repo

    async def create_product(self,product_data: ProductCreate,session: AsyncSession) -> ProductResponse:

        existing_product = await self.repo.get_by_product_code(product_code=product_data.product_code,session=session)

        if existing_product:
            raise DuplicateProductCode("Duplicate product code")

        return await self.repo.create_product(product_data=product_data,session=session)

    async def get_all_products(self,session: AsyncSession,
                               name: Optional[str] = None,
                               min_price: Optional[int] = None,
                               max_price: Optional[int] = None,
                               category_id: Optional[int] = None) -> List[ProductResponse]:

        if min_price is not None and min_price < 0:
            raise ValueError("Minimum price cannot be negative.")

        if max_price is not None and max_price < 0:
            raise ValueError("Maximum price cannot be negative.")

        if min_price is not None and max_price is not None and min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        return await self.repo.get_all_products(session=session,name=name,min_price=min_price,max_price=max_price,category_id=category_id)