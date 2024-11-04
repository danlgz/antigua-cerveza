# main.py
from typing import List

from application.use_cases import (
    ListBeersStockByIdsUseCase,
    ListOrdersUsecase,
    RetrieveOrderUsecase,
)
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from infra.data.memory import MemoryBeersStockRepository, MemoryOrdersRepository

app = FastAPI(title="Antigua Cerveza API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For prod specify the frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOCK_ORDERS = [
    {
        "created": "2024-09-10 12:00:00",
        "paid": False,
        "subtotal": 0,
        "taxes": 0,
        "discounts": 0,
        "items": [],
        "rounds": [
            {
                "created":  "2024-09-10 12:00:30",
                "items": [
                    {
                        "name": "Corona",
                        "quantity": 2
                    },
                    {
                        "name": "Club Colombia",
                        "quantity": 1
                    }
                ]
            }
        ]
    }
]

@app.get("/")
async def root():
    return {"message": "Antigua Cerveza API is running"}


@app.get("/api/v1/beers-stock")
async def list_beers_stock(ids: List[str] = Query([], alias="id")):
    repo = MemoryBeersStockRepository()
    use_case = ListBeersStockByIdsUseCase(beers_stock_repository=repo)

    beers_stock = use_case.execute(ids=ids)
    return beers_stock


@app.get("/api/v1/orders")
async def list_orders():
    orders_repo = MemoryOrdersRepository()
    beers_stock_repo = MemoryBeersStockRepository()
    use_case = ListOrdersUsecase(orders_repository=orders_repo, beers_stock_repository=beers_stock_repo)

    orders = use_case.execute()
    return orders


@app.get("/api/v1/orders/{id}")
async def get_order(id: str):
    orders_repo = MemoryOrdersRepository()
    beers_stock_repo = MemoryBeersStockRepository()
    use_case = RetrieveOrderUsecase(orders_repository=orders_repo, beers_stock_repository=beers_stock_repo)

    order = use_case.execute(id=id)
    return order
