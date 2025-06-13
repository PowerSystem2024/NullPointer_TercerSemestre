class DispositivoEntrada {
    constructor(tipoEntrada, marca){
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }
    get tipoEntrada(){
        return this._tipoEntrada;
    }
    get marca(){
        return this._marca;
    }
    toString(){
        return `DispositivoEntrada: [tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}

class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }

    get idRaton(){
        return this._idRaton;
    }

    toString(){
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }
}

let raton2 = new Raton("Bluetooth", "Dell");
console.log(raton2.toString());

class Teclado extends DispositivoEntrada {
    static contadorTeclado = 0;

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclado;
    }

    get idTeclado(){
        return this._idTeclado;
    }

    toString(){
        return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }
}

let teclado1 = new Teclado("USB", "HP");
let teclado2 = new Teclado("Bluetooth", "Acer");
console.log(teclado1.toString());
console.log(teclado2.toString());

class Monitor {
    static contadorMonitores = 0;

    constructor(marca, tamanio){
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;
        this._tamanio = tamanio;
    }

    get idMonitor(){
        return this._idMonitor;
    }

    toString(){
        return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._tamanio}]`;
    }
}

let monitor1 = new Monitor("HP", 15);
let monitor2 = new Monitor("Dell", 27);
console.log(monitor1.toString());
console.log(monitor2.toString());

class Computadora {
    static contadorComputadoras = 0;

    constructor(nombre, monitor, raton, teclado){
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._raton = raton;
        this._teclado = teclado;
    }

    toString(){
        return `Computadora ${this._idComputadora}: ${this._nombre}\n ${this._monitor}\n ${this._teclado}\n ${this._raton}`;
    }
}

let raton1 = new Raton("USB", "Logitech");
let computadora1 = new Computadora("HP", monitor1, raton1, teclado1);
let computadora2 = new Computadora("Acer", monitor2, raton2, teclado2);
console.log(`${computadora1}`);
console.log(`${computadora2}`);

class Orden {
    static contadorOrdenes = 0;

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = [];
    }

    get idOrden(){
        return this._idOrden;
    }

    agregarComputadora(computadora){
        this._computadoras.push(computadora);
    }

    mostrarOrden(){
        let computadorasOrden = '';
        for(let computadora of this._computadoras){
            computadorasOrden += `\n${computadora}`;
        }
        console.log(`Orden: ${this.idOrden}, Computadoras: ${computadorasOrden}`);
    }
}

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.agregarComputadora(computadora2);
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.agregarComputadora(computadora1);
orden2.mostrarOrden();

function mostrarDispositivo(dispositivo){
    console.log(dispositivo.toString());
}

mostrarDispositivo(raton2);     
mostrarDispositivo(teclado1);   
mostrarDispositivo(teclado2); 
//Se aplicó polimorfismo al definir el método toString() en las clases Raton, Teclado, Monitor, y Computadora. También se creó la función 
// mostrarDispositivo() que permite recibir cualquier objeto que herede de DispositivoEntrada, y llama al toString() correspondiente según el tipo de objeto. 
// Además, se corrigió el método mostrarOrden() para que utilice correctamente la interpolación y se muestren bien los datos de las computadoras.
