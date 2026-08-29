def encryption(s):
    s=s.replace(" ","")
    n=len(s)
    r=int(math.sqrt(n))
    c=r
    if r*c<n:
        c=c+1
        r=r+1
    result=""
    for j in range(c):
        for i in range(r):
            k=i*c+j
            if k<n:
                result=result+s[k]
        result=result+" "
    return resultS