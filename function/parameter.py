def func(first, second, third="3"):
    print(f"first: {first}, second: {second}, third: {third}")


# argument(引数に渡す値) <-> parameter(引数)
func("1", "2", "3")
func("1", third="3", second="2")
func("1", "2")
func("1", "2", "33")


# キーワード引数は必ず位置引数の後に書く
# def func(first, second="2", third):
#     print(f"first: {first}, second: {second}, third: {third}")

# "2"はsecondに入るべきかthirdに入るべきかわからない
# func("1", "2")
