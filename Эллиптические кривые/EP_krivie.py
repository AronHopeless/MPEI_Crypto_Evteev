def binary_representation(n):
    binary_repr = bin(n)[2:]  # Преобразование в двоичное представление и удаление префикса '0b'
    binary_repr = binary_repr[::-1]  # Инверсия строки для более удобной работы
    powers_of_two = [i for i, bit in enumerate(binary_repr) if bit == '1']
    # Создание списка степеней двойки, где бит равен 1
    return powers_of_two

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

def udvoenie_G(G, P, a, b):
    NewG = Slogenie_G(G, G, P, a, b)
    return NewG

def Slogenie_G(P1, P2, P, a, b):
    # P1 = P2 = G
    Q = []
    Y2 = []
    X = []
    Y = []
    # print(f'y**2 = x**3 + a*x + b')
    # print (f'y**2 = x**3 + {a}*x + {b}')
    # print (f'Q(x) = x**3 + {a}*x + {b}')
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
    # print(f'x  | {strX}\nQ  | {strQ}\ny  | {strY}\ny^2| {strY2}')
    massivtochek = []
    for t in range(0, P):
        for k in range(0, P):
            if Q[t] == Y2[k]:
                newpoint = (X[t], Y[k])
                massivtochek.append(newpoint)
    t2 = (P2[0] - P1[0]) % P
    if t2 != 0:
        print(f'k = (y2-y1)/(x2-x1) = (y2-y1) * (x2-x1)**-1\nРасчёт (x2-x1)**-1 mod p')
        t2 = vzlom(t2, P) % P
        print(f'(x2-x1)**-1 по модулю {P} равно {t2}')
        t1 = (P2[1] - P1[1]) % P
        k = (t1 * t2) % P
        print(f'k = (y2-y1) * (x2-x1)**-1 = {t1} * {t2} mod {P} = {k}')
        # print(f'k = {k}')
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
    # print(f'P3 = {P3}')    
    # print(P3)
    return P3

def ChisloNaTochku(k, G, P, a, b, Chislo, Tochka):
    Temp = G
    stepeni_k = binary_representation(k)
    temp = ' + '.join([f'2**{x}' for x in stepeni_k])
    print(f'Число {k} можно представить в виде {temp}')
    print(f'Вычисляем {Chislo} * {Tochka} = {k} * {G}')
    maks_stepen = max(stepeni_k)
    massiv_stepeney_G = []
    massiv_stepeney_G.append(Temp)
    for i in range(1, maks_stepen + 1):
        print(f'\nРасчёт {2**i}{Tochka}: ')
        Temp = udvoenie_G(Temp, P, a, b)
        massiv_stepeney_G.append(Temp)
        print(f'{2**i}{Tochka} = {Temp} ')
    duplicate_stepeni_k = stepeni_k
    if len(duplicate_stepeni_k) > 1:
        print(f'\nРасчёт {massiv_stepeney_G[duplicate_stepeni_k[0]]} + {massiv_stepeney_G[duplicate_stepeni_k[1]]}')
        temp_result_sum_G = Slogenie_G(massiv_stepeney_G[duplicate_stepeni_k[0]], massiv_stepeney_G[duplicate_stepeni_k[1]], P, a, b)
        duplicate_stepeni_k = duplicate_stepeni_k[2:]
    else:
        temp_result_sum_G = massiv_stepeney_G[duplicate_stepeni_k[0]]
        duplicate_stepeni_k = duplicate_stepeni_k[1:]
    while len(duplicate_stepeni_k) > 0:
        print(f'\nРасчёт {temp_result_sum_G} + {massiv_stepeney_G[duplicate_stepeni_k[0]]}')   
        temp_result_sum_G = Slogenie_G(temp_result_sum_G, massiv_stepeney_G[duplicate_stepeni_k[0]], P, a, b)
        duplicate_stepeni_k = duplicate_stepeni_k[1:]
    return temp_result_sum_G

def Generatsiya(P, a, b, G, n, d, e, k):
    # while True:
    print(f'\nРасчёт kG = {d} * {G}:')
    kG = ChisloNaTochku(k, G, P, a, b, 'k', 'G')
    x = kG[0]
    y = kG[1]
    print(f'\nkG = {kG} -> x = {x}, y = {y}')
    r = x % n
    print(f'r = x mod n = {x} mod {n} = {r}')
        # if r == 0:
        #     continue
    z = vzlom(k, n) % n
    print(f'z = k**-1 mod n = {k}**-1 mod {n} = {z}')
    s = (z * (e + d * r)) % n
    print(f's = (z * (e + d * r)) mod n = s = ({z} * ({e} + {d} * {r})) mod {n} = {s}')
        # if s == 0:
        #     continue
    podpis_k_m = (r, s)
    return(podpis_k_m)
    
