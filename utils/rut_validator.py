"""
Utilidad para validar y calcular dígito verificador de RUT chileno
"""
import operator
import math
from typing import Union


def calcular_dv(rut: str) -> str:
    """
    Calcula el dígito verificador de un RUT chileno.
    
    Args:
        rut (str): RUT sin puntos ni dígito verificador (primeros 8 dígitos)
        
    Returns:
        str: Dígito verificador ('0'-'9' o 'k')
        
    Example:
        >>> calcular_dv("12345678")
        '5'
    """
    # Limpiar el RUT (remover puntos, guiones, espacios)
    rut_limpio = ''.join(filter(str.isdigit, str(rut)))
    
    if not rut_limpio:
        raise ValueError("RUT inválido: debe contener al menos un dígito")
    
    # Convertir a lista de enteros
    rut_list_int = [int(x) for x in rut_limpio]
    
    # Secuencia de multiplicadores (de derecha a izquierda: 2,3,4,5,6,7)
    # Se repite si el RUT tiene más de 6 dígitos
    multiplicadores = [2, 3, 4, 5, 6, 7]
    
    # Calcular desde el final hacia atrás
    suma = 0
    for i, digito in enumerate(reversed(rut_list_int)):
        multiplicador = multiplicadores[i % len(multiplicadores)]
        suma += digito * multiplicador
    
    # Calcular el dígito verificador
    resto = suma % 11
    dv = 11 - resto
    
    if dv == 11:
        return "0"
    elif dv == 10:
        return "k"
    else:
        return str(dv)


def validar_rut(rut_completo: str) -> bool:
    """
    Valida un RUT completo (con dígito verificador).
    
    Args:
        rut_completo (str): RUT con formato XX.XXX.XXX-X o XXXXXXXX-X
        
    Returns:
        bool: True si el RUT es válido, False en caso contrario
        
    Example:
        >>> validar_rut("12.345.678-5")
        True
        >>> validar_rut("12345678-5")
        True
    """
    try:
        # Limpiar y separar RUT y DV
        rut_limpio = rut_completo.replace(".", "").replace("-", "").replace(" ", "")
        
        if len(rut_limpio) < 2:
            return False
        
        rut = rut_limpio[:-1]
        dv_ingresado = rut_limpio[-1].lower()
        
        # Calcular DV esperado
        dv_calculado = calcular_dv(rut).lower()
        
        return dv_ingresado == dv_calculado
    except (ValueError, IndexError):
        return False


def formatear_rut(rut: str, incluir_dv: bool = True) -> str:
    """
    Formatea un RUT con el formato estándar chileno: XX.XXX.XXX-X
    
    Args:
        rut (str): RUT sin formato
        incluir_dv (bool): Si es True, calcula y agrega el DV
        
    Returns:
        str: RUT formateado
        
    Example:
        >>> formatear_rut("12345678")
        '12.345.678-5'
    """
    # Limpiar
    rut_limpio = ''.join(filter(str.isdigit, str(rut)))
    
    if not rut_limpio:
        return ""
    
    # Calcular DV si se requiere
    if incluir_dv:
        dv = calcular_dv(rut_limpio)
    else:
        dv = ""
    
    # Formatear con puntos
    rut_formatted = ""
    for i, digit in enumerate(reversed(rut_limpio)):
        if i > 0 and i % 3 == 0:
            rut_formatted = "." + rut_formatted
        rut_formatted = digit + rut_formatted
    
    # Agregar DV
    if incluir_dv:
        rut_formatted += f"-{dv}"
    
    return rut_formatted


# Script independiente para uso en terminal
if __name__ == "__main__":
    print("=== Calculadora de Dígito Verificador RUT ===\n")
    
    while True:
        rut = input("Ingrese RUT (sin puntos, sin DV) o 'salir' para terminar: ").strip()
        
        if rut.lower() in ['salir', 'exit', 'quit', 'q']:
            print("¡Hasta luego!")
            break
        
        try:
            dv = calcular_dv(rut)
            rut_formateado = formatear_rut(rut, incluir_dv=True)
            
            print(f"✓ Dígito verificador: {dv}")
            print(f"✓ RUT completo: {rut_formateado}")
            
            # Validar
            if validar_rut(rut_formateado):
                print("✓ RUT válido\n")
            else:
                print("✗ Error en validación\n")
                
        except ValueError as e:
            print(f"✗ Error: {e}\n")
