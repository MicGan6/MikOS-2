import os, sys
import DOS.lib.DOSLib as DOSLib
from DOS.lib.DOSLib import show_later
# 获取工作目录、上级目录
path = os.getcwd() + '\\MikDOS'

parent_path = os.path.abspath('.')
#打印系统信息

print('MikDOS V1')
print('© Ark Krin Studio MikOS Dev Team 保留所有权利')
while True:
    #获取用户输入
    inp = input('MikDOS>>')
    #统一输入格式
    comd = inp.lower()
    #判断
    #帮助
    if comd == 'help':
        show_later()
        DOSLib.helpdos(path)
    #关机
    elif comd == 'shutdown':
        print('正在关闭')
        show_later()
        sys.exit()
    #启动MikOS
    elif comd == 'startmik':
        show_later()
        DOSLib.startmik(parent_path)
        sys.exit()
    #打开设置
    elif comd == 'setting':
        show_later()
        DOSLib.setting(parent_path)
    #打印时间
    elif comd == 'time':
        show_later()
        DOSLib.p_time()
    #未输入指令
    else:
        print(inp, '不是一个可以执行的命令')
        continue
