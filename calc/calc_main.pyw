from tkinter import Tk,Button,Canvas


#----------Made by 悠然自得、添亮了（肝肝甘甘的野生电脑）----------#


# 定义主窗口
root = Tk()
root.title("计算器")
root.geometry("250x340")
root.resizable(False, False)



def Button_main(text,bg='#D4F1F4',width=3):
    return Button(root, text=text, font=("Arial", 14), width=width, height=1, bd=4, bg=bg,command=lambda :yunsuan(text),overrelief='sunken',activebackground="light yellow")


c = Canvas(root, width=250, height=340)
c.yunsuan = ''
c.color = 'black'


def update():
    c.create_rectangle(0, 0, 250, 340, fill='light gray', outline=None)
    c.create_rectangle(20, 20, 230, 70, width=2, fill='white',outline='black')
    if c.yunsuan == 'ERROR':
        c.color = 'tomato'
    else:
        c.color = 'black'
    c.create_text(225,70, text=c.yunsuan,font=('arial',30),fill = c.color,anchor='se')
    c.create_rectangle(0,19,18,70,fill='light gray',outline='light gray')





def yunsuan(num):
    num = str(num)
    if c.yunsuan == 'ERROR' and num != 'CE':
        print('Debug:ERROR状态下无法运算')
        return


    if num in '0123456789+-*/.':
        if c.yunsuan == 0 or c.yunsuan =='0':
            c.yunsuan = num
        else:
            c.yunsuan += num
    elif num == '←':
        c.yunsuan = ''.join(list(c.yunsuan)[0:-1])
    elif num == 'CE':
        c.yunsuan = '0'
    elif num == '=':
        try:
            c.yunsuan = str(eval(c.yunsuan))
        except:
            c.yunsuan = 'ERROR'
        finally:
            print('Debug:try语句资源释放成功')
    print('Deubg:显示框内容',c.yunsuan)
    update()

# 定义数字按钮
btn_1 = Button_main('1')
btn_2 = Button_main('2')
btn_3 = Button_main('3')
btn_4 = Button_main('4')
btn_5 = Button_main('5')
btn_6 = Button_main('6')
btn_7 = Button_main('7')
btn_8 = Button_main('8')
btn_9 = Button_main('9')
btn_0 = Button_main('0',width=9)
btn_point = Button_main('.')


# 定义操作符按钮
btn_add = Button_main('+')
btn_sub = Button_main('-')
btn_mul = Button_main('*')
btn_div = Button_main('/')
btn_eq = Button_main('=',width=8)
btn_ce = Button_main(text='CE',bg='#F7AF9D')
btn_back = Button_main(text='←')


btn_1.place(x=10, y=80)
btn_2.place(x=70, y=80)
btn_3.place(x=130, y=80)
btn_4.place(x=10, y=130)
btn_5.place(x=70, y=130)
btn_6.place(x=130, y=130)
btn_7.place(x=10, y=180)
btn_8.place(x=70, y=180)
btn_9.place(x=130, y=180)
btn_0.place(x=10, y=230)
btn_point.place(x=70, y=280)



btn_add.place(x=190, y=80)
btn_sub.place(x=190, y=130)
btn_mul.place(x=190, y=180)
btn_div.place(x=190, y=230)
btn_eq.place(x=130, y=280)
btn_ce.place(x=10, y=280)
btn_back.place(x=130,y=230)

c.pack()
# 运行主循环

update()
root.mainloop()