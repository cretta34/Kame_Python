import json

# json.load: jsonファイルをpythonのデータ構造で読み込み
with open("example.json") as f:
    data = json.load(f)

print(data)
print(data['glossary']['GlossDiv'])

# json.dump: pythonのデータ構造をjsonファイルに書き込み
new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open("new_json.json", 'w') as f:
    json.dump(new_json, f)

with open("new_json.json", 'r') as f:
    new_json_reload = json.load(f)
# jsonにdumpしてloadすろとtupleがlistになることに注意
print(new_json_reload)
print(type(new_json_reload['key2']))

# json.dumps: pythonのデータ構造をjson文字列に変換
# dumpsのsはstringのこと
json_str = json.dumps(new_json)
print(json_str)
print(type(json_str))

# json.loads: json文字列をpythonのデータ構造に変換
# loadsのsはstringのこと
python_data = json.loads(json_str)
print(python_data)
print(type(python_data))