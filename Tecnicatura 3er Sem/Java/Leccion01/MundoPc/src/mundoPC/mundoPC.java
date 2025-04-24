package mundoPC;

import ar.com.system2025.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP",13); // Importar la clase
        Teclado tecladoHP = new Teclado("HP","Bluetooth");
        Raton ratonHP = new Raton("HP","Bluetooth");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        //Creamos otro objetos de diferente marca
        Monitor monitorGamer = new Monitor("Gamer",32); 
        Teclado tecladoGamer= new Teclado("Gamer","Bluetooth");
        Raton ratonGamer = new Raton("Gamer","Bluetooth");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        Monitor monitorSamsung = new Monitor("Samsung",24); 
        Teclado tecladoSamsung= new Teclado("Samsung","Bluetooth");
        Raton ratonSamsung = new Raton("Samsung","Bluetooth");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung",monitorSamsung,tecladoSamsung,ratonSamsung);
        
          Monitor monitorGFAST = new Monitor("GFAST",24); 
        Teclado tecladoGFAST= new Teclado("GFAST","Bluetooth");
        Raton ratonGFAST = new Raton("GFAST","Cable");
        Computadora computadoraGFAST = new Computadora("Computadora GFAST",monitorGFAST,tecladoGFAST,ratonGFAST);
        
         Monitor monitorDell = new Monitor("Dell",27); 
        Teclado tecladoDell= new Teclado("Dell","Cable");
        Raton ratonDell = new Raton("Dell","Cable");
        Computadora computadoraDell = new Computadora("Computadora Dell",monitorDell,tecladoDell,ratonDell);
        
        Monitor monitorAcer = new Monitor("Acer",27); 
        Teclado tecladoAcer= new Teclado("Acer","Cable");
        Raton ratonAcer= new Raton("Acer","Cable");
        Computadora computadoraAcer = new Computadora("Computadora Acer",monitorAcer,tecladoAcer,ratonAcer);
        
         Monitor monitorAsus = new Monitor("Asus ",27); 
        Teclado tecladoAsus = new Teclado("Asus ","Cable");
        Raton ratonAsus = new Raton("Asus ","Cable");
        Computadora computadoraAsus  = new Computadora("Computadora Asus ",monitorAsus ,tecladoAsus ,ratonAsus );

    Computadora computadoraVarias2 = new Computadora("Computadora de diferentes marcas", monitorGamer,tecladoGFAST,ratonAsus);   
    Computadora computadoraVarias3 = new Computadora("Computadora de diferentes marcas", monitorDell,tecladoAsus,ratonGamer);
    Computadora computadoraVarias4 = new Computadora("Computadora de diferentes marcas", monitorSamsung,tecladoGFAST,ratonDell);
    Computadora computadoraVarias5 = new Computadora("Computadora de diferentes marcas", monitorAcer,tecladoSamsung,ratonHP);
        Orden orden1 = new Orden();// Inicializamos el arreglo vacio
        Orden orden2 = new Orden(); //UNA NUEVA LISTA PARA EL OBJETO ORDEN2
        orden1.agregarComputadoras(computadoraHP);
        orden1.agregarComputadoras(computadoraGamer);
        orden1.agregarComputadoras(computadoraSamsung);
        orden1.agregarComputadoras(computadoraGFAST);
        orden1.agregarComputadoras(computadoraDell);
        orden1.agregarComputadoras(computadoraAcer);
        orden1.agregarComputadoras(computadoraAsus);
        orden1.agregarComputadoras(computadoraVarias2);
        orden1.agregarComputadoras(computadoraVarias3);
        orden1.agregarComputadoras(computadoraVarias4);
        orden1.agregarComputadoras(computadoraVarias5);
        orden1.mostrarOrden();
        
        
        Computadora computadoraVarias = new Computadora("Computadora de diferentes marcas", monitorHP,tecladoGamer,ratonHP);
        orden2.agregarComputadoras(computadoraHP);
        orden2.agregarComputadoras(computadoraVarias);
        orden2.mostrarOrden();
        
        
        
    }
    
}
