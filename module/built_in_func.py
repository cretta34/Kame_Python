# dir(): 今のスクリプトが何にアクセスできるのかを確認できる
from re import search
import time
# print(dir())
# print(dir(__builtins__))
__builtins__.print('hello world')
print(dir())
