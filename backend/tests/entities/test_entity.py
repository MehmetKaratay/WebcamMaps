import unittest
from src.entities.entity import *

from configparser import ConfigParser

class Test_Entity(unittest.TestCase):

		# This test reads in the same password as entity.py so should always pass
		# but it there is a mistake in the code of EITHER src/ or test/ then it will
		# highlight a problem. I am trying to avoid hard-coding the pw into the repo.
		def test_dbConfig(self):
				def pwImport():
						config = ConfigParser()
						config.read(CONFIG)
						return config['database']['pw']

				want = pwImport()
				got = getDbPw()
				msgLen = 'Password has zero characters'
				msgEql = 'Password do not match'
				self.assertGreater(len(got), 0, msgLen)
				self.assertEqual(got, want, msgEql)

				
