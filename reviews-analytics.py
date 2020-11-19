# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:06:27 2020

@author: Linter
"""
data = []
sum_line = 0
with open  ("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        
    print("總共有", len(data),"筆留言")
    
for d in data:
    sum_line += len(d)
    
print("平均留言長度為", int(sum_line / (len(data))),"個字")