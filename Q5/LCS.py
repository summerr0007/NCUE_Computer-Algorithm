
form = [[]]


n=0
alen=0
if __name__ == "__main__":
    print("please enter two string")
    s1,s2 = input().split()

    arr = [ [0 for i in range(len(s1)+1)] for j in range(len(s2)+1) ]

    tout = "\t\t"
    for i in s2:
        tout += f"{i}\t"
    print(tout)
    tout='\t'
    for i in range(len(s2)+1):
        tout += "0\t"
    print(tout)
    # print(arr)
    
