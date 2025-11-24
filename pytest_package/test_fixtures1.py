def outer(func):
    def wrapper(*args,**kwargs):
        print('good morning')
        func(*args,**kwargs)
        print('good evening')

    return wrapper()

@outer
def add(a,b,c):
    print(a+b+c)

add(1,2,3)
