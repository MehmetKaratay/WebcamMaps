from sqlalchemy import Column, String, DateTime
from .entity import Entity, Base

class Webcam(Entity, Base):
		__tablename__ = 'webcams'

		name = Column(String)
		area = Column(String)
		country = Column(String)
		webpage = Column(String)
		imgurl = Column(String)
		updated = Column(DateTime)

		def __init__(self, name, area, country, webpage, imgurl):
				Entity.__init__(self)
				self.name = name
				self.area = area
				self.country = country
				self.webpage = webpage
				self.imgurl = imgurl
				
