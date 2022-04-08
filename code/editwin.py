from tkinter import *

from data import getgrade
from treeview import showtree


def create(root, item_text, data, tree, tmp, weight):
    newwin = Toplevel(root)
    newwin.geometry('+200+200')
    newwin.title('编辑窗口')

    temp = dict()
    temp[0] = tree

    new_data = list()
    test_data = dict()
    bj_new = StringVar()
    xm_new = StringVar()
    xh_new = StringVar()
    sxpdsz_new = StringVar()
    xycj_new = StringVar()
    sxsz_new = StringVar()
    cxsjnl_new = StringVar()
    xyts_new = StringVar()

    bj = Label(newwin, text='班级: ', font=('', '20'), width=15)
    xm = Label(newwin, text='学号: ', font=('', '20'), width=15)
    xh = Label(newwin, text='姓名: ', font=('', '20'), width=15)
    sxpdsz = Label(newwin, text='思想品德素质: ', font=('', '20'), width=15)
    xycj = Label(newwin, text='学业成绩: ', font=('', '20'), width=15)
    sxsz = Label(newwin, text='身心素质: ', font=('', '20'), width=15)
    cxsjnl = Label(newwin, text='创新实践能力: ', font=('', '20'), width=15)
    xyts = Label(newwin, text='学院特色: ', font=('', '20'), width=15)

    bj_in = Entry(newwin, font=('', '20'), width=15, textvariable=bj_new)
    xm_in = Entry(newwin, font=('', '20'), width=15, textvariable=xm_new)
    xh_in = Entry(newwin, font=('', '20'), width=15, textvariable=xh_new)
    sxpdsz_in = Entry(newwin, font=('', '20'), width=15, textvariable=sxpdsz_new)
    xycj_in = Entry(newwin, font=('', '20'), width=15, textvariable=xycj_new)
    sxsz_in = Entry(newwin, font=('', '20'), width=15, textvariable=sxsz_new)
    cxsjnl_in = Entry(newwin, font=('', '20'), width=15, textvariable=cxsjnl_new)
    xyts_in = Entry(newwin, font=('', '20'), width=15, textvariable=xyts_new)

    bj.grid(row=0, sticky='e')
    xm.grid(row=1, sticky='e')
    xh.grid(row=2, sticky='e')
    sxpdsz.grid(row=3, sticky='e')
    xycj.grid(row=4, sticky='e')
    sxsz.grid(row=5, sticky='e')
    cxsjnl.grid(row=6, sticky='e')
    xyts.grid(row=7, sticky='e')

    bj_in.grid(row=0, column=1, sticky='w')
    xm_in.grid(row=1, column=1, sticky='w')
    xh_in.grid(row=2, column=1, sticky='w')
    sxpdsz_in.grid(row=3, column=1, sticky='w')
    xycj_in.grid(row=4, column=1, sticky='w')
    sxsz_in.grid(row=5, column=1, sticky='w')
    cxsjnl_in.grid(row=6, column=1, sticky='w')
    xyts_in.grid(row=7, column=1, sticky='w')

    def reset():
        bj_in.delete(0, END)
        xm_in.delete(0, END)
        xh_in.delete(0, END)
        sxpdsz_in.delete(0, END)
        xycj_in.delete(0, END)
        sxsz_in.delete(0, END)
        cxsjnl_in.delete(0, END)
        xyts_in.delete(0, END)
        bj_in.insert(0, item_text[1])
        xm_in.insert(0, item_text[2])
        xh_in.insert(0, item_text[3])
        sxpdsz_in.insert(0, item_text[4])
        xycj_in.insert(0, item_text[5])
        sxsz_in.insert(0, item_text[6])
        cxsjnl_in.insert(0, item_text[7])
        xyts_in.insert(0, item_text[8])

    reset()

    def save():
        new_data.clear()
        new_data.append(bj_new.get())
        new_data.append(int(xm_new.get()))
        new_data.append(xh_new.get())
        new_data.append(int(sxpdsz_new.get()))
        new_data.append(int(xycj_new.get()))
        new_data.append(int(sxsz_new.get()))
        new_data.append(int(cxsjnl_new.get()))
        new_data.append(int(xyts_new.get()))

        data[int(item_text[0])-1] = new_data
        print(data)
        getgrade(tmp, data, weight)
        temp[0] = showtree(tree, data)
        # newwin.destroy()

    bu1 = Button(newwin, command=save, text='保存', font=('', 20))
    bu2 = Button(newwin, command=reset, text='重置', font=('', 20))
    bu1.grid(row=8, column=0, sticky='e')
    bu2.grid(row=8, column=1, sticky='w')
    newwin.mainloop()
    return temp[0]

