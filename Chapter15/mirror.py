

class LookingMe:
    def __enter__(self):
        import sys
        self.origin_wirte=sys.stdout.write
        sys.stdout.write=self.reverse_wirte
        return "SwordLight"

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''

        :param exc_type: 异常类
        :param exc_val: 异常实例
        :param exc_tb: traceback对象
        :return:
        '''
        import sys
        sys.stdout.write=self.origin_wirte
        if exc_type is ZeroDivisionError:
            print("/0 is illegal")
            return True
    def reverse_wirte(self,text):
        self.origin_wirte(text[::-1])

if __name__=="__main__":
    with LookingMe() as me:
        print("I You")
        print(me)
    print("Normal me:")
