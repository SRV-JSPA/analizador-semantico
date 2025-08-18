// Test 6.7: Array con tipos inconsistentes
let mixto: integer[] = [1, "dos", 3];  // ERROR: elementos deben ser del mismo tipo

// Test 6.8: Índice de tipo incorrecto
let array: integer[] = [1, 2, 3];
let valor: integer = array["indice"];  // ERROR: índice debe ser integer

// Test 6.9: Acceso a array no declarado
let elemento: integer = arrayInexistente[0];  // ERROR: array no declarado

// Test 6.10: Asignación de tipo incorrecto a elemento
let numeros: integer[] = [1, 2, 3];
numeros[0] = "texto";  // ERROR: elemento debe ser integer

// Test 6.11: Acceso por índice a no-array
let texto: string = "hola";
let caracter: string = texto[0];  // ERROR: no se puede indexar string

// Test 6.12: Array sin especificar tipo de elemento
let indefinido[] = [1, 2, 3];  // ERROR: debe especificar tipo de elemento