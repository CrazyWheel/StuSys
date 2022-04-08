import tkinter
import editwin
import file
import treeview
import weightwin
import findwin

from tkinter import * #导入窗口控件

from helpdoc import _help

name = dict()
tmp = dict()
dic = dict()
weight = [0.1, 0.7, 0.05, 0.1, 0.05]  #设置各项比重

root = Tk()
root.title('山东理工大学学生综合素质测评系统')
root.geometry('+200+300')
tree = treeview.layout(root)



def click_edit(event):
    global tree
    for item in tree.selection():
        item_text = tree.item(item, "values")
    tree = editwin.create(root, item_text, dic, tree, tmp, weight)

def importname():
    global tree
    tree = treeview._importname(tree, name)

def importtmp():
    global tree
    tree = treeview._importtmp(tree, tmp)

def setweight():
    global tree
    tree = weightwin._setweight(root, tree, tmp, dic, weight)

def importgrade():
    global tree
    tree = treeview._importgrade(tmp, tree, dic, weight)

def findstu():
    global tree
    tree = findwin._findstu(root, tree, dic)

def cleardata():
    global tree
    name.clear()
    tmp.clear()
    dic.clear()
    tree = treeview._cleartmp(tree)
    tree = treeview.showtree(tree, dic)

men = Menu(root)
cho1 = Menu(men, tearoff=0)
cho2 = Menu(men, tearoff=0)

tree.bind("<Double-1>", click_edit)
# tree.bind("<Button-3>", click_del)
cho1.add_command(label='导入学生姓名', command=lambda: importname())
cho1.add_separator()
cho1.add_command(label='导入统计模板', command=lambda: importtmp())
cho1.add_separator()
cho1.add_command(label='设置各项所占比例', command=lambda: setweight())
cho1.add_separator()
cho1.add_command(label='导入成绩', command=lambda: importgrade())
cho2.add_separator()
cho2.add_command(label='帮助文档', command=lambda: _help())
cho2.add_separator()
cho2.add_command(label='删除原数据库', command=lambda: cleardata())
men.add_cascade(label='导入', menu=cho1)
men.add_cascade(label='查询/修改', command=lambda: findstu())
men.add_cascade(label='导出', command=lambda: file.savefile(dic))
men.add_cascade(label='帮助/退出',menu=cho2)
root.config(menu=men)

tree.grid()

root.mainloop()
