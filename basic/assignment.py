# 変数へ代入: assignment
hello = "konnichiwa"
world = "sekai"
print(hello + world)

print("konnichiwa" + "sekai")  # ハードコーディング

# format
print("{} {}".format(hello, world))

name = "Emily"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))

# fstring
print(f"{hello} {world}")
print(f"Hey, {name}!! How are you doing?")
print(f"balance: {balance}")
