from enum import Enum, unique
import sys

# 計算機

# EnumでModeを定義
@unique
class Mode(Enum):
    SUM = 1
    SUB = 2
    MULTI = 3
    DIV = 4

# 計算関数
# 引数 << int:1つ目の数値 , int:2つ目の数値 , int:モード >>
# 戻り値 << int: 計算結果, str: 計算式 >>
def calc(num1, num2, mode):
    mode = Mode(mode)
    # 足し算
    if mode is Mode.SUM:
        result = num1 + num2
        formula = f"{num1} + {num2} = {result}"
    # 引き算
    elif mode is Mode.SUB:
        result = num1 - num2
        formula = f"{num1} - {num2} = {result}"
    # 掛け算
    elif mode is Mode.MULTI:
        result = num1 * num2
        formula = f"{num1} * {num2} = {result}"
    # 割り算
    elif mode is Mode.DIV:
        result = num1 / num2
        formula = f"{num1} / {num2} = {result}"
    else:
        # 1~4以外の数値が投げられた場合例外を投げる
        raise ValueError
    
    return result, formula


# メイン処理
if __name__ == "__main__":
    try:
        # コマンドライン引数を入力した場合
        args = sys.argv
        mode = int(args[1])
        num1 = int(args[2])
        num2 = int(args[3])

        # 計算
        result, formula = calc(num1, num2, mode)
        # 出力
        print(formula)

    except IndexError as e:
        # コマンドライン引数を入力しなかった場合
        print("-----------計算機-----------")
        while True:
            try:
                # モード選択
                print("|MODE 1:足し算 2:引き算 3:掛け算 4:割り算")
                mode = int(input("|モードを入力してください"))
                num1 = int(input("|1つ目の整数を入力してください"))
                num2 = int(input("|2つ目の整数を入力してください"))

                # 計算
                result, formula = calc(num1, num2, mode)
                # 出力
                print("|" + formula)
                print("-------------------------")
            except ValueError as e:
                # モード選択もしくは数値入力で正しい値が入力されなかった場合
                print("------------ERROR------------")
                print("|正しい数値を入力してください")
                print("-----------------------------")
    
    except ValueError as e:
        # コマンドライン引数が正しい値でなかった場合
        print("------------ERROR------------")
        print("正しい数値を入力してください")
        print("-----------------------------")
        