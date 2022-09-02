class Person(object):

    num_legs = 2
    count = 0

    # constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking... with {Person.num_legs} legs!!")

    def run(self):
        print(f"{self.name} is running... with {Person.num_legs} legs!!")


john = Person("John", 28, 'male')
print(Person.count)
taro = Person("Taro", 18, 'male')
print(Person.count)
emma = Person("Emma", 40, 'female')
print(Person.count)

# インスタンス変数
# 「.」に続けてアクセス可能
print(john.name)
print(f"変更前: {john.age}")
john.age = 29
print(f"変更後: {john.age}")
print(taro.age)

# インスタンスメソッド
john.walk()
emma.walk()
john.run()

# クラス変数
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
print(Person.num_legs)
print("Person.num_legs = 3 を実行")
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
print(Person.num_legs)
# <インスタンス>.<クラス変数>で値を更新すると上書きしてしまうので注意
print("john.num_legs = 4 を実行")
john.num_legs = 4
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)
print(Person.num_legs)
