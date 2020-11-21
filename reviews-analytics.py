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
        if len(data) % 100000 == 0:
            print("讀取了", len(data), "筆留言")
        
    print("總共有", len(data),"筆留言")
    
#利用字典來個字數的統計
wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1    
        else:
            wc[word] = 1
            
#查詢字的出現次數
while True:
    word = input("請輸入查詢單字")
    if word == "q":
        break
    if word in wc:
        print(word, "這單字有",wc[word],"次")
    else:
        print("這字沒出現過喔")
    
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
        


for d in data:
    sum_line += len(d)     
print("平均留言長度為", int(sum_line / (len(data))), "個字")


new = []
#new = [d for d in data if len(d) < 100] 為下面的縮寫
for d in data:
    if len(d) < 100:
        new.append(d)
print("留言小於一百個字有", len(new), "筆")

good = []
for d in data:
    if "good" in d:
        good.append(d)
print("Good的留言有", len(good), "筆")


