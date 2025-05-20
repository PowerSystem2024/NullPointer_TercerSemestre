function nueveReinas(N) {
  const soluciones = [];
  const tablero = Array(N).fill().map(() => Array(N).fill('.'));
  const reina = [];

  function esSeguro(row, col) {
    for (let i = 0; i < row; i++) {
      if (
        reina[i] === col || 
        reina[i] - i === col - row || 
        reina[i] + i === col + row
      ) {
        return false;
      }
    }
    return true;
  }

  function backtrack(row = 0) {
    // la funcion backtrack se colocan reinas fila x fila y retrocede si hay problemas
    if (row === N) {
      const copia = tablero.map(fila => fila.join(''));
      soluciones.push({
        tablero: copia,
        indices: reina.slice()
      });
      return;
    }

    for (let col = 0; col < N; col++) {
      if (esSeguro(row, col)) {
        tablero[row][col] = 'R';
        reina[row] = col;
        backtrack(row + 1);
        tablero[row][col] = '.';
      }
    }
  }

  backtrack();
  return soluciones;
}

// 🧪 Ejemplo: resolver para N = 8
const N = 8;
const results = nueveReinas(N);

console.log(`Se encontraron ${results.length} soluciones para N = ${N}`);

results.forEach((solucion, index) => {
  console.log(`Solución ${index + 1}:`);
  console.log(solucion.tablero.join('\n'));
  console.log("Índices de las reinas (columna por fila):", solucion.indices);
  console.log("---");
});