// Test 2.7: Asignación de tipo incompatible
let numero: integer = 10;
numero = "texto";  // ERROR: no se puede asignar string a integer



// Test 2.10: Redeclaración en el mismo ámbito
let variable: integer = 5;
let variable: string = "error";  // ERROR: identificador ya declarado

// Test 2.11: Uso de variable no declarada
let resultado: integer = noExiste + 5;  // ERROR: variable no declarada

// Test 2.12: Reasignación de constante
const FIJO: integer = 100;
FIJO = 200;  // ERROR: no se puede reasignar constante

