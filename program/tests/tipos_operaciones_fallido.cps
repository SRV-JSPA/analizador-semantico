// Test 1.7: Suma entre string y boolean (incompatible)
let texto: string = "hola";
let flag: boolean = true;
let invalido: string = texto + flag;  // ERROR: tipos incompatibles

// Test 1.8: División entre string e integer
let cadena: string = "abc";
let numero: integer = 5;
let error: integer = cadena / numero;  // ERROR: operación inválida

// Test 1.9: Operación lógica con tipos incorrectos
let num: integer = 10;
let bool: boolean = true;
let mal: boolean = num && bool;  // ERROR: && requiere ambos operandos boolean

// Test 1.10: Comparación entre tipos incompatibles
let texto: string = "hola";
let numero: integer = 42;
let comp: boolean = texto > numero;  // ERROR: no se puede comparar string con integer

// Test 1.11: Operador unario incorrecto
let cadena: string = "test";
let neg: integer = -cadena;  // ERROR: no se puede negar una string

// Test 1.12: Módulo con tipos incorrectos
let a: boolean = true;
let b: integer = 5;
let mod: integer = a % b;  // ERROR: % requiere operandos numéricos

