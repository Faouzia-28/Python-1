Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="Teddy"
a=list(a)
>>> a
['T', 'e', 'd', 'd', 'y']
>>> a.append(s)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.append(s)
NameError: name 's' is not defined
>>> a.append("s")
>>> a
['T', 'e', 'd', 'd', 'y', 's']
>>> a.pop()
's'
>>> a
['T', 'e', 'd', 'd', 'y']
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.remove(2)
ValueError: list.remove(x): x not in list
>>> a.remove("y")
>>> a
['T', 'e', 'd', 'd']
>>> b=['y','s']
>>> a+b
['T', 'e', 'd', 'd', 'y', 's']
>>> a.extend(b)
>>> a
['T', 'e', 'd', 'd', 'y', 's']
>>> a.insert(2,'e')
>>> a
['T', 'e', 'e', 'd', 'd', 'y', 's']
