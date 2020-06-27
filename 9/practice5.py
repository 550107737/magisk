def f(n):
    base=ord("A")
    index=0
    for i in range(1,n+1):
        str1=""
        for _ in range(15):
            str1+=chr(base+index)
            index+=1
            if index==26:
                index=0
        if i % 2 == 1:
            print(str1)
        else:
            print(str1[::-1])
f(9)