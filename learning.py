
a = 2
b= 2
print(a+b)
###########################################

a = 2
b = 4

result = a*b
print(result)

####################################################

def simple_decorator(func):
    def wrapper(*args,**kwargs):
        print('before the function')
        result = func(*args,*kwargs)
        print('after the function')
        return result
    return wrapper()

@simple_decorator
def hallo(name):
    print('hallo',{name})

 hallo("alice")
