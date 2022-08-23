# import文は一番上に書く
# 標準ライブラリ, サードパーティのライブラリ, 自分たちのライブラリ, ローカルのライブラリ
# それぞれの間に1行空ける
# それぞれの中でabc順で書く
import sys
sys.path.append("/Users/hiroyuki/Desktop/UdemyLecture/Kame_Python/function/")
import docstring
# import mymodule
# mymodule.myfunc()
# print(mymodule.myvariable)
# mymodule.anotherfunc()

# from mymodule import myfunc, myvariable, anotherfunc
# myfunc()
# print(myvariable)
# anotherfunc()

# *は便利だが何がimportされているかわからないので非推奨
# また、*では_から始まる関数はimportできない
# from mymodule import *
# myfunc()
# print(myvariable)
# anotherfunc()

# 自分で作ったモジュールにasを使うのはわかりにくくなるので非推奨
# サードパーティのものでみんなが同じように略すものに使う
import mymodule as mm
mm.myfunc()
print(mm.myvariable)
mm.anotherfunc()

print(sys.path)
print(docstring.multiply(3, 4))