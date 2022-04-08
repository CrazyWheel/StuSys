import tkinter
from tkinter import *

from treeview import clear, insert2


def _findstu(root, tree, dic):

    temp = dict()
    temp[0] = tree

    win = Toplevel(root)  # 创建窗口
    win.geometry("400x80+600+300")  # 小写x代表乘号500x400为窗口大小，+0+0窗口显示位置
    win.title("查询窗口")

    def findkey():
        key = txt.get()
        if key == "":
            tkinter.messagebox.showinfo("提示",'请输入数据')
        else:
            for k in dic.keys():
                lst = dic[k]
                if (key.isdigit() and int(key) in lst) or key in lst:
                        # print(lst)
                        temp[0] = clear(temp[0])
                        temp[0] = insert2(temp[0], dic, k)
                        print(dic)
                        break
            else:
                temp[0] = clear(temp[0])
                tkinter.messagebox.showinfo("提示", '没有数据')

    lab = Label(win,text='请输入单个学号或姓名',font=('黑体','15'))
    txt = StringVar()
    entry = Entry(win,textvariable=txt,width=25,font=('','16'))
    button = Button(win, text='查询', command=findkey)
    lab.grid(row=0,column=0)
    entry.grid(row=1,column=0,padx=10, pady=0)
    button.grid(row=1,column=1,padx=20, pady=0)
    win.mainloop()
    return temp[0]
