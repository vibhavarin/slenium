def greet(func):
    def wrappers(*args,**kwargs):
        print('good morning')
        return func(*args,**kwargs)
    return wrappers()

@greet
def piku():
    print('hi,how are you?')
piku()
@greet
def vibha():
    print('hi,how are you?')
vibha()


