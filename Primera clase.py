Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print()

>>>
>>> print
<built-in function print>
>>> print("Emilia)
  File "<stdin>", line 1
    print("Emilia)
                  ^
SyntaxError: EOL while scanning string literal
>>> print("Emilia")
Emilia
>>> print("Miguel papi chulo")
Miguel papi chulo
>>> 2+2
4
>>> 2*2+1
5
>>> Emilia
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Emilia' is not defined
>>> "Emilia"
'Emilia'
>>> print(2+2+2+2)
8
>>> 'Emilia'
'Emilia'
>>> 'can't'
  File "<stdin>", line 1
    'can't'
         ^
SyntaxError: invalid syntax
>>>
>>> "can't"
"can't"
>>> 'can\'t'
"can't"
>>> 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000+2
1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002
>>> 'don\'t'
"don't"
>>> ("Miguel")
'Miguel'
>>> 1_000_000+2
1000002
>>> 1_0_000+2
10002
>>> 0000_3
  File "<stdin>", line 1
    0000_3
         ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> True
True
>>> False
False
>>> 99>100
False
>>> -10>1
False
>>> -1>-3
True
>>> 19<27
True
>>> 10==10
True
>>> 30==30
True
>>> 20==10
False
>>> Emilia
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Emilia' is not defined
>>> Emilia=19
>>> Emilia
19
>>> Miguel
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Miguel' is not defined
>>> Miguel=27
>>> Miguel
27
>>> wao
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wao' is not defined
>>> Emilia<Miguel
True
>>> Emilia>Miguel
False
>>> Emilia==Miguel
False
>>> Emilia=Miguel
>>> Emilia
27
>>> 19!=2
True
>>> 19>20 and Emilia==Miguel
False
>>> 19>20 or Emilia==Miguel
True
>>> not true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> not True
False
>>> not False
True
>>> not Emilia=Miguel
  File "<stdin>", line 1
    not Emilia=Miguel
    ^
SyntaxError: cannot assign to operator
>>> not Emilia==Miguel
False
>>> print("Posho")
Posho
>>> "te amo"
'te amo'
>>> 30+30
60
>>> Fabio=1
>>> Emilia=2
>>> Marco=3
>>> Fabiola=4
>>> Fabio+Emilia*Marco+Fabiola
11
>>> 1+2
3
>>> 3+4
7
>>> 3*7
21
>>> Emilia*Marco
6
>>> 6+Fabio+Fabiola
11
>>> (Fabio+Emilia)*(Marco+Fabiola)
21
>>> L==M
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'L' is not defined
>>> "Hola"== "Hola"
True
>>> "A"<"B"
True
>>> "Emilia"<"Miguel"
True
>>> "Emilia"==="Miguel"
  File "<stdin>", line 1
    "Emilia"==="Miguel"
              ^
SyntaxError: invalid syntax
>>> "Emilia"+"Miguel"
'EmiliaMiguel'
>>> "Emilia" + "Miguel"
'EmiliaMiguel'
>>> "Emilia "+ "Miguel"
'Emilia Miguel'
>>> "Emilia "+ "Miguel"
'Emilia Miguel'
>>> "Emilia "+ "Miguel".
  File "<stdin>", line 1
    "Emilia "+ "Miguel".
                        ^
SyntaxError: invalid syntax
>>> "Emilia "+ "Miguel"."
  File "<stdin>", line 1
    "Emilia "+ "Miguel"."
                         ^
SyntaxError: EOL while scanning string literal
>>> "Emilia "+ "Miguel"\.
  File "<stdin>", line 1
    "Emilia "+ "Miguel"\.
                        ^
SyntaxError: unexpected character after line continuation character
>>> "Emilia "+ "Miguel."
'Emilia Miguel.'
>>> "Emilia es la mejor"
'Emilia es la mejor'
>>> "Emilia"+3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> "Emilia3"
'Emilia3'
>>> E=19
>>> E
19
>>> E<20
True
>>> input("cual es la edad de Emilia")
cual es la edad de Emilia 19
' 19'
>>> E=input cual es la edad de Emilia
  File "<stdin>", line 1
    E=input cual es la edad de Emilia
            ^
SyntaxError: invalid syntax
>>> E=input ("cual es la edad de Emilia")
cual es la edad de Emilia 19
>>> E
' 19'
>>> None
>>> None==print ()

True
