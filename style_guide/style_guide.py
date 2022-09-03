# 変数の定義
# correct
x = 1
y = 1
# wrong
xxxx      = 1
y         = 1

x = 1   # 行の後ろに無駄なスペースを入れないようにする

# 関数の引数の「=」にはスペース不要
# correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
# wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

# operatorの周りにスペース1個,operatorにpriorityがある場合はスペースをなくす
# correct
x = x + 1
x += 1
x = x*2 - 1
a = x*x + y+y
c = (a+1) * (a-1)
# wrong
x=x+1
x +=1
x = x * 2 - 1
a = x * x + y + y
c = (a + 1) * (a - 1)

# カンマの後にはスペースを入れる
# correct
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)
# wrong
range(1,11)
a = [1,2,3,4]
b = (1,2,3,4)

# カンマの後に閉じカッコが来る場合はスペースは不要
# correct
foo = (0,)
# wrong
foo = (0, )

# 要素を並べる時にカンマで終わることができる
# Gitなどのバージョン管理でその行を編集しなくて住むので便利
# ただし、閉じカッコは別の行にしておくこと(結局その行を編集してしまうことになるため)
# correct
FILES = [
    'setup.cfg',
    'tox.ini',
    'tox.ini',
    'tox.ini',
]
# wrong
FILES = ['setup.cfg', 'tox.ini',]

# 行の折り返し
# 引数の頭を揃える
# correct
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
# wrong
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# 関数の引数の場合はスペース8個あける。4個だと処理内容と同じインデントになって見づらい
# correct
def long_function_name(
        var_one, var_two,
        var_three, var_four):
    print(var_one)
# wrong
def long_function_name(
    var_one, var_two,
    var_three, var_four):
    print(var_one)

# '\'で区切って改行する
print("このように表示する文章が長かったりする場合は\
バックスラッシュで区切ると改行できます")

# 演算子を含む改行の場合は演算子が並ぶように改行する
# correct
a = 10000000000000000000 \
    + 100000000000000 \
    + 10000000000000000000000000 \
    + 1000000
# wrong
a = 10000000000000000000 +\
    100000000000000 +\
    10000000000000000000000000 +\
    1000000

# 関数間は2行空ける
def func():
    pass


def func2():
    pass


# classのメソッド間は1行空ける
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

# importStyle
# import文は一番上に書く

# import文は別々に書く
# correct
import os
import sys
# wrong
import os, sys

# fromをつけるときは1行にまとめてもok
from subprocess import Popen, PIPE

# 書く順番
# 1. Standard library (time, sys)
# 2. Third party (numpy, pandas)
# 3. Our library
# 4. Local library
# それぞれ1行空ける (abc順)

# なるべくabsolute importを心がける
import mypkg.sibling
from mypkg. import sibling
from mypks.sibling import example

# あまりに長くなりすぎるようなら相対インポートにする
from package.subpackage1.subpackage2.subpackage3.module4 import function

# コメント
# ・コメントは常に最新にする。コメントとコードの中身が異なるなら、コメントはないほうがまし。
# ・なるべく英語で書く。絶対に日本語がわからない人が読まないなら日本語でもok
# ・書くときは文章で書くのが好ましい。
# ・#の後には半角スペースを入れる。
# ・インラインコメントはコードのあとに半角スペースを2つ入れて#を書く。
# ・Docstringは基本的には全てのmodule, class, methodにつける(non publicな外からアクセスしない関数には不要)
# ・そのコードが「なにをしているか」より「なぜそう書いたか」の方が有益

# 命名規則(name convention)
# 変数名や関数(メソッド)名: snake_case 例) balance, image_height
# クラス名: CamelCase 例: Person, MyClass
# モジュールやパッケージ名: なるべく短いlower caseで、必要であればsnake_case 例) time, numpy

# アンダースコア
# - _xxx: internal use only(non public)の意味
# - xxx_: Pythonで既に使われている単語を使いたいとき 例) type_, class_
# - __xxx: クラスの属性として使うことで名前修飾される
# - __xxx__: magic methodと呼ばれるもので、Pythonが特別に設定しているもの、開発者定義することはない。(overrideすることはある)
# - _: 最近実行した戻り値や、iterationの時に使わない変数

# l, I, O: 一文字の変数は1や0に見間違えるので使わない
# correct
length = len(letter)
# wrong
l = len(letter)

# Constants(宣言後に変更しない変数)は大文字のsnakecaseを使う
PI = 3.14
# ただし意思表示であり変更自体はできる
PI = 3

# Return
# returnを書くならなくても動くとしても全て書く
def foo(x):
    if x > 0:
        return math.sqrt(x)
    else:
        return None

# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int):
# wrong
if type(obj) is type(1):

# Booleanに比較演算子を使わない
bool_var = True
# correct
if bool_var:
# wrong
if bool_var == True:

# type hint (type annotation)
def greeting(name: str) -> str:
    return "Hello" + name
# 1つでもhintをつけたら全てにつける
# Pythonがtypeのチェックをしてくれるわけではない
# Pythonは動的型付け言語であることを意識
# type hintを強制したり、命名規約に入れるべきではない
