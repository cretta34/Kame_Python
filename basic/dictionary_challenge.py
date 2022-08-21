age = int(input("何歳ですか？"))
casino_age = 18
game_dict = {'a': 'バカラ', 'b': 'ブラックジャック', 'c': 'ポーカー', 'd': 'スロット'}

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(':')
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("正しい選択肢を選んでください")
            continue
else:
    print(f"{casino_age}歳未満の方はカジノへは入れません")