from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from models.dishes import dishes
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.dishes import Dishes

r_dishes = APIRouter()

@r_dishes.get("/dishes")
def get_all_dishes():
    return conn.execute(dishes.select()).fetchall() 

@r_dishes.get("/dishes/{id}")
def get_dish(id : int):
    res = conn.execute(dishes.select().where(dishes.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(dishes.select().where(dishes.c.id== id)).first()

@r_dishes.post("/dishes/create")
def create_dish(new_dish : Dishes):
    new_dish = {
        "id_menu": new_dish.id_menu,
        "id_type": new_dish.id_type,
        "name": new_dish.name,
        "principal_ingredient": new_dish.principal_ingredient,
        "price": new_dish.price
    }
    result = conn.execute(dishes.insert().values(new_dish))
    print(result.lastrowid)
    return conn.execute(dishes.select().where(dishes.c.id == result.lastrowid)).first()

@r_dishes.delete("/dishes/delete/{id}")
def delete_dish(id : int):
    res = conn.execute(dishes.delete().where(dishes.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)

