def search(p, sheep, wolf, info, tree, path):
    if info[tree[p][0]] == 0 and info[tree[p][1]] == 0:
        sheep += 2
        path.append(tree[p][0])
        path.append(tree[p][1])
        p = tree[p][1]
    elif info[tree[p][0]] == 0 and info[tree[p][1]] == 1:
        sheep += 1
        path.append(tree[p][0])
        p = tree[p][1]
    elif 

def solution(info, edges):
    answer = 0
    sheep = 1
    wolf = 0
    p = 0
    path = []

    tree = [[] * 11]
    for i in range(len(edges)):
        tree[edges[i][0]].append(edges[i][1])
    
    search(0, sheep, wolf, info, tree, path)
    
    return answer