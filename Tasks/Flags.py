'''
Флаги
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов. Изображение одного флага
имеет размер 4×4 символов, между двумя соседними флагами также имеется пустой (из пробелов) столбец.
Разрешается вывести пустой столбец после последнего флага. Внутри каждого флага должен
быть записан его номер — число от 1 до n.

Пример
1.

3

+___ +___ +___
|1 / |2 / |3 /
|__\ |__\ |__\
|    |    |
2.

2

+___ +___
|1 / |2 /
|__\ |__\
|    |

'''


class MyClass:

    def flags(self, var):
        var = int(var)

        for i in range(var):
            print("+___", end=" ")
        print()
        for i in range(var):
            print("|%s /" % (i + 1), end=" ")
        print()
        for i in range(var):
            print("|__\\", end=" ")
        print()
        for i in range(var):
            print("|   ", end=" ")
        print()


        return



if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input Number of Flags: ')

    result = MyClass().flags(var)
