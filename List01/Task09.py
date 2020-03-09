from math import sin, cos, tan

while True:
    x = input('Wyrazenie: ')
    x.replace('^', '**')
    x.replace('ctg', '(1/tan)')
    eval(x)
