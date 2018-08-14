#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *           # 导入 Tkinter 库
import os
import tkFileDialog
import sys
name=r""

root = Tk()                     # 创建窗口对象的背景色
root.title("数据挖掘算法实现")
root.geometry('500x600')                 #是x 不是*
root.resizable(width=True, height=True) #宽不可变, 高可变,默认为True

view = Frame(root)
var = StringVar()
e = Entry(view,textvariable = var)
var.set("hello")
e.pack()

def seeview(a):
    t.insert('0.0',a)
t = Text()
t.pack()

def chooseFile():
    global name
    default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录
    filename = tkFileDialog.askopenfilename(title=u"选择文件")
                                     
    if filename != '':
        lb.config(text = u"您选择的文件是："+filename);
    else:
        lb.config(text = u"您没有选择任何文件");
    name = filename
    filea = open(filename)
    lines = filea.readlines()
    for line in lines:
        seeview(line)
        seeview( "\n")

def dealwith():
    """
    Test
    """
    data_set = loadDataSet()
#    seeview(data_set)
    L, support_data = generate_L(data_set, k=2, min_support=0.2)
#    seeview(L)
    big_rules_list = generate_big_rules(L, support_data, min_conf=0.7)
    for Lk in L:
        seeview( "~"*50),
        seeview( "\n")
        seeview(str(len(list(Lk)[0])) + "-itemsets\tsupport" +  "\t\tfrequent ")
        seeview( "\n")
        for freq_set in Lk:
            seeview(str(support_data[freq_set])),
            seeview(freq_set),
            seeview( "\n")
    seeview( "\n")
    seeview("Big Rules")
    seeview( "\n")
    for item in big_rules_list:
        seeview(str(item[2])+"\t"),
        seeview(str(item[1])+ "conf: "+"\t"), 
        seeview(str(item[0])+ "==>"+"\t"),
        seeview( "\n")

def loadDataSet():   #读取数据（这里只有两个特征）
    dataMat = []
    labelMat = []
    fr = open(name)
    for line in fr.readlines():
        lineArr = line.strip().split()
        try:
            dataMat.append([str(lineArr[0]), str(lineArr[1]),str(lineArr[2])])
        except:
            dataMat.append([str(lineArr[0]), str(lineArr[1])])
    return dataMat

def create_C1(data_set):
    """
    通过扫描数据集，创建频繁候选对象1-itemset C1 
    输入:
        data_set: 事务列表。每个事务包含若干项。
    输出:
        C1:包含所有频繁候选项集的集合
    """
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


    """
    判断是否有候选频繁k项集满足Apriori性质。
    """
def is_apriori(Ck_item, Lksub1):
    """
    输入:
        Ck_item: a frequent candidate k-itemset in Ck which contains all frequent
                 candidate k-itemsets.
        Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
    """
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True
    """
    输出:
        True: satisfying Apriori property.
        False: Not satisfying Apriori property.
    """

    """
    创建Ck, 包含所有频繁候选k项集的集合
    通过LK-1自己的连接操作。

    """
def create_Ck(Lksub1, k):
    """
    输入:
        Lksub1:LK-1，包含所有频繁候选（K-1）项集的集合。
        k:频繁项集的项的数量。
    """
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]: # 修剪	
                Ck_item = list_Lksub1[i] | list_Lksub1[j] 
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    """
    输出:
        Ck:包含所有频繁候选k项集的集合。
    """
    return Ck


    """
    通过从CK执行删除策略生成LK。
    """
def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    """
    输入:
        data_set:
        Ck:事务列表。每个事务包含若干项。
        min_support:最小支持度。
        support_data:一个字典，关键是频繁项集，值是支持度。
    """
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    """
    输出:
        Lk:它包含了所有的频繁项集的所有k-项集。
    """
    return Lk


    """
    生成所有的频繁项集。
    """
def generate_L(data_set, k, min_support):
    """
    输入:
        data_set:事务列表。每个事务包含若干项。
        k:所有频繁项的最大相数目
        min_support:最小支持度。
    """
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k+1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    """
    输出:
        L: LK的列表。
        support_data:一个字典，关键是频繁项集，值是支持度。
    """
    return L, support_data

    """
    从大的频繁项集产生的规则集。
    """
def generate_big_rules(L, support_data, min_conf):
    """
    输入:
        L: LK的列表。
        support_data:一个字典，关键是频繁项集，值是支持度。
        min_conf: 最小置信度
    """
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    """
    输出:
        big_rule_list: 一个包含所有大规则的列表。每个大的规则表示为2元组。
    """
    return big_rule_list



lb = Label(root,text = '')
lb.pack()
btn = Button(root,text=u"选择文件",command=chooseFile)
btn.pack()


Button(root, text="处理", command = dealwith).pack()

root.mainloop()                 # 进入消息循环