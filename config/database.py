from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:G7v3R2001@veganfooddb.ckn3utwh3nqz.us-east-1.rds.amazonaws.com:3307/pruebas")
#engine = create_engine("mysql+pymysql://gerardo:G7v3R2001@localhost:3306/pruebas")
meta = MetaData()

conn = engine.connect()