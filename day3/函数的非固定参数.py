def test(x,y=2):
    print(x)
    print(y)
test(1,3)
test(3,y=109)
#test(2,y=100)
#默认参数特点：调用函数的时候，默认参数非必须传递
#用途：
def test1(x,*args):
    print(x)
    print(args)
test1(1,2,3,6,7,8)