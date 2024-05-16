import os
from funciones_varias import *
from funciones_matematicas import *

ejecutando = True

opciones_menu_principal = ['    *** Menu principal ***   ',
                           '1. Ingresar 1er operando',
                           '2. Ingresar 2do operando',
                           '3. Calcular operaciones',
                           '4. Informar resultados',
                           '5. Salir']

elecciones_validas_menu_principal = ['1', '2', '3', '4', '5']

elecciones_validas_punto_3 = ['a', 'b', 'c', 'd', 'e']

while ejecutando:
    os.system('cls')

    opcion_elegida_menu_principal = crear_menu(opciones_menu_principal)
    while not verificar_opcion(opcion_elegida_menu_principal, elecciones_validas_menu_principal):
        print('\n',
              'Opcion invalida. Reingrese la opcion (1, 2, 3, 4, 5)\n')
        opcion_elegida_menu_principal = crear_menu(
            opciones_menu_principal)

    match(opcion_elegida_menu_principal):

        case '1':
            operando_a = input('Ingrese el primer operando: ')
            while not validar_digito(operando_a):
                operando_a = input(
                    'El valor ingresado no es un numero. Reingrese el primer valor: ')

        case '2':
            operando_b = input('Ingrese el segundo operando: ')
            while not validar_digito(operando_b):
                operando_b = input(
                    'El valor ingresado no es un numero. Reingrese el segundo valor: ')

        case '3':
            operando_a, operando_b = normalizar_operandos(
                [operando_a, operando_b])

            opcion_elegida_punto_3 = crear_menu([f'a. Calcular la suma ({operando_a} + {operando_b})',
                                                 f'b. Calcular la resta ({operando_a} - {operando_b})',
                                                 f'c. Calcular la division ({operando_a} / {operando_b})',
                                                 f'd. Calcular la multiplicacion ({operando_a} * {operando_b})',
                                                 f'e. Calcular factorial ({operando_a}!)'])
            while not verificar_opcion(opcion_elegida_punto_3, elecciones_validas_punto_3):
                print('\n',
                      'Opcion invalida. Reingrese la opcion (a, b, c, d, e)\n')
                opcion_elegida_punto_3 = crear_menu([f'a. Calcular la suma ({operando_a} + {operando_b})',
                                                     f'b. Calcular la resta ({operando_a} - {operando_b})',
                                                     f'c. Calcular la division ({operando_a} / {operando_b})',
                                                     f'd. Calcular la multiplicacion ({operando_a} * {operando_b})',
                                                     f'e. Calcular factorial ({operando_a}!)'])

            match(opcion_elegida_punto_3):

                case 'a':
                    resultado_suma = sumar(operando_a, operando_b)
                    informar_operacion_exitosa()

                case 'b':
                    resultado_resta = restar(operando_a, operando_b)
                    informar_operacion_exitosa()

                case 'c':
                    try:
                        resultado_division = dividir(
                            operando_a, operando_b)
                        informar_operacion_exitosa()
                    except ZeroDivisionError:
                        print('ERROR. No se puede dividir por 0.')
                        os.system('pause')

                case 'd':
                    resultado_multiplicacion = multiplicar(
                        operando_a, operando_b)
                    informar_operacion_exitosa()

                case 'e':
                    resultado_factorializacion = factorializar(operando_a)
                    informar_operacion_exitosa()

        case '4':

            print('\nINFORME DE RESULTADOS\n')
            try:
                if resultado_suma is not None:
                    print(
                        f'El resultado de {operando_a} + {operando_b} es {resultado_suma}\n')
            except NameError:
                pass

            try:
                if resultado_resta is not None:
                    print(
                        f'El resultado de {operando_a} - {operando_b} es {resultado_resta}\n')
            except NameError:
                pass

            try:
                if resultado_division is not None:
                    print(
                        f'El resultado de {operando_a} / {operando_b} es {resultado_division}\n')
            except NameError:
                pass

            try:
                if resultado_multiplicacion is not None:
                    print(
                        f'El resultado de {operando_a} * {operando_b} es {resultado_multiplicacion}\n')
            except NameError:
                pass

            try:
                if resultado_factorializacion is not None:
                    print(
                        f'El resultado de {operando_a}! es {resultado_factorializacion}\n')
            except NameError:
                pass

            os.system('pause')

        case '5':
            if input('CONFIRMAR SALIDA (si/no):') == 'si':
                ejecutando = False
