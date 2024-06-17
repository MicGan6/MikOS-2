
import requests, json, os
from tkinter.messagebox import showinfo, showerror
p = os.getcwd()
def get_OLD_Ver():
    global p
    try:
        f = open(p + '\\setting\\Version.Ver', mode = 'r')
        v = f.readline()
    except:
        f = open(os.path.dirname(os.getcwd()) + '\\setting\\Version.Ver')
        v = f.readline()
    return v
try:
    old_version = get_OLD_Ver()
    old_version = float(old_version)
    showinfo('提示', '已经开始检查最新版本啦！请不要同时多次检查更新，慢的原因是版本核对文件在Github上')
    Update = json.loads(requests.get('https://gangan1.github.io/MikOS_Update/Version.json').text) #获取并加载版本的json文件
    #获取json数据中的值
    last_version = Update.get('version')
    LV_State = Update.get('State')
    link = Update.get('link')
    password = Update.get('password')
    #转化类型
    last_version = float(last_version)
    #检查更新
    if last_version > old_version and LV_State == 'Release':
        showinfo('检查更新', f'发现新版本，由于技术原因，请手动下载。\n链接{link}\n提取码{password}')
    elif last_version == old_version:
        showinfo('检查更新', '您的版本已是最新')
    elif last_version > old_version and LV_State == 'Devlope':
        showinfo('检查更新', '新版本正在开发哦~请坐和放宽~')
except requests.exceptions.ConnectionError:
    showerror('错误', '网络原因，请稍后再试')




