import random
secret = random.randint(1,5)
temp = input("猜一下人心里想的是哪个数字：")
guess = int(temp)
if isinstance(guess, int) == false:
	print("请输入数字")
cnt = 0
while guess != secret and cnt <= 3:
    cnt = cnt+1
    temp = input("猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("我草，你是我肚子里的蛔虫吗？！")
        print("哼，猜中也没有奖励！")
    else:
        if guess > secret:
            print("大了大了")
        else:
            print("小了小了")
print("游戏结束，不玩啦")
