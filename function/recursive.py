# 再帰関数 (recursive function): 関数内で自身の関数をcallする関数
# 階乗 (factorial): 3! = 3 × 2 × 1 = 6
# n! = n * (n-1) * (n-2)* ... * 1
# n! = n * (n-1)!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))


# challenge1 再帰バージョン
def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(6))


# challenge2 再帰じゃないバージョン
def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


print(fibonacci(6))

for i in range(40):
    print(i, fibonacci(i))