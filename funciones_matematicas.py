def sumar(primer_sumando: int, segundo_sumando: int) -> int:
    """Recibe dos enteros por parametros y los suma.

    Args:
        primer_sumando (int): Primer sumando.
        segundo_sumando (int): Segundo sumando.

    Returns:
        int: Resultado de la suma.
    """
    return primer_sumando + segundo_sumando


def restar(minuendo: int, sustraendo: int) -> int:
    """Recibe dos enteros por parametros y resta el sustraendo al minuendo.

    Args:
        minuendo (int): Minuendo de la resta.
        sustraendo (int): Sustraendo de la resta.

    Returns:
        int: Resultado de la resta.
    """
    return minuendo - sustraendo


def dividir(dividendo: int, divisor: int) -> int | float:
    """Recibe dos enteros por parametros y divide el dividendo por el divisor.

    Args:
        dividendo (int): Dividendo de la division.
        divisor (int): Divisor de la division.

    Returns:
        int | float: Resultado de la division.
    """
    return dividendo / divisor


def multiplicar(multiplicando: int, multiplicador: int) -> int:
    """Recibe dos enteros por parametros y realiza el producto del multiplicando por el multiplicador.

    Args:
        multiplicando (int): Multiplicando del producto.
        multiplicador (int): Multiplicador del producto.

    Returns:
        int: Producto.
    """
    return multiplicando * multiplicador


def factorializar(operando_a: int) -> int:
    """Calcula el factorial de un nuemro.

    Args:
        n (int): numero a calcular.

    Raises:
        ValueError: valida numero entero natural.
        TypeError: valida tipo entero.

    Returns:
        int: factorial del numero recibido
    """
    if isinstance(operando_a, int):
        if operando_a < 0:
            raise ValueError('No esta definido el factorial de un negativo')
        fact = 1
        for i in range(2, operando_a + 1):
            fact *= i
        return fact
    else:
        raise TypeError('No es un numero')
