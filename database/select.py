import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

# cursorオブジェクトがiteratorになっている
# for row in cursor.execute("SELECT * FROM User"):
#     print(row)
cursor.execute("SELECT * FROM User")
# print(next(cursor))
# print(next(cursor))

# .fetchall(): 現在のcursor以下全てをタプルのリストで返す。全てのレコードがメモリにのるので注意
# print(cursor.fetchall())

# .fetchone(): 現在のcursorのレコードをタプルで返す
print(cursor.fetchone())
print(cursor.fetchone())