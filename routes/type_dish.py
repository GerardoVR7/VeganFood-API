from fastapi import APIRouter, Response, HTTPException
from pymysql import NULL
from sqlalchemy import null
from config.database import conn
from models.type_dish import type_dish
from starlette.status import HTTP_204_NO_CONTENT
from cryptography.fernet import Fernet
from schema.type_dish import Type



