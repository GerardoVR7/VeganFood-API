from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

restaurant = Table(
    "restaurant",
    meta,
    Column("idRestaurant", Integer, primary_key=True, autoincrement=True),
    Column("name",String(255),),
    Column("description", String(255))
)

meta.create_all(engine)