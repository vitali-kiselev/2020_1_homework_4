'''
Мне нравится 👍
Создайте функцию, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

def likes(*arr: str) -> str:
    pass
Примеры:

likes() -> "no one likes this"
likes("Peter") -> "Peter likes this"
likes("Jacob", "Alex") -> "Jacob and Alex like this"
likes("Max", "John", "Mark") -> "Max, John and Mark like this"
likes("Alex", "Jacob", "Mark", "Max") -> "Alex, Jacob and 2 others like this"
Бонусные очки
Функция работает на нескольких языках и кодировках - язык ответа определяется по языку входного массива.
'''


class MyClass:

    def likes(self, var: str) -> str:
        if len(var) == 0:
            result = "no one likes this"
        if len(var) == 1:
            result = (var[0], 'likes this')
        if len(var) == 2:
            result = (f'{var[0]} and {var[1]} like this')
        if len(var) == 3:
            result = (f'{var[0]}, {var[1]} and {var[2]} like this')
        if len(var) > 3:
            result = (f'{var[0]}, {var[1]} and {len(var)-2} others like this')





        return result



if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input names: ')
    var = var.split(', ')

    result = MyClass().likes(var)

    print(result)
