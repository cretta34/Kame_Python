# range(10)
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr = myrange(10)
# print(type(mr))
# print(mr)
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print(next(mr))
print("end of next()")
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))  # 9
# print(next(mr))

print("beginning of for loop")
for i in myrange(10):
    print(i)

print(next(mr))


# challenge
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


# print("======================")
print("=" * 30)
for i in even(10):
    print(i)

print("=" * 30)
# generatorはnext()で回せるし、iter()でイテレータである自分自身を返しているのでiteratorである
even_gen = even(10)
print(next(even_gen))
print(next(even_gen))
print(iter(even_gen))
print(id(even_gen))
print(id(iter(even_gen)))