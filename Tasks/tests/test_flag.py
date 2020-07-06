import unittest
from coursepy.HW4.Tasks.Flags import MyClass


class LikeTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_flag(self):
        self.var = '5'
        self.assertEquals(MyClass().flags(self.var), )



    def test_flags_error(self):
        self.var = '100'
        self.assertEquals(MyClass().flags(self.var), 'Error')




if __name__ == '__main__':
    unittest.main()