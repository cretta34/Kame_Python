class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print("This is normal method! from {}".format(self))

    @staticmethod
    def mystaticmethod():
        print("This is staticmethod!")

    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is classmethod and now the count is {cls.classmethod_count}")


c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
# インスタンスからでも呼べるが呼ぶ意味がない
# c.mystaticmethod()

MyClass.myclassmethod()
MyClass.myclassmethod()
# インスタンスからでも呼べるが呼ぶ意味がない
# c.mystaticmethod()

# 外からアクセスすることを想定していない関数(特にstaticmethodやclassmethodに多い)には
# 関数の前に_をつけるとその意思表示になる
