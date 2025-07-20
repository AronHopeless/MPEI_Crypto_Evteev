import sympy as sp
import re

def uprostit_p(p):
    x = sp.symbols('x')
    p = sp.expand(p)                #упростили
    p = str(p)
    #убираем все остальные множители
    lisp = p.split(" + ")
    QQQ = 0
    while QQQ < len(lisp):
        for i in range(len(lisp)):
            if "*x" in lisp[i]:
                mnogitel = int(lisp[i][:lisp[i].find("*")])
                if mnogitel % 2 == 1:
                    index_x = lisp[i].find("x")
                    lisp[i] = lisp[i][index_x : ]
                else:
                    lisp.pop(i)
                    break
        QQQ+=1
    p = " + ".join(lisp)
    while True:
    #надо убрать первый множитель
        poly_p = sp.Poly(p, x)
        poly_mnog = poly_p.all_terms()[0][1]
        first_mnogitel = int(poly_mnog)
        # print(f"Первый множ = {first_mnogitel}, {type(first_mnogitel)}")
        if first_mnogitel % 2 == 1:
            if first_mnogitel != 1:
                first_mnogitel = str(first_mnogitel)
                p = p[len(first_mnogitel)+1 :]
            break
        else:
            list__p = p.split(" ")
            list__p.pop(0)
            list__p.pop(0)
            p = " ".join(list__p)
            continue    
    p = p.replace(" x ", " x**1 ")  #заменили x на х**1 везде кроме начала и конца
    p = p.replace("x ", "x**1 ")
    if p[-1] == "x":
        p = p + "**1"               #заменили x на х**1 в конце
    list_p = p.split(" ")           #пофиксили свободный член
    if "x" not in list_p[-1]:
        temp = int(list_p[-1])
        temp = temp % 2
        if temp == 0:
            list_p.pop()
            list_p.pop()
        else:
            # list_p[-1] = "1"
            list_p[-1] = "x**0"
    p = " ".join(list_p)
    #фиксим мномжимтели
# Вывод массива с индексами вхождений
    return p

def obnovit_m(matrix):
    global m
    N_na_kotorom_k_izmen = None
 
    for i in range(0, len(matrix)-1):
        if matrix[i][1] < matrix[i+1][1]:
            N_na_kotorom_k_izmen = i + 1
            m = N_na_kotorom_k_izmen #matrix[m][0]
            
def extract_exponents(poly_string):
    # Используем регулярное выражение для поиска степеней
    exponents = [int(match.group(1)) for match in re.finditer(r'\*\*(\d+)', poly_string)]
    # print(f"\tСтепени: {exponents}")
    return exponents

def find_max_number(text):
    # Извлекаем все числа из строки
    numbers = [int(match.group(1)) for match in re.finditer(r'\*\*(\d+)', text)]
    if numbers:
        # Находим максимальное число
        max_number = max(numbers)
        return max_number
    else:
        return None

def find_row_by_element(matrix, stolb_matrix, element):
    for index, row in enumerate(matrix):
        if row[stolb_matrix] == element:
            return index
    return -1    

