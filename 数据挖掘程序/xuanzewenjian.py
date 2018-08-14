#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：通过打开一个文件对话窗口来选择文件，获得文件路径（包含文件名和后缀）
时间：2017年3月10日 15:40:06
"""

from Tkinter import *
import os
import tkFileDialog
import sys



root = Tk()

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
		print(line)
		
lb = Label(root,text = '')
lb.pack()
btn = Button(root,text=u"弹出选择文件对话框",command=xz)
btn.pack()
root.mainloop()