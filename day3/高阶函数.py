#变量可以指向函数，函数的参数能接受变量，那么一个函数可以 接受另一个函数作为参数，这种函数称为高阶函数
def add(x,y,f):
    return f(x) + f(y)
res = add(3,-6,abs)
print(res)