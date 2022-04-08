import os
import webbrowser

def _help():
    title= os.getcwd()
    print(title)
    webbrowser.open(title+'\使用手册.docx')