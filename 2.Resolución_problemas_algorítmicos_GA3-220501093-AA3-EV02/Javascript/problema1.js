//Desarrollar un programa que permita almacenar las edades de un grupo de 10 personas en un
//vector de enteros y luego determine la cantidad de personas que son menores de edad, mayores
//de edad, cuántos adultos mayores, la edad más baja, la edad más alta y el promedio de edades
//ingresadas. Para el ejercicio anterior, suponga que un adulto mayor debe tener una edad igual o
//superior a 60. Debe validar para cada ingreso, que los valores estén en un rango entre 1 y 120 años.
//En caso de error deberá notificar y solicitar un nuevo valor

const prompt = require("prompt-sync")();


let edades = [];
let persona = 1;

while (true){
    try{
        ingresar_edad = parseInt(prompt(`Ingrese la edad de la persona número ${persona}:`));

        if (ingresar_edad < 0){
            console.log("Error: la edad no puede ser un número negativo. Intente de nuevo.");
            continue
        }
        if (ingresar_edad > 120){
            console.log("Error: la edad no puede superar el limite de 120 años. Intente de nuevo.");
            continue
        }
        //guardar edad
        edades.push(ingresar_edad)
        persona += 1
        //limite de personas
        if (persona > 10){
            break
        }

    }catch(error){
        console.log("Error: Ingrese un número entero válido.");
        
    }
}

let menor_de_edad = 0
let mayor_de_edad  = 0
let adulto_mayor = 0

for (let edades_recorridas of edades){
    if (edades_recorridas < 18){
        menor_de_edad ++
    }else if (edades_recorridas > 18 && edades_recorridas < 60){
        mayor_de_edad ++
    }else if (edades_recorridas >= 60 && edades_recorridas <= 120){
        adulto_mayor ++
    }
}


// Edad mas alta y mas baja 

let edad_baja = Math.min(...edades)
let edad_alta = Math.max(...edades)

//promedio edades
let promedio = edades.reduce((acum, edad) => acum + edad, 0) / edades.length;



console.log(`\nResultados del análisis:`)
console.log(`- Menores de edad: ${menor_de_edad}`)
console.log(`- Mayores de edad: ${mayor_de_edad}`)
console.log(`- Adultos mayores: ${adulto_mayor}`)
console.log (`- Edad más baja: ${edad_baja}`)
console.log (`- Edad más alta: ${edad_alta}`)
console.log (`- Promedio de edades:  ${promedio.toFixed(2)}`)  