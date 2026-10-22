from fastapi import FastAPI
from app.core import create_tables
from app.api.routers.products_router import router as product_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="POS_APPLICATION_BACKEND",
    description="RESTful API for POS System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(product_router)

@app.on_event("startup")
async def on_startup():
    await create_tables()


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to FastAPI POS Backend",
        "version": "1.0.0"
    }


@app.get("/health", tags=["Health"])
async def health():
    return {
        "status": "ok",
        "message": "FastAPI POS Backend is running"
    }

