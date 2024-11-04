from datetime import datetime
from uuid import UUID

from domain.entities import BeerStock, Order, OrderRound, OrderRoundItem

date_format = "%Y-%m-%d %H:%M:%S"

BEERS_STOCK = [
    BeerStock(
        id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
        name="Sin Novia",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
        img="sin-novia",
    ),
    BeerStock(
        id=UUID("152b6a83-2069-4cd8-a67e-9eb70dfc444b"),
        name="Cucurucho",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
        img="cucurucho",
    ),
    BeerStock(
        id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
        name="Muy Noble",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
        img="muy-noble",
    ),
    BeerStock(
        id=UUID("ae32e245-b08d-434f-b4c8-aef38aef7e38"),
        name="Don Nadie",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
        img="don-nadie",
    )
]

ORDERS = [
    Order(
        id=UUID("96413732-3142-47c4-ad78-e99fec8a5492"),
        discounts=4.0,
        items=[],
        paid=True,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:30:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=2
                    )
                ]
            ),
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("152b6a83-2069-4cd8-a67e-9eb70dfc444b"),
                        quantity=1
                    ),
                    OrderRoundItem(
                        beer_stock_id=UUID("ae32e245-b08d-434f-b4c8-aef38aef7e38"),
                        quantity=3
                    ),
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=1
                    )
                ]
            )
        ],
        subtotal=0, # calculated from rounds
        taxes=10, # this should be calculated based on some tax country criteria, in this example will be hardcoded
        total=0, # calculaded from subtotal, taxes and discounts
    ),
    Order(
        id=UUID("f008d7af-3c95-46ef-b29f-72c9f6040d7e"),
        discounts=4.0,
        items=[],
        paid=False,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
                        quantity=3
                    ),
                ]
            )
        ],
        subtotal=0,
        taxes=4.0,
        total=0,
    ),
    Order(
        id=UUID("8fa3f53a-0319-4df7-bc3a-1968cb21b191"),
        discounts=4.0,
        items=[],
        paid=True,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=6
                    ),
                ]
            )
        ],
        subtotal=0,
        taxes=4.0,
        total=0,
    ),
    Order(
        id=UUID("0ce1d1f7-9f09-436a-955f-0760bb4e8a46"),
        discounts=4.0,
        items=[],
        paid=True,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:30:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=2
                    )
                ]
            ),
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("ae32e245-b08d-434f-b4c8-aef38aef7e38"),
                        quantity=3
                    ),
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=6
                    )
                ]
            )
        ],
        subtotal=0, # calculated from rounds
        taxes=10, # this should be calculated based on some tax country criteria, in this example will be hardcoded
        total=0, # calculaded from subtotal, taxes and discounts
    ),
    Order(
        id=UUID("335fa884-1cda-4a3d-b5b5-2381b6928de2"),
        discounts=0.0,
        items=[],
        paid=True,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("152b6a83-2069-4cd8-a67e-9eb70dfc444b"),
                        quantity=10
                    ),
                ]
            )
        ],
        subtotal=0,
        taxes=4.0,
        total=0,
    ),
]
