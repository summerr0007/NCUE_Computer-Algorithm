import math
maxsize = float('inf')


def cM(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]


def fM(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min


def sM(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif(adj[i][j] <= second and
             adj[i][j] != first):
            second = adj[i][j]
    return second


def TSPR(adj, curr_bound, curr_weight,
         level, curr_path, visited):
    global final_res
    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:

            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                cM(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if (adj[curr_path[level-1]][i] != 0 and
                visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= ((fM(adj, curr_path[level - 1]) +
                                fM(adj, i)) / 2)
            else:
                curr_bound -= ((sM(adj, curr_path[level - 1]) +
                                fM(adj, i)) / 2)
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                TSPR(adj, curr_bound, curr_weight,
                     level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp

            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True


def TSP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N
    for i in range(N):
        curr_bound += (fM(adj, i) + sM(adj, i))
    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0
    TSPR(adj, curr_bound, 0, 1, curr_path, visited)


f = open("test.txt", 'r')
text = f.read()
f.close()
list = text.split()
N = int(list[0])
adj = [[0 for i in range(int(N))] for j in range(int(N))]
count = 1
for i in range(int(N)):
    for j in range(int(N)):
        adj[i][j] = int(list[count])
        count = count + 1

final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize
TSP(adj)

print("Order of nodes : ", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')

print("\nMinimum cost :", final_res)
