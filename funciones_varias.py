import os


def crear_menu(lista_opciones):
    """
    Crea un menu de opciones con las opciones recibidas y devuelve la opcion elegida por el usuario.

    Args:
        opciones (list): Son las opciones del menu

    Returns:
        char: Es la opcion elegida por el usuario
    """
    for opcion in lista_opciones:
        print(f'{opcion}')

    return input('ingrese una opcion: ')


def validar_digito(valor: any) -> True | False:
    """Recibe un valor cualquiera por parametros y verifica si es un digito o no.

    Args:
        valor (any): Valor a verificar.

    Returns:
        True | False: Si el valor es un digito: True | Si el valor no es un digito: False
    """
    return valor.isdigit()


def informar_operacion_exitosa():
    """Imprime un mensaje de operacion exitosa y realiza una pausa en la ejecucion.
    """
    print('Operacion realizada con exito.')
    os.system('pause')


def normalizar_operandos(operandos: list) -> list[int]:
    """Recibe una lista de valores y los convierte a enteros.

    Args:
        operandos (list): Lista de valores a convertir.

    Returns:
        list[int]: Lista de valores convertidos a enteros.
    """
    operandos_normalizados = []
    for operando in operandos:
        operandos_normalizados.append(int(operando))

    return operandos_normalizados


def verificar_opcion(opcion: str, opciones_validas: list) -> True | False:
    """Recibe por parametros una opcion solicitada y una lista con opcione validas y comprueba que la opcion solicitada este dentro de las validas.

    Args:
        opcion (str): Opcion solicitada.
        opciones_validas (list): Lista de opciones validas

    Returns:
        True | False: Si la opcion solicitada es valida: True | Si la opcion solicitada es invalida: False.
    """
    return opcion in opciones_validas
