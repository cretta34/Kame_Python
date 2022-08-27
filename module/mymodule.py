myvariable = "This is global variable"


def myfunc():
    print("This is my function!!")


def anotherfunc():
    print("This is another function!!")


if __name__ == "__main__":
    myfunc()
    anotherfunc()
    print(myvariable)
    print("This is mymodule!!")
    print(f"mymodule.__name__: {__name__}")