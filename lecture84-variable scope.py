def func():
    global x
    x=7
    return x
print(func())
x=5
def func2(x):
    print(x)
func2()
