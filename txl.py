print('|---欢迎进入通讯录程序---|')
print('|---1：查询联系人资料 ---|')
print('|---2：插入新的联系人 ---|')
print('|---3：删除已有联系人 ---|')
print('|---4：退出通讯录程序 ---|')

contacts = dict()

while 1:
    action = int(input('\n请输入指令：'))
    if action == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name + ':' + contacts[name])
        else:
            print("您输入的姓名不在通讯录中！")
    if action == 2:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name + "已存在通讯录中 -->>", end='')
            print(name + ':' + contacts[name])
            if input('是否修改用户资料（y/n）：') == 'y':
                contacts[name] = input('请输入联系人电话：')
        else:
             contacts[name] = input('请输入联系人电话：')
    if action == 3:
        name = input('请输入联系人姓名：')
        if name in contacts:
            del(contacts[name])
        else:
            print('联系人不存在')
    if action == 4:
        break

print('|---4：欢迎再次使用   ---|')
