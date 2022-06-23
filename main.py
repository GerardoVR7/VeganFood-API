from fastapi import FastAPI
from routes.restaurants import restaurants
from routes.menus import menus
from routes.type_dish import type_dish
from routes.dishes import dishes

app = FastAPI()
app.include_router(restaurants)
# app.include_router(menus)

@app.get("/")
def home():
    return {"Home": "Creado"}

