from tkinter.messagebox import showinfo
from tkinter import Tk, Listbox
from tkinter.simpledialog import askstring
import requests, json
from shutil import move, Error
# 伪装自己的信息


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://kuwo.cn',
    'Secret': '10373b58aee58943f95eaf17d38bc9cf50fbbef8e4bf4ec6401a3ae3ef8154560507f032',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1687520303,1689840209; _ga=GA1.2.2021483490.1666455184; _ga_ETPBRPM9ML=GS1.2.1689840210.4.1.1689840304.60.0.0; Hm_Iuvt_cdb524f42f0ce19b169b8072123a4727=NkA4TadJGeBWwmP2mNGpYRrM8f62K8Cm; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1689840223; _gid=GA1.2.1606176174.1689840209; _gat=1',

}

name = askstring('获取名称', "请输入你要搜索的“音乐名称”或“歌手")
# 音乐列表的地址
list_url = f'https://songsearch.kugou.com/song_search_v2?keyword={name}&platform=WebFilter'

list_resp = requests.get(list_url, headers=headers)
m_list = json.loads(list_resp.text[:])['data']['lists']
name_list = []
for i, s in enumerate(m_list):
    name_list.append(f'{i + 1}------{s.get("FileName")}')
Download_window = Tk()
Download_window.geometry('300x300')
Download_window.title('搜索结果')
MusicN_List = Listbox(Download_window, width = 40, height = 37)
MusicN_List.pack()
for j in name_list:
    MusicN_List.insert("end", j)
num = askstring('输入序列号', '请输入要下载的音乐号（输入格式为 1 2）：').split()
for s in num:
    # 此处的 header1 可有可无 但是不带 cookie 的 headers 请求时 可能会出现问题
    headers1 = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
        #'Cookie': 'kg_mid=536e52feec7d1c95137aa1d341f8144e; kg_dfid=3exupN3BZJMQ3ftR4x0KOXDk; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=536e52feec7d1c95137aa1d341f8144e'}

    # 构造你请求资源的URL

    info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={m_list[int(s) - 1].get("FileHash")}&album_audio_id={m_list[int(s) - 1].get("ID")}'

    # 进行访问
    info_resp = requests.get(url = info_url, headers=headers1)
    info_resp = info_resp.text
    print(info_resp)
    # 拿取你所请求资源的数据（这里是得到播放音乐的地址）
    get_music_url = info_resp.json()['data']['play_url']
    # print(f"音乐的播放地址为：'\n'{get_music_url}")

    # 发送请求到服务器，获取音乐资源
    m_resp = requests.get(url = get_music_url, headers=headers1)

    # 服务器回应的数据 --保存数据
    name = m_list[int(s) - 1].get('FileName') + '.mp3'

    # 打开一个文件 写入二进制数据 并输出提示信息
    with open(name, 'wb') as f:  # wb 写进二进制
        f.write(m_resp.content)
        if s in num:
            showinfo('成功', f"第{s}首，已经OK啦!")
            f.close()
            try:
                move(name, 'Music_Download')
            except Error:
                pass
            if s == num[-1]:
                showinfo('成功', f"\n您挑选的{len(num)}首音乐，已经全部下载完成!")