from os import listdir
from tkinter import Tk, StringVar,Button,messagebox, Radiobutton
from tkinter import ttk
from sys import exit as ex
from pygame import mixer
import threading
from tkinter.simpledialog import askfloat
from tkinter.messagebox import showerror
play_window = Tk()
play_window.title('播放')
play_window.configure(background='gray')
play_window.geometry("500x150")

play_window.resizable(width=False, height=False)
music_name = listdir('Music_Download')
try:
    selected_music = StringVar(value=music_name[0])
except:
    showerror('错误', '没有找到')
else:
    music_dropdown = ttk.Combobox(play_window, textvariable=selected_music, values=music_name,state='readonly', width = 60)
    music_dropdown.place(x=20,y=20)
    def play_m():
        mixer.init()
        mixer.music.set_volume(0.1)
        music_name_in_def = music_dropdown.get()
        mixer.music.load('Music_Download/' + music_name_in_def)
        mixer.music.play(2)
        while mixer.music.get_busy():
            pass
    def pause_m():
        mixer.init()
        mixer.music.pause()
    def start_pause():
        mixer.init()
        global fadeout_TF
        mixer.music.unpause()

    #创建多线程，以防应用未响应
    def start_tread_1():
        thread = threading.Thread(target = pause_m, args = ())
        thread.setDaemon(True)
        thread.start()
    def start_tread_2():
        thread = threading.Thread(target = play_m, args = ())
        thread.setDaemon(True)
        thread.start()
    def start_tread_3():
        thread = threading.Thread(target = start_pause, args = ())
        thread.setDaemon(True)
        thread.start()
    def val_set():
        mixer.init()
        val = askfloat('音量设置', '请输入音量大小(0-1之间的小数)')
        if val > 1 or val < 0:
            showerror('错误', '请输入一个小于1或大于0的数')
        else:
            mixer.music.set_volume(val)

    play_button = Button(play_window, text="开始播放", command=start_tread_2,overrelief='sunken',bd=4,cursor='hand2')
    play_button.place(x=50, y=60)

    pause_button = Button(play_window, text="暂停", command=start_tread_1,overrelief='sunken',bd=4,cursor='hand2')
    pause_button.place(x=400, y=60)
    unpause_button = Button(play_window, text="继续播放", command=start_tread_3,overrelief='sunken',bd=4,cursor='hand2')
    unpause_button.place(x=200, y=60)
    val_button = Button(play_window, text = "声音设置", command = val_set, overrelief='sunken',bd=4,cursor='hand2')
    val_button.place(x = 300, y = 60)
    play_window.mainloop()