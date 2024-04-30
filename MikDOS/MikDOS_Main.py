import os, sys
import DOS.lib.DOSLib as DOSLib
from DOS.lib.DOSLib import show_later
# 获取工作目录和上级目录
path = os.getcwd() + '\\MikDOS'
print(path)
parent_path = os.path.abspath('.')
#打印系统信息
print(parent_path)
print('MikDOS V1')
print('© Ark Krin Studio MikOS Dev Team 保留所有权利')
while True:
    #获取用户输入
    inp = input('MikDOS>>')
    #统一输入格式
    comd = inp.lower()
    #判断
    if comd == 'help':
        show_later()
        DOSLib.helpdos(path)
    elif comd == 'shutdown':
        print('正在关闭')
        show_later()
        sys.exit()
    elif comd == 'startmik':
        show_later()
        DOSLib.startmik(parent_path)
        sys.exit()
    elif comd == 'setting':
        show_later()
        DOSLib.setting(parent_path)
    elif comd == 'time':
        show_later()
        DOSLib.p_time()
    else:
        print('未知指令')
        continue
