from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://services_api:3$Q66^2Uqp1N@veganfood.cbxabxrm8scs.us-west-1.rds.amazonaws.com:3306/vegan_food")

meta = MetaData()

conn = engine.connect()