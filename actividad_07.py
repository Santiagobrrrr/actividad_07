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
            print(f"SUMA - PROMEDIO - POSTITIVO , NEGATIVO o CEROS, MULTIPLOS DE 3")

        case "2":
            print(f"CALCULAR ÁREA Y PERIMETRO DE UN RECTÁNGULO")

        case "3":
            print(f"VERIFICACIÓN DE NUMERO PRIMO")

        case "4":
            print(f"PROMEDIO DE CALIFICACIONES, MAYOR A 85, EN RIESGO DE ZONA")

        case "5":
            print(f"VERIFICACIÓN DE NUMERO MAYOR O MENOR DE LISTA")

        case "6":
            print(f"CALCULADORA")

        case "7":
            print(f"Ha salido del programa, nos vemos...")
            break

        case _:
            print(f"Valor erroneo ingresado, intente de nuevo")