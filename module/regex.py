import re

# Regular Expression (正規表現　通称RegEx)
email = "myemail@gmail.com"
print("@" in email)  # if文で全て考えるのは大変

result = re.search('@\w+\.', email)
if result:
    print(result)
    print("Matched")
else:
    print("Not found")


# metacharacter
# [] []内の文字と同じものがあればマッチ
print(re.search('[abc]', 'b'))
print(re.search('[abc]', 'apple'))
print(re.search('[a-c]', 'apple'))
print(re.search('[0-9]', 'cretta34'))

# ^　最初の文字
print(re.search('^[0-9]', '0test'))
print(re.search('^[0-9]', 'test0'))

# {n} m回リピート
print(re.search('^[0-9]{4}', '2021/3/31'))
print(re.search('^[0-9]{4}', '21/3/31'))

# {n,m} 最低n回、最高m回リピート
print(re.search('^[0-9]{2,4}', '2021/3/31'))
print(re.search('^[0-9]{2,4}', '21/3/31'))

# $ 最後の文字
print(re.search('[0-9]{2}$', '2021/3/31'))
print(re.search('[0-9]{2}$', '2021/3/1'))

# * 左のパターンを0回以上繰り返す
print(re.search('a*b', 'b'))
print(re.search('a*b', 'ab'))
print(re.search('a*b', 'a'))

# + 左のパターンを1回以上繰り返す
print(re.search('a+b', 'b'))
print(re.search('a+b', 'ab'))
print(re.search('a+b', 'a'))

# ? 左のパターンを0回か1回繰り返す
print(re.search('ab?c', 'ac'))
print(re.search('ab?c', 'abc'))
print(re.search('ab?c', 'ab'))
print(re.search('ab?c', 'abbbc'))

# | or
print(re.search('abc|012', 'abc'))
print(re.search('abc|012', '012'))
print(re.search('abc|012', '01'))

# () グループ
print(re.search('te(s|x)t', 'test'))
print(re.search('te(s|x)t', 'text'))
print(re.search('te(s|x)t', 'teat'))

# . 任意の一文字
print(re.search('h.t', 'hat'))
print(re.search('h.t', 'hot'))

# \ エスケープ
print(re.search('h\.t', 'h.t'))

# \w {a-zA-Z0-9_} 全てのアルファベット、数字及びアンダースコア
print(re.search('h\wt', 'hit'))
print(re.search('h\wt', 'hiit'))
print(re.search('h\wt', 'h_t'))
print(re.search('h\wt', 'h.t'))

# challenge1
# pattern_dob = '^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9)|1[0-9]|2[0-9]|3[01])$'
# while True:
#     dob = input("生年月日を入力してください(yyyy/mm/dd):")
#     result = re.search(pattern_dob, dob)
#     if result:
#         print(f"{dob}は正しいフォーマットです")
#         break
#     else:
#         print(f"{dob}は正しくないフォーマットです")

# challenge2
pattern_email = '^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$'
while True:
    email = input("emailアドレスを入力してください:")
    result = re.search(pattern_email, email)
    if result:
        print(f"{email}は正しいフォーマットです")
        break
    else:
        print(f"{email}は正しくないフォーマットです")
