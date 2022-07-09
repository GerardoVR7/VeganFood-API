from fastapi.testclient import TestClient
import service.main as main
from starlette.status import HTTP_204_NO_CONTENT

client = TestClient(main.app)

new_data_restaurant = {
    "idRestaurant": 19,
    "name": "prueba3",
    "description": "esto es una prueba3"
}

data_in_restaurant = {
    "idRestaurant": 3,
    "name": "santa hierva",
    "description": "lugar bonito"
}


data_in_dishes = {
    "id": 3,
    "id_menu": 1,
    "id_type": 5,
    "name": "agua de limon",
    "principal_ingredient": "limon",
    "price": 20
}



def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Home": "Creado"}


def test_restaurants():
    response = client.get("/restaurants")
    assert response.status_code == 200


def test_create_restaurant():
    response = client.post("/restaurants/create", json=new_data_restaurant)
    assert response.status_code == 200
    assert response.json() == new_data_restaurant


def test_get_all_restaurants():
    response = client.get("/restaurants")
    assert response.status_code == 200
    assert data_in_restaurant in response.json()


def test_restaurant_update():
    response = client.put("/restaurants/update/15", json={
        "name": "prueba15",
        "description": "chingon"
    })
    assert response.status_code == 200
    assert response.json() == "ready update"


def test_delete_restaurant():
    response = client.delete("/restaurants/delete/16")
    assert response.status_code == HTTP_204_NO_CONTENT


def test_get_all_dishes():
    response = client.get("/dishes")
    assert response.status_code == 200
    assert data_in_dishes in response.json()


def test_dishes_update():
    response = client.put("/dishes/update/1", json={
            "id_menu": 1,
            "id_type": 1,
            "name": "carlota",
            "principal_ingredient": "limon",
            "price": 100
    })
    assert response.status_code == 200
    assert response.json() == "ready update"


def test_delete_dish():
    response = client.delete("/dishes/delete/2")
    assert response.status_code == HTTP_204_NO_CONTENT


def test_search_dish_for_types():
    response = client.get("/dishes/search_type/5")
    assert data_in_dishes in response.json()

def test_search_dish_by_principal_ingredient():
    response = client.get("/dishes/search_ingredient/limon")
    assert data_in_dishes in response.json()