from fractions import Fraction
from tabulate import tabulate

def smart_print(frac):
    if isinstance(frac, Fraction):
        if frac.denominator == 1:
            return frac.numerator
        d = frac.denominator
        while d % 2 == 0: d //= 2
        while d % 5 == 0: d //= 5
        return float(frac) if d == 1 else str(frac)
    else:
        return frac

def ShowFractalTable(matrix: list[list[any]]):
    m = [[cell for cell in row] for row in matrix]
    for a in range(len(m)):
        for b in range(len(m[a])):
            if isinstance(m[a][b], Fraction):
                m[a][b] = smart_print(m[a][b])
    print(tabulate(m[1:], headers=m[0], tablefmt="fancy_grid"))

def vvod_usloviy():
    a = int(input('Введите количество базовых переменных: '))
    b = int(input('Введите количество условий: '))
    return a, b

def vvod_parametrov(kolvo_base_X, kolvo_uslov):
    matrix_parametrov = []
    for a in range(kolvo_uslov):
        param_usloviya = []
        print(f'Введите параметры для условия {a+1}:')
        for b in range(kolvo_base_X):
            param_usloviya.append(float(input(f'Множитель при x{b+1}: ')))
        param_usloviya.append(float(input('Ограничение: ')))
        matrix_parametrov.append(param_usloviya)
    return matrix_parametrov

def vvod_func_coeff(kolvo_base_X, kolvo_uslov):
    mass_koef = []
    print(f'Введите коэффициенты целевой функции:')
    for b in range(kolvo_base_X):
        mass_koef.append(float(input(f'Коэффициент x{b+1}: ')))
    # коэффициенты для искусственных/доп. переменных = 0
    mass_koef += [0]*kolvo_uslov
    return mass_koef

def build_initial_table(matrix_param: list[list[any]], mass_koef: list[any], num_base_X):
    num_usloviy = num_dop_X = len(matrix_param)
    num_vseh_X = num_base_X + num_usloviy
    table = []
    header = ['i', 'Б', 'C', 'P']
    tailer = ['M+1', None, None, 0]
    for k in range(num_vseh_X):
        header.append(f'x{k+1}')
        tailer.append(-mass_koef[k])
    table.append(header)
    for a in range(num_usloviy):
        stroka = [a + 1, f'x{num_base_X + a + 1}', mass_koef[num_base_X + a], matrix_param[a][-1]]
        for b in range(num_base_X):
            stroka.append(matrix_param[a][b])
        for c in range(num_dop_X):
            if a == c:
                stroka.append(1)
            else:
                stroka.append(0)
        # print(stroka)
        table.append(stroka)
    table.append(tailer)
    return table

