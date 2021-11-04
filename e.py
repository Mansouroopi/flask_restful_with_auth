from functools import wraps
def dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        s,h,w = args
        h,w = w,h
        s = '*'
        args = s,h,w
        func(*args, **kwargs)
    return inner

@dec
def drawshepe(s, h, w):
    print(s*w)
    for i in range(h-2):
        print(s+' '*(w-2)+s)
    print(s*w)

if __name__=='__main__':
    drawshepe("#", 10, 26)
