import unittest
from coursepy.HW4.Tasks.Like import MyClass

class LikeTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_like(self):
        self.var = ['Valera', 'Kolya', 'Vova', 'Djeka', 'Stepan']
        self.assertEqual(MyClass().likes(self.var), f'{self.var[0]}, {self.var[1]} and {len(self.var)-2} others like this')
        self.assertEqual(MyClass().likes(['Valera']), f'{self.var[0]} likes this')
        self.assertEqual(MyClass().likes(['Valera', 'Kolya']), f'{self.var[0]} and {self.var[1]} like this')
        self.assertEqual(MyClass().likes(['Valera', 'Kolya', 'Vova']), f'{self.var[0]}, {self.var[1]} and {self.var[2]} like this')







if __name__ == '__main__':
    unittest.main()