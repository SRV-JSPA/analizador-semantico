// Test 8.7: Código después de return
function muerto(): integer {
    return 42;
    let inalcanzable: integer = 5;  // ERROR: código muerto
}

// Test 8.8: Expresión sin sentido
function sinSentido(): void {
    5 + 3;  // ERROR: expresión sin efecto
}

// Test 8.9: Declaración duplicada de función
function repetida(): void {}
function repetida(x: integer): void {}  // ERROR: función ya declarada

// Test 8.10: Llamada a función como variable
function miFuncion(): integer {
    return 5;
}
let resultado: integer = miFuncion + 3;  // ERROR: no se puede usar función como variable

// Test 8.11: Asignación a literal
42 = 100;  // ERROR: no se puede asignar a literal

// Test 8.12: Uso de break/continue fuera de contexto válido
function malFormada(): void {
    if (true) {
        break;  // ERROR: break solo en bucles/switch
    }
}