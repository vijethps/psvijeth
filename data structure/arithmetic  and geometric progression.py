n=int(input())
start=2
diff=3
list=[start]
for i in range(0,n-1):
    list.append(list[i]+diff)
print(list)
print(sum(list))


n=10
start=2
diff=3
list=[start]
for i in range(0,n-1):
    list.append(list[i]*diff)
print(list)
print(sum(list))
