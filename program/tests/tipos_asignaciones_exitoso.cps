// Test 2.1: Declaraciones básicas correctas
let edad: integer = 25;
let nombre: string = "Juan";
let activo: boolean = true;

// Test 2.2: Constantes con inicialización
const PI: integer = 3;
const MENSAJE: string = "Constante";

// Test 2.3: Asignaciones posteriores correctas
let variable: integer = 10;
variable = 20;
variable = variable + 5;

// Test 2.4: Inferencia de tipos
let automatico = 42;  // Se infiere como integer
let cadena = "texto";  // Se infiere como string

// Test 2.5: Arrays con tipos consistentes
let numeros: integer[] = [1, 2, 3, 4];
let textos: string[] = ["a", "b", "c"];

// Test 2.6: Variables con el mismo nombre en diferentes ámbitos
let x: integer = 5;
{
    let x: string = "local";  // Válido en ámbito diferente
}
