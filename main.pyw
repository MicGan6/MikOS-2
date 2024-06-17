from tkinter import Tk,Canvas,Button,messagebox
from PIL import ImageTk, Image
from sys import exit as ex
from os import startfile, getcwd



#----------Made by 悠然自得、MicGan----------#


#创建窗口
root = Tk()

#窗口位置
rootxy = None

#不可放大缩小：设置
root.resizable(width=False, height=False)



#标题
root.title('MikOS')

#尺寸及背景
chicun = None

bg = None



#图标位置

imgpos = [[70,50],[70,120],[70, 190]]


#获取配置文件
with open('配置.txt', 'r+') as f:
    lines = f.readlines()
    #f.seek(0)  # 将指针移动到文件开头
    #f.truncate()  # 清空文件内容


    lines[0] = lines[0].replace('\n','')#清空换行符
    lines[1] = lines[1].replace('\n', '')
    chicun = [lines[0],lines[0].split('x')]   #赋值“chicun” ；格式 [a×h,[a,h]]

    #打印尺寸，用于调试
    print('Debug:尺寸变量',chicun)


    #获取背景路径
    bg = lines[1]

    #关闭配置文件
    f.close()

#root尺寸
root.geometry(chicun[0])

#设置画布
c = Canvas(root,width=int(chicun[1][0]), height=int(chicun[1][1]), highlightthickness=0)



#设置直接关闭事件（点击“X”）

def if_exit_in_x():
    if messagebox.askokcancel('MikOS：提示','确认要关闭MikOS吗？'):
        ex()





# 加载bg图片
bgimg = Image.open(bg)


# 图片缩放至合适大小
bgimg = bgimg.resize((int(chicun[1][0]), int(chicun[1][1])))

#转化为tkinter格式
bgimg = ImageTk.PhotoImage(bgimg)





#-----------


#设置背景
background = c.create_image(0, 0, anchor='nw', image=bgimg)

#设置状态栏
titlebar = c.create_rectangle(0,0,20,1000, fill='white',outline = 'white')



#重启主程序
def restart_main():
    startfile('restart.pyw')
    ex()


# 加载遮挡图片
tranimg = Image.open('translucent.png')

# 图片缩放至合适大小
tranimg = tranimg.resize((int(chicun[1][0])-20, int(chicun[1][1])))

#转化为tkinter格式
tranimg = ImageTk.PhotoImage(tranimg)

#遮挡
masking = c.create_image(20, 0, anchor='nw', image=tranimg)





#----软件------------------------------




#设置按钮响应事件
def setting(*args):
    startfile(getcwd() + '/setting/setting.pyw')

def calc(*args):
    startfile('calc\calc_main.pyw')

def  mouse_hand(*args):
    root.config(cursor = 'hand2')

def mouse_arrow(*args):
    root.config(cursor = 'arrow')

def Music_Center(*args):
    startfile('music\MMC Main.py')

#设置



setting_img = Image.open('icon\setting.png')

setting_btn = None  # 定义一个空对象

setting_img = setting_img.resize((50,50))

setting_img = ImageTk.PhotoImage(setting_img)

setting_btn = c.create_image(imgpos[0][0],imgpos[0][1], image=setting_img)

c.tag_bind(setting_btn,'<Button-1>',setting)


# 将鼠标事件绑定到图片项上
c.tag_bind(setting_btn, '<Enter>', mouse_hand)
c.tag_bind(setting_btn, '<Leave>', mouse_arrow)


#设置结束


#计算器
calc_img = Image.open('icon\calc.png')


calc_btn = None  # 定义一个空对象

calc_img = calc_img.resize((38,50))

calc_img = ImageTk.PhotoImage(calc_img)

calc_btn = c.create_image(imgpos[1][0],imgpos[1][1], image=calc_img)

c.tag_bind(calc_btn,'<Button-1>',calc)
# 将鼠标事件绑定到图片项上
c.tag_bind(calc_btn, '<Enter>', mouse_hand)
c.tag_bind(calc_btn, '<Leave>', mouse_arrow)

# 音乐中心
M_img = Image.open('icon\Music.png')


M_btn = None  # 定义一个空对象

M_img = M_img.resize((50,50))

M_img = ImageTk.PhotoImage(M_img)

M_btn = c.create_image(imgpos[2][0],imgpos[2][1], image=M_img)

c.tag_bind(M_btn,'<Button-1>',Music_Center)
# 将鼠标事件绑定到图片项上
c.tag_bind(M_btn, '<Enter>', mouse_hand)
c.tag_bind(M_btn, '<Leave>', mouse_arrow)



#----软件---- 结束


#设置“重启按钮”
restart = Button(root,text='重\n启',overrelief='sunken',bd=2,height=2,width=1,command=restart_main,cursor='hand2')
restart.place(x=2,y=60)

#设置“关机按钮”
off = Button(root,text='关\n机',overrelief='sunken',bd=2,height=2,width=1,command=ex,cursor='hand2')
off.place(x=2,y=0)


#界面主程序
def main_interface():
    global root,c
    pass


#更新函数

def root_update():
    global chicun,background,bgimg
    with open('配置.txt', 'r') as update_file:
        update_img_path = update_file.readlines()[1].replace('\n','')

        update_file.close()
    # 加载bg图片
    bgimg = Image.open(update_img_path)

    # 图片缩放至合适大小
    bgimg = bgimg.resize((int(chicun[1][0]), int(chicun[1][1])))

    '''
    bgimg.save('Debug.png')
    '''

    # 转化为tkinter格式
    bgimg = ImageTk.PhotoImage(bgimg)



    c.itemconfigure(background,image=bgimg)
    print('Debug:更新背景成功，背景路径：',repr(update_img_path))
    c.update()
    #准备再次更新
    print('Debug:更新函数调用成功')
    root.after(1000,root_update)





#获取位置函数
def get_xy():
    global rootxy

    #获取窗口位置
    rootxy = root.winfo_geometry()

    print('Debug:窗口参数',rootxy)

    #1000毫秒后再次调用
    root.after(1000,get_xy)



#放置画布
c.pack()







#开启get_xy函数
root.after(3000,get_xy)

#开启更新函数
root.after(100,root_update)

#设置关闭时的事件
root.protocol("WM_DELETE_WINDOW",if_exit_in_x)


#开启主循环
root.mainloop()
