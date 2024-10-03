from flask import render_template, Blueprint, request

from app.models.base import Session
from app.models.position import Position
from app.models.pizza import Pizza


pizza_blueprint = Blueprint("pizzas", __name__, url_prefix="/pizzas/")


@pizza_blueprint.get("/")
@pizza_blueprint.post("/")
def add_pizza():
    with Session() as session:
        if request.method == "POST":
            name = request.form.get("name")
            ingredients = request.form.get("ingredients")
            price = request.form.get("price")
            

            positions = request.form.getlist("positions")
            positions = session.query(Position).where(Position.id.in_(positions)).all()

            pizza = Pizza(name = name , price = price , ingredients = ingredients, positions=positions)
            session.add(pizza)
            session.commit()

        pizzas = session.query(Pizza).all()
        positions = session.query(Position).all()
        return render_template("pizza/management.html", pizzas=pizzas, positions=positions)


@pizza_blueprint.get("/<int:id>/")
def get_pizza(id):
    with Session() as session:
        pizza = session.query(Pizza).where(Pizza.id == id).first()
        return render_template("pizza/info.html", pizza=pizza, title="Інформація про піцци")
