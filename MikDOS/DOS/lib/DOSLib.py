"""
本程序为MikDOS的运行库
变量path为工作目录，p_path为上级目录
"""
import os, sys, time
#帮助指令
def helpdos(path):
    with open(path + '\\DOS\\Command.txt', mode='r', encoding='utf-8') as cmd:
        file = cmd.read()
        print(file)
#启动MikOS
def startmik(p_path):
    os.startfile(p_path + '\\logon.pyw')
#打开设置
def setting(p_path):
    os.startfile(p_path + '\\setting\\setting.pyw')
#打印时间
def p_time():
    print(time.ctime())
#延时打印(故意滴doge)
def show_later():
    time.sleep(1)