# プリント分はデフォルトで改行コードがついている
# print("hello\n", end="")
# print("world\n", end="")

# try:
#     f = open("pep8_introduction.txt")
#     for line in f:
#         print(line, end="")
#
# finally:
#     f.close()

# with statement
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")