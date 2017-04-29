### 1. 函数式编程
纯函数式编程的特点：
```
* 把计算视为函数而非指令
* 纯函数式编程：不需要变量，没有副作用，测试简单
* 支持高阶函数，代码简洁
```
Python的函数式编程的特点：
```
* 不是纯函数式编程：允许有变量
* 支持高阶函数：函数也可以作为变量传入
* 支持闭包：有了闭包就能返回函数
* 有限度的支持匿名函数
```
### 2. Python中的高阶函数
变量可以指向函数
```
f = abs
print f(-20)
20
```
函数名其实就是指向函数的变量
```
abs = len
abs(-20)
-> error
abs([1,2,3])
3
```
高阶函数：能接受函数作为参数的函数
```
* 变量可以指向函数
* 函数的参数接收变量
* 一个函数可以接收另一个函数作为参数
* 能接受函数作为参数的函数叫做高阶函数
```
### 3. Python中的map()函数
`map()`是 Python 内置的高阶函数，它接收一个函数`f`和一个`list`，并通过把函数 f *依次作用在list 的每个元素上*，得到一个新的 `list` 并返回。

例如，对于`list [1, 2, 3, 4, 5, 6, 7, 8, 9]`

如果希望把list的每个元素都作平方，就可以用map()函数：

因此，我们只需要传入函数f(x)=x*x，就可以利用map()函数完成这个计算：
```
def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
```
输出结果：`[1, 4, 9, 10, 25, 36, 49, 64, 81]`

注意：map()函数不改变原有的 `list`，而是*返回一个新的 list*。

利用map()函数，可以把一个 `list` 转换为另一个 `list`，只需要传入转换函数。

由于`list`包含的元素可以是任何类型，因此，`map()` 不仅仅可以处理只包含数值的 `list`，事实上它可以处理包含任意类型的 `list`，只要传入的函数f可以处理这种数据类型。
### 4. Python中reduce()函数
`reduce()`函数也是Python内置的一个高阶函数。`reduce()`函数接收的参数和`map()`类似，一个函数 `f`，一个`list`，但行为和`map()`不同，`reduce()`传入的函数`f`必须接收两个参数，`reduce()`对`list`的每个元素反复调用函数`f`，并返回最终结果值。

例如，编上述计算实际上是对`list`的所有元素求和。虽然Python内置了求和函数`sum()`，但是，利用`reduce()`求和也很简单。

`reduce()`还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100，计算：

`reduce(f, [1, 3, 5, 7, 9], 100)`

结果将变为125，因为第一轮计算是：

计算初始值和第一个元素：`f(100, 1)`，结果为101。

写一个f函数，接收x和y，返回x和y的和：
```
def f(x, y):
    return x + y
```
调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
```
先计算头两个元素：f(1, 3)，结果为4；
再把结果和第3个元素计算：f(4, 5)，结果为9；
再把结果和第4个元素计算：f(9, 7)，结果为16；
再把结果和第5个元素计算：f(16, 9)，结果为25；
由于没有更多的元素了，计算结束，返回结果25。
```
### 5. Python中filter()函数
`filter()`函数是 Python 内置的另一个有用的高阶函数，`filter()`函数接收一个函数`f`和一个`list`，这个函数`f`的作用是对每个元素进行判断，返回 True或 False，`filter()`根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新`list`。

例如，要从一个`list [1, 4, 6, 7, 9, 12, 17]`中删除偶数，保留奇数，首先，要编写一个判断奇数的函数：
```
def is_odd(x):
    return x % 2 == 1
```
然后，利用`filter()`过滤掉偶数：
```
filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
结果：[1, 7, 9, 17]
```
利用`filter()`，可以完成很多有用的功能，例如，删除 None 或者空字符串：
```
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
结果：['test', 'str', 'END']
```
注意: `s.strip(rm)` 删除 s 字符串中开头、结尾处的 rm 序列的字符。

当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：
```
a = '     123'
a.strip()
```
结果： *'123'*
```
a='\t\t123\r\n'
a.strip()
```
结果：*'123'*
### 6. Python中自定义排序函数
Python内置的 `sorted()`函数可对list进行排序：
```
>>>sorted([36, 5, 12, 9, 21])
[5, 9, 12, 21, 36]
```
但 `sorted()`也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，*传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0*。

因此，如果我们要实现倒序排序，只需要编写一个reversed_cmp函数：
```
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
```
这样，调用 `sorted()` 并传入 `reversed_cmp` 就可以实现倒序排序：
```
>>> sorted([36, 5, 12, 9, 21], reversed_cmp)
[36, 21, 12, 9, 5]
```
`sorted()`也可以对字符串进行排序，字符串默认按照ASCII大小来比较：
```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```
'Zoo'排在'about'之前是因为'Z'的ASCII码比'a'小。
### 7. Python中返回函数
Python的函数不但可以返回int、str、list、dict等数据类型，还**可以返回函数**！

