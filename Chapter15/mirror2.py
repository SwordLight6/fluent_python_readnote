import contextlib
'''
使用contextmanager 来实现上下文处理
'''
@contextlib.contextmanager
def looking_glass():
    import sys
    original_write=sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write=reverse_write
    msg=''
    try:
        yield "SwordLight" # 绑定到as后面 然后停下来
    except ZeroDivisionError:
        msg="/0 is illegal"
    finally:
        sys.stdout.write=original_write
        if msg:
            print(msg)
if __name__=='__main__':
    with looking_glass() as me:
        print("I You")
        print(me)
    print("Normal me:")
