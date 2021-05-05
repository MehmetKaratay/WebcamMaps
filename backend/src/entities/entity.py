from configparser import ConfigParser
#from src.myConfigParser import config
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONFIG = '/home/karatay/Repositories/weather/WebcamMaps/backend/webcam.backend.config'
config = ConfigParser()
config.read(CONFIG)

dbName = config['database']['name']
dbUrl = config['database']['url']
dbUser = config['database']['user']
dbPw = config['database']['pw']

