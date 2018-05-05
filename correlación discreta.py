#h=[0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0]
#x=[0,0,1,1,1,1,1,1,0,0,0]
h=[1,2,1,-1]
x=[1,2,3,1]
#h=[1,2,3,2,1]
#x=[1,2,3,2,1]
h.reverse()

Y=[]

if(len(h)>len(x)):
    for i in range(0,len(h)-len(x)):
        x.append(0)

if(len(x)>len(h)):
    for i in range(0,len(x)-len(h)):
        h.append(0)

if(len(h)==len(x)):
    for i in range(0,len(h)):
        tmp=0
        for j in range(0,i+1):
            tmp=tmp+x[j]*h[i-j]
        Y.append(tmp)
    for i in range(1,len(x)):#va saliendo
        tmp=0
        for j in range(i,len(x)):#j=1,2,3 x[j]
            tmp=tmp+(x[j]*h[(i-j)-1])
        Y.append(tmp)

print(Y)
