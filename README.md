# Compiscript – Análisis Semántico


### Santiago Pereira 22318
### Nancy Mazariegos 22513


## Descripción
Este proyecto implementa el análisis semántico para el lenguaje Compiscript.  
El compilador revisa que los programas no solo estén bien escritos de forma sintáctica, sino que también tengan sentido lógico: tipos compatibles, variables declaradas, funciones correctamente llamadas y clases bien utilizadas.

## Estructura del proyecto
- `main.py`: punto de entrada del compilador, coordina las fases y muestra resultados.  
- `analizador_semantico.py`: visitor que aplica las reglas semánticas sobre el AST.  
- `sistema_tipos.py`: reglas de verificación de tipos en operaciones, asignaciones y literales.  
- `tabla_simbolos.py`: manejo de ámbitos y almacenamiento de variables, funciones, clases y métodos.  

## Funcionalidades principales
- Validación de tipos en operaciones aritméticas, lógicas y comparaciones  
- Manejo de ámbitos: variables globales, locales, clases y funciones  
- Validación de funciones: parámetros, retornos, llamadas y recursión  
- Control de flujo: condiciones booleanas, uso correcto de break, continue y return  
- Clases y objetos: atributos, métodos, constructores y uso de this  
 

## Uso
1. Colocar un archivo fuente en Compiscript, por ejemplo `archivo.cps`  
2. Ejecutar el compilador desde terminal:  
   ```bash
   python main.py archivo.cps
