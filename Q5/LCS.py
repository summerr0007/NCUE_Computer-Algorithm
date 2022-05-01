
form = [[0 for i in range(50)] for j in range(50)]

lcs = []

alen = 0
nag =0

def LCS(i, j,na):
    if na == alen:
        return
    if form[i][j] == 1:
        lcs.append(s1[i-1])
        na += 1
        LCS(i - 1, j - 1,na)
    elif form[i][j] == 2:
        LCS(i, j-1,na)
    else:
        LCS(i-1, j,na)


if __name__ == "__main__":
    nag =0
    print("please enter two string")
    s1, s2 = input().split()	
    
    arr = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]

    tout = "\t\t"
    for i in s2:
        tout += f"{i}\t"
    print(tout)
    tout = '\t'
    for i in range(len(s2)+1):
        tout += "0\t"
    print(tout)
    # print(arr)

    for i in range(1, len(s1)+1):
        print(f"{s1[i-1]}\t0\t", end='')
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
                print(f"{arr[i][j]}\t", end='')
                form[i][j] = 1
            else:
                if arr[i][j - 1] >= arr[i - 1][j]:
                    arr[i][j] = arr[i][j - 1]
                    print(f"{arr[i][j-1]}\t", end='')
                    form[i][j] = 2
                else:
                    arr[i][j] = arr[i - 1][j]
                    print(f"{arr[i][j]}\t", end='')
                    form[i][j] = 3
        print("")
    
    alen = arr[len(s1)][len(s2)]
    LCS(len(s1), len(s2),nag)
    print("LCS is ")
    lcs.reverse()
    print(''.join(lcs))
