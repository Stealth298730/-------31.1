from typing import List

from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models.base import Base
from app.models.position import Position
from app.models.associates import position_pizza_assoc_table

  
class Pizza(Base):
    __tablename__ = "pizzas"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    ingredients: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float())
    
    positions: Mapped[List[Position]] = relationship(secondary=position_pizza_assoc_table)
