from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from models.restaurant import restaurant
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.restaurant import Restaurant

restaurants = APIRouter()

key = Fernet.generate_key()
f = Fernet(key)
# example of use
# new_user["password"] = f.encrypt(user.password.encode("utf-8"))


@restaurants.get("/restaurants")
def get_all_restaruants():
    return conn.execute(restaurant.select()).fetchall()


@restaurants.post("/restaurants/create")
def create_restaurant(n_restaurant: Restaurant):
    new_restaurant = {
        "name": n_restaurant.name,
        "description": n_restaurant.description
    }
    result = conn.execute(restaurant.insert().values(new_restaurant))
    print(result.lastrowid)
    return conn.execute(restaurant.select().where(restaurant.c.idRestaurant == result.lastrowid)).first()


@restaurants.get("/restaurants/{id}")
def get_restaurant(id: int):
    res = conn.execute(restaurant.select().where(restaurant.c.idRestaurant == id)).first()
    print(res)
    if id < 0:
        return HTTPException(status_code=404, detail="Item negative ot exist")

    if res is None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(restaurant.select().where(restaurant.c.idRestaurant == id)).first()


@restaurants.delete("/restaurants/delete/{id}")
def delete_restaurant(id: int):
    res = conn.execute(restaurant.delete().where(restaurant.c.idRestaurant == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)


@restaurants.put("/restaurants/update/{id}")
def update_dish(id: str, u_restaurant: Restaurant):
    conn.execute(restaurant.update().values(
        name=u_restaurant.name,
        description=u_restaurant.description
    ).where(restaurant.c.idRestaurant == id)
                 )
    return "ready update"
