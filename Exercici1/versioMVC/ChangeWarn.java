package versioMVC;

public class ChangeWarn {

    int changeType;
    String str;
    char c;
    boolean ins;

    public ChangeWarn(int chT) {
        this.changeType = chT;        
    }

    public ChangeWarn(int chT,  String parteaEscribir) {
        this.changeType = chT;
        this.str = parteaEscribir;
    }
    
    public ChangeWarn(int chT, boolean insert, String parteaEscribir, char caracteraInsertar) {
        this.changeType = chT;
        this.ins=insert;
        this.str = parteaEscribir;
        this.c = caracteraInsertar;
    }
}