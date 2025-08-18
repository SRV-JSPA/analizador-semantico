// Test 7.1: Variables en diferentes ámbitos
let global: integer = 10;

function funcion(): void {
    let local: integer = 20;
    print("local");
}

// Test 7.2: Shadowing válido
let x: integer = 5;
{
    let x: string = "local";  // Válido
    print(x);
}
print("x");  // Se refiere al x integer

// Test 7.3: Acceso a variable global desde función
let contador: integer = 0;

function incrementar(): void {
    contador = contador + 1;
}

// Test 7.4: Parámetros ocultan variables globales
let valor: integer = 100;

function procesar(valor: string): void {
    print(valor);  // Se refiere al parámetro
}

// Test 7.5: Variables en bloques anidados
{
    let nivel1: integer = 1;
    {
        let nivel2: string = "dos";
        print("nivel1");  // Acceso válido al nivel superior
    }
}

// Test 7.6: Múltiples funciones con variables locales
function funcion1(): void {
    let temp: integer = 1;
}

function funcion2(): void {
    let temp: string = "dos";  // Válido, diferente ámbito
}