#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# encoding=utf-8
import string
import jieba
import jieba.analyse

f=open("hw1-dataset.txt", "r" ,encoding = "utf8")
lines=f.readlines()

for i in range(0,lines.__len__(),1):
    
    list=[]
    for word in lines[i].split():
        word=word.strip(string.whitespace)
        list.append(word);
    for line in list:
        seg_list=jieba.cut(line,cut_all=False)
        print("Default Mode: " + "/ ".join(seg_list))

f.close()

"""f=open("hw1-dataset.txt", "r" ,encoding = "utf8")
for lines in f.readlines():
    seg_list=jieba.cut(lines,cut_all=False)
#    print("Default Mode: " + "/ ".join(seg_list))
f.close()"""


# In[ ]:




