import os

file_list = os.listdir()

for file in file_list:
    with open(file,'a') as f:
        if file != 'md5changer.py':
            f.write('hello md5')

print('修改完成')
