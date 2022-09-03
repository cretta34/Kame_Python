# position と truncateの有無に注意する

# mode='a' (append): ファイルの最後尾に内容を追加
# with open("writing_file.txt", mode='a') as f:
#     f.write("mode=a appends text")

# mode='r+': 読み書きどちらも可能。ファイルの一番最初に戻って上書き
# with open("writing_file.txt", mode='r+') as f:
#     f.write("You can write and read with r+ mode!!")
#     print(f.read())  # writeが終わったポジションからreadしている
#     # readが終わったポジションからwriteする
#     f.write("This should be the last sentence.")
#     # さらにwriteが終わったポジションからread
#     print(f.read())

# mode='w+': 読み書きどちらも可能。Truncateされることに注意
# with open("writing_file.txt", mode='w+') as f:
#     print(f.read())
#     f.write("You can write and read with w+ mode!!")
#     # このままreadしてもポジションがwrite後なので何も表示されない
#     # .seek(0)で一番最初にポジションを戻してからreadする
#     f.seek(0)
#     print(f.read())

# mode='a+': 読み書きどちらも可能で、ポジションは最後尾から始まり、truncateされない
with open("writing_file.txt", mode='a+') as f:
    print(f.read())
    f.write("\nYou add sentences to the last of the file content with a+ mode")
    f.seek(0)
    print(f.read())