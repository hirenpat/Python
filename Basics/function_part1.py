
def hello():
    pass

def hello_world():
    print('Hello World!')

def hello_world_return():
    return 'Hello World Return!'

def hello_func(greeting):
    return '{} There.'.format(greeting)

print(hello_func('Hey'))

def hello_func(greeting, name = 'you'):
    return '{} {}'.format(greeting, name)

print(hello_func('Hi'))
print(hello_func('Hi', name = 'abcd'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'art']
info = {'name': 'abcd', 'age':24}

student_info(*courses, **info)
