# Type annotation
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2


# pythonは動的型付け言語、実行するまでその変数の型はわからない <-> 静的型付け言語
one = 1
two = 2
one = 'hello'
print(add_nums('1', '2'))