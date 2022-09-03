# for文でループで回す
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")

# .read()でファイルの中身の全てを一つのstringとして返す
# 大きなファイルに対してはやらないように注意
with open("pep8_introduction.txt") as f:
    print(f.read())

# .readline()で一行ずつstringで返す
with open("pep8_introduction.txt") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

# .readlines()で全ての行をlistで返す
# これも大きなファイルには使わないようにする
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)