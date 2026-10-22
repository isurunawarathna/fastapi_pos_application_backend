from typing import List,Optional
from fastapi import APIRouter,Depends
from starlette import status
from starlette.exceptions import HTTPException
from app.core import get_db
from app.schemas import ProductCreate,ProductResponse
from app.service import ProductService
from app.repository import ProductRepository
from sqlalchemy.ext.asyncio import AsyncSession

service = ProductService(repo=ProductRepository())

router = APIRouter(prefix="/api/v1/products", tags=["Product"])

@router.post("/", response_model=ProductResponse ,status_code=status.HTTP_201_CREATED)
async def create_product(product_data: ProductCreate, session: AsyncSession = Depends(get_db) ) -> ProductResponse:
    try:
        product = await service.create_product(product_data=product_data,session=session)
        return product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get("/", response_model=List[ProductResponse],status_code=status.HTTP_200_OK)
async def get_all_products(session: AsyncSession =Depends(get_db) ,
                           name: Optional[str] = None,
                           min_price: Optional[int] = None,
                           max_price: Optional[int] = None,
                           category_id: Optional[int] = None) -> List[ProductResponse]:
    try:
        products = await service.get_all_products(session=session,min_price=min_price,max_price=max_price,name=name,category_id=category_id)
        return products

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))