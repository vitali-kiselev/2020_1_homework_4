'''
Из молекулы в атомы
Напишите функцию, которая, принимая как параметр строку - формулу молекулы, возвращала бы атомы из этой молекулы и их количество в виде Dict[str, int]:

def parse_molecule(molecule: str) -> dict:
    pass
Примеры:¶
H2O -> {H: 2, O: 1}
Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}
Замечания:
Скобки в формулах могут быть круглыми, квадратными и фигурными. Также они могут быть вложены друг в друга.
Индекс после скобки означает количество раз, которое повторяется каждый атом внутри скобок.
Индекс после скобки необязателен. Если его нет, значит содержимое скобок повторяется 1 раз.
'''


class MyClass:

    def parse(self, var: str) -> dict:
        result = {}

        return result



if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input formula: ')

    result = MyClass().parse(var)

    print(result)