例如，定义一个函数 f()，我们让它返回一个函数 g，可以这样写：
```
def f():
    print 'call f()...'
    # 定义函数g:
    def g():
        print 'call g()...'
    # 返回函数g:
    return g
```
仔细观察上面的函数定义，我们在函数 f 内部又定义了一个函数 g。由于函数 g 也是一个对象，函数名 g 就是指向函数 g 的变量，所以，最外层函数 f 可以返回变量 g，也就是函数 g 本身。

调用函数 f，我们会得到 f 返回的一个函数：
```
>>> x = f()   # 调用f()
call f()...
>>> x   # 变量x是f()返回的函数：
<function g at 0x1037bf320>
>>> x()   # x指向函数，因此可以调用
call g()...   # 调用x()就是执行g()函数定义的代码
```
请注意**区分返回函数和返回值**：
```
def myabs():
    return abs   # 返回函数
def myabs2(x):
    return abs(x)   # 返回函数调用的结果，返回值是一个数值
```
返回函数可以把一些计算延迟执行。例如，如果定义一个普通的求和函数：
```
def calc_sum(lst):
    return sum(lst)
调用calc_sum()函数时，将立刻计算并得到结果：
>>> calc_sum([1, 2, 3, 4])
10
```
但是，如果返回一个函数，就可以“**延迟计算**”：
```
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum

# 调用calc_sum()并没有计算出结果，而是返回函数:
>>> f = calc_sum([1, 2, 3, 4])
>>> f
<function lazy_sum at 0x1037bfaa0>
# 对返回的函数进行调用时，才计算出结果:
>>> f()
10
```
由于可以返回函数，我们在后续代码里就可以决定到底要不要调用该函数。
### 8. Python中闭包
在函数内部定义的函数和外部定义的函数是一样的，只是他们*无法被外部访问*：
```
def g():
    print 'g()...'

def f():
    print 'f()...'
    return g
```
将 g 的定义移入函数 f 内部，防止其他代码调用 g：
```
def f():
    print 'f()...'
    def g():
        print 'g()...'
    return g
```
但是，考察上一小节定义的 calc_sum 函数：
```
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
```
> 注意: 发现没法把 lazy_sum 移到 calc_sum 的外部，因为它引用了 calc_sum 的参数 lst。
> 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为*闭包（Closure）*。
> 闭包的特点是返回的函数还引用了*外层函数的局部变量*，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。举例如下：

```
# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```
你可能认为调用`f1()，f2()和f3()`结果应该是1，4，9，但实际结果全部都是 9（请自己动手验证）。

原因就是当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3。由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i，当 f1 被调用时：
```
>>> f1()
9     # 因为f1现在才计算i*i，但现在i的值已经变为3
```
*因此，返回函数不要引用任何循环变量，或者后续会发生变化的变量*。
### 9. python中匿名函数
高阶函数可以接收函数做参数，有些时候，我们不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以`map()`函数为例，计算 `f(x)=x2` 时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
```
>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
通过对比可以看出，匿名函数 `lambda x: x * x` 实际上就是：
```
def f(x):
    return x * x
```
关键字*lambda*表示匿名函数，冒号前面的 *x* 表示函数参数。

匿名函数有个限制，就是**只能有一个表达式，不写return**，*返回值*就是*该表达式的结果*。

使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码：
```
>>> sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
[9, 5, 3, 1, 0]
```
返回函数的时候，也可以返回匿名函数：
```
>>> myabs = lambda x: -x if x < 0 else x 
>>> myabs(-1)
1
>>> myabs(1)
1
```
### 10. Python中decorator装饰器
Python内置的`@`语法就是为了简化装饰器调用
装饰器的作用：
```
* 打印日志：@log
* 检测性能：@performance
* 数据库事务：@transaction
* URL路由：@post('/register')
```
### 11. Python中编写无参数decorator
Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。

使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。

考察一个@log的定义：
```
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
```
对于阶乘函数，@log工作得很好：
```
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
结果：
call factorial()...
3628800
```
但是，对于参数不是一个的函数，调用将报错：
```
@log
def add(x, y):
    return x + y
print add(1, 2)
结果：
Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print add(1,2)
TypeError: fn() takes exactly 1 argument (2 given)
```
因为 `add()` 函数需要传入两个参数，但是 @log 写死了只含一个参数的返回函数。
要让 @log 自适应任何参数定义的函数，可以利用Python的 `*args` 和 `**kw`，保证任意个数的参数总是能正常调用：
```
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
```
现在，对于任意函数，@log 都能正常工作。
### 12. Python中编写带参数decorator
考察上一节的 @log 装饰器：
```
def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
```
发现对于被装饰的函数，log打印的语句是不能变的（除了函数名）。

如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数，类似这样：
```
@log('DEBUG')
def my_func():
    pass
