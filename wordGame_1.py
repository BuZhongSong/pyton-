import random
import easygui as g

secret = random.randint(1,5)
temp = g.enterbox("猜一下我心里想的是哪个数字：")
guess = int(temp)

cnt = 0
while guess != secret and cnt <= 3:
    cnt = cnt+1
    temp = g.enterbox("猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        g.msgbox("我草，你是我肚子里的蛔虫吗？！")
        g.msgbox("哼，猜中也没有奖励！")
    else:
        if guess > secret:
            g.msgbox("大了大了")
        else:
            g.msgbox("小了小了")
g.msgbox("游戏结束，不玩啦")
