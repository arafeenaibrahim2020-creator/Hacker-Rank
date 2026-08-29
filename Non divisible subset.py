def nonDivisibleSubset(k, s):
    count=[0]*k
    for num in s:
        count[num % k]=count[num % k]+1
    result=0
    if count[0]>0:
        result=result+1
    for i in range(1,(k+1)//2):
        if i==k-i:
            result=result+1
        else:
            result=result+max(count[i],count[k-i])
    return result