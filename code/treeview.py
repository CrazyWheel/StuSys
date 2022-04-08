from tkinter import ttk

from data import getgrade
from file import openfile

def layout(root):
    tree = ttk.Treeview(root, show="headings")
    tree['columns'] = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
    tree.column('c0', width=100)
    tree.column('c1', width=100)
    tree.column('c2', width=100)
    tree.column('c3', width=100)
    tree.column('c4', width=100)
    tree.column('c5', width=100)
    tree.column('c6', width=100)
    tree.column('c7', width=100)
    tree.column('c8', width=100)
    tree.column('c9', width=100)
    tree.heading('c0', text='ID', anchor='w', command=lambda _col='c0': treeview_sort_column(tree, _col, False))
    tree.heading('c1', text='班级', anchor='w')
    tree.heading('c2', text='学号', anchor='w', command=lambda _col='c2': treeview_sort_column(tree, _col, False))
    tree.heading('c3', text='姓名', anchor='w')
    tree.heading('c9', text='总分', anchor='w', command=lambda _col='c9': treeview_sort_column(tree, _col, False))
    return tree

def clear(tree):
    items = tree.get_children()
    [tree.delete(item) for item in items]
    return tree

def insert1(tree, dic, i):
    dic[i].insert(0, i)
    tree.insert('', i, values=dic[i])
    dic[i].remove(i)
    return tree

def insert2(tree, dic, i):
    dic[i].insert(0, i+1)
    tree.insert('', i, values=dic[i])
    dic[i].remove(i+1)
    return tree

def _importname(tree, dic):
    maxrow = openfile(dic)
    for i in range(1, maxrow):
        tree = insert1(tree, dic, i)
    return tree

def _importtmp(tree, dic):
    openfile(dic)
    tree.heading('c4', text=dic[0][0], anchor='w', command=lambda _col='c4': treeview_sort_column(tree, _col, False))
    tree.heading('c5', text=dic[0][1], anchor='w', command=lambda _col='c5': treeview_sort_column(tree, _col, False))
    tree.heading('c6', text=dic[0][2], anchor='w', command=lambda _col='c6': treeview_sort_column(tree, _col, False))
    tree.heading('c7', text=dic[0][3], anchor='w', command=lambda _col='c7': treeview_sort_column(tree, _col, False))
    tree.heading('c8', text=dic[0][4], anchor='w', command=lambda _col='c8': treeview_sort_column(tree, _col, False))
    return tree

def _cleartmp(tree):
    tree.heading('c4', text='', anchor='w', command=lambda _col='c4': treeview_sort_column(tree, _col, False))
    tree.heading('c5', text='', anchor='w', command=lambda _col='c5': treeview_sort_column(tree, _col, False))
    tree.heading('c6', text='', anchor='w', command=lambda _col='c6': treeview_sort_column(tree, _col, False))
    tree.heading('c7', text='', anchor='w', command=lambda _col='c7': treeview_sort_column(tree, _col, False))
    tree.heading('c8', text='', anchor='w', command=lambda _col='c8': treeview_sort_column(tree, _col, False))
    return tree

def _importgrade(tmp, tree, dic, weight):
    openfile(dic)
    getgrade(tmp, dic, weight)
    tree = showtree(tree, dic)
    # print(dic)
    return tree

def showtree(tree, dic):
    tree = clear(tree)
    maxrow = len(dic)
    for i in range(0, maxrow):
        tree = insert2(tree, dic, i)
    return tree


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    # print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        # print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

