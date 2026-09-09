def matrixRotation(matrix, r):
    m=len(matrix)
    n=len(matrix[0])
    layers=min(m,n)//2
    for l in range(layers):
        elements=[]
        for i in range(l,n-l):
            elements.append(matrix[l][i])
        for i in range(l+1,m-l-1):
            elements.append(matrix[i][n-l-1])
        for i in range(n-l-1,l-1,-1):
            elements.append(matrix[m-l-1][i])
        for i in range(m-l-2,l,-1):
            elements.append(matrix[i][l])
        rot=r%len(elements)
        elements=elements[rot:]+elements[:rot]
        idx=0
        for i in range(l,n-l):
            matrix[l][i]=elements[idx]
            idx=idx+1
        for i in range(l+1,m-l-1):
            matrix[i][n-l-1]=elements[idx]
            idx=idx+1
        for i in range(n-l-1,l-1,-1):
            matrix[m-l-1][i]=elements[idx]
            idx=idx+1
        for i in range(m-l-2,l,-1):
            matrix[i][l]=elements[idx]
            idx=idx+1
    for row in matrix:
        print(*row)