```
把上面的定义翻译成高阶函数的调用，就是：
```
my_func = log('DEBUG')(my_func)
```
上面的语句看上去还是比较绕，再展开一下：
```
log_decorator = log('DEBUG')
my_func = log_decorator(my_func)
```
上面的语句又相当于：
```
log_decorator = log('DEBUG')
@log_decorator
def my_func():
    pass
```
所以，带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数：
```
def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
执行结果：
[DEBUG] test()...
None
```
对于这种3层嵌套的decorator定义，你可以先把它拆开：
```
# 标准decorator:
def log_decorator(f):
    def wrapper(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrapper
return log_decorator

# 返回decorator:
def log(prefix):
    return log_decorator(f)
```
拆开以后会发现，调用会失败，因为在3层嵌套的decorator定义中，最内层的wrapper引用了最外层的参数prefix，所以，把一个闭包拆成普通的函数调用会比较困难。不支持闭包的编程语言要实现同样的功能就需要更多的代码。
### 13. Python中完善decorator
@decorator可以动态实现函数功能的增加，但是，经过@decorator“改造”后的函数，和原函数相比，除了功能多一点外，有没有其它不同的地方？

在没有decorator的情况下，打印函数名：
```
def f1(x):
    pass
print f1.__name__
输出： f1
```
有decorator的情况下，再打印函数名：
```
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__
输出： wrapper
```
可见，由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'。这对于那些依赖函数名的代码就会失效。decorator还改变了函数的`__doc__`等其它属性。如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中：
```
def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
```
这样写decorator很不方便，因为我们也很难把原函数的所有必要属性都一个一个复制到新函数上，所以Python内置的*functools*可以用来自动化完成这个“复制”的任务：
```
import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
```
最后需要指出，由于我们把原函数签名改成了`(*args, **kw)`，因此，*无法获得原函数的原始参数信息*。即便我们采用固定参数来装饰只有一个参数的函数：
```
def log(f):
    @functools.wraps(f)
    def wrapper(x):
        print 'call...'
        return f(x)
    return wrapper
```
也可能改变原函数的参数名，因为新函数的参数名始终是 'x'，原函数定义的参数名不一定叫 'x'。
### 14. Python中偏函数
当一个函数有很多参数时，调用者就需要提供多个参数。如果减少参数个数，就可以简化调用者的负担。

比如，`int()`函数可以把字符串转换为整数，当仅传入字符串时，`int()`函数默认按十进制转换：
```
>>> int('12345')
12345
```
但`int()`函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做 N 进制的转换：
```
>>> int('12345', base=8)
5349
>>> int('12345', 16)
74565
```
假设要转换大量的二进制字符串，每次都传入`int(x, base=2)`非常麻烦，于是，我们想到，可以定义一个`int2()`的函数，默认把base=2传进去：
```
def int2(x, base=2):
    return int(x, base)
```
这样，我们转换二进制就非常方便了：
```
>>> int2('1000000')
64
>>> int2('1010101')
85
```
`functools.partial`就是帮助我们创建一个偏函数的，不需要我们自己定义`int2()`，可以直接使用下面的代码创建一个新的函数int2：
```
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
```
所以，`functools.partial`可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。
### 15. Python之定义类并创建实例
在Python中，类通过 class 关键字定义。以 Person 为例，定义一个Person类如下：
```
class Person(object):
    pass
```
按照 Python 的编程习惯，类名以*大写字母*开头，紧接着是`(object)`，表示该类是从哪个类继承下来的。

有了Person类的定义，就可以创建出具体的实例。创建实例使用`类名+()`，类似函数调用的形式创建：
```
xiaoming = Person()
xiaohong = Person()
```
### 16. Python中创建实例属性
虽然可以通过Person类创建出xiaoming、xiaohong等实例，但是这些实例看上除了地址不同外，没有什么其他不同。在现实世界中，区分xiaoming、xiaohong要依靠他们各自的名字、性别、生日等属性。

如何让每个实例拥有各自不同的属性？由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值，例如，给xiaoming这个实例加上name、gender和birth属性：
```
xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'
```
给xiaohong加上的属性不一定要和xiaoming相同：
```
xiaohong = Person()
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2
```
实例的属性可以像普通变量一样进行操作：
```
xiaohong.grade = xiaohong.grade + 1
```
### 17. python中初始化实例属性
虽然我们可以自由地给一个实例绑定各种属性，但是，现实世界中，一种类型的实例应该拥有相同名字的属性。例如，Person类应该在创建的时候就拥有 name、gender 和 birth 属性，怎么办？

在定义 Person 类时，可以为Person类添加一个特殊的`__init__()`方法，当创建实例时，`__init__()`方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
```
class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
```
`__init__()` 方法的第一个参数必须是 **self**（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别。

相应地，创建实例时，就必须要提供除 self 以外的参数：
```
xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
```
有了`__init__()`方法，每个Person实例在创建时，都会有 name、gender 和 birth 这3个属性，并且，被赋予不同的属性值，访问属性使用`.`操作符：
```
print xiaoming.name
# 输出 'Xiao Ming'
print xiaohong.birth
# 输出 '1992-2-2'
```
要特别注意的是，初学者定义__init__()方法常常忘记了 self 参数,这会导致创建失败或运行不正常，因为第一个参数name被Python解释器传入了实例的引用，从而导致整个方法的调用参数位置全部没有对上。
### 18. Python中访问限制
我们可以给一个实例绑定很多属性，如果有些属性不希望被外部访问到怎么办？

Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头`(__)`，该属性就无法被外部访问。看例子：
```
class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob')
print p.name
# => Bob
print p._title
# => Mr
print p.__job
# => Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__job'
```
可见，只有以双下划线开头的`"__job"`不能直接被外部访问。

但是，如果一个属性以`"__xxx__"`的形式定义，那它又可以被外部访问了，以`"__xxx__"`定义的属性在Python的类中被称为*特殊属性*，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用`"__xxx__"`定义。

以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。
### 19. Python中创建类属性
类是模板，而实例则是根据类创建的对象。

绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

定义类属性可以直接在 class 中定义：
```
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
```
因为类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：
```
print Person.address
# => Earth
```
对一个实例调用类的属性也是可以访问的，所有实例都可以访问到它所属的类的属性：
```
p1 = Person('Bob')
p2 = Person('Alice')
print p1.address
# => Earth
print p2.address
# => Earth
```
由于Python是动态语言，类属性也是可以*动态添加和修改*的：
```
Person.address = 'China'
print p1.address
# => 'China'
print p2.address
# => 'China'
```
因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了。
### 20. Python中类属性和实例属性名字冲突怎么办
修改类属性会导致所有实例访问到的类属性全部都受影响，但是，如果在实例变量上修改类属性会发生什么问题呢？
```
class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')

print 'Person.address = ' + Person.address

p1.address = 'China'
print 'p1.address = ' + p1.address

print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address
结果如下：
Person.address = Earth
p1.address = China
Person.address = Earth
p2.address = Earth
```
我们发现，在设置了`p1.address = 'China'` 后，p1访问 address 确实变成了 'China'，但是，Person.address和p2.address仍然是'Earch'，怎么回事？

> 原因是 p1.address = 'China'并没有改变 Person 的 address，而是给p1这个实例绑定了实例属性address ，对p1来说，它有一个实例属性address（值是'China'），而它所属的类Person也有一个类属性address，所以:
> 访问 p1.address 时，优先查找实例属性，返回'China'。
> 访问 p2.address 时，p2没有实例属性address，但是有类属性address，因此返回'Earth'。
> 可见，当实例属性和类属性重名时，*实例属性优先级高*，它将屏蔽掉对类属性的访问。

当我们把 p1 的 address 实例属性删除后，访问 p1.address 就又返回类属性的值 'Earth'了：
```
del p1.address
print p1.address
# => Earth
```
可见，千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。
### 21. Python中定义实例方法
一个实例的私有属性就是以__开头的属性，无法被外部访问，那这些属性定义有什么用？

虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。除了可以定义实例的属性外，还可以定义实例的方法。

实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：
```
class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```
`get_name(self)` 就是一个实例方法，它的第一个参数是self。__init__(self, name)其实也可看做是一个特殊的实例方法。

调用实例方法必须在实例上调用：
```
p1 = Person('Bob')
print p1.get_name()  # self不需要显式传入
# => Bob
```
在实例方法内部，可以访问*所有实例属性*，这样，如果外部需要访问私有属性，可以通过方法调用获得，这种数据**封装**的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。
### 22. Python中方法也是属性
我们在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象：
```
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob', 90)
print p1.get_grade
# => <bound method Person.get_grade of <__main__.Person object at 0x109e58510>>
print p1.get_grade()
# => A
```
也就是说，p1.get_grade 返回的是一个函数对象，但这个函数是一个*绑定到实例的函数*，p1.get_grade() 才是方法调用。

因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用`types.MethodType()`把一个函数变为一个方法：
```
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
print p2.get_grade()
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade
```
> 给一个实例动态添加方法并不常见，直接在class中定义要更直观。
### 23. python中定义类方法
和属性类似，方法也分实例方法和类方法。

在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

要在class中定义类方法，需要这么写：
```
class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
```
通过标记一个 `@classmethod`，该方法将绑定到 Person 类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count。

因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。











