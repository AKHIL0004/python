def fibseries(n):
    if n==0:
      print(n)
    if n==1:
        a=0
        b=1
        print(a)
        print(b)
    if n>1:
        a=0
        b=1
        print(a)
        print(b) 
        for i in range(2,n+1):
                c= a+b
                a=b
                b=c
                print(c)
fibseries(50)

        