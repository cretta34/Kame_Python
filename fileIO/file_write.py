with open("writing_file.txt", mode='w') as f:
    # truncatedされる: byte=0に切り詰める つまりファイルの中身が消えて上書きされる
    f.write("You can write contents here\nuse 'backslash' to break the row")
    f.write("new write() doesn't break row")

    print("You can add a new row using 'file' parameter", file=f)
    print("new print() method breaks the row for you!!", file=f)
    # mode='w'はreadはできない
    print(f.read())
