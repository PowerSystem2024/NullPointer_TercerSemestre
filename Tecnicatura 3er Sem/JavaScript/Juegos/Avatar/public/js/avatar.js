function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
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

    function seleccionarPersonajeEnemigo() {
    let personajes = ['Zuko', 'Katara', 'Aang', 'Toph'];
    let indiceAleatorio = Math.floor(Math.random() * personajes.length);

    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo');
    spanPersonajeEnemigo.innerHTML = personajes[indiceAleatorio]; 
}

}
window.addEventListener('load', iniciarJuego)