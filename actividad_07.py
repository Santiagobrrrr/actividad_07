list_numbers = []
def list_user():
    how_number = int(input("Introduce un numero de valores a ingresar: "))
    for i in range(how_number):
        numbers_user = float(input(f"Ingrese el valor: "))
        list_numbers.append(numbers_user)

def sum_total():
    return print(f"La suma de la lista es de: {sum(list_numbers)}\n")

def prom_list():
    return print(f"El promedio es de {sum(list_numbers)/len(list_numbers)}\n")

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
                        sum_total()

                    case "2":
                        prom_list()

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

        case "3":
            print(f"VERIFICACIÓN DE NUMERO PRIMO")

        case "4":
            print(f"PROMEDIO DE CALIFICACIONES, MAYOR A 85, EN RIESGO DE ZONA")
            list_user()

        case "5":
            print(f"VERIFICACIÓN DE NUMERO MAYOR O MENOR DE LISTA")
            list_user()

        case "6":
            print(f"CALCULADORA")

        case "7":
            print(f"Ha salido del programa, nos vemos...")
            break

        case "8":
            print(list_numbers)

        case _:
            print(f"Valor erroneo ingresado, intente de nuevo")