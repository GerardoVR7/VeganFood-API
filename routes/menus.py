from fastapi import APIRouter, Response, HTTPException
from config.database import conn
from models.menu import menus as auxmenu
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.menu import Menus

menus = APIRouter()

@menus.get("/menus")
def get_all_menus():
    return conn.execute(auxmenu.select()).fetchall() 

@menus.get("/menus/{id}")
def get_restaurant(id : int):
    res = conn.execute(auxmenu.select().where(auxmenu.c.id == id)).first()
    print(res)
    if res == None:
        return HTTPException(status_code=404, detail="Item not found")

    return conn.execute(auxmenu.select().where(auxmenu.c.id== id)).first()

@menus.post("/menus/create")
def create_menu(n_menu : Menus):
    new_menu = {
        "id_restaurant": n_menu.id_restaurant,
        "name": n_menu.name
    }
    result = conn.execute(auxmenu.insert().values(new_menu))
    print(result.lastrowid)
    return conn.execute(auxmenu.select().where(auxmenu.c.id == result.lastrowid)).first()

@menus.delete("/menu/delete/{id}")
def delete_menu(id : int):
    res = conn.execute(auxmenu.delete().where(auxmenu.c.id == id))
    if res == None:
        return HTTPException(status_code=404, detail="Item not exist")

    return Response(status_code=HTTP_204_NO_CONTENT)


