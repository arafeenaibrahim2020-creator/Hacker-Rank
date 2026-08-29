def organizingContainers(container):
    n=len(container)
    container_sum=[]
    for i in range(n):
        container_sum.append(sum(container[i]))
    type_sum=[0]*n
    for i in range(n):
        for j in range(n):
            type_sum[j]=type_sum[j]+container[i][j]
    container_sum.sort()
    type_sum.sort()
    if container_sum==type_sum:
        return "Possible" 
    else:
        return "Impossible"