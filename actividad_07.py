list_numbers = []
def list_user():
    how_number = int(input("Introduce un numero de valores a ingresar: "))
    for i in range(how_number):
        numbers_user = float(input(f"Ingrese el valor: "))
        list_numbers.append(numbers_user)

def sum_total():
    return sum(list_numbers)

def prom_list():
    return sum(list_numbers)/len(list_numbers)

def positive_negative_zero():
    count_positive = 0
    count_negative = 0
    count_zero = 0
    for i in list_numbers:
        if i > 0:
            count_positive += 1
        elif i < 0:
            count_negative += 1
        elif i == 0:
            count_zero += 1
    print(f"La cantidad de positivos es de: {count_positive}")
    print(f"La cantidad de negativos es de: {count_negative}")
    print(f"La cantidad de cero es de: {count_zero}\n")

def multiples_3():
    count = 0
    for i in list_numbers:
        if i % 3 == 0:
            count += 1
    print(f"La cantidad de multiplos de 3 es de: {count}\n")

def area_rectangle(base_rectangle,height_rectagle):
    return print(f"El área del rectangulo es de: {base_rectangle * height_rectagle}")

def perimeter_rectangle(base_rectangle,height_rectagle):
    return print(f"El perimetro del rectangulo es de: {(2*base_rectangle) + (2*height_rectagle)}")

def greater_than_85():
    count_greater_than_85 = 0
    for i in list_numbers:
        if i >= 85:
            count_greater_than_85 += 1
    return count_greater_than_85

def less_than_60():
    count_less_than_60 = 0
    for i in list_numbers:
        if i >0 and i <= 60:
            count_less_than_60 += 1
    return count_less_than_60

def max_num():
    return max(list_numbers)

def min_num():
    return min(list_numbers)

def add_calculator(number_user_1, number_user_2):
    return number_user_1 + number_user_2

def subtrac_calculator(number_user_1, number_user_2):
    return number_user_1 - number_user_2

def multiply_calculator(number_user_1, number_user_2):
    return number_user_1 * number_user_2

def divide_calculator(number_user_1, number_user_2):
    return number_user_1 / number_user_2

while True:
    print(f"MENÚ")
    print(f"1. SUMA - PROMEDIO - POSTITIVO , NEGATIVO o CEROS, MULTIPLOS DE 3")
    print(f"2. CALCULAR ÁREA Y PERIMETRO DE UN RECTÁNGULO")
    print(f"3. VERIFICACIÓN DE NUMERO PRIMO")
    print(f"4. PROMEDIO DE CALIFICACIONES, MAYOR A 85, EN RIESGO DE ZONA")
    print(f"5. VERIFICACIÓN DE NUMERO MAYOR O MENOR DE LISTA")
    print(f"6. CALCULADORA")
    print(f"7. SALIR")

    option_user = input(f"Ingrese una de las opciones (1-7): ")

    match option_user:
        case "1":
            list_user()
            while True:
                print(f"SUMA - PROMEDIO - POSTITIVO , NEGATIVO o CEROS, MULTIPLOS DE 3")
                print(f"¿Qué opción desea realizar?")
                print(f"1. Suma")
                print(f"2. Promedio")
                print(f"3. Cantidad de positivos, negativos, ceros")
                print(f"4. Multiplos de 3")
                print(f"5. Salir")
                option_number = input(f"Ingrese la opción que desea realizar (1-5): ")

                match option_number:
                    case "1":
                        print(f"La suma total es de {sum_total()}")

                    case "2":
                        print(f"El promedio es de {prom_list()}")

                    case "3":
                        positive_negative_zero()

                    case "4":
                        multiples_3()

                    case "5":
                        print("Regresando al menú...")
                        break
            list_numbers.clear()

        case "2":
            print(f"CALCULAR ÁREA Y PERIMETRO DE UN RECTÁNGULO")
            base_rectangle = float(input(f"Ingrese la base del rectangulo: "))
            height_rectangle = float(input(f"Ingrese la altura del rectangulo: "))
            area_rectangle(base_rectangle,height_rectangle)
            perimeter_rectangle(base_rectangle,height_rectangle)

        case "3":
            print(f"VERIFICACIÓN DE NUMERO PRIMO")

        case "4":
            print(f"PROMEDIO DE CALIFICACIONES, MAYOR A 85, EN RIESGO DE ZONA")
            list_user()
            print(f"El promedio de calificaciones es de: {prom_list()}")
            print(f"Cantidad de notas mayores a 85: {greater_than_85()}")
            print(f"Cantidad de notas en zona de riesgo: {less_than_60()}\n")
            list_numbers.clear()

        case "5":
            print(f"VERIFICACIÓN DE NUMERO MAYOR O MENOR DE LISTA")
            list_user()
            print(f"El número mayor de la lista es de: {max_num()}")
            print(f"El número menor de la lista es de: {min_num()}\n")
            list_numbers.clear()

        case "6":
            while True:
                print(f"-CALCULADORA-")
                print(f"1. Suma")
                print(f"2. Resta")
                print(f"3. Multiplicación")
                print(f"4. División")
                print(f"5. Salir")
                option_number = input(f"Ingrese la opción que desea realizar (1-5): ")

                if option_number == "5":
                    print(f"Regresando al menú...\n")
                    break

                number_user_1 = float(input(f"Ingrese el valor del primer número: "))
                number_user_2 = float(input(f"Ingrese el valor del segundo número: "))

                match option_number:
                    case "1":
                        print(f"La Suma es de: {add_calculator(number_user_1, number_user_2)}\n")

                    case "2":
                        print(f"La resta es de: {subtrac_calculator(number_user_1, number_user_2)}\n")

                    case "3":
                        print(f"La multiplicación de: {multiply_calculator(number_user_1, number_user_2)}\n")

                    case "4":
                        if number_user_2 == 0:
                            print(f"No se puede divir entre 0\n")

                        else:
                            print(f"La división es de: {divide_calculator(number_user_1, number_user_2)}\n")

                    case _:
                        print(f"valor inválido")

        case "7":
            print(f"Ha salido del programa, nos vemos...")
            break

        case _:
            print(f"Valor erroneo ingresado, intente de nuevo")