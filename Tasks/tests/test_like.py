import unittest
from coursepy.HW4.Tasks.Like import MyClass

class LikeTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_like(self, var):
        self.assertEqual(MyClass().likes(f'{len(var)==1}'), f'{var[0]} likes this')
        self.assertEqual(MyClass().likes(f'{len(var) == 2}'), f'{var[0]} and {var[1]} like this')
        self.assertEqual(MyClass().likes(f'{len(var) == 3}'), f'{var[0]}, {var[1]} and {var[2]} like this')
        self.assertEqual(MyClass().likes(f'{len(var) > 3}'), f'{var[0]}, {var[1]} and {len(var)-2} others like this')












if __name__ == '__main__':
    unittest.main()