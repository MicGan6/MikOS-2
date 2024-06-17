# -*- coding: utf-8 -*-
# @Time    : 2023/12/10 22:02
# @Author  : MicGan
# @FileName: A_start.py
# @Software: PyCharm
# @Blog    ：https://gangan1.github.io
import os, time
from tkinter.messagebox import showerror
print('正在重定向...')
try:
    os.startfile('logon.pyw')
except:
    try:
        showerror('错误', '无法找到登录文件，我们即将将您重定向至MikDOS')
        os.startfile('MikDOS\\MikDOS_Main.py')
    except:
        print('因为系统文件丢失，我们将您重定向至MikDOS')
        os.startfile('MikDOS\\MikDOS_Main.py')