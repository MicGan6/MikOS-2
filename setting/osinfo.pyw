from tkinter import messagebox,Tk
import os
root = Tk()
root.withdraw()
def get_OLD_Ver():

    try:
        f = open(os.getcwd() + '\\setting\\Version.Ver', mode = 'r')
        v = f.readline()
    except:
        f = open(os.path.dirname(os.getcwd()) + '\\setting\\Version.Ver')
        v = f.readline()
    return v
Version = get_OLD_Ver()
p_path = os.getcwd() #获取父目录地址
f = open(p_path + '\MayDOS\important\Version.ver', mode = 'r') #获取MayDOS版本
MayDOS_v = f.readline()
messagebox.showinfo('操作系统信息','名称：MikOS \n版本号：'+Version+'\nPowered by Python Tkinter\n© 2023 G Dev Hub MikOS Dev Team')
messagebox.showinfo('终端信息', '名称：MayDOS \n版本号：' + MayDOS_v + '© 2023 MayDOS Team')
root.mainloop()
