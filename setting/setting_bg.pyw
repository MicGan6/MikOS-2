from os import listdir
from tkinter import Tk, StringVar,Button,messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from sys import exit as ex


#----------Made by 悠然自得、MicGan----------#


# 创建主窗口
root = Tk()
root.title("修改背景")

#设置背景色
root.configure(background='gray')
#设置大小及不可缩放

root.geometry("200x100")

root.resizable(width=False, height=False)
# 读取BG文件夹内容
try:
    bg_files = listdir("bg")
except:
    bg_files = listdir("../bg")

# 创建下拉菜单并添加选项
selected_bg = StringVar(value=bg_files[0])
bg_dropdown = ttk.Combobox(root, textvariable=selected_bg, values=bg_files,state='readonly')
bg_dropdown.place(x=20,y=20)



def get_new_img():
    main_img = askopenfilename(initialdir='C:/Users/', filetypes=[('图片', '*.png;*.jpg;*.jpeg;*.bmp;')])
    if main_img == '' or main_img == None:
        print('Debug:检测到路径失效或关闭路径选择窗口，已取消写入配置文件')
        return
    print('Debug:导入选择路径为：',main_img)
    current_selection = bg_dropdown.get()
    try:
        with open("配置.txt", "r") as f:
            lines = f.readlines()
        lines[1] = f"{main_img}\n"
        with open("配置.txt", "w") as f:
            f.writelines(lines)
            print(f"Debug:将 {repr(main_img)} 写入配置文件")
    except:
        with open("..\配置.txt", "r") as f:
            lines = f.readlines()
        lines[1] = f"{main_img}\n"
        with open("..\配置.txt", "w") as f:
            f.writelines(lines)
            print(f"Debug:将 {repr(main_img)} 写入配置文件")
    finally:
        print('Debug:try语句资源释放成功')
    messagebox.showinfo('MyOS：提示', '背景修改成功！')
    ex()


def modify_config():
    current_selection = bg_dropdown.get()
    try:
        with open("配置.txt", "r") as f:
            lines = f.readlines()
        lines[1] = f"bg\{current_selection}\n"

        with open("配置.txt", "w") as f:
            f.writelines(lines)
            print(f"Debug:将选项 {current_selection} 写入配置文件")
    except:
        with open("..\配置.txt", "r") as f:
            lines = f.readlines()
        lines[1] = f"bg\{current_selection}\n"
        with open("..\配置.txt", "w") as f:
            f.writelines(lines)
            print(f"Debug:将选项 {current_selection} 写入配置文件")
    finally:
        print('Debug:try语句资源释放成功')
    messagebox.showinfo('MyOS：提示','背景修改成功！')
    ex()



modify_button = Button(root, text="修改背景", command=modify_config,overrelief='sunken',bd=4,cursor='hand2')
modify_button.place(x=20, y=60)

new_img_button = Button(root,text="自定义", command=get_new_img,overrelief='sunken',bd=4,cursor='hand2')
new_img_button.place(x=86, y=60)


quit_button = Button(root, text="关闭", command=ex,overrelief='sunken',bd=4,cursor='hand2')
quit_button.place(x=140, y=60)
# 运行主循环
root.mainloop()