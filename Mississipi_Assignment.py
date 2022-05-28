str = input("Enter a string: ")
print("String is ",str)

count = {}
for i in str:
    if i in count.keys():
        count[i] +=1
    else:
        count[i] = 1

for x in count.items():
    print(x[0],':',x[1])
