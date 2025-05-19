
function miFuncion(){
    console.log('Saludos desde mi funcion')
}
miFuncion();

let myFuncion = function (){
    console.log('Saludos desde la funcion anonima')
}

//Ahora vamos a crear una funcion flecha

let miFuncionFlecha = () => {
    console.log ('Saludos desde mi funcion flecha');
}
//Hay mas variantes para funciones flecha que vamos a ir viendo
miFuncionFlecha();

//lo hacemos en una linea 
const saludar = () => console.log('Saludos a todos desde esta funcion flecha');
saludar();
//otro ejemplo
const saludar2 = () =>{
    return 'Saludos desde la funcion flecha dos'
}
console.log(saludar2());

//Simplificamos la funcion anterior
const saludar3 = () => 'Saludamos desde la funcion flecha tres'

console.log(saludar3);

//Continuamos con otro ejemplo
const regresaObjeto = () => ({nombre: 'Juan', apellido: 'Lara'});
console.log(regresaObjeto());

//Funciones flechas que reciben parametros
const funcionParametros = (mensaje) => console.log(mensaje);
funcionParametros('Saludos desde esta funcion con parametros');

//Una funcion clasica 
const funcionParametrosClasica = function(mensaje ){
    console.log(mensaje);
}
funcionParametrosClasica('Saludos desde la funcion clasica');

//Se pueden omitir los parentesis en la funcion flecha de la siguiente manera
const funcionConParametros = mensaje => console.log(mensaje);
funcionConParametros('Otra forma de trabajar con funcion flecha');

//Ahora vemos funciones flecha con varios parametros
//Podemos abrir la funcion y tener mas cosas dentro de ella

const funcionConParametros2 = (op1,op2) => {
    let resultado = op1 + op2;
    return resultado;
}
console.log(funcionConParametros2(3,5));

