package versioMVCmill;

import java.util.Observable;
import java.util.Observer;

public class Console implements Observer {

    public Console(){
    }

    static class ChangeWarn {

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

    

    @Override
    public void update(Observable o, Object arg) {
         
        ChangeWarn cw = (ChangeWarn) arg;

        switch(cw.changeType){
            case Key.RIGHT:
                System.out.print("\033[C");
                break;
            case Key.LEFT:
                System.out.print("\033[D");
                break;
            case Key.HOME:
                System.out.print("\033[G");
                break;
            case Key.END:
                System.out.print(cw.str);
                break;
            case Key.DELLAST:
                System.out.print("\033[D"); //movem el cursor esquerra
                System.out.print(" ");  //sobresescrivim espai en blanc
                System.out.print("\033[D"); //tornem el cursor on era
                break;
            case Key.DEL:
                System.out.print("\033[D");//tirem el cursor un a l'esquerra
                System.out.print("\033[s");//guardem cursor
                System.out.print(cw.str + " "); //sobrescrivim y tapem el ultim caracter
                System.out.print("\033[u"); //cargar posicio cursor guardada
                break;
            case Key.SUPLAST:
                System.out.print(" ");
                System.out.print("\033[D");
                break;
            case Key.SUP:
                System.out.print("\033[s");//guardem cursor
                System.out.print(cw.str + " "); //sobreescribim des del cursor i tapem l'ultim caracter
                System.out.print("\033[u"); //cargar posicion cursor guardada
                break;
            case Key.WRITE:
                System.out.print(cw.c);
                if(!cw.ins){
                    System.out.print("\033[s");//guardem cursor
                    System.out.print(cw.str); //sobreescribim des del cursor 
                    System.out.print("\033[u"); //cargar posicion cursor guardada
                    break;
                }
        
        }
        
    }
    
}