def Solution(nabor_tabl, mass_kef, num_base_x):
    current_iteration = 0
    flag_zaversheniya = False
    while not flag_zaversheniya:
        matrix = nabor_tabl[current_iteration]
        Mmin = min(matrix[-1][4:len(matrix[0])])
        print(f'\nВ строке M+1 находим минимальный элемент: {Mmin}')   
        razresh_stolb = matrix[-1][4:len(matrix[0])].index(Mmin) + 4
        print(f'{Mmin} находится в столбце {matrix[0][razresh_stolb]}. Он является разрешающим')
        print(f'Разделим значения столбца P на соответствующие значения разрешающего столбца:')
        min_index = 1
        d = (Fraction(matrix[min_index][3]) / Fraction(matrix[min_index][razresh_stolb])).limit_denominator()
        print(f'{matrix[min_index][3]} / {smart_print(matrix[min_index][razresh_stolb])} = {d}')
        for e in range(2, len(matrix) - 1):
            if matrix[e][razresh_stolb] > 0:
                t = (Fraction(matrix[e][3]) / Fraction(matrix[e][razresh_stolb])).limit_denominator()
                print(f'{matrix[e][3]} / {smart_print(matrix[e][razresh_stolb])} = {t}')
                if t < d:
                    d = t
                    min_index = e
        print(f'Из полученных значений минимальным является {d} в строке i={min_index}')
        
        pivot = matrix[min_index][razresh_stolb]
        print(f'Значит, разрешающим элементом является значение из строки i={min_index} и разрешающего столбца: {smart_print(pivot)}\n')
        print(f'Определим симплекс-таблицу {current_iteration + 2}')
        
        new_matrix = [[cell for cell in row] for row in matrix]
        
        new_matrix[min_index][1] = matrix[0][razresh_stolb]
        print(f'В столбец С записывается коэффициент соответствующего х')
        for a in range(1, len(matrix) - 1):
            new_matrix[a][2] = mass_kef[int(new_matrix[a][1][1:]) - 1]
        
        for a in range(1, len(new_matrix)):
            if a != min_index:
                new_matrix[a][razresh_stolb] = 0
        print(f'В новую таблицу переносится строка предыдущей таблицы, содержащая разрашающий элемент и разделённая на него же')
        print(f'Все остальные элементы разрешающего столбца заполняются нулями')
        for b in range(3, len(new_matrix[0])):
            # if b != razresh_stolb:
            new_matrix[min_index][b] = (Fraction(new_matrix[min_index][b]) / Fraction(pivot)).limit_denominator()
                
        print(f'К остальным элементам применяется метод прямоугольника')
        for a in range(1, len(new_matrix)):
            if a != min_index:
                for b in range(3, len(new_matrix[0])):
                    if b != razresh_stolb:
                        new_matrix[a][b] = (Fraction(matrix[a][b] * pivot - matrix[a][razresh_stolb] * matrix[min_index][b]) / Fraction(pivot)).limit_denominator()


        print(f'Получаем следующую симплекс-таблицу {current_iteration + 2}: ')
        ShowFractalTable(new_matrix)
        current_iteration += 1
        nabor_tabl[current_iteration] = new_matrix
        
        
        
        
        print('Проверим корректность решения, рассчитав Z:')
        Zz = 0
        temp_1 = []
        temp_2 = []
        temp_z = []
        for a in range(1, len(nabor_tabl[current_iteration]) - 1):
            temp_1.append(nabor_tabl[current_iteration][a][2])
            temp_2.append(nabor_tabl[current_iteration][a][3])
            temp = nabor_tabl[current_iteration][a][2] * nabor_tabl[current_iteration][a][3]
            temp_z.append(temp)
            Zz += temp
        print(f'Z = {" + ".join(f"{xi}*{yi}" for xi, yi in zip(temp_1, temp_2))} = {' + '.join(str(a) for a in temp_z)} = {Zz} ≈ {round(float(Zz))}')    
            
        if nabor_tabl[current_iteration][-1][3] == Zz:
            print(f'Значение Z = {Zz} совпало со значением в строке М+1 таблицы = {nabor_tabl[current_iteration][-1][3]}')
        else:
            print(f'Значение Z = {Zz} НЕ совпало со значением в строке М+1 таблицы = {nabor_tabl[current_iteration][-1][3]}. Допущена ошибка!')
        
        
        print(f'Проверим, является ли полученное решение оптимальным. Для этого строка M+1 не должна содержать отрицательных значений.')
        minusovie_znach = []
        for a in new_matrix[-1][4:len(new_matrix[-1])]:
            if a < 0:
                minusovie_znach.append(smart_print(a))
        if minusovie_znach != []:
            print(f'В строке М+1 содержатся отрицательные значения: {', '.join(str(a) for a in minusovie_znach)}, значит найденное решение не оптимально, следует повторить вычисления')
            
        else:
            print(f'Строка M+1 не содержит отрицательных значений, значит решение оптимально')
            flag_zaversheniya = True
            print(f'Текущая максимальная прибыль составляет {round(float(Zz))}, однако она рассчитывается исходя из нецелого кол-ва продукции.')
            print(f'Проведём округление до целых единиц продукции. В таком случае будет выпущено: ')
            kolvo_vipuska = {}
            for a in range(len(mass_kef)):
                kolvo_vipuska[f'x{a + 1}'] = 0
            for a in range(1, len(new_matrix) - 1):
                kolvo_vipuska[new_matrix[a][1]] = new_matrix[a][3]
            kolvo_vipuska_int = {}
            for g in range(num_base_x):
                kolvo_vipuska_int[f'x{g + 1}'] = int(kolvo_vipuska[f'x{g + 1}'])
            for b in range(num_base_x):
                print(f'продукции х{b+1}: {kolvo_vipuska_int[f'x{b + 1}']}')
                
            terms = []
            Cash = 0
            for c in range(num_base_x):
                terms.append(f'{kolvo_vipuska_int[f'x{c+1}']} • {mass_kef[c]}')
                Cash += kolvo_vipuska_int[f'x{c+1}'] * mass_kef[c]
            result = " + ".join(terms)
            result = result + f' = {Cash}'

            print(f'Тогда и реальная максимальная прибыль составит: ')
            print(result)
        
def print_usloviya(matrix_param, kolvo_base_X):
    for i in range(len(matrix_param)):
        terms = []
        for j in range(kolvo_base_X):
            coeff = matrix_param[i][j]
            if coeff == 0:
                continue
            # Определяем знак
            sign = "+" if coeff > 0 else "-"
            abs_coeff = abs(coeff)
            term = f"{abs_coeff}*x{j+1}" if abs_coeff != 1 else f"x{j+1}"
            if j == 0:
                term = f"{coeff}*x{j+1}" if coeff != 1 else f"x{j+1}"
            else:
                term = f" {sign} {term}"
            terms.append(term)
        equation = "".join(terms) + f' + x{len(matrix_param) + i}' + f" = {matrix_param[i][-1]}"
        print(equation)


def print_objective_function(coefficients):
    terms = []
    for i, coeff in enumerate(coefficients):
        sign = "+" if coeff >= 0 else "-"
        abs_coeff = abs(coeff)
        term = f"{abs_coeff}*x{i+1}" 
        if i == 0:
            term = f"{coeff}*x{i+1}"
        else:
            term = f" {sign} {abs_coeff}*x{i+1}"
        terms.append(term)
    equation = "".join(terms) + " -> max"
    print(equation)

# Ввод данных
kolvo_base_peremennix, kolvo_usloviy = vvod_usloviy()
matrix_parametrov = vvod_parametrov(kolvo_base_peremennix, kolvo_usloviy)
mass_koef = vvod_func_coeff(kolvo_base_peremennix, kolvo_usloviy)

# kolvo_base_peremennix, kolvo_usloviy = 3, 3

# matrix_parametrov = [
#     [1,1,1,2000],
#     [15,150,5,80000],
#     [0.5,5,0.1,2000]
# ]
# mass_koef = [100, 500, 75, 0, 0, 0]

# kolvo_base_peremennix, kolvo_usloviy = 3, 4 

# matrix_parametrov = [
#     [1,1,1,5800],
#     [0,1,1,1400],
#     [1.4,19,1.2,27000],
#     [1.4,3.4,1.4,12000]
# ]
# mass_koef = [160, 340, 270, 0, 0, 0, 0]



print_usloviya(matrix_parametrov, kolvo_base_peremennix)
print_objective_function(mass_koef)
VseTabl = {}
Tabl0 = build_initial_table(matrix_parametrov, mass_koef, kolvo_base_peremennix)
VseTabl[0] = Tabl0
ShowFractalTable(Tabl0)
Solution(VseTabl, mass_koef, kolvo_base_peremennix)
