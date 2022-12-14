name="pallavi"
if name=="pallavi":
    print("You are pallavi")
elif name=="pallavi" or name=="Pallavi":
    print("youu are pallavi")
else:
    print("You are not pallavi")

i=1
while i<10:
    print(i)
    i+=i

for i in range(1,11):
    print(i)
#break keyword
for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)
