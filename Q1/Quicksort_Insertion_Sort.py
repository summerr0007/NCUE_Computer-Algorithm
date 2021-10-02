import logging
import sys

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
            return self.testfile.read().split(" ")
        except Exception as e:
            logger.critical(e)
            exit()
        

class QuickSort:
    def __init__(self,sortlist:list) -> None:
        self.sortlist = sortlist

    def swap(self,a,b):
        temp = self.sortlist[a]
        self.sortlist[a] = self.sortlist[b]
        self.sortlist[b] = temp

    def partition(self,f,e):
        p = self.sortlist[e]
        i = f-1
        for j in range(f,e):
            if self.sortlist[j] < p:
                i=i+1
                self.swap(i,j)
        i=i+1
        self.swap(i,e)
        return i

    def sort(self,f,e):
        if f<e:
            p = self.partition(f,e)
            self.sort(f,p-1)
            self.sort(p+1,e)
        return self.sortlist

class Insertionsort:
    def __init__(self,sortlist:list) -> None:
        self.sortlist = sortlist
        logger.debug(self.sortlist)
    def sort(self): 
        self.sorted = self.sortlist         
        for i in range(1,len(self.sorted)):
            key = self.sorted[i]
            j = i-1
            while key < self.sorted[j] and j >= 0 :
                self.sorted[j+1] = self.sorted[j]
                j=j-1

            self.sorted[j+1] =key
            
        return self.sorted

if __name__ == "__main__":
    print("1執行快速排序法，2執行插入排序法，3程式結束")
    ch = input()
    f =  filereader("test1.txt")
    if ch == '1':
        i=QuickSort(f())
        r = i.sort(0,len(i.sortlist)-1)
        print(i.sortlist)
        print(f'len = {len(r)}')
        print(f'max = {r[-1]}')
        print(f'min = {r[0]}')
    elif ch == '2' :
        i=Insertionsort(f())
        r = i.sort()
        print(i.sort())
        print(f'len = {len(r)}')
        print(f'max = {r[-1]}')
        print(f'min = {r[0]}')

    else :
        print('bye')

