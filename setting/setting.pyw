from tkinter import Tk,Button,Canvas,messagebox,OptionMenu,StringVar
from os import startfile,path,getcwd,system
from sys import exit as ex

#----------Made by 悠然自得、MicGan----------#










#设置尺寸为None值
chicun = None

# 创建主窗口
root = Tk()

#创建调整大小窗口

root2 = Tk()

#暂时隐藏副窗口
root2.withdraw()

#设置尺寸
root.geometry("230x290")
root2.geometry("100x150")

#标题设置
root.title("设置")

#设置背景色
root.configure(background='gray')
root2.configure(background='gray')


#不可放大缩小：设置
root.resizable(width=False, height=False)
root2.resizable(width=False, height=False)


def Button1():
    global chicun
    chicun = '500x300'
    root2.withdraw()

def Button2():
    global chicun
    chicun = '750x450'
    root2.withdraw()

def Button3():
    global chicun
    chicun = '1000x600'
    root2.withdraw()
#副窗口按钮
button1 = Button(root2, text="500x300",overrelief='sunken',bd=4,command=Button1)
button1.pack(side="top", pady=8)

button2 = Button(root2, text="750x450",overrelief='sunken',bd=4,command=Button2)
button2.pack(side="top", pady=8)

button3 = Button(root2, text="1000x600",overrelief='sunken',bd=4,command=Button3)
button3.pack(side="top", pady=8)


#定义按钮响应事件
def open1():
    global chicun

    root2.deiconify()

    open1_2()

def open1_2():
    global chicun  # 全局变量 chicun，用于保存新的配置参数值

    

    try:
         # 获取当前文件夹的上级目录的绝对路径
        parent_dir = getcwd()
        # 尝试读取"合作"文件夹下的"配置.txt"文件
        with open(parent_dir+'\配置.txt' , 'r') as f:
            # 读取文件内容并按行分割
            neirong = f.read().split('\n')
            print(neirong)
            f.close()

        # 如果 chicun 不为空，则表示需要更新文件中的配置参数
        if chicun != None:
            # 尝试以写模式打开文件，将新的配置参数值写入文件中，并关闭文件
            with open(parent_dir+'\配置.txt', 'w') as f:
                f.write(chicun+'\n'+neirong[1])
                f.close()

            # 隐藏启动窗口，清除 chicun 值，并直接返回
            root2.withdraw()
            chicun = None
            messagebox.showinfo('MyOS：提示', '尺寸修改成功！\n设置重启后生效')
            return
        # 如果 chicun 为空，则表示不需要更新，继续定时器计时
        else:
            root.after(100,open1_2)

    # 如果读取文件出现 FileNotFoundError 异常，则尝试从上级目录中读取
    except FileNotFoundError:
        # 获取当前文件夹的上级目录的绝对路径
        parent_dir = path.dirname(getcwd())
        # 尝试以读模式打开文件，读取其内容并按行分割
        with open(parent_dir+'\配置.txt', 'r') as f:
            neirong = f.read().split('\n')
            print(neirong)
            f.close()

        # 如果 chicun 不为空，则将新的配置参数值写入文件中
        if chicun != None:
            # 尝试以写模式打开文件，将新的配置参数值写入文件中，并关闭文件
            with open(parent_dir+'\配置.txt', 'w') as f:
                f.write(chicun+'\n'+neirong[1])
                f.close()

            # 隐藏启动窗口，清除 chicun 值，并直接返回
            root2.withdraw()
            chicun = None
            messagebox.showinfo('MyOS：提示', '尺寸修改成功！\n设置重启后生效')
            return
        # 如果 chicun 为空，则表示不需要更新，继续定时器计时
        else:
            root.after(100,open1_2)
    finally:
        print('Debug:try语句资源释放成功')





    #startfile(parent_dir+'/配置.txt')


def open2():
    try:
        startfile('setting\setting_bg.pyw')
    except FileNotFoundError:
        startfile('setting_bg.pyw')
    finally:
        print('Debug:try语句资源释放成功')

def open3():
    try:
        startfile('..\配置.txt')
    except FileNotFoundError:
        startfile('配置.txt')
    finally:
        print('Debug:try语句资源释放成功')

def open4():
    try:
        startfile(getcwd()+'\\MikDOS\\MikDOS_Main.py')
    except:
        startfile(path.dirname(getcwd())+'\\MikDOS\\MikDOS_Main.py')
def open5():
    try:
        startfile(getcwd()+'\\osinfo.pyw')
        print(getcwd())
    except:
        startfile(getcwd()+'\\setting\\osinfo.pyw')
        
def open6():
    try:
        startfile(getcwd()+'\\Update.pyw')
        print(getcwd())
    except:
        startfile(getcwd()+'\\setting\\Update.pyw')
    


# 创建按钮
button1 = Button(root, text="设置窗口大小", command=open1, width=20,overrelief='sunken',bd=4)
button2 = Button(root, text="修改背景", command=open2, width=20,overrelief='sunken',bd=4)
button3 = Button(root, text="修改配置文件", command=open3, width=20,overrelief='sunken',bd=4)
button4 = Button(root, text="终端", command=open4, width=20,overrelief='sunken',bd=4)
button5 = Button(root, text="关于系统", command=open5, width=20,overrelief='sunken',bd=4)
button6 = Button(root, text="检查更新", command=open6, width=20,overrelief='sunken',bd=4)

# 将按钮竖着并排显示在窗口中
button1.grid(row=0, column=0, padx=40, pady=(16,0))
button2.grid(row=1, column=0, padx=40, pady=(10,0))
button3.grid(row=2, column=0, padx=40, pady=(10,0))
button4.grid(row=3, column=0, padx=40, pady=(10,0))
button5.grid(row=4, column=0, padx=40, pady=(10,0))
button6.grid(row=5, column=0, padx=40, pady=(10,0))

root2.protocol("WM_DELETE_WINDOW", root2.withdraw)
root.protocol("WM_DELETE_WINDOW",ex)
# 运行主程序
root.mainloop()
