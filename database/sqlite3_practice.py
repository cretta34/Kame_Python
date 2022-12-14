import sqlite3

# .connectでconnectionオブジェクトを返す
con = sqlite3.connect("sample.db")

# connectionオブジェクトに.cursorでcursorオブジェクトを返す
cursor = con.cursor()

# pythonでは;は不要
# IF NOT EXISTSをつけることですでにその名前のテーブルがあってもエラーが出ない
create_user_table_query = """
CREATE TABLE IF NOT EXISTS User (
    UserId INTEGER PRIMARY KEY NOT NULL,
    Name TEXT DEFAULT 'anonymous',
    Email TEXT NOT NULL,
    Age INTEGER CHECK(Age > 0)    
)
"""
cursor.execute(create_user_table_query)

insert_user_query = """
INSERT INTO User VALUES (1, 'John', 'john@gmail.com', 30);
INSERT INTO User VALUES (2, 'Emily', 'emily@gmail.com', 20);
INSERT INTO User VALUES (3, 'Taro', 'taro@gmail.com', 25);
"""
cursor.executescript(insert_user_query)
# .commitでこのconnectionオブジェクトに関する今までのqueryをcommitする
# CREATE TABLEはオートコミットされるがINSERTはされないので.commitが必要
# terminalでの作業もオートコミットされる
con.commit()