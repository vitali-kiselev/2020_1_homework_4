'''
Декоратор типов
Напишите декоратор, который проверял бы тип параметров функции следующим образом:
При вызове без аргументов осуществлял бы конвертацию параметров и возвращаемого значения в указанные типы:

@typed
def add(a: int, b: int) -> str:
    return a + b

add("3", 5) -> "8"
add(2.35, True) -> "3"
При вызове с параметром strict=True выбрасывал бы исключение при неправильной передаче параметров:

@typed(strict=True)
def convert_upper(msg: str) -> str:
    return msg.upper()

convert_upper('abc') -> 'ABC'
convert_upper(5) -> TypeError('`convert_upper` argument `msg` required to be a `str` instance')
Если типы параметров функции не указаны декоратор должен предполагать их тип как Any:

@typed
def acc(a, b, c):
    return a + b + c

acc('a', 'b', 'c') -> 'abc'
acc(5, 6, 7) -> 18
acc(0.1, 0.2, 0.4) -> 0.7000000000000001
'''


class MyClass:

    @typed
    def add(a: int, b: int) -> str:
        return a + b

    @typed(strict=True)
    def convert_upper(msg: str) -> str:
        return msg.upper()

    @typed
    def acc(a, b, c):
        return a + b + c

if __name__ == '__main__':
    # Here we can make console input and check how function works

    a =
    b =

    result = MyClass().add(a, b)
    print(result)

    msg =
    result = MyClass().convert_upper(msg)
    print(result)

    a =
    b =
    c =
    result = MyClass().convert_upper(a, b, c)
    print(result)
