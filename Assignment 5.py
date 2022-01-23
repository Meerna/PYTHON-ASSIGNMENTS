#1
for i in range(1,20,2):
    print(i)
    
#2
j=[1]
for i in j:
    j.append(i+1)
    print(i)

#3
X=("telephone","ringing")
a=list(X)
a.append("now")
print(a)
X=tuple(a)
print(X) 

