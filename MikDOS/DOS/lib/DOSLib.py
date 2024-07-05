"""
本程序为MikDOS的运行库
变量path为DOS工作目录，p_path为DOS上级目录
"""
import os, time



#帮助指令
def helpdos(path):
    with open(path + '\\DOS\\file\\Command.txt', mode='r', encoding='utf-8') as cmd:
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
def dos_config(path):
    print('请阅读下面的教程')
    print('---------------------------------')
    with open(path + '\\DOS\\file\\config_eg.txt', mode='r', encoding='utf-8') as config_eg:
        file_con_eg = config_eg.read()
        print(file_con_eg)
