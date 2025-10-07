# Validador de RUT Chileno

Este módulo proporciona utilidades para validar, calcular y formatear RUTs chilenos.

## Uso en el Proyecto Django

### 1. Validar RUT en formularios

```python
from utils.rut_validator import validar_rut, formatear_rut, calcular_dv

# Validar un RUT completo
if validar_rut("12.345.678-5"):
    print("RUT válido")

# Calcular dígito verificador
dv = calcular_dv("12345678")  # Retorna "5"

# Formatear RUT
rut_formateado = formatear_rut("12345678")  # Retorna "12.345.678-5"
```

### 2. Integración en Modelos

El formulario `ConductoresForm` ya tiene validación automática de RUT:

```python
# En CrudConductores/forms.py
class ConductoresForm(forms.ModelForm):
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not validar_rut(rut):
            raise forms.ValidationError('RUT inválido')
        return formatear_rut(rut)
```

### 3. Uso en Scripts

#### Opción A: Usar el módulo mejorado

```bash
python -m utils.rut_validator
```

Este script interactivo permite:
- Calcular dígito verificador
- Validar RUTs completos
- Formatear RUTs

#### Opción B: Usar el script simple original

```bash
python scripts/calcular_dv_simple.py
```

Script original con el código tal como lo proporcionaste.

## API del Módulo

### `calcular_dv(rut: str) -> str`

Calcula el dígito verificador de un RUT.

**Parámetros:**
- `rut`: String con los dígitos del RUT (sin DV)

**Retorna:**
- String con el dígito verificador ('0'-'9' o 'k')

**Ejemplo:**
```python
>>> calcular_dv("12345678")
'5'
```

### `validar_rut(rut_completo: str) -> bool`

Valida un RUT completo (número + DV).

**Parámetros:**
- `rut_completo`: RUT con formato XX.XXX.XXX-X o XXXXXXXX-X

**Retorna:**
- `True` si el RUT es válido, `False` en caso contrario

**Ejemplo:**
```python
>>> validar_rut("12.345.678-5")
True
>>> validar_rut("12345678-5")
True
>>> validar_rut("12345678-9")
False
```

### `formatear_rut(rut: str, incluir_dv: bool = True) -> str`

Formatea un RUT con el formato estándar chileno.

**Parámetros:**
- `rut`: RUT sin formato
- `incluir_dv`: Si es True, calcula y agrega el DV

**Retorna:**
- String con RUT formateado: XX.XXX.XXX-X

**Ejemplo:**
```python
>>> formatear_rut("12345678")
'12.345.678-5'
>>> formatear_rut("12345678", incluir_dv=False)
'12.345.678'
```

## Algoritmo de Cálculo

El dígito verificador se calcula usando el algoritmo módulo 11:

1. Se multiplica cada dígito por la secuencia 2,3,4,5,6,7 (de derecha a izquierda)
2. Se suman los resultados
3. Se calcula el resto de dividir por 11
4. El DV es 11 - resto
5. Casos especiales:
   - Si DV = 11 → '0'
   - Si DV = 10 → 'k'

## Integración Actual en el Proyecto

✅ **CrudConductores**: El formulario valida automáticamente RUTs al crear/editar conductores

## Testing

```bash
# Ejecutar tests del módulo (cuando se implementen)
python manage.py test utils

# O usar el script interactivo para pruebas manuales
python -m utils.rut_validator
```

## Ejemplos de RUTs Válidos

- 12.345.678-5
- 11.111.111-1
- 22.222.222-k
- 9.999.999-4

## Archivos Creados

1. `utils/rut_validator.py` - Módulo principal con funciones de validación
2. `utils/__init__.py` - Inicializador del módulo
3. `scripts/calcular_dv_simple.py` - Script original del usuario
4. `CrudConductores/forms.py` - Actualizado con validación automática
