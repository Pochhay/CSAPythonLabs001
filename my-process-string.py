# application 1
user = input("enter a word:")
list1 = list(user)
a = len(list1)
for i in range(a):
    print(list1[i]*2, end="")
print()

#application 2
alpha = "abcdefghijklmnopqrstuvwxyz"
user = input("Enter a range of letters (e.g., a-z):")
start, end = user.split("-")
a = alpha.index(start)
b = alpha.index(end)
print(alpha[a:b+1])
