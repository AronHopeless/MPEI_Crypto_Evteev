import sympy as sp
#разделил бы на функции
#разделил бы на функции

def Convert_to_Polinom(string):
    # variables = sp.symbols(' '.join(f'x{i}' for i in range(2, DLINA + 2)))
    temp = sp.expand(string)
    simplier_temp = sp.simplify(temp)
    # print(simplier_temp)
    factors = sp.factor(simplier_temp)                
    # Создайте список слагаемых, в которых есть чётные множители
    chetnble_slagaemie = [term for term in sp.Add.make_args(factors) if any(factor.is_even for factor in sp.Mul.make_args(term))]

    # Исключите чётные слагаемые из многочлена
    res = simplier_temp - sp.Add(*chetnble_slagaemie)
    res = str(res)
    # print(res)
    if res[0] != "1" and res[0] != "x":
        res = res[2:]
    indexis = []
    first_index = res.find(" + ")
    while first_index != -1:
        indexis.append(first_index)
        first_index = res.find(" + ", first_index + 1) 
    # print(indexis)

    counter_umenshit_index = 0
    for i in indexis:
        # print(f"x[i+3] = {res[i+3+counter_umenshit_index]}")
        if res[i+3+counter_umenshit_index] != "1" and res[i+3+counter_umenshit_index] != "x":
            temp = res[:(i+3+counter_umenshit_index)] + res[(i+5+counter_umenshit_index):]
            counter_umenshit_index -= 2
            res = temp
    return res




def modulo_add(a, b):
    return (a + b) % 2

class Num:
    def __init__(self, des, doub):
        self.des = des
        self.doub = doub

# Пользователь вводит длину регистра сдвига
DLINA = int(input("Введите длину регистра сдвига: "))

# Создаем пустой список для хранения объектов класса Num
mass_sostoyaniy = []
mass_sootvetstviy = []

# Заполняем список объектами класса Num
for i in range(2**DLINA):
    des_view = i
    doub_view = bin(i)[2:].zfill(DLINA)
    Num_massiva = Num(des_view, doub_view)
    mass_sostoyaniy.append(Num_massiva)

print("Введите функцию f")
print("Пример ввода функции (x - английский, через пробел): 'x2 + x3 * x4 + x5 + 1'")
print("xi считается СПРАВА НАЛЕВО начиная с х1, как завещал безумный дед")
while True:
    func_obratniy = input("f = ")
    vse_ne_ok = []
    for i in func_obratniy:
        if i == 'x' or i == ' ' or i == '+' or i == '*':
            vse_ne_ok.append(0)
        else:            
            try:
                temp = int(i)
                if temp > DLINA:
                    print("Неверно задана f.")
                    vse_ne_ok.append(1)
                else:
                    vse_ne_ok.append(0)
            except:
                vse_ne_ok.append(1)
                
    temp = 1            
    if temp in vse_ne_ok:
        print("Неверно задана f.")
        continue
    else: 
        break
# func_obratniy = "x1 + x2 * x3 + 1"
f_list = list(func_obratniy)  # Преобразуем строку в список символов один раз
zamenbI = {}  # Создадим словарь для отслеживания замен

for j in range(len(f_list)):
    if f_list[j] == 'x' and j + 1 < len(f_list) and f_list[j + 1].isdigit():
        value_afte_x = ''
        k = j + 1
        while k < len(f_list) and f_list[k].isdigit():
            value_afte_x += f_list[k]
            k += 1
        if value_afte_x:
            zamenbI[j] = str(DLINA + 1 - int(value_afte_x))

for j, change in zamenbI.items():
    f_list[j + 1] = change

func = ''.join(f_list)
for k in range(2**DLINA):
    var_dict_view = {}
    for i in range(1, DLINA + 1):
        name_var = f"x{i}"
        value = int(mass_sostoyaniy[k].doub[i-1])
        var_dict_view[name_var] = value
    
        new_registr = 0
    #сделали словарь переменных 

    #считаем теперь новый элемент    
    index_vhoda = -1
    splited_f = func.split(" ")
    mass_vhodov_umnogenia = []
    indices = [i for i, x in enumerate(splited_f) if x == "*"]    
    # print (indices)  #индексы входа всех знаков умножить
    while len(indices) > 0:
        if splited_f[indices[0]-1] in var_dict_view:
            temp = var_dict_view[splited_f[indices[0]-1]] * var_dict_view[splited_f[indices[0]+1]]
        else:
            temp = splited_f[indices[0]-1] * var_dict_view[splited_f[indices[0]+1]]
        # print(f"{var_dict_view[splited_f[indices[0]-1]]} * {var_dict_view[splited_f[indices[0]+1]]}")
        # print (f"{temp} это новая переменная на месте умножения")   
        splited_f[indices[0]-1 : indices[0]+2] = [temp]
        indices = [i for i, x in enumerate(splited_f) if x == "*"]    
     
    # print (f"{splited_f} 'это после удаления умножений")

    for i in range(0, len(splited_f)):
        if splited_f[i] in var_dict_view:
            splited_f[i] = var_dict_view[splited_f[i]]
        elif splited_f[i] == "1":
            splited_f[i] = 1

    # print (f"{splited_f} 'это после подставновки переменных")

    for i in splited_f:
        if type(i) != type("1"):
            new_registr += i
    new_registr = str(new_registr % 2)
    # print (f"{new_registr} - новое значение первой ячейки")
    doub_view = new_registr + mass_sostoyaniy[k].doub[0:-1]
    des_view = int(doub_view, 2)
    Num_sootvetstv = Num(des_view, doub_view)
    mass_sootvetstviy.append(Num_sootvetstv)
    