def proverka_generatsii(_STROKA, y_fut, dlina_rega, function):
    print(f"Работаем с регистром: {function}")
    y_pre = y_fut - 1
    reg_pre = _STROKA[y_pre + 1 - dlina_rega : y_pre + 1]
    revesed_reg_pre = reg_pre[::-1]
    noviy_simvol = 0
    for i in extract_exponents(function)[1:]:
        noviy_simvol += int(reg_pre[i])
    noviy_simvol = str(noviy_simvol % 2)
    reg_fut_real = noviy_simvol + revesed_reg_pre[:-1]
    reg_fut_imag = _STROKA[y_fut + 1 - dlina_rega : y_fut + 1]
    reversed_reg_fut_imag = reg_fut_imag[::-1]
    print(f"Чтобы сохранить регистр, нужно:")
    print(f"{revesed_reg_pre}  ➔  {reversed_reg_fut_imag}")
    print(f"В реальности получаем:")
    q = f"┌—{revesed_reg_pre}"
    stroka_chertochek = ""
    for r in range (0, len(reg_pre)):
        if r in extract_exponents(function)[1:]:
            stroka_chertochek = "|" + stroka_chertochek
        else: 
            stroka_chertochek = " " + stroka_chertochek
    w = f"{noviy_simvol} " + stroka_chertochek
    stroka_s_plusom = ""
    if len(reg_pre) < 3:
        stroka_s_plusom = "⊕"
        t = ""
    elif len(reg_pre) == 3:
        stroka_s_plusom = " ⊕"
        t = ""
    else:
        plus = ""
        for g in range(0, len(reg_pre) - 2):
            if g == ((len(reg_pre) - 2) // 2)-1:
                plus = plus + "⊕"
            else:
                plus = plus + "‾"
        stroka_s_plusom = "|" + plus + "|"
        t = "   " + "‾" * (len(reg_pre) - 2)
    r = "└—" + stroka_s_plusom
    next = "  ➔  "
    print(f"{q}{next}{reg_fut_real}\n{w}\n{r}\n{t}")
    
    if reg_fut_real == reversed_reg_fut_imag:
        print("Сохраняем регистр")
        return True
    else:
        print("Меняем регистр")
        return False
# STROKA = "00011011101010"
# STROKA = "100111110001101"
STROKA = str(input("Введите строку бит: "))
DLINA_STROKI = len(STROKA)
matrix = []
N0 = STROKA.find("1")
x = sp.symbols('x')
print(f"\nПодбираем регистр сдвига для генерации битовой строки {STROKA}")
print(f"N0 = {N0}")
if N0 == 0:
    N = -1
    k = 0
    p = "x**0"
    mass = [N, k, p]
    matrix.append(mass)
    print(f"При N0 = 0 начальные условия:")
    index_dlya_vivoda = find_row_by_element(matrix, 0, -1)
    print(f"{matrix[index_dlya_vivoda][0]}\t{matrix[index_dlya_vivoda][1]}\t{matrix[index_dlya_vivoda][2]}")    
else:
    print(f"При N0 != 0 начальные условия:")
    for N in range (0, N0):
        k = 0
        p = 1
        mass = [N, k, p]
        matrix.append(mass)
        print(f"{mass[0]}\t{mass[1]}\t{mass[2]}")
Pn0 = f"x**{N0+1} + x**0"
kn0 = find_max_number(Pn0)
mass = [N0, kn0, Pn0]
matrix.append(mass)
print(f"{mass[0]}\t{mass[1]}\t{mass[2]}")
m = N0
print(f"___________________________________\nНачинаем рассчёт реального регистра\n___________________________________")
dlina_registra = kn0
if matrix[0][0] == -1:
    first_line = matrix.pop(0)
for VVV in range(N0 + 1, len(STROKA)):
    mogem_ispolsovat_proshliy = proverka_generatsii(STROKA, VVV, dlina_registra, matrix[VVV-1][2])
    if mogem_ispolsovat_proshliy:
        mass = [VVV, matrix[VVV-1][1], matrix[VVV-1][2]]
        matrix.append(mass)
        print(f"P({VVV}) = P({VVV-1}) = {mass[2]}")
        print("___________________________________")
    else:
        if m == 0:
            print(f"m = 0")
            t1 = 0 - first_line[1]
            print(f"t1 = m - k(m-1) = 0 - {first_line[1]} = {t1}")
        else:
            print(f"m = {m}")
            t1 = m - matrix[m-1][1]
            print(f"t1 = m - k(m-1) = {m} - {matrix[m-1][1]} = {t1}")
        t2 = VVV - matrix[VVV-1][1]
        print(f"t2 = n - k(n-1) = {VVV} - {matrix[VVV-1][1]} = {t2}")
        if t1 >= t2:
            if m == 0:
                new_p = f"{matrix[VVV-1][2]} + x**{t1-t2} * ({first_line[2]})" 
            else:
                new_p = matrix[VVV-1][2] + f" + x**{t1-t2} * ({matrix[m-1][2]})" 
            new_p = str(sp.simplify(sp.expand(new_p)))
            new_p = uprostit_p(new_p)
            print('t1 >= t2')
            print(f"P(n) = P(n-1) + x**(t1-t2) * P(m-1)\nP({VVV}) = P({VVV-1}) + x**{t1-t2} * P({m-1})")
            print(f"Новый регистр: {new_p}")
            new_k = find_max_number(new_p)
        elif t2 > t1:
            if m == 0:
                new_p = f"x**{t2-t1} * ({matrix[VVV-1][2]}) + ({first_line[2]})"
            else:
                new_p = f"x**{t2-t1} * ({matrix[VVV-1][2]}) + ({matrix[m-1][2]})" 
            new_p = str(sp.simplify(sp.expand(new_p)))
            new_p = uprostit_p(new_p)
            new_k = find_max_number(new_p)
            print('t2 > t1')
            print(f"P(n) = x**(t2-t1) * P(n-1) + P(m-1)\nP({VVV}) = x**{t2-t1} * P({VVV-1} + P({m-1}))")
            print(f"Новый регистр: {new_p}")
        mass = [VVV, new_k, new_p]
        matrix.append(mass)
        print("___________________________________")
    obnovit_m(matrix)
    new_dlina_registra = matrix[len(matrix)-1][1] 
    if new_dlina_registra > dlina_registra:
        dlina_registra = new_dlina_registra
print("\nВывод матрицы:")
if N0 == 0:
    matrix.insert(0, first_line)
Zagolovok = ["N", "k", "P(N)"]
matrix.insert(0, Zagolovok)
for i in range(len(matrix)):
    print(f"{matrix[i][0]}\t{matrix[i][1]}\t{matrix[i][2]}")
