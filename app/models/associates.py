from sqlalchemy import Table, Column, ForeignKey

from app.models.base import Base


position_pizza_assoc_table = Table(
    "position_pizza_assoc_table",
    Base.metadata,
    Column(
        "position_id",
        ForeignKey("positions.id"),
        primary_key=True,
    ),
    Column(
        "pizza_id",
        ForeignKey("pizzas.id"),
        primary_key=True,
    ),
)
