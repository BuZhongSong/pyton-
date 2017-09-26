file_name = input('请输入文件名:')
file_content = input('请输入内容【单独输入‘:w’保存退出】:\n')
(content, action) = file_content.split(':', 1)
if action == 'w':
    f = open(file_name, 'w')
    f.write(content)
f.close()
