def func1(x):
    print('func1', x)
    return

y = func1
y(3)

global x
x = 'Ram'
def func2():
    y = 'Raj'
    def func3():
        nonlocal y
        y = 'Robert'  
    func3()
    print(x, y)
    return

func2()

def func4(*a):
    print(a)
    return
l1 = [1,2,3,4,5]
func4(l1)

def func5(**k):
    print(k)
    for k, v in k.items():
        print('key is ',k,' value is ',v)
    return

func5(name='Arul', age=10)
d1 = {'key1':['v1','v2'],
      'key2':['v3','v4']}

func5(**d1)