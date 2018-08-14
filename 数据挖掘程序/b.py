#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：通过打开一个文件对话窗口来选择文件，获得文件路径（包含文件名和后缀）
时间：2017年3月10日 15:40:06
"""

import os
import tkFileDialog

default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
fname = tkFileDialog.askopenfilename(title=u"选择文件",
                                     initialdir=(os.path.expanduser(default_dir)))

print fname  # 返回文件全路径
print tkFileDialog.askdirectory()  # 返回目录路径