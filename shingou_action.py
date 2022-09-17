from enum import Enum
import sys

class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

def act_shingou(color):
    color = Shingou(int(color))
    if color is Shingou.RED:
        print("とまれ")
    elif color is Shingou.BLUE:
        print("すすめ")
    elif color is Shingou.YELLOW:
        print("ちゅうい")
    else:
        print("信号機の色に対応していません")

    return Shingou(color)


args = sys.argv
color = act_shingou(args[1])