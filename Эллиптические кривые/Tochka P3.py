def vzlom(A, B):
    Верхняя_строка = [1, 0, A]
    Нижняя_строка = [0, 1, B]
    print (f'\t{Верхняя_строка}')
    print (f'\t{Нижняя_строка}')
    
    while True:
        if (Верхняя_строка[2] == 1 and Нижняя_строка[2] == 0) or (Верхняя_строка[2] == 0 and Нижняя_строка[2] == 1):
            break            
        elif Верхняя_строка[2] < Нижняя_строка[2]:
            множитель = Нижняя_строка[2] // Верхняя_строка[2]
            for i in range (0, 3):
                Нижняя_строка[i] -= (Верхняя_строка[i]*множитель)
        else:
            множитель = Верхняя_строка[2] // Нижняя_строка[2]
            for i in range (0, 3):
                Верхняя_строка[i] -= (Нижняя_строка[i]*множитель)
        print ("")
        print (f'\t{Верхняя_строка}')
        print (f'\t{Нижняя_строка}')
    if Верхняя_строка[2] == 1:
        if Верхняя_строка[0] > 0:
            return Верхняя_строка[0]
        else:
            itog = Верхняя_строка[0]
            while itog < 0:
                itog += Нижняя_строка[0]
                print(f'\tК верхней прибавить нижнюю, чтобы положительные')
            return itog    
            
    elif Нижняя_строка[2] == 1:
        if Нижняя_строка[0] > 0:
            return Нижняя_строка[0]
        else:
            itog = Нижняя_строка[0]
            while itog < 0:
                itog += Верхняя_строка[0]
                print(f'\tК нижней прибавить верхнюю, чтобы положительные')
            return itog   

def addsym(arr, n):
    newarr = []
    for i in range(0, len(arr)):
        newarr.append(str(arr[i]))
    newarr = [f'{" " * (n-len(e))}{e}' for e in newarr]
    return newarr

print(f'Эллиптические кривые, поиск P3') 
P = int(input('Введите P: '))
a = int(input('Введите a: '))
b = int(input('Введите b: '))
temp = input('Введите через пробел координаты точки Р1: ')
l1, l2 = temp.split()
l1 = int(l1)
l2 = int(l2)
P1 = (l1, l2)
temp = input('Введите через пробел координаты точки Р2: ')
l1, l2 = temp.split()
l1 = int(l1)
l2 = int(l2)
P2 = (l1, l2)
Q = []
Y2 = []
X = []
Y = []
print(f'y**2 = x**3 + a*x + b')
f = f'y**2 = x**3 + {a}*x + {b}'
print (f)
print (f'Q(x) = x**3 + {a}*x + {b}')
for w in range (0, P):
    Xi = Yi = w
    Qi = (w**3 + a*w + b) % P
    Y2i = (w**2) % P
    Q.append(Qi)
    Y2.append(Y2i)
    X.append(Xi)
    Y.append(Yi)

kolvosimvolov = len(str(P))
strmassX = addsym(X, kolvosimvolov)
strmassY = addsym(Y, kolvosimvolov)
strmassQ = addsym(Q, kolvosimvolov)
strmassY2 = addsym(Y2, kolvosimvolov)
strQ = '  '.join(strmassQ)
strY2 = '  '.join(strmassY2)
strX = '  '.join(strmassX)
strY = '  '.join(strmassY)
print(f'x  | {strX}\nQ  | {strQ}\ny  | {strY}\ny^2| {strY2}')
massivtochek = []
for t in range(0, P):
    for k in range(0, P):
        if Q[t] == Y2[k]:
            newpoint = (X[t], Y[k])
            massivtochek.append(newpoint)
print(f'Массив точек кривой: ')    
for i in massivtochek:
    print(i)
if P1 in massivtochek and P2 in massivtochek:
    print(f'Указанные точки {P1} и {P2} находятся в списке точек эллипса')
else:
    print(f'Указанные точки {P1} и {P2} НЕ находятся в списке точек эллипса, дальнейшие вычисления неоднозначны')
    exit()
print(f'Расчет P3 = P2 + P1. Все вычисления по модулю p.')
print(f'Расчет k:')
t2 = (P2[0] - P1[0]) % P
if t2 != 0:
    print(f'k = (y2-y1)/(x2-x1) = (y2-y1) * (x2-x1)**-1\nРасчёт (x2-x1)**-1 mod p')
    #print(f'знаменатель без модуля равен {t2}')
    t2 = vzlom(t2, P) % P
    print(f'(x2-x1)**-1 по модулю {P} равно {t2}')
    t1 = (P2[1] - P1[1]) % P
    k = (t1 * t2) % P
    print(f'k = (y2-y1) * (x2-x1)**-1 = {t1} * {t2} mod {P}= {k}')
    #print(f'k = {k}')
else:
    t1 = 3 * (P1[0]**2) + a
    print(f'k = (3 * x1**2 + a) / (2 * y1) = (3 * x1**2 + a) * (2 * y1)**-1\nРасчёт (2 * y1)**-1 mod p')
    t2 = 2 * P1[1]
    t2 = vzlom(t2, P) % P
    print(f'(2 * y1)**-1 по модулю {P} равно {t2}')
    k = (t1 * t2) % P
    print(f'k = (3 * x1**2 + a) * (2 * y1)**-1 = {t1} * {t2} mod {P} = {k}')
x3 = (k**2 - P1[0] - P2[0]) % P
print(f'x3 = k**2 - x1 - x2 = {x3}')
y3 = (k * (P1[0] - x3) - P1[1]) % P
print(f'y3 = k*(x1 - x3) - y1 = {y3}')
P3 = (x3, y3) 
print(f'P3 = {P3}')