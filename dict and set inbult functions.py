Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={}
dict1['name']='faouzia'
dict1
{'name': 'faouzia'}
type(dict1)
<class 'dict'>
dict1[name]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dict1[name]
NameError: name 'name' is not defined
dict1['name']
'faouzia'
dict1.keys()
dict_keys(['name'])
d1{'a':'A','b':'B','c':'C']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d1{'a':'A','b':'B','c':'C'}
SyntaxError: invalid syntax
KeyboardInterrupt
KeyboardInterrupt
d1={'a':'A','b':'B','c':'C'}
d
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'd1'?
d1
{'a': 'A', 'b': 'B', 'c': 'C'}
d1.items()
dict_items([('a', 'A'), ('b', 'B'), ('c', 'C')])
d1.values()
dict_values(['A', 'B', 'C'])
d1.get('b')
'B'
d1.keys()
dict_keys(['a', 'b', 'c'])
d1.pop('c')
'C'
d1
{'a': 'A', 'b': 'B'}
d1.update({'b':2})
d1
{'a': 'A', 'b': 2}
d1.update({'c':3})
d1
{'a': 'A', 'b': 2, 'c': 3}
d1.update({'a':1})
d1
{'a': 1, 'b': 2, 'c': 3}
d1.update([('d',4)])
d1
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
d1.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d1.pop()
TypeError: pop expected at least 1 argument, got 0
d1.popitem()
('d', 4)
d1
{'a': 1, 'b': 2, 'c': 3}
d1.clear()
d1
{}
d1={1:2,3:4,5:6}
d1
{1: 2, 3: 4, 5: 6}
d2=d1.copy()
d2
{1: 2, 3: 4, 5: 6}
d2.setdefault()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d2.setdefault()
TypeError: setdefault expected at least 1 argument, got 0
d2.setdefault(3)
4
d2
{1: 2, 3: 4, 5: 6}
d2.pop(3)
4
d2
{1: 2, 5: 6}
d2.setdefault(3:4)
SyntaxError: invalid syntax
d2.setdefault(4:9)
SyntaxError: invalid syntax
d2.setdefault(3,4)
4
d2
{1: 2, 5: 6, 3: 4}
d1
{1: 2, 3: 4, 5: 6}
s={1,2,3,4,4,5}
s
{1, 2, 3, 4, 5}
r=set()
r
set()
s.add(6)
s
{1, 2, 3, 4, 5, 6}
s.add(0)
s
{0, 1, 2, 3, 4, 5, 6}
a={1,2,3,4}
>>> b={3,4,6,7,8}
>>> a-b
{1, 2}
>>> a.difference(b)
{1, 2}
>>> a.difference_update(b)
>>> a
{1, 2}
>>> a={1,2,3,4,5}
>>> a.symmetric_difference(b)
{1, 2, 5, 6, 7, 8}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> a.intersection(b)
{3, 4}
>>> a
{1, 2, 3, 4, 5}
>>> a.discard(4)
>>> a
{1, 2, 3, 5}
>>> a.isdisjoint
<built-in method isdisjoint of set object at 0x000001FA1F454040>
>>> a.isdisjoint(b)
False
>>> a.issubset(b)
False
>>> a.issuperset(b)
False
>>> a.update(b)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8}
