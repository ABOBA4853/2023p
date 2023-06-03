from iterator import Iterator
#iter1 = iter([1,2,3,4,5,6,7,8,9,10])
'''
for i in iter1:
    print(i)
'''
'''
try:
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
    print(iter1.__next__())
except StopIteration:
    pass
'''
iter0 = Iterator(21)
for i in iter0:
    print(i)