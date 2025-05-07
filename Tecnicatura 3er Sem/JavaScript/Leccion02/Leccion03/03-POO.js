class Empleado{
    constructor(nombre,sueldo){
        this._nombre =nombre;
        this._sueldo = sueldo;
    }
    obtenerDetalles(){
        return `Empleado: nombre ${this._nombre},
        Sueldo: ${this._sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre,sueldo, departamento){
        super(nombre,sueldo);
        this._departamento = departamento;
    }

    //AGREGAMOS LA SOBREESCRITURA
    obtenerDetalles(){
        return`Gerente: ${super.obtenerDetalles()} depto: ${this._departamento}`;
    }
}

function imprimir(tipo){ //Recibe una variable
    console.log(tipo.obtenerDetalles()); //Segun el tipo que le pasemos, sera la informacion
if(tipo instanceof Gerente){
    console.log('Es un objeto de tipo Gerente');
    }
    else if (tipo instanceof Empleado){
        console.log('Es de tipo Empleado');
    }
    else if(tipo instanceof Object){ //El orden siempre es jerarquico
        console.log('Es de tipo Object');
    }
}


let gerente1 = new Gerente("Carlos", 5000, "Sistemas");
console.log(gerente1); //OBJETO DE LA CLASE HIJA

let empleado1 = new Empleado("Juan", 3000);
console.log(empleado1); //OBJETO DE LA CLASE PADRE

imprimir(gerente1); // EN el polimorfismo esta llamando al metodo de cla clase padre
imprimir(empleado1); // Esta llmando al metodo de la clase hija
//Son las multiples formas en tiempo de ejecucion del polimorfismo
