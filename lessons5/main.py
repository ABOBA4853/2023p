
import requests
'''
help(requests)
import requests
r = requests.get ('http://www.python.org')
print(r.status_code)
'''
import requests

'''
students= list()
for method in dir(students):
    print(method)
help(list())
'''
'''
print(hasattr(list(), 'reverse'))
print(getattr(list(), 'remove'))
print(callable(list().remove))
print(callable(requests.status_codes))
print(issubclass(Exception, BaseException))
print(issubclass(Exception, str))
'''

class Human:
    pass
class Student(Human):
    pass
student = Student()
print(issubclass(Student, Human))
print(issubclass(Student, object))