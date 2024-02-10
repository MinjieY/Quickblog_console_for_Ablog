import tkinter as tk
from tkinter import messagebox
import time
import os
import sys
import json

cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
timeline_filepath = "xxx/timeline.json"
root = tk.Tk()
root.title("创建博客timeline事件")
root.geometry('300x300+600+200')


tk.Label(root, text="date: ").place(x=70, y=30, anchor='ne')
tk.Label(root, text="content: ").place(x=70, y=70, anchor='ne')

date_var = tk.StringVar()

date_var.set(str(cur_time))

tk.Entry(root, textvariable=date_var, width=28).place(x=70, y=30, anchor='nw')
content_var = tk.Text(root, width=28, height=12)
content_var.place(x=70, y=70)

def get_md_file():
    date = date_var.get()
    content = content_var.get(1.0, "end")
    with open(timeline_filepath, "rt", encoding='utf-8') as fp:
        load_dict = json.load(fp)
        load_dict.insert(0, {'date': date, 'content': content})
        with open(timeline_filepath, "wt", encoding='utf-8') as f:
            json.dump(load_dict, f, indent=4, ensure_ascii=False)
        f.close()
        fp.close()

    messagebox.showinfo(title="添加成功", message="date: {date}content：{content}".format(date=date, content=content))
    sys.exit(0)

tk.Button(root, text='创建', command=get_md_file, width=10).place(x=190, y=240)

root.mainloop()
