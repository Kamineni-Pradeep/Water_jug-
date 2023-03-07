jug1,jug2=int(input("Enter high capacity : ")),int(input("Enter low capacity : "))
goal=int(input("Enter goal: "))
a=b=0
x=[]
if jug1>jug2:
        a=jug1
        x.append((a,b))
        y=jug2
        if a>b:
                a-=jug2
                x.append((a,b))
                b=a
                a=0
                x.append((a,b))
                a=jug1
                x.append((a,b))
                a=jug1-jug2+b
                b=jug2
                x.append((a,b))
                b=0
                x.append((a,b))
        if a==goal:
                print(x)		
else:
        print("Not possible")              
        