#encoding=utf-8
import tkinter
import tkinter.messagebox
from  tkinter  import ttk
import webbrowser
'''
https://api.flvsp.com/?url=                 mp4或m3u8结尾的媒体文件地址
http://j.zz22x.com/jx/?url=                  ...
https://vip.hackmg.com/jx/index.php?url=    √
'''
def Button():
    if varRadio.get() == 0:
        a = 'https://660e.com/?url='
    elif varRadio.get() == 1:
        a = 'https://vip.hackmg.com/jx/index.php?url='
    elif varRadio.get() == 2:
        a = 'http://www.82190555.com/video.php?url='
    elif varRadio.get() == 3:
        a = 'https://api.flvsp.com/?url='
    b = entry_movie_link.get()
    webbrowser.open(a+b)
def qk():
    entry_movie_link.delete(0,'end')

def openaqy():
    webbrowser.open('http://www.iqiyi.com')

def opentx():
    webbrowser.open('http://v.qq.com')

def openyq():
    webbrowser.open('http://www.youku.com/')

def about():
    abc='''
    经过测试爱奇艺、优酷、腾讯的VIP视频可以播放
    链接格式为
    http://www.iqiyi.com/v_19rrb2u62s.html?fc=82992814760eeac6
    '''
    tkinter.messagebox.showinfo(title='帮助文件', message=abc)
def zzxx():
    msg='''
    作者：chm
    邮箱：1152633386@qq.com
    '''
    tkinter.messagebox.showinfo(title='联系方式', message=msg)

def bz():
    msg = '''
    备注：通道四用于解析mp4或m3u8结尾的媒体文件地址
    '''
    tkinter.messagebox.showinfo(title='tips',message=msg)
if __name__ == '__main__':
    root=tkinter.Tk()
    root.title('VIP视频破解软件')
    root['width']=500
    root['height']=300

    menubar = tkinter.Menu(root)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label='帮助文档', command=about)
    helpmenu.add_command(label='作者信息', command=zzxx)
    helpmenu.add_command(label='备注', command=bz)
    menubar.add_cascade(label='帮助(H)', menu=helpmenu)
    root.config(menu=menubar)

    varentry1= tkinter.StringVar(value='')
    lab_movie_gallery=tkinter.Label(root, text='视频播放通道')
    lab_movie_gallery.place(x=20,y=20,width=100,height=20)
    varRadio=tkinter.IntVar(value=0)
    Radiobutton1_movie_gallery=tkinter.Radiobutton(root,variable=varRadio,value=0,text='通道1')
    Radiobutton2_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=1, text='通道2')
    Radiobutton3_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=2, text='通道3')
    Radiobutton4_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=3, text='通道4')
    Radiobutton1_movie_gallery.place(x=130,y=20,width=100,height=20)
    Radiobutton2_movie_gallery.place(x=210, y=20, width=100, height=20)
    Radiobutton3_movie_gallery.place(x=290, y=20, width=100, height=20)
    Radiobutton4_movie_gallery.place(x=370, y=20, width=100, height=20)
    # number = tkinter.StringVar(value='')
    # numberChosen = ttk.Combobox(root, width=12, textvariable=number)
    # numberChosen['values'] = (1, 2, 4, 42, 100) # 设置下拉列表的值
    # numberChosen.grid(column=, row=1) # 设置其在界面中出现的位置 column代表列 row 代表行
    # numberChosen.current(2)
    # numberChosen.bind("<<ComboboxSelected>>",Button)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
    # numberChosen.pack()

    #varentry2=tkinter.StringVar(value='https://v.qq.com/x/cover/u4s2zisluorvkgt.html')
    varentry2=tkinter.StringVar(value='https://v.youku.com/v_show/id_XMjI2NzU0NTI0.html?spm=a2h0k.11417342.soresults.dselectbutton&s=cbfcd9b8962411de83b1&lang=%E7%B2%A4%E8%AF%AD')
    lab_movie_link = tkinter.Label(root, text='视频播放链接')
    lab_movie_link.place(x=20, y=60, width=100, height=20)
    entry_movie_link = tkinter.Entry(root, textvariable=varentry2)
    entry_movie_link.place(x=130, y=60, width=300, height=20)
    button_movie_link=tkinter.Button(root,text='清空',command=qk)
    button_movie_link.place(x=440,y=60,width=30,height=20)
    lab_remind = tkinter.Label(root, text='将视频链接复制到框内，点击播放VIP视频')
    lab_remind.place(x=50, y=90, width=400, height=20)
    varbutton=tkinter.StringVar
    button_movie= tkinter.Button(root, text='播放VIP视频', command=Button)
    button_movie.place(x=140, y=120, width=200, height=60)

    button_movie1 = tkinter.Button(root, text='爱奇艺', command=openaqy)
    button_movie1.place(x=60, y=200, width=100, height=60)

    button_movie2 = tkinter.Button(root, text='腾讯视频', command=opentx)
    button_movie2.place(x=180, y=200, width=100, height=60)

    button_movie3 = tkinter.Button(root, text='优酷视频', command=openyq)
    button_movie3.place(x=300, y=200, width=100, height=60)

    root.mainloop()
