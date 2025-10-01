// Realizar la conversión de una temperatura dada en grados Centígrados a grados Fahrenheit
// (Fórmula: F = (9/5) C + 32).
// Necesitas instalar prompt-sync con: npm install prompt-sync
const prompt = require("prompt-sync")();

console.log("=== Conversor de Temperatura ===");
console.log();

let opcion;

while (true) {
  try {
    console.log("(1 = Centígrados a Fahrenheit) o (2 = Fahrenheit a Centígrados)");
    opcion = parseInt(prompt("Elija una opción de conversión: "));

    if (opcion === 1 || opcion === 2) {
      console.log("=====================");
      console.log(`Elegiste la opción ${opcion}`);
      console.log("=====================");
      break;
    } else {
      console.log("Opción inválida. Intente de nuevo.");
    }
  } catch (error) {
    console.log("Debe ingresar un número válido");
  }
}

switch (opcion) {
  case 1:
    let gradosCentigrados = parseFloat(prompt("Ingrese los grados centígrados: "));
    let fahrenheit = gradosCentigrados * 9 / 5 + 32;
    console.log(`El resultado de la conversión a Grados Fahrenheit es de: ${fahrenheit.toFixed(2)}`);
    console.log();
    break;

  case 2:
    let gradosFahrenheit = parseFloat(prompt("Ingrese los grados Fahrenheit: "));
    let centigrados = (gradosFahrenheit - 32) * 5 / 9;
    console.log(`El resultado de la conversión a Grados Centígrados es de: ${centigrados.toFixed(2)}`);
    console.log();
    break;

  default:
    console.log("Opción inválida.");
    break;
}

 