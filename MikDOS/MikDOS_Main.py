import os, sys
import DOS.lib.DOSLib as DOSLib

# 获取工作目录和上级目录
path = os.getcwd()
parent_path = os.path.abspath('..')
print('MikDOS V1')
print('© Ark Krin Studio MikOS Dev Team 保留所有权利')
while True:
    #获取用户输入
    inp = input('MikDOS>>')
    #统一输入格式
    comd = inp.lower()
    #判断
    if comd == 'help':
        DOSLib.helpdos(path)
    elif comd == 'shutdown':
        print('正在关闭')
        sys.exit()
    elif comd == 'startmik':
        DOSLib.startmik(parent_path)
    else:
        print('未知指令')
        continue
