def stepen_by_modul(chislo, stepen, modul):
    bit_view = str(bin(stepen))
    PlusesAndMinuses = []
    for i in range(2, len(bit_view)):
        PlusesAndMinuses.insert(0, int(bit_view[i]))
    spisok_resultatov = []
    result = chislo % modul
    if PlusesAndMinuses[0] == 1:
        print(f"2^0:\t{chislo} mod {modul} = {result}    \t+")
    elif PlusesAndMinuses[0] == 0:
        print(f"2^0:\t{chislo} mod {modul} = {result}    \t-")
    spisok_resultatov.append(result)
    for i in range(1, len(PlusesAndMinuses)):
        if PlusesAndMinuses[i] == 1:
            print(f"2^{i}:\t{result}^2 mod {modul} = {(result**2) % modul}    \t+")
        elif PlusesAndMinuses[i] == 0:  
            print(f"2^{i}:\t{result}^2 mod {modul} = {(result**2) % modul}    \t-")  
        result = (result**2) % modul
        spisok_resultatov.append(result)
    spisok_mnogiteley = []
    poslednee_deystvo = 1;    
    for t in range (0, len(spisok_resultatov)):
        if PlusesAndMinuses[t] == 1:
            poslednee_deystvo *= spisok_resultatov[t]
            spisok_mnogiteley.append(spisok_resultatov[t])
        else:
            pass
    spisok_mnogiteley = '*'.join(map(str, spisok_mnogiteley))
    poslednee_deystvo = poslednee_deystvo % modul
    print (f"{spisok_mnogiteley} mod {modul} = {poslednee_deystvo}") 
    return poslednee_deystvo

def proisvedenie_cravneniy(mnogitel, chislo, stepen, modul):
    print ("Так как числа целые и модуль больше нуля, то используем распределительный закон: ")
    print (f"({mnogitel}*{chislo}^{stepen}) mod {modul} = ({mnogitel} mod {modul})*({chislo}^{stepen} mod {modul})")
    return (((mnogitel % modul)* (stepen_by_modul(chislo, stepen, modul))) % modul)

FLAG = int(input("Чтобы зашифровать введите 1. Чтобы расшифровать, введите 2: "))
if FLAG == 1:
    P = int(input("Введите значение модуля Р: "))
    alfa = int(input("Введите значение множества ненулевых вычетов alfa: "))
    a = int(input("Введите секретный ключ а: "))
    r = int(input("Введите случайное число r: "))
    x = int(input("Введите значение для шифрования X: "))
    print (f"Вычисляем beta = alfa^a mod p\tbeta = {alfa}^{a} mod {P}")
    beta = stepen_by_modul(alfa, a, P)
    print (f"\tbeta = {beta}")
    print (f"Вычисляем y1 = alfa^r mod p\ty1 = {alfa}^{r} mod {P}")
    y1 = stepen_by_modul(alfa, r, P)
    print (f"\ty1 = {y1}")
    print (f"Вычисляем y2 = (x*beta^r) mod p\ty2 = {x}*{beta}^{r} mod {P}")
    y2 = proisvedenie_cravneniy(x, beta, r, P)
    print (f"\ty2 = {y2}")
    y = (y1, y2)
    print (f"y = (y1, y2) = {y}")
    print("\n")
    print("Проверка. Расшифрование.")
    print(f"x = (y2 * (y1^(-a))mod P")
    st = P - ((a*r) % (P-1)) - 1
    print(f"y1 = alfa^r mod p; -> y1^(-a) = alfa^-(a*r) mod P = alfa^(P - (a*r)mod P - 1) = {alfa}^{st}")
    NewX = proisvedenie_cravneniy(y2, alfa, st, P)
    print (f"Результат расшифрования: {NewX}")
elif FLAG == 2:
    P = int(input("Введите значение модуля Р: "))
    alfa = int(input("Введите значение множества ненулевых вычетов alfa: "))
    a = int(input("Введите секретный ключ а: "))
    r = int(input("Введите случайное число r: "))
    y1 = int(input("Введите y1: "))
    y2 = int(input("Введите y2: "))
    print(f"x = (y2 * (y1^(-a))mod P")
    st = P - ((a*r) % (P-1)) - 1
    print(f"y1 = alfa^r mod p; -> y1^(-a) = alfa^-(a*r) mod P = alfa^(P - (a*r)mod P - 1) = {alfa}^{st}")
    NewX = proisvedenie_cravneniy(y2, alfa, st, P)
    print (f"Результат расшифрования: {NewX}")
    