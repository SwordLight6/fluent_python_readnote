


'''
def simple_coroutine():
    print("-> coroutine start")
    x=yield
    print("->coroutine stop")

my_cor=simple_coroutine()
my_cor
<generator object simple_coroutine at 0x7f94702d7c10>
next(my_cor)
-> coroutine start
my_cor.send(100)
Traceback (most recent call last):
->coroutine stop
  File "<input>", line 1, in <module>
StopIteration
import inspect
inspect.getgeneratorstate(my_cor)
'GEN_CLOSED'
'''
def simple_coroutine():
    print("-> coroutine start")
    x=yield
    print("->coroutine stop")


'''
def simple_coroutine2(a):
    print("-> Start:a:{}".format(a))
    b=yield a
    print("->Received:b:{}".format(b))
    c=yield a+b
    print("->Received:c:{}".format(c))
    
my_cor2=simple_coroutine2(97)
next(my_cor2)
-> Start:a:97
97
my_cor2.send(3)
->Received:b:3
100
my_cor2.send(4)
->Received:c:4
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration'''
def simple_coroutine2(a):
    print("-> Start:a:{}".format(a))
    b=yield a
    print("->Received:b:{}".format(b))
    c=yield a+b
    print("->Received:c:{}".format(c))



if __name__=='__main__':
    my_cor=simple_coroutine()


