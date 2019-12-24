from sys import argv
import readline

def ayuda():
    print (argv[0] + ' a b c',
        'a b',
        'a c',
        '',
        sep=f'\n{argv[0]} ')
    print ('\n    -h, --help    muestra esta ayuda y finaliza')

def error(numero):
    print ('Los {numero} argumentos tienes que ser numéricos…')
    exit (2)

def equis():
    print ('X\u2081 \u2192 ' + str(X1), 'X\u2082 \u2192 ' + str(X2), sep='\n', end='\n\n')

if len(argv) is 1:
    while True:
        try:
            a = int(input('Ingrese el valor de a: '))
            break
        except ValueError:
            print ('Tiene que ser un número…')
    while True:
        try:
            b = int(input('Ingrese el valor de b: '))
            break
        except ValueError:
            print ('Tiene que ser un número…')
    while True:
        try:
            c = int(input('Ingrese el valor de c: '))
            break
        except ValueError:
            print ('Tiene que ser un número…')
elif len(argv) is 2:
    try:
        a = int(argv[1])
        print ('No hay solución…')
        exit()
    except ValueError:
        if argv[1] == '-h' or argv[1] == '--help':
            ayuda()
            exit()
        else:
            print ('Error, el argumento no es un número…')
            exit(2)
elif len(argv) is 3:
    while True:
        try:
            if int(argv[2]) < 0:
                o = '-'
                num = int(argv[2]) * -1
            else:
                o = '+'
                num = int(argv[2])
            a = int(input(f'[1] {argv[1]}X\u00B2 {o} {num}X.\n[2] {argv[1]} {o} {num}\nSeleccione 1 o 2: '))
            a = a - 1
            print
            break
        except ValueError:
            print ('Ingrese 1 o 2…')
    if bool(a): 
        try:
            a = int(argv[1])
        except ValueError:
            error('dos')
        b = 0
        try:
            c = int(argv[2])
        except ValueError:
            error('dos')
    else:
        try:
            a = int(argv[1])
        except ValueError:
            error('dos')
        try:
            b = int(argv[2])
        except ValueError:
            error('dos')
        c = 0
elif len(argv) is 4:
    try:
        a = int(argv[1])
    except ValueError:
        error('tres')
    try:
        b = int(argv[2])
    except ValueError:
        error('tres')
    try:
        c = int(argv[3])
    except ValueError:
        error('tres')
else:
    ayuda()
    exit(2)

aux = pow(b,2) - 4*a*c

if b < 0:
    oX = '-'
    B = b * -1
else:
    oX = '+'
    B = b

if c < 0:
    o = '-'
    C = c * -1
else:
    o = '+'
    C = c

if b != 0 and c != 0:
    print (f'{a}X\u00b2 {oX} {B}X {o} {C}\n')
    completa = True
elif c == 0:
    print (f'{a}X\u00b2 {oX} {B}X\n')
    completa = False
elif b == 0:
    print (f'{a}X\u00b2 {o} {C}\n')
    completa = False

if aux >= 0 or len(argv) == 3:
    if completa:
        if ((-b + pow(aux, 0.5))%(2*a)) == 0:
            X1 = int((-b + pow(aux, 0.5))//(2*a))
        else:
            X1 = (-b + pow(aux, 0.5))/(2*a)
        if ((-b - pow(aux, 0.5)) % (2*a)) == 0:
            X2 = int((-b - pow(aux, 0.5))//(2*a))
        else:
            X2 = (-b - pow(aux, 0.5))/(2*a)
        if aux != 0:
            equis()
        else:
            print (f'X es {X1} doble')
    elif c != 0:
        aux = abs(pow(-c/a, 0.5))
        if int(aux) == float(aux):
            aux = int(aux)
        X1, X2 = aux, -aux
        equis()
    elif b != 0:
        X1 = abs(abs((-b + pow(aux, 0.5))/(2*a)))
        if int(X1) == X1:
            X1 = int(X1)
        X2 = abs(abs((-b - pow(aux, 0.5))/(2*a)))
        if int(X1) == X1:
            X2 = int(X2)
        equis()
else:
    print ('Sin solución\n')

Xv = -b / (2 * a)
if int(Xv) == float(Xv):
    Xv = int(Xv)

Yv = a * pow(Xv, 2) + b * Xv + c
if int(Yv) == float(Yv):
    Yv = int(Yv)

print (f'Vértice X \u2192 {Xv}\nVértice Y \u2192 {Yv}')