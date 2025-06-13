
class KnightsTour {
    constructor(boardSize = 8) {
        this.boardSize = boardSize;
        this.board = Array(this.boardSize).fill(0).map(() => Array(this.boardSize).fill(-1));
        this.path = []; 
        this.solutionFound = false;

        
        this.moveX = [2, 1, -1, -2, -2, -1, 1, 2];
        this.moveY = [1, 2, 2, 1, -1, -2, -2, -1];
    }

    /** 
     * @param {number} x 
     * @param {number} y 
     * @returns {boolean} 
    */
    isValidMove(x, y) {
        return (x >= 0 && x < this.boardSize &&
                y >= 0 && y < this.boardSize &&
                this.board[x][y] === -1);
    }

    /**
     * @param {number} x 
     * @param {number} y 
     * @param {number} moveCount 
     * @returns {boolean} 
     */
    solveTour(x, y, moveCount) {
        
        if (moveCount === this.boardSize * this.boardSize) {
            this.solutionFound = true;
            return true;
        }

        
        for (let i = 0; i < 8; i++) {
            const nextX = x + this.moveX[i];
            const nextY = y + this.moveY[i];

            if (this.isValidMove(nextX, nextY)) {
                this.board[nextX][nextY] = moveCount;
                this.path.push({ x: nextX, y: nextY, move: moveCount });


                if (this.solveTour(nextX, nextY, moveCount + 1)) {
                    return true; 
                }
               
                this.board[nextX][nextY] = -1; 
                this.path.pop(); 
            }
        }
        return false; 
    }

    /**
     * @param {number} startX 
     * @param {number} startY 
     */
    startTour(startX, startY) {
       
        if (!this.isValidMove(startX, startY) && this.board[startX][startY] !== -1) {
            console.log(`Error: La posición inicial (${startX}, ${startY}) es inválida o ya está visitada.`);
            return;
        }

        this.board[startX][startY] = 0; 
        this.path.push({ x: startX, y: startY, move: 0 });

        console.log(`Iniciando el tour del caballo desde (${startX}, ${startY})...`);

        if (this.solveTour(startX, startY, 1)) {
            console.log("¡Solución encontrada!");
            this.printSolution();
        } else {
            console.log("No se encontró ninguna solución para el tour del caballo desde esta posición inicial.");
        }
    }

    
    printSolution() {
        if (!this.solutionFound) {
            console.log("No hay solución para imprimir.");
            return;
        }
        console.log("\nTablero con la secuencia de saltos:");
        for (let i = 0; i < this.boardSize; i++) {
            let row = "";
            for (let j = 0; j < this.boardSize; j++) {
                row += (this.board[i][j] < 10 ? "  " : " ") + this.board[i][j];
            }
            console.log(row);
        }

        console.log("\nCamino de la solución:");
        this.path.forEach(pos => {
            console.log(`Salto ${pos.move}: (${pos.x}, ${pos.y})`);
        });
    }
}


const tour = new KnightsTour(8); 
tour.startTour(0, 0); 