def Proverka(r, s, P, a, b, G, n, e, Q):
    if r < 1 or r > n - 1 or s < 1 or s > n - 1:
        print('Нарушено свойство 1 <= r <= n - 1 или 1 <= s <= n - 1. Подпись недействительна.')
        exit()
    v = vzlom(s, n) % n
    print(f'v = s**-1 mod n = {s}**-1 mod{n} = {v}')
    u1 = (e * v) % n
    print(f'u1 = e * v mod n = {e} * {v} mod {n} = {u1}')
    u2 = (r * v) % n
    print(f'u2 = r * v mod n = {r} * {v} mod {n} = {u2}')
    print(f'X = u1 * G + u2 * Q')
    print(f'Расчёт u1 * G: ')
    X_ch1 = ChisloNaTochku(u1, G, P, a, b, 'u1', 'G')
    print(f'u1 * G = {X_ch1}')
    print(f'Расчёт u2 * Q: ')
    X_ch2 = ChisloNaTochku(u2, Q, P, a, b, 'u2', 'Q')
    print(f'u2 * Q = {X_ch2}')
    print(f'Расчёт X = {X_ch1} + {X_ch2}: ')
    X = Slogenie_G(X_ch1, X_ch2, P, a, b)
    
    print(f'X = {X} = (x, y)')
    print(f'Подпись действительна, если r = x mod n')
    print(f'r = {r}, x mod n = {X[0] % n}')
    if r == X[0] % n:
        print(f'Подпись действительна')
        return True
    else:
        print(f'Подпись не действительна')
        return False
    
print(f'ЭП эллиптических кривых')
flack = int(input("Введите 1, чтобы сгенерировать подпись. \n2, чтобы проверить подпись \n3, чтобы сгенерировать и сразу проверить. \n -> "))
if flack == 1:
    P = int(input('Введите P: '))
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    G = input('Введите координаты G через пробел: ')
    g1, g2 = G.split()
    G = (int(g1), int(g2))
    n = int(input('Введите n: '))
    e = int(input('Введите e: '))
    d = int(input('Введите d: '))
    k = int(input('Введите k: '))
    # P = 751
    # a = -1
    # b = 1
    # G = (416, 55)   #точка
    # n = 13          #порядок точки, простое число
    # d = 3           #секретный ключ, 0 < d < n
    # e = 9           #хэщ сообщения
    # #N = 728        #порядок кривой
    # k = 5
    PODPIS = Generatsiya(P, a, b, G, n, d, e, k)
    print(f'Получена электронная подпись: {PODPIS}')
elif flack == 2:
    podpis = input('Введите значения ЭП через пробел: ')
    r, s = podpis.split()
    r = int(r)
    s = int(s)
    P = int(input('Введите P: '))
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    G = input('Введите координаты G через пробел: ')
    g1, g2 = G.split()
    G = (int(g1), int(g2))
    n = int(input('Введите n: '))
    e = int(input('Введите e: '))
    # P = 751
    # a = -1
    # b = 1
    # G = (416, 55)   #точка
    # n = 13          #порядок точки, простое число
    # e = 9           #хэщ сообщения
    Q = input('Введите координаты Q через пробел: ')
    q1, q2 = Q.split()
    Q = (int(q1), int(q2))
    Proverka(r, s, P, a, b, G, n, e, Q)
elif flack == 3:
    P = int(input('Введите P: '))
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    G = input('Введите координаты G через пробел: ')
    g1, g2 = G.split()
    G = (int(g1), int(g2))
    n = int(input('Введите n: '))
    e = int(input('Введите e: '))
    d = int(input('Введите d: '))
    k = int(input('Введите k: '))
    # P = 751
    # a = -1
    # b = 1
    # G = (416, 55)   #точка
    # n = 13          #порядок точки, простое число
    # d = 3           #секретный ключ, 0 < d < n
    # e = 9           #хэщ сообщения
    # #N = 728        #порядок кривой
    # k = 5
    PODPIS = Generatsiya(P, a, b, G, n, d, e, k)
    print(f'Получена электронная подпись: {PODPIS}')
    print(f'\nПроверка:\nРасчёт Q = {d} * {G}:')
    Q = ChisloNaTochku(d, G, P, a, b, 'd', 'G')
    print(f'Q = {Q}')
    Proverka(PODPIS[0], PODPIS[1], P, a, b, G, n, e, Q)
else:
    print('Смотри что вводишь, поц')
    
    