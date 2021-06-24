# 幽灵游戏
from random import randint
from turtle import getscreen

feeling_brave = True
score = 0


while feeling_brave:
    ghost_door = randint(1, 3)
    screen = getscreen()
    program = screen.textinput('幽灵游戏👻', '''|当前分数 ： {}|
    三扇门在你前面……
    鬼在其中一扇门后。
    你要开那一扇门？
    第一扇，第二扇还是第三扇？（输入1/2/3）'''.format(score))
    if not (int(program) == ghost_door):
        print('安全(*^^*)')
        score += 1
    else:
        print('幽灵👻！')
        print('跑！')
        print('游戏结束 分数：{}'.format(score))
        break
