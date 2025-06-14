let ataqueJugador
let ataqueEnemigo

function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    let botonPunio = document.getElementById('boton-punio') 
    botonPunio.addEventListener('click', ataquePunio)
    let botonPatada = document.getElementById('boton-patada')
    botonPatada.addEventListener('click', ataquePatada)
    let botonBarrida = document.getElementById('boton-barrida')
    botonBarrida.addEventListener('click', ataqueBarrida)
}

function seleccionarPersonajeJugador(){
    let inputZuko = document.getElementById('zuko')
    let inputKatara = document.getElementById('katara')
    let inputAang = document.getElementById('aang')
    let inputToph = document.getElementById('toph')

    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    if(inputZuko.checked){
        spanPersonajeJugador.innerHTML = 'Zuko'
    }else if(inputKatara.checked){
        spanPersonajeJugador.innerHTML = 'Katara'
    }else if(inputAang.checked){
        spanPersonajeJugador.innerHTML = 'Aang'
    }else if(inputToph.checked){
        spanPersonajeJugador.innerHTML = 'Toph'
    }else{
        alert('Selecciona un personaje')
        return
    }
    
    seleccionarPersonajeEnemigo();
}

function seleccionarPersonajeEnemigo() {
    let personajes = ['Zuko', 'Katara', 'Aang', 'Toph'];
    let indiceAleatorio = Math.floor(Math.random() * personajes.length);

    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo');
    spanPersonajeEnemigo.innerHTML = personajes[indiceAleatorio]; 
    }

function ataquePunio(){ //Modificamos la variable global ataqueJugador
    ataqueJugador = 'Punio'
    ataqueAleatorioEnemigo()
}

function ataquePatada(){ //Modificamos la variable global ataqueJugador
    ataqueJugador = 'Patada'
    ataqueAleatorioEnemigo()
}

function ataqueBarrida(){ //Modificamos la variable global ataqueJugador
    ataqueJugador = 'Barrida'
    ataqueAleatorioEnemigo()
}

function aleatorio(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min)
    
}

function ataqueAleatorioEnemigo(){//Ahora ocupando la variable global nueva le decimos el ataque y necesitamos la funcion aleatoria nuevamente
    let ataqueAleatorio = aleatorio(1, 3)

    if(ataqueAleatorio == 1){
        ataqueEnemigo = 'Punio'
    } else if(ataqueAleatorio == 2){
        ataqueEnemigo = 'Patada'
    } else {
        ataqueEnemigo = 'Barrida'
    }
    combate()  // Ahora se ejecuta el combate luego de elegir ataque enemigo
}

function combate(){
    let resultado = ""

    if(ataqueEnemigo === ataqueJugador){
        resultado = "EMPATE"
    } else if(ataqueJugador === 'Puño' && ataqueEnemigo === 'Barrida'){
        resultado = "GANASTE"
    } else if(ataqueJugador === 'Patada' && ataqueEnemigo === 'Puño'){
        resultado = "GANASTE"
    } else if(ataqueJugador === 'Barrida' && ataqueEnemigo === 'Patada'){
        resultado = "GANASTE"
    } else {
        resultado = "PERDISTE"
    }

    crearMensaje(resultado)
}

function crearMensaje(resultado){
    let sectionMensaje = document.getElementById('mensajes')
    let parrafo = document.createElement('p')

    parrafo.innerHTML = `Tu personaje atacó con <strong>${ataqueJugador}</strong>, el personaje del enemigo atacó con <strong>${ataqueEnemigo}</strong> → <strong>${resultado}</strong>`
    sectionMensaje.appendChild(parrafo)
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}