name=input("Enter your name")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp+=name[i]
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
