from configparser import ConfigParser
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONFIG = '/home/karatay/Repositories/weather/WebcamMaps/backend/webcam.backend.config'
def getDbPw ():
		#Needs error handling incase file is missing or corrupted.
		config = ConfigParser()
		config.read(CONFIG)
		return config['database']['pw']

dbPw = getDbPw()
