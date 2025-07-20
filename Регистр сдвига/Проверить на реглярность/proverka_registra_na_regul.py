STROKA = str(input("Введите битовую строку без запятых: "))
#STROKA = "1010101001010101"
STROKA_list = [g for g in STROKA]
temp = ", ".join(STROKA_list)
if len(STROKA) == 16:
    print(f"\nРассчитываем регистр с f(x1, x2, x3, x4) = ({temp})")
    print("Регистр сдвига регулярный, если выполняется условие: f = x1 ⊕ g(x2, x3, x4), где g - полином Жегалкина ")
    print("Построим полином Жегалкина для имеющейся битовой строки.")
    matrix = []
    mass = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    matrix.append(mass)
    mass = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    matrix.append(mass)
    mass = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    matrix.append(mass)
    mass = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    matrix.append(mass)
    new_STROKA_list = []
    string_stroka = STROKA_list
    #print(string_stroka)
    for i in STROKA_list:
        new_STROKA_list.append(int(i))
    STROKA_list = new_STROKA_list
    mass_vihod = []
    matrix.append(STROKA_list)
    print(f"x1|x2|x3|x4|f\tПолином Жегалкина")
    temp = "".join(string_stroka)
    bitoviy_polinom = ""
    for i in range(0, 16):
        #print(temp)
        print(f"{matrix[0][i]} |{matrix[1][i]} |{matrix[2][i]} |{matrix[3][i]} |{matrix[4][i]}\t{temp}")
        newtemp = ""
        for i in range (1, len(temp)):
            if temp[i-1] == "0" and temp[i] == "0":
                newtemp = newtemp + "0"
            elif temp[i-1] == "1" and temp[i] == "1":
                newtemp = newtemp + "0"
            elif temp[i-1] == "0" and temp[i] == "1":
                newtemp = newtemp + "1"
            elif temp[i-1] == "1" and temp[i] == "0":
                newtemp = newtemp + "1"
        bitoviy_polinom = bitoviy_polinom + temp[0]
        temp = newtemp
    #print(bitoviy_polinom, type(bitoviy_polinom))
    polinom = []
    for i in range(0, len(bitoviy_polinom)):
        slagaemoe_polinoma = []
        if bitoviy_polinom[i] == "1":
            for k in range(0, 4):
                if matrix[k][i] != 0:
                    slagaemoe_polinoma.append(f"x{k+1}")
        str_slag_pol = "*".join(slagaemoe_polinoma)
        if str_slag_pol != "":
            polinom.append(str_slag_pol)
    str_polinom = " ⊕ ".join(polinom)
    flag_regul = True
    print("Полином Жегалкина:")
    print(str_polinom)
    
    if "x1" not in polinom:
        flag_regul = False
    else:
        a = polinom.index("x1")
        for i in range(0, len(polinom)):
            if i != a:
                t = polinom[i].find("x1")
                if t != -1:
                    flag_regul = False
    print("Регистр является регулярным, если его можно привести к виду f = x1 ⊕ g(x2, x3, x4)")
    if flag_regul: 
        print("\nДанный регистр регулярный\n")
    else: 
        print("\nДанный регистр не является регулярным\n")
else:
    print('Внимание! Введено не 16 символов')