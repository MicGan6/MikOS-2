from tkinter import *
import requests
import json
from tkinter.simpledialog import askstring
from os import getcwd, mkdir, startfile
from tkinter.messagebox import showinfo
from shutil import move, Error
from os.path import exists
def init():
    if exists('Music_Download'):
        pass
    else:
        dir_name = getcwd()
        mkdir(dir_name + '\\Music_Download')
def search():
    startfile(getcwd() + '\\music\\MMC Download.py')
def open_mmc_paly_file():
    startfile(getcwd() + '\\music\\MMC Player.py')
def info():
    showinfo('关于', '网络歌曲来源于酷狗音乐，仅供学习交流使用，请勿用于商业用途\n主要开发：肝肝甘甘的野生电脑\nGUI修改以及美化：一只悠然自得\n版本：MyOS Special Edition V1(β2)')
#初始化
init()
#创建窗口对象
main_window = Tk()
main_window.resizable(False, False)
#窗口大小
main_window.geometry('202x30')
#窗口标题
main_window.title('MMC')
#--菜单栏
#搜索网络歌曲选项
into_search = Button(main_window, text = '搜索网络歌曲', command = search)
into_search.grid(row = 0, column = 0)
#播放歌曲选项
into_play = Button(main_window, text = '播放本地歌曲', command = open_mmc_paly_file)
into_play.grid(row = 0, column = 1)
#关于选项
into_play = Button(main_window, text = '关于', command = info)
into_play.grid(row = 0, column = 2)
#定义背景颜色
main_window.configure(background='gray')
#显示窗口
main_window.mainloop()