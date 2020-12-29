"""
LEGB --> Local, Enclosing, Global, Built-in
"""
import builtins

print(dir(builtins))

x = 'global x'

def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)
