def разложить_на_множители(n):
    множители = []
    делитель = 2
    while делитель <= n:
        if n % делитель == 0:
            множители.append(делитель)
            n //= делитель
        else:
            делитель += 1
    return множители

def НОД(a, b):
    while b:
        a, b = b, a % b
    return a

def vzlom(A, B):
    Верхняя_строка = [1, 0, A]
    Нижняя_строка = [0, 1, B]
    print (Верхняя_строка)
    print (Нижняя_строка)
    
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
        print (Верхняя_строка)
        print (Нижняя_строка)
    if Верхняя_строка[2] == 1:
        if Верхняя_строка[0] > 0:
            print (f"\n\tПодобран закрытый ключ D(b): {Верхняя_строка[0]}", end="\n")
            return Верхняя_строка[0]
        else:
            itog = Верхняя_строка[0]
            while itog < 0:
                itog += Нижняя_строка[0]
            print (f"\n\tПодобран закрытый ключ D(b): {itog}", end="\n")
            return itog    
            
    elif Нижняя_строка[2] == 1:
        if Нижняя_строка[0] > 0:
            print (f"\n\tПодобран закрытый ключ D(b): {Нижняя_строка[0]}", end="\n")
            return Нижняя_строка[0]
        else:
            itog = Нижняя_строка[0]
            while itog < 0:
                itog += Верхняя_строка[0]
            print (f"\n\tПодобран закрытый ключ D(b): {itog}", end="\n")
            return itog   

n = int(input("Введите N: "))
PandQ = разложить_на_множители(n)
p, q = PandQ
print ("\tp: " + str(p) + "\n\tq: " + str(q), end="\n")    

fi = (p-1)*(q-1)
e = int(input("Введите E(b) (Ключ шифрования атакуемого): "))

est_li_D = int(input("Если есть d введите 1. Если нужно его рассчитать, введите 2. Если его нужно забрутфорсить, введите 3: "))
if est_li_D == 1:
    d = int(input ("Введите d: "))
elif est_li_D == 2:
    print ("Атакуем секретный ключ")
    print (f"Некий B получает сообщение, шифрованное на открытом ключе Е(b) = {e}")
    print ("У атакующего A также есть открытый ключ Е(а) и секретный ключ D(а)")
    Ea = int(input("Введите Е(a): "))
    Da = int(input("Введите D(a): "))
    g0 = g = Ea * Da - 1
    h0 = h = НОД(g0, e)
    print (f"\tg0 = [см тетрадь] = {g0}, h0 = [см тетрадь] = {h0}")
    if h0 == 1:
        d = vzlom(e, g0)
    else:
        while h != 1:
            g = g/h
            h = НОД(g, e)
        d = vzlom(e, g)
        
elif  est_li_D == 3: #подбор d
    for i in range (1, fi-1):
        if (e*i-1)%fi == 0:
            print (f"Подобран d: {i}")
            d = i
            break
d = int(d)
print ("\n\tФункция эйлера: " + str(fi), end="\n")
# print ("\tN: " + str(n), end="\n")        
# print ("\te: " + str(e), end="\n")     
print ("\td: " + str(d), end="\n")     
if (e * d) % fi == 1:
	print("Значения e и d подобраны верно")
else:
	print("Значения e и d подобраны неверно")
    
        
vibor = int(input("Зашифровать - 1; Расшифровать - 2: "))
if vibor == 1:
    X = int(input("Введите значение для шифрования: "))
    j = 0
    while True:
        j=j+1
        if (j-X**e)%n == 0:
            Y = j
            break
    print ("\nX: " + str(X) + "\nY: " + str(Y), end="")
if vibor == 2:
    encrypted_message = int(input("\n\tВведите сообщение для дешифрования -> "))
    a = str(bin(d))
    # print(a, "Выводим а")
    # print(d, "Выводим d")

    ostatok = encrypted_message % n
    print(f"\t({ostatok} ** 0) mod {n} = {encrypted_message % n}\t2 ** 0", end="")
    if int(a[len(a) - 1]) == 1:
        print("\t+")
        asd = ostatok
    else:
        asd = 1
        print("\t-")
    for i in range(len(a) - 2, 1, -1):
        print(f"\t({ostatok} ** 2) mod {n} = {(ostatok ** 2) % n}\t2 ** {len(a) - 1 - i}", end="")
        ostatok = (ostatok ** 2) % n
        
        if int(a[i]) == 1:
            asd = asd * ostatok
            print("\t+")
        else:
            print("\t-")
    print(f"\tРезультат расшифровки -> {asd % n}")


