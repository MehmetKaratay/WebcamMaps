import unittest
from src.entities.entity import Session, engine, Base
from src.entities.webcam import Webcam

class Test_WebcamEntitiy(unittest.TestCase):

		def test_EntryExists(self):
				Base.metadata.create_all(engine) #generate db schema
				session = Session() # start session
				webcams = session.query(Webcam).all()
				self.assertEqual(len(webcams),0,'There are entries and there shouldn\'t be')
