// Test 8.1: Función con múltiples paths de retorno
function buscar(array: integer[], target: integer): boolean {
    for (let i: integer = 0; i < 5; i = i + 1) {
        if (array[i] == target) {
            return true;
        }
    }
    return false;
}

// Test 8.2: Try-catch (si está implementado)
function dividir(a: integer, b: integer): integer {
    try {
        return a / b;
    } catch (error) {
        return 0;
    }
}

// Test 8.3: Expresiones complejas válidas
let resultado: boolean = (5 > 3) && (10 < 20) || false;

// Test 8.4: Declaraciones mixtas
let entero: integer = 42;
const TEXTO: string = "constante";
let booleano: boolean = entero > 0;

// Test 8.5: Función con lógica de control compleja
function compleja(x: integer): string {
    if (x > 100) {
        return "grande";
    } else if (x > 50) {
        return "mediano";
    } else {
        return "pequeño";
    }
}

// Test 8.6: Inicialización de múltiples variables
let a: integer = 1;
let b: integer = 2;
let c: integer = a + b;