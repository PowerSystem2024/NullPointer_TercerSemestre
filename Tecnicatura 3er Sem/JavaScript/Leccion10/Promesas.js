//----------LA PROMESAS: son unnmecamismo para manejar operaciones asincronicas, permitiendo que el codigocontinue ejecutandose 
//mientras se espera el resultado de la tarea.
// y se utiliza para evitar ek calback hell, que es cuando se anidan muchas funciones callback una dentro de otra,
// lo que hace que el código sea difícil de leer y mantener.

//Sintaxis: new Promise((resolver, rechazar)=>{código a ejecutar})
//La promesa puede estar en uno de los 3 estados:
//1. Pendiente(pending): La operación aín no ha finalizado.
//2. Resuelta(fulfilled): La operación se ha completado con éxito.
//3. Rechazada(rejected): La operación ha fallado o hubo un error.


let miPromesa = new Promise((resolver, rechazar)=> { //Definimo la promesa
    let expresion = true; //Simulamos una condición para resolver o rechazar la promesa
    if (expresion) {
        resolver('Resolvió corectamente');
    } else {
        rechazar('Se producjo un error');
    }
});

// ---------El métdo then(): se usa con promesas para manejar operaciones asincronicas de menera clara y estructurada.
// Permite encadenar funciones que se ejecutan cuando promesa se resuelve o rechaza.
// ---------El método catch(): se usa para manejar errores en promesas. Se ejecuta cuando una promesa es rechazada.


//miPromesa.then(
//    valor => console.log(valor), //Si se resuelve correctamente
//    error => console.log(error)//Si se rechaza
//);
    
//miPromesa  //Utilizamos el método then para manejar la resolución y el rechazo de la promesa
//    .then(valor => console.log(valor)) //Si se resuelve correctamente
//    .catch(error=> console.log(error));

let promesa = new Promise((resolver) => {  //Definimos una nueva promesa
    //Simulamos una operación asincrónica con setTimeout
    //console.log('Inicio de la promesa')
    //setTimeout( () => resolver('Saludos desde promesa, callback,funcion flecha y seTimeout'),3000);//Simulamos una operación asincronica con seTimeout
    //setTimeout( () =>  console.log('Fin de la promesa'),4000);
});

//El llamado a la promesa
//promesa.then( valor => console.log(valor)); //Utilizamos el método then para manejar la resolución de la promesa

//async indica que una funcion regresa una promesa
async function miFuncionPromesa (){
    return 'Saludo acon promesas y asinc';
}

//miFuncionPromesa().then(valor => console.log(valor)); //Llamamos a la función y manejamos la resolución de la promesa

//async/await: es una forma de escribir código asíncrono de manera más legible y estructurada.
//AWAIT: pausa o detiene la ejecución hasta que la promesa se resuelva. !!!1SOLO SE USA DENTRO DE UNA FUNCIÓN DECLARADA CON ASYNC¡¡¡

async function funcionConPromesaYAwait (){ 
    let miPromesa = new Promise(resolver => {
        resolver('Promesa con await');
    });
    console.log(await miPromesa); //Utilizamos await para esperar a que la promesa se resuelva
}

//funcionConPromesaYAwait();

//Promesas, await, async y seTimeout 
async function funcionConPromesaAwaitTimeout (){
    let miPromesa =new Promise(resolver => {//definimos una promesa
        console.log('Inicio de la función');
        setTimeout(()=> resolver('Promesa con await y Timeout'),3000);
        setTimeout ( () => console.log('Fin de la función'),4000);
    });
    console.log(await miPromesa);
}
funcionConPromesaAwaitTimeout();