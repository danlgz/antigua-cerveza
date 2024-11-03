# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/api/orders")
async def get_order():
    return MOCK_ORDERS
