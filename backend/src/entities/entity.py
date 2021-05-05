from configparser import ConfigParser
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONFIG = '/home/karatay/Repositories/weather/WebcamMaps/backend/webcam.backend.config'
config = ConfigParser()
config.read(CONFIG)

dbName = config['database']['name']
dbUrl = config['database']['url']
dbUser = config['database']['user']
dbPw = config['database']['pw']

engine = create_engine(f'postgresql://{dbUser}:{dbPw}@{dbUrl}/{dbName}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Entity():
		id = Column(Integer, primary_key = True)

		def __init__(self):
				pass
		
