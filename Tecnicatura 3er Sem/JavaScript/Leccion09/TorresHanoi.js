
function hanoi(n, origen, auxiliar, destino) {
  if (n === 1) {
    console.log(`Mover disco 1 de ${origen} a ${destino}`);
    return;
  }

  hanoi(n - 1, origen, destino, auxiliar); 
  console.log(`Mover disco ${n} de ${origen} a ${destino}`); 
  hanoi(n - 1, auxiliar, origen, destino); 
}


const numeroDeDiscos = 3;


hanoi(numeroDeDiscos, 'A', 'B', 'C');
