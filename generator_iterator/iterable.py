fruits = ['apple', 'lemon', 'peach']

# next()で回せないのでリストはiteratorではない
# print(next(fruits))

# iter()を試す
print(iter(fruits))
# iter(fruits)はnext()で回せた
fruits_iterator = iter(fruits)
# print(next(fruits_iterator))
# print(next(fruits_iterator))

print(iter(fruits_iterator))
# idを確認すると自分自身を返している
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))
# ということはiter(fruits)はiteratorであり、fruitsというリストはiterableである

print("=" * 30)
print(next(fruits_iterator))
print(fruits_iterator.__next__())