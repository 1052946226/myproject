#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *           # 导入 Tkinter 库
import os
import tkFileDialog
import sys

root = Tk()                     # 创建窗口对象的背景色
root.title("数据挖掘算法实现")
root.geometry('500x600')                 #是x 不是*
root.resizable(width=True, height=True) #宽不可变, 高可变,默认为True

view = Frame(root)
var = StringVar()
e = Entry(view,textvariable = var)
var.set("hello")
e.pack()

def printhello(a):
    t.insert('1.0',a)
    
t = Text()
t.pack()
Button(root, text="press", command = printhello).pack()

def xz():

	default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
	filename = tkFileDialog.askopenfilename(title=u"选择文件",initialdir=(os.path.expanduser(default_dir)))
									 
	if filename != '':
		lb.config(text = u"您选择的文件是："+filename);
	else:
		lb.config(text = u"您没有选择任何文件");
	print filename  # 返回文件全路径
	print tkFileDialog.askdirectory()  # 返回目录路径
	filea = open(filename)
	lines = filea.readlines()
	
	for line in lines:
		printhello(line)
#		print(line)
		
lb = Label(root,text = '')
lb.pack()
btn = Button(root,text=u"弹出选择文件对话框",command=xz)
btn.pack()

frm = Frame(root)
Label(frm, text="算法名：", bg="pink", font=("Arial", 12), width=15, height=2).pack(side=TOP)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
#left
frm_L = Frame(frm)
Label(frm_L, text='厚德', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='博学', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='敬业', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='乐群', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

                                # 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
listb2 = Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()                 # 进入消息循环