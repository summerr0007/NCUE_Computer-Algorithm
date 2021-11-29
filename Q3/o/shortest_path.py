import tkinter as tk
from tkinter import filedialog
from tkinter.constants import X
import numpy as np

print("請選擇要開啟的檔案")
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(parent=root,
                filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

f = open(file_path, 'r')
# text = f.readline()
# list = text.split( )
# n = len(list)
# print(text)

inf = 99999999
key_point = 0

text = f.readline()
# 讀入頂點個數，邊個數
# n, m = map(int, text.split(' '))
n = int(text.split()[0])
# print(n)

e = np.zeros((n, n), dtype=int)
# r = np.zeros((11, 11), dtype=float) #路幅
r = [[0.0 for i in range(int(n))] for j in range(int(n))]  # 路幅
# t = np.zeros((11, 11), dtype=np.string_) #通行種類
t = [['0' for i in range(int(n))] for j in range(int(n))]  # 通行種類

# 初始化
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            e[i][j] = 0
        else:
            e[i][j] = inf

# 讀入邊
# for i in range(1, m+1):
#     text = f.readline()
#     t1, t2, t3 = map(int, text.split(' '))
#     e[t1][t2] = t3

# for i in range(1, m+1):
while 1:
    text = f.readline()
    if text:
        list = text.split()
        tmp = len(list)
        if int(list[0])==int(list[1]):
            print("不允許self-loop!")
            exit(1)
        if int(list[2])<=0 or float(list[3])<=0:
            print("距離、路幅值需均為正實數，不可以有負數或0!")
            exit(1)
        if int(list[0])>=n or float(list[1])>=n:
            print("不符規定的節點編號!")
            exit(1)
        # print(int(list[0]))
        # print(int(list[1]))
        # print(int(list[2]))
        if tmp == 5:
            e[int(list[0])][int(list[1])] = int(list[2])
            r[int(list[0])][int(list[1])] = float(list[3])
            t[int(list[0])][int(list[1])] = list[4]
        elif tmp == 4:
            e[int(list[0])][int(list[1])] = int(list[2])
            r[int(list[0])][int(list[1])] = float(list[3])
            t[int(list[0])][int(list[1])] = "0"
    else:
        break
print("請輸入 來源節點:")
while 1:
    s = int(input())
    if s<0 or s>=n:
        print("請重新輸入正確範圍!")
    else:
        break

print("請輸入 目的節點:")
while 1:
    d = int(input())
    if d<0 or d>=n:
        print("請重新輸入正確範圍!")
    else:
        break

print("請輸入 交通方式:")
while 1:
    typ = int(input())
    if typ<1 or typ>5:
        print("請重新輸入正確範圍!")
    else:
        break

key_point = s
#typ=交通方式 typn=該交通方式最低路幅限度
if typ == 5:
    typn = 6
elif typ ==4:
    typn = 4
elif typ ==3:
    typn = 2
elif typ ==2:
    typn = 1.5
elif typ ==1:
    typn = 0.5  
for i in range(0, n):
    for j in range(0, n):
        if typn>r[i][j] and r[i][j]!=0.0:
            e[i][j] = inf
        if t[i][j]!="0":
            if t[i][j][5-typ] == "0":
                e[i][j] = inf  
# 初始 dis 陣列，從 key_point 到其餘各點的初始路程
dis = np.zeros(n, dtype=int)
path = np.zeros(n, dtype=int)
for i in range(0, n):
    dis[i] = e[key_point][i]
    path[i] = key_point if(dis[i] < inf and dis[i] != 0) else -1
# 初始 book 陣列
book = np.zeros(11, dtype=int)
book[key_point] = 1
print(path)
print(f"book\n{book}")
# Dijkstra Algorithm
for i in range(1, n):
    # 找到離 key_point 點最近的頂點
    min = inf
    for j in range(0, n):
        if book[j] == 0 :
            uu = j
            if dis[j] < min:
                min = dis[j]
                u = j
    if min == inf:
        u = uu  
    book[u] = 1
    for v in range(0, n):
        # if e[u][v] < inf:
        if not (book[v]):
            if dis[v] > dis[u] + e[u][v]:
                dis[v] = dis[u] + e[u][v]
                path[v] = u

answer = []


# 輸出
print(dis[d])
# for i in range(0, n):
#     print(dis[i])
# for i in range(0, 6):
#     print(path[i])


def find(x,ans):
    if path[x] == key_point:
        ans += str(key_point)
        print(key_point)
    else:
        find(path[x],ans)
    
    ans += str(x)
    print(" -> "+str(x))
    print(r[path[x]][x])
    print(t[path[x]][x])




pat = 't2_out.txt'
f = open(pat, 'w')
if dis[d] == inf:
    f.write('無法到達!')
else:
    find(d,answer)
    f.write('最短路徑: '+str(answer))
    f.write('\n\n總距離: '+str(dis[d]))
    f.write('\n\n路徑資訊: ')
    for i in range(0,len(answer)-1):
        if str(t[int(answer[i])][int(answer[i+1])]) != "0":
            f.write('\n'+str(answer[i])+" "+str(answer[i+1])+" "+str(e[int(answer[i])][int(answer[i+1])])+" "+str(r[int(answer[i])][int(answer[i+1])])+" "+str(t[int(answer[i])][int(answer[i+1])]))
        else:
            f.write('\n'+str(answer[i])+" "+str(answer[i+1])+" "+str(e[int(answer[i])][int(answer[i+1])])+" "+str(r[int(answer[i])][int(answer[i+1])]))
f.close()
  