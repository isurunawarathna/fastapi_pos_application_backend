from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product
from app.schemas import ProductCreate,ProductResponse
from typing import Optional
from sqlalchemy import select
from typing import List

class ProductRepository:

    @staticmethod
    async def create_product(product_data : ProductCreate, session: AsyncSession) -> ProductResponse:

        new_product = Product(**product_data.model_dump())

        try:
            session.add(new_product)
            await session.flush()
            await session.commit()
            await session.refresh(new_product)

            return ProductResponse.model_validate(new_product)

        except Exception:
            await session.rollback()
            raise

    @staticmethod
    async def get_by_product_code(product_code: str,session: AsyncSession) -> Optional[ProductResponse]:
        stmt = select(Product).where(Product.product_code == product_code)

        product = await session.execute(stmt)

        result = product.scalar_one_or_none()

        return ProductResponse.model_validate(result)

    @staticmethod
    async def get_all_products(session: AsyncSession,
                               name: Optional[str] = None,
                               min_price: Optional[int] = None,
                               max_price: Optional[int] = None,
                               category_id: Optional[int] = None) -> List[ProductResponse]:

        query = select(Product)

        if name is not None:
            query = query.where(Product.product_name.ilike(f"%{name}%"))

        if min_price is not None:
            query = query.where(Product.unit_price >= min_price)

        if max_price is not None:
            query = query.where(Product.unit_price <= max_price)

        if category_id is not None:
            query = query.where(Product.category_id == category_id)

        result = await session.execute(query)

        products = result.scalars().all()

        return [ProductResponse.model_validate(product) for product in products]