print("Список переходов: ")
for k, l in zip(mass_sostoyaniy, mass_sootvetstviy):
    print(f"{k.doub} -> {l.doub}; {k.des} -> {l.des}")
    
print("\nИмеющиеся циклы:")
vse_tsikli = []
spisok_vseh_znacheniy_dlya_tsiklov = []
for i in mass_sostoyaniy:
    spisok_vseh_znacheniy_dlya_tsiklov.append(i.des)

while spisok_vseh_znacheniy_dlya_tsiklov != []:
    new_tsikl = []
    new_tsikl.append(spisok_vseh_znacheniy_dlya_tsiklov[0])
    spisok_vseh_znacheniy_dlya_tsiklov.pop(0)

    
    while True:
        k = None
        for i, obj in enumerate(mass_sostoyaniy):
            if obj.des == new_tsikl[-1]:
                k = i
                break
        
        if mass_sootvetstviy[k].des == new_tsikl[0]:
            break
        new_tsikl.append(mass_sootvetstviy[k].des) 
        spisok_vseh_znacheniy_dlya_tsiklov.remove(mass_sootvetstviy[k].des)
    vse_tsikli.append(new_tsikl)
    
for k in vse_tsikli:
    strings = [str(x) for x in k]
    print("[" + " -> ".join(strings) + "]")

f_otvet = func_obratniy

# hvatit = 0
while len (vse_tsikli) != 1:
    for k in vse_tsikli[0]:
        if len(vse_tsikli) == 1:
            break
        for t in vse_tsikli[1]:
            if bin(k)[:-1] == bin(t)[:-1] and bin(k)[-1] != bin(t)[-1]:
                alfa = k
                alfa_strih = t
                for i, obj in enumerate(mass_sostoyaniy):
                    if obj.des == k:
                        beta = mass_sootvetstviy[mass_sostoyaniy.index(obj)].des
                        break
                for i, obj in enumerate(mass_sostoyaniy):
                    if obj.des == t:
                        beta_strih = mass_sootvetstviy[mass_sostoyaniy.index(obj)].des
                        break
                print()    
                print(f"Рассмотрим два цикла: ")
                strings = [str(x) for x in vse_tsikli[0]]
                print("[" + " -> ".join(strings) + "]")
                strings = [str(x) for x in vse_tsikli[1]]
                print("[" + " -> ".join(strings) + "]")
                print(f"Найдём такие альфа и бета, чтобы они были в разных циклах и отличались последним символом двоичного представления.")
                print(f"\ta = {alfa}, a' = {alfa_strih}")
                print(f"\tb = {beta}, b' = {beta_strih}")
                print(f"Раньше выполнялись связи:\n\ta->b и a'->b'\n\t{alfa}->{beta} и {alfa_strih}->{beta_strih}")
                print(f"Теперь новые связи:\n\ta->b' и a'->b\n\t{alfa}->{beta_strih} и {alfa_strih}->{beta}")
                new_tsikl = []
                for k in vse_tsikli[0]:         #в первом цикле
                    new_tsikl.append(k)         #в новый цикл добавляем элементы из первого цикла
                    if k == alfa:               #если мы добавили элемент, с которого переход во второй цикл
                        index_vhoda_vo_vtoroy = vse_tsikli[1].index(beta_strih)          #ищем индекс входа во второй цикл
                        for i in range(0, len(vse_tsikli[1])):
                            new_tsikl.append(vse_tsikli[1][index_vhoda_vo_vtoroy % len(vse_tsikli[1])])
                            index_vhoda_vo_vtoroy += 1
                            
                # print(f"найдена пара: {k} - в кольце 0, {t} - в кольце 1")
                vse_tsikli[:2] = [new_tsikl]
                strings = [str(x) for x in new_tsikl]
                print("[" + " -> ".join(strings) + "]")
                
                bin_alfa = bin(alfa)[2:].zfill(DLINA)
                f_strih = ""
                
                
                
                w = 0
                i = DLINA
                # print(bin_alfa)
                while i > 1:
                    # print(bin_alfa[w])
                    if bin_alfa[w] == "0":
                        f_strih = f" * (x{i} + 1)" + f_strih
                    elif bin_alfa[w] == "1":
                        f_strih = f" * x{i}" + f_strih
                    i -= 1
                    w += 1
                f_strih = f_strih[3:]
                print(f"При склеивании были:\n\tиспользована альфа: {bin_alfa}\n\tполучена f' = {f_strih}")    
                f_otvet = f_otvet + " + " + f_strih
                
print(f"\nИтоговое выражение после объединения циклов: \n{f_otvet}")

result = Convert_to_Polinom(f_otvet)
print(f"\nИтоговое выражение после раскрытия скобок в формате полинома ЛжеГалкина: \n{result}")
