package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{// Bloque de inicializacion estatico
        System.out.println("Ejecucion del bloque estatico");
        ++Persona.contadorPersonas;
        // idPersona =10; NO ES UN ATRIBUTO ESTATICO, POR ESO ERROR
    }
    
    { //Bloque de inicializacion NO estatico(contexto dinamico)
        System.out.println("Ejecucion del bloque NO estatico");
        this.idPersona = Persona.contadorPersonas++; //INCREMENTA
    }
    
    //Los bloques de inicializacion se ejecutan antes del constructor
    
    public Persona(){
        System.out.println("Ejecucion del constructor");
    }
    
    public int getidPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
}
