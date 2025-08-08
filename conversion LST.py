l=[10,20,30]
t=(40,50,60)
s={70,80,90}

print(type(l))
print(type(t))
print(type(s))

print("----------------")
a=list(l)
b=list(t)
c=list(s)

print("----------------")
a1=tuple(l)
b1=tuple(s)
c1=tuple(t)

print("----------------")
a2=set(l)
b2=set(s)
c2=set(t)
print("-----------------")

l=["ram","raj",9865438967]
print(l[0])

l=[["ramu","tena",9865438967],
   ["ram","raj",9865478967],
   ["raj","ram",9865412967]]

print(l[0])
print(l[0][2])

for i in l:
    for j in i:
        print(j)


print("----------------------")
d={"fname":"ram","lname":"raj","ph":1234567890}
print(d.get("ph"))

l=[{"fname":"ram","lname":"raj","ph":1234567890}]
print(l[0])
print(l[0],["fname"])

l=[{"fname":"ram","lname":"raju","ph":1234567890},
    {"fname":"ramu","lname":"raj","ph":1234565690},
    {"fname":"raju","lname":"ramu","ph":1234567845}]

print(l[1])
print(l[1]["ph"])

for i in l:
    for j in i.items():
        print(j)



















