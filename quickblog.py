import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox
import time
import os

# 获取当前的时间
cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
root = tk.Tk()
root.title("创建博客markdown文章")
root.geometry('400x400+600+200') # 400x400为对话框大小 600为向右偏移 200为向下偏移


tk.Label(root, text="title: ").place(x=90, y=30, anchor='ne')
tk.Label(root, text="date: ").place(x=90, y=70, anchor='ne')
tk.Label(root, text="categories: ").place(x=90, y=110, anchor='ne')
tk.Label(root, text="tags: ").place(x=90, y=160, anchor='ne')
tk.Label(root, text="comments: ").place(x=90, y=200, anchor='ne')
tk.Label(root, text="filename: ").place(x=90, y=240, anchor='ne')

title_var = tk.StringVar()
date_var = tk.StringVar()
categories_var = tk.StringVar()
tags_var = tk.StringVar()
comments_var = tk.StringVar()
filename_var = tk.StringVar()

date_var.set(str(cur_time))
comments_var.set("true")

tk.Entry(root, textvariable=title_var, width=40).place(x=90, y=30, anchor='nw')
tk.Entry(root, textvariable=date_var, width=40).place(x=90, y=70, anchor='nw')
tk.Entry(root, textvariable=categories_var, width=40).place(x=90, y=110, anchor='nw')
tk.Entry(root, textvariable=tags_var, width=40).place(x=90, y=160, anchor='nw')
tk.Entry(root, textvariable=comments_var, width=40).place(x=90, y=200, anchor='nw')
tk.Entry(root, textvariable=filename_var, width=40).place(x=90, y=240, anchor='nw')

def get_md_file():
    title = title_var.get()
    date = date_var.get()
    categories = categories_var.get()
    tags = tags_var.get()
    comments = comments_var.get()
    filename = filename_var.get()
    if filename == "":
        filepath = os.path.join(os.getcwd(), title + '.md')
    else:
        filepath = os.path.join(os.getcwd(), filename + '.md')
    fp = open(filepath, 'w')
    fp.write("---\n")
    fp.write("title: {title}\n".format(title=title))
    fp.write("date: {date}\n".format(date=date))
    fp.write("categories: [{categories}]\n".format(categories=categories))
    fp.write("tags: [{tags}]\n".format(tags=tags))
    fp.write("comments: {comments}\n".format(comments=comments))
    fp.write("---\n\n\n\n<!-- more -->\n")
    fp.close()

    messagebox.showinfo(title="创建成功", message="文件被创建在：{filepath}".format(filepath=filepath))
    exit(0) # 创建成功后，直接结束任务。

tk.Button(root, text='创建', command=get_md_file, width=20).place(x=140, y=280)

root.mainloop()
