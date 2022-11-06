from operator import le


a=[10,25,30,35,6,59,75,32,105]
s=0
t=0
ss=0
for i in range(1,len(a)-1):
    if a[i]>a[i+1]:
        print(a[s])
        t=a[i]-a[s]
        tem=a[s]
        a[s]=a[i]
        a[i]=tem
        print(a)
        ss=ss+t
        s=i+1
       # i=i+1
ss=ss+a[len(a)-1]-a[len(a)-2]
print(ss)