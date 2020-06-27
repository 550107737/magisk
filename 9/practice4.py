def f(n):
    base=ord("A")
    index=0
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for _ in range(2*i-1):
            print(chr(base+index),end="")
            index+=1
            if index==26:
                index=0
        print()
f(3)