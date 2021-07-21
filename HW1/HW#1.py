#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from collections import Counter
from pyecharts.charts import Bar,Line


def DrawB(keyList,valueList):
    
        
        bar=Bar()
        bar.add_xaxis(keyList)
        bar.add_yaxis("關鍵字統計",valueList)
        bar.render("Freq.html")
        
def DrawL(keyList,valueList)->Line:
    
        line=Line()
        line.add_xaxis(keyList)
        line.add_yaxis("TF/IDF統計",valueList)
        line.render("TFIDF.html")
    
def Jieba_TFIDF():
    
    sentence=open("hw1-dataset.txt","rb").read()
    keywords=jieba.analyse.extract_tags(sentence,topK=100,withWeight=True,allowPOS=())
    keyList=[n for n in range(1,100)]
    valueList=[]
    print('\nTF/IDF結果:')
    i=1
    for item in keywords:
        print(i,item[0],item[1])
        i+=1
        valueList.append(item[1])
    DrawL(keyList,valueList)
        
def Jieba_Freq():
    
    cut_words=""
    for line in open('hw1-dataset.txt',encoding='utf-8'):
        line.strip('\n')
        line=re.sub("[\'\: \·\—\\.\，\。\“ \”\n\u3000\？\、\'*\',\']", "", line)
        seg_list=jieba.cut(line,cut_all=False)
        cut_words+=(" ".join(seg_list))
    all_words=cut_words.split()
    c=Counter()
    total=0
    for x in all_words:
        if len(x)>1 and x!= '\r\n':
            c[x]+=1
            total+=1        
    print('\n頻率結果:')
    dict={}
    
    i=1
    for(k,v) in c.most_common(100):
        dict[k]=v
        print("%d.%s:%f"%(i,k,v/total))
        i+=1
    keyList=[n for n in range(1,100)]
    valueList=[]
    for k,v in dict.items():
        valueList.append(v/total)
    DrawB(keyList,valueList)

if __name__ == "__main__":

    Jieba_Freq()
    Jieba_TFIDF()


# In[ ]:




