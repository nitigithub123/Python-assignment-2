s1=int(input("enter side 1 :"))
s2=int(input("enter side 2 :"))
s3=int(input("enter side 3 :"))
d=s1>s2+s3
e=s2>s1+s3
f=s3>s2+s1
while d==True or e==True or f==True:
    print("no")
    break
print("yes")