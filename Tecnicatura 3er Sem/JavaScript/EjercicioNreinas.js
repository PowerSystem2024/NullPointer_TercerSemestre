function resolverReinas(n) {
  const tablero = Array(n).fill(null).map(() => Array(n).fill(0)); // Inicializar el tablero
  const soluciones = [];
  let contadorSoluciones = 0; // Contador de soluciones

  function esSeguro(tablero, fila, columna) {
    // Verificar si la reina en fila, columna está segura (no en la misma fila, columna o diagonal)
    for (let i = 0; i < fila; i++) {
      // Verificar columna
      if (tablero[i][columna] === 1) {
        return false;
      }
      // Verificar diagonal
      if (Math.abs(i - fila) === Math.abs(columna - Array.from({length: n}, (_, k) => k).find(c => tablero[i][c] === 1))) {
          return false;
      }
    }
    return true;
  }

  function resolverRecursivamente(tablero, fila) {
    if (fila === n) {
      // Hemos colocado todas las reinas sin conflicto
      soluciones.push(tablero.map(filaTablero => filaTablero.map(columna => columna === 1 ? ' Q ' : ' . ').join('')));
      contadorSoluciones++; // Incrementar el contador de soluciones
      return;
    }

    for (let columna = 0; columna < n; columna++) {
      if (esSeguro(tablero, fila, columna)) {
        // Colocar la reina en la posición actual
        tablero[fila][columna] = 1;

        // Llamar recursivamente para la siguiente fila
        resolverRecursivamente(tablero, fila + 1);

        // Retroceder: quitar la reina de la posición actual para explorar otras opciones
        tablero[fila][columna] = 0;
      }
    }
  }

  resolverRecursivamente(tablero, 0); // Comenzar la resolución desde la primera fila
  return {
    soluciones,
    contadorSoluciones
  }; // Devolver las soluciones y el contador
}

// Ejemplo: Resolver el problema para 8 reinas
const resultado8Reinas = resolverReinas(8);
console.log("\n---");
console.log("Número de soluciones para 8 reinas:", resultado8Reinas.contadorSoluciones);
console.log("Soluciones para 8 reinas:");
resultado8Reinas.soluciones.forEach((solucion, index) => {
  console.log(`\nSolución ${index + 1}:`);
  solucion.forEach(fila => console.log(fila));
});

