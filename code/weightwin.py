from tkinter import *

from data import getgrade
from treeview import showtree


def change(str):
    tmp = float(str.strip('%'))  # 去掉s 字符串中的 %
    ans = tmp / 100.0  # 运行环境是Python2.7   其中Python2.X  与 python 3X中的除法是有区别
    return ans

def _setweight(root, tree, tmp, dic, weight):

    temp = dict()
    temp[0] = tree

    def myclick():
        weight[0] = change(txt1.get())
        weight[1] = change(txt2.get())
        weight[2] = change(txt3.get())
        weight[3] = change(txt4.get())
        weight[4] = change(txt5.get())

        getgrade(tmp, dic, weight)
        temp[0] = showtree(temp[0], dic)

    win = Toplevel(root)  # 创建窗口
    win.geometry("460x200+600+300")  # 小写x代表乘号500x400为窗口大小，+0+0窗口显示位置
    win.title("设置窗口")
    lab = Label(win,text='请设置各项所占比例，例如10%',font=('黑体','15'))
    lab1 = Label(win,text='思想品德素质', font=('黑体','10'))
    lab2 = Label(win,text='学业成绩', font=('黑体','10'))
    lab3 = Label(win,text='身心素质', font=('黑体','10'))
    lab4 = Label(win,text='创新实践能力', font=('黑体','10'))
    lab5 = Label(win,text='学院特色', font=('黑体','10'))
    txt1 = StringVar()
    txt2 = StringVar()
    txt3 = StringVar()
    txt4 = StringVar()
    txt5 = StringVar()
    txt1.set("10%")
    txt2.set("70%")
    txt3.set("5%")
    txt4.set("10%")
    txt5.set("5%")
    entry1 = Entry(win,textvariable=txt1,width=15,font=('','16'))
    entry2 = Entry(win,textvariable=txt2,width=15,font=('','16'))
    entry3 = Entry(win,textvariable=txt3,width=15,font=('','16'))
    entry4 = Entry(win,textvariable=txt4,width=15,font=('','16'))
    entry5 = Entry(win,textvariable=txt5,width=15,font=('','16'))
    button = Button(win, text='提交',command=myclick)

    lab.grid(row=0, column=0)
    lab1.grid(row=1, column=0)
    lab2.grid(row=2, column=0)
    lab3.grid(row=3, column=0)
    lab4.grid(row=4, column=0)
    lab5.grid(row=5, column=0)
    entry1.grid(row=1,column=1)
    entry2.grid(row=2, column=1)
    entry3.grid(row=3, column=1)
    entry4.grid(row=4, column=1)
    entry5.grid(row=5, column=1)
    button.grid(row=6,column=0)

    win.mainloop()
    return temp[0]

