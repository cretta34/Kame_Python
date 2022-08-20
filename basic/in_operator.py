# in演算子
fruits = ['apple', 'peach', 'grapes', 'banana']
print('apple' in fruits)
print('lemon' not in fruits)

print('h' in 'hello')

# challenge
favorite = input("好きなフルーツは何ですか？")

if favorite in fruits:
    fruits.remove(favorite)
    print("{}ですね、差し上げますよ".format(favorite))
else:
    fruits.append(favorite)
    print("{}ですね、仕入れました！".format(favorite))

print("今あるフルーツはこちらです。{}".format(fruits))
