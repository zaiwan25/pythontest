
animal = 'fruibat'
print('at the top level:', animal, globals())

def print_global():

    animal = 'wombat'
    print('inside print_global:', animal, globals())

print_global()
# def docIt(func):
#     def newFuncInDocIt(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return newFuncInDocIt
#
# def squareIt(func):
#     def newFuncInSquareIt(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return newFuncInSquareIt
#
#
# @squareIt
# @docIt
# def addInts(a, b):
#     return a + b
#
# print(addInts(1, 2))
#
# print(addInts(3, 4))

# def makeMenu(wine, dessert='pudding'):
#     return {'wine': wine, 'dessert': dessert}
#
# menu = makeMenu('red')
# print(menu)
#
# def buggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)
#
# buggy('a')
# buggy('b')
# arr = []
# buggy('c', arr)
# buggy('d')
#
# def printArgs(*args):
#     print('args tuple:', args)
#
# printArgs()
# printArgs(1, 2)
# printArgs(1, 'test')

# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
# weekDays = ['fri', 'sat', 'sun']
# def add_day(weekDay):
#     return weekDay + 'day'
#
# edit_story(weekDays, add_day)
# edit_story(weekDays, lambda param: param + 'day!!')

