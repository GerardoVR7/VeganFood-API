from fastapi import FastAPI
from routes.restaurants import restaurants
from routes.menus import menus
from routes.type_dish import type
from routes.dishes import r_dishes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [

    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(restaurants)
app.include_router(menus)
app.include_router(type)
app.include_router(r_dishes)

@app.get("/")
def home():
    return {"Home": "Creado"}

