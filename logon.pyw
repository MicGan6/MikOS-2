from tkinter import Tk,Button,Canvas,messagebox
from os import startfile
from sys import exit as ex
from PIL import ImageTk, Image
import time

#----------Made by 悠然自得、MicGan----------#


def logon():
    startfile("main.pyw")
    print('open')
    ex()
# 创建主窗口
root = Tk()
root.title("登录：欢迎进入 MikOS Tkinter Edition")
root.geometry("500x300")

#不可放大缩小：设置
root.resizable(width=False, height=False)

# 创建画布
c = Canvas(root, width=500, height=300)
c.pack()

# 加载遮挡图片
tranimg = Image.open('translucent.png')

# 图片缩放至合适大小
tranimg = tranimg.resize((480,280))

#转化为tkinter格式
tranimg = ImageTk.PhotoImage(tranimg)






with open('配置.txt', 'r+') as f:
    lines = f.readlines()


    lines[0] = lines[0].replace('\n','')#清空换行符
    lines[1] = lines[1].replace('\n', '')
    chicun = [lines[0],lines[0].split('x')]   #赋值“chicun” ；格式 [h×a,[h,a]]

    #打印尺寸，用于调试
    print(chicun)


    #获取背景路径
    bg = lines[1]

    #关闭配置文件
    f.close()


# 加载bg图片
bgimg = Image.open(bg)

# 图片缩放至合适大小
bgimg = bgimg.resize((500,300))

#转化为tkinter格式
bgimg = ImageTk.PhotoImage(bgimg)



#设置背景
background = c.create_image(0, 0, anchor='nw', image=bgimg)


#遮挡
c.create_image(250,150, image=tranimg)


c.create_text(245,105, text="Welcome to MikOS",font=('arial',25),fill = 'black')
c.create_text(246,106, text="Welcome to MikOS",font=('arial',25),fill = 'dark gray')
c.create_text(247,107, text="Welcome to MikOS",font=('arial',25),fill = 'gray')
c.create_text(248,108, text="Welcome to MikOS",font=('arial',25),fill = 'gray')
c.create_text(249,109, text="Welcome to MikOS",font=('arial',25),fill = 'light gray')
c.create_text(250,110, text="Welcome to MikOS",font=('arial',25),fill = 'white')

# 创建按钮
button = Button(root, text="登录", bg="sky blue", command=logon,width = 15,overrelief='sunken',bd=4,cursor="hand2",activebackground="sky blue")
button.place(x=250, y=180, anchor="center")

#设置直接关闭事件（点击“X”）

def if_exit_in_x():
    if messagebox.askokcancel('MikOS：提示','您要关闭MikOS登录界面吗？'):
        ex()

#设置关闭时的事件
root.protocol("WM_DELETE_WINDOW",if_exit_in_x)

# 进入消息循环
root.mainloop()
