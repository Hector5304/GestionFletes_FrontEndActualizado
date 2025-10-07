"""
Script de prueba para el validador de RUT
"""
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.rut_validator import calcular_dv, validar_rut, formatear_rut

def test_rut_validator():
    """Ejecuta pruebas del validador de RUT"""
    print("=== Pruebas del Validador de RUT ===\n")
    
    tests = [
        {
            'nombre': 'Calcular DV de 12345678',
            'funcion': lambda: calcular_dv("12345678"),
            'esperado': '5'
        },
        {
            'nombre': 'Calcular DV de 11111111',
            'funcion': lambda: calcular_dv("11111111"),
            'esperado': '1'
        },
        {
            'nombre': 'Formatear RUT 12345678',
            'funcion': lambda: formatear_rut("12345678"),
            'esperado': '12.345.678-5'
        },
        {
            'nombre': 'Validar RUT correcto 12.345.678-5',
            'funcion': lambda: validar_rut("12.345.678-5"),
            'esperado': True
        },
        {
            'nombre': 'Validar RUT incorrecto 12.345.678-9',
            'funcion': lambda: validar_rut("12.345.678-9"),
            'esperado': False
        },
        {
            'nombre': 'Validar RUT sin formato 12345678-5',
            'funcion': lambda: validar_rut("12345678-5"),
            'esperado': True
        },
        {
            'nombre': 'Calcular DV que resulta en K',
            'funcion': lambda: calcular_dv("1000005"),
            'esperado': 'k'
        },
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(tests, 1):
        try:
            resultado = test['funcion']()
            if resultado == test['esperado']:
                print(f"✓ Test {i}: {test['nombre']}")
                print(f"  Resultado: {resultado}")
                passed += 1
            else:
                print(f"✗ Test {i} FALLÓ: {test['nombre']}")
                print(f"  Esperado: {test['esperado']}, Obtenido: {resultado}")
                failed += 1
        except Exception as e:
            print(f"✗ Test {i} ERROR: {test['nombre']}")
            print(f"  Excepción: {e}")
            failed += 1
        print()
    
    print("=" * 50)
    print(f"Resultado: {passed} pasados, {failed} fallidos de {len(tests)} tests")
    print("=" * 50)
    
    return failed == 0


if __name__ == "__main__":
    success = test_rut_validator()
    sys.exit(0 if success else 1)
