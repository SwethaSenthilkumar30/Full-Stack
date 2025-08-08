s1=input("Enter first string: ")
s2=input("Enter second string: ")
if s1==s2:
    print("Both string are equal")
else:
    print("Both string are not same")

print("-----------")

a=10
if a>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

print("------------")

a=10
if a % 2 ==0:
    print("even")
else:
    print("odd")

print("----------------")

for i in range (0,101):
    if i % 2==0:
        print(i,end=" ")

print("-------------")

sum_odd=0
for i in range (0,101):
    if i % 2 !=0:
        sum_odd += i
print(sum_odd)

print("------------------")

count_even=0
for i in range (1,101):
    if i % 2==0:
        count_even+=1
print(count_even)

print("---------------")

def factorial (n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

number=input("enter factorial number:")

def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series


























