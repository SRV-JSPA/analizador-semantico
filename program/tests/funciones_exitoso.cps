// Test 3.1: Función con parámetros y retorno
function suma(a: integer, b: integer): integer {
    return a + b;
}

// Test 3.2: Función sin parámetros
function saludar(): string {
    return "Hola mundo";
}

// Test 3.3: Función void
function imprimir(mensaje: string): void {
    print(mensaje);
}

// Test 3.4: Llamadas a función correctas
let resultado: integer = suma(5, 3);
let saludo: string = saludar();
imprimir("Test");

// Test 3.5: Función recursiva
function factorial(n: integer): integer {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Test 3.6: Múltiples returns en función
function absoluto(x: integer): integer {
    if (x < 0) {
        return -x;
    }
    return x;
}