# main.py
from typing import List

from application.use_cases import (
    ListBeersStockByIdsUseCase,
    ListOrdersUsecase,
    RetrieveOrderUsecase,
)
from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from infra.data.memory import MemoryBeersStockRepository, MemoryOrdersRepository
from infra.handlers.status_codes import get_error_status_code_from_exception

app = FastAPI(title="Antigua Cerveza API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For prod specify the frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Antigua Cerveza API is running"}


@app.get("/api/v1/beers-stock")
async def list_beers_stock(response: Response, ids: List[str] = Query([], alias="id")):
    try:
        repo = MemoryBeersStockRepository()
        use_case = ListBeersStockByIdsUseCase(beers_stock_repository=repo)

        beers_stock = use_case.execute(ids=ids)
        return beers_stock
    except Exception as e:
        status_response, detail = get_error_status_code_from_exception(e)
        response.status_code = status_response
        return detail


@app.get("/api/v1/orders")
async def list_orders(response: Response):
    try:
        orders_repo = MemoryOrdersRepository()
        beers_stock_repo = MemoryBeersStockRepository()
        use_case = ListOrdersUsecase(orders_repository=orders_repo, beers_stock_repository=beers_stock_repo)

        orders = use_case.execute()
        return orders
    except Exception as e:
        status_response, detail = get_error_status_code_from_exception(e)
        response.status_code = status_response
        return detail


@app.get("/api/v1/orders/{id}")
async def get_order(id: str, response: Response):
    try:
        orders_repo = MemoryOrdersRepository()
        beers_stock_repo = MemoryBeersStockRepository()
        use_case = RetrieveOrderUsecase(orders_repository=orders_repo, beers_stock_repository=beers_stock_repo)

        order = use_case.execute(id=id)
        return order
    except Exception as e:
        status_response, detail = get_error_status_code_from_exception(e)
        response.status_code = status_response
        return detail
