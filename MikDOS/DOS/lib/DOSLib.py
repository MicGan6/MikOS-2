"""
本程序为MikDOS的运行库
"""
import os, sys
def helpdos(path):
    with open(path + '\\DOS\\Command.txt', mode='r', encoding='utf-8') as cmd:
        file = cmd.read()
        print(file)
def startmik(p_path):
    os.startfile(p_path + '\\logon.pyw')
    
