import logging
from os import path
import sys
import numpy as np
import math

from numpy.core.fromnumeric import size

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") 
handler.setFormatter(formatter)

logger.addHandler(handler)

class filereader:
    def __init__(self,path) -> None:
        self.path = path

    def __call__(self):
        try:
            self.testfile = open(self.path,"r")
            lines = self.testfile.readlines()
            lines = [ line.strip().split(' ') for line in lines]
            self.testfile.close()
            return lines
        except Exception as e:
            logger.critical(e)
            exit()

class Graph:
    def __init__(self) -> None:
        self.width = {5:6,4:4,3:2,2:1.5,1:0.5}
        self.dis=[]
        self.path=[]
        self.book=[]
        self.ans=[]
        self.stro='最短路徑 :\n'

    def setVehicle(self,v):
        self.vehicle = v

    def setStart(self,s):
        self.start = s

    def setEnd(self,e):
        self.end = e

    def readGraph(self,f:filereader):
        lists = f()
        self.vex = int(lists[0][0])
        lists = lists[1:]
        self.arcs = np.full((self.vex,self.vex),math.inf)
        # for i in range(self.vex):
        #     self.arcs[i][i]=0
        for i in lists:
            i[0]=int(i[0])
            i[1]=int(i[1])
            i[2]=float(i[2])
            i[3]=float(i[3])
            if(len(i)==5):
                i[4]=int(i[4])
            if i[0]==i[1]:
                logger.critical("self-loop")
                exit()
            if i[0]> self.vex or i[1] > self.vex:
                logger.critical("node number error")
                exit()
            if i[2]<= 0 or i[3] <= 0 :
                logger.critical("value error")
                exit()
            if self.width[self.vehicle] <= i[3]:
                if len(i) == 5:
                    pa = str(i[4])[::-1]
                    if len(pa) >= self.vehicle and pa[self.vehicle-1] == '1':
                        self.arcs[i[0]][i[1]] = i[2]
                    else:
                        self.arcs[i[0]][i[1]] = math.inf
                else:
                    self.arcs[i[0]][i[1]] = i[2]
            else:
                self.arcs[i[0]][i[1]] = math.inf
        
    def pullout(self):
        f= open("t2_out.txt",'w')
        logger.debug(f'path = \n{self.path}')
        if not self.dis[self.end] == math.inf:
            self.find(self.end)
            # print(self.stro)
            self.stro+=f'\n總距離: {self.dis[self.end]}'
            self.stro+="\n路徑資訊:"
            lists = filereader("test3.txt")()
            for list in lists:
                for q in range(len(self.ans)-1):
                    if int(list[0]) == self.ans[q] and int(list[1]) == self.ans[q+1]:
                        self.stro+=f'\n{list}'
        else:
            self.stro = "無法到達"
        print(self.stro)
        f.write(self.stro)
        f.close()
        
        

    def find(self,x):
        if self.path[x] == self.start:
            self.ans.append(self.start)
            self.stro += f'{self.start}'
        else:
            self.find(self.path[x])
        
        self.ans.append(x)
        self.stro += f' -> {x}'
class Dijkstra:  
    def __init__(self) -> None:
        pass
    def __call__(self, g:Graph):
        self.dis=[0 for i in range(g.vex)]
        self.path=[0 for i in range(g.vex)]
        self.book=[False for i in range(g.vex)]
        for i in range(g.vex):
            self.dis[i] =g.arcs[g.start][i]
            self.path[i] =  g.start if(self.dis[i] < math.inf and self.dis[i] != 0) else -1
        logger.debug(f'\n{g.arcs}')
        logger.debug(f'\n{self.path}')
        
        self.book[g.start] = True
        self.dis[g.start] = 0
        logger.debug(f'\n{self.book}')
        for i in range(g.vex):
            min = math.inf
            u=1
            logger.debug(f'g.vex = {g.vex}')
            for j in range(1,g.vex):
                if (not self.book[j]):
                    uu=j
                    logger.debug(f'uu = {uu}')
                    if(min > self.dis[j] ):
                        min = self.dis[j]
                        u = j
            if min == math.inf:
                u =uu
            self.book[u] =True
            for j in range(g.vex):
                if((not self.book[j] )and self.dis[j] > self.dis[u]+g.arcs[u][j]):
                    self.dis[j] = self.dis[u]+g.arcs[u][j]
                    self.path[j] =u
        
        g.dis = self.dis
        # logger.debug()
        g.path = self.path
        g.book = self.book



if __name__ == '__main__':
    try:
        s,d,v=input("source destination vehicle\n").split(' ')
    except Exception as e:
        logger.critical(e,)
        exit()
    f = filereader("test3.txt")
    gap = Graph()
    gap.setStart(int(s))
    gap.setEnd(int(d))
    gap.setVehicle(int(v))
    gap.readGraph(f)
    dd = Dijkstra()
    dd(gap)
    gap.pullout()