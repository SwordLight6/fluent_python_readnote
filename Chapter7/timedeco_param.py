import time
DEFAULT_FMT="[{elapsed:0.8f}s] {name}(args) -> {result} hhh"
def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args):
            t0=time.time()
            _result=func(*args)
            elapsed=time.time()-t0
            name=func.__name__
            args=",".join(repr(arg) for arg in args)
            result=repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

if __name__=="__main__":
    @clock()
    def snooze(second):
        time.sleep(second)
    snooze(1)




