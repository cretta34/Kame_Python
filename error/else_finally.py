def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
        return "try"
    except ZeroDivisionError as e:
        print("0で割ることはできません。正しい値を入力してください")
        print(e)
    # except ValueError:
    #     print("数字を入力してください")
    else:
        print(5 / 0)
        print(f"一人{each}円です")
    finally:
        print("ご利用ありがとうございます")
        return "finally"


if __name__ == "__main__":
    # split_bill(10000)
    print(split_bill(10000))
