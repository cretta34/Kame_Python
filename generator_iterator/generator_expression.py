import sys

# リスト内包表記
square_list = [num * num for num in range(100)]
print(type(square_list))

print(square_list)

# generator
square_gen = (num * num for num in range(100))
print(type(square_gen))

print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

# リスト内包表記
even_square = [num * num for num in range(10) if num % 2 == 0]
print(even_square)

# generator
even_squares_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_squares_gen:
    print(num)
