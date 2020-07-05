import unittest
from coursepy.HW4.Tasks.Like import MyClass

class LikeTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_like(self):
        self.assertEqual(MyClass().likes('Alex'), 'Alex' 'likes this')










if __name__ == '__main__':
    unittest.main()