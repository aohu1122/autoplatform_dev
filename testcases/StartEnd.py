import unittest

class SetUp_TearDown(unittest.TestCase):
    def SetUp(self):
        print("start test")

    def TearDown(self):
        print("end test")