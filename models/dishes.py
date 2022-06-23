from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

dishes = Table(
    "dishes",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_menu", Integer, ForeignKey("menu.id")),
    Column("id_type", Integer, ForeignKey("type_dish.id")),
    Column("name",String(255),),
)

meta.create_all(engine)