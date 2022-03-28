package versioMVC;

import java.util.ArrayList;
import java.util.Observable;

public class Line extends Observable {
    
    private boolean ins;
    private int pos;
    private ArrayList<Character> arr;

    public Line() {
        ins = false;
        pos = 0;
        arr = new ArrayList<>();
    }

    public void moveRight() {
        if (pos < arr.size()) {
            super.setChanged();
            pos++;
            super.notifyObservers(new ChangeWarn(Key.RIGHT));
                        
        }
    }

    public void moveLeft() {
        if (pos > 0) {
            super.setChanged();
            pos--;
            super.notifyObservers(new ChangeWarn(Key.LEFT));
        }
    }
    public void toHome() {
        if(pos>0){
            super.setChanged();
            pos = 0;
            super.notifyObservers(new ChangeWarn(Key.HOME));
        }
    }

    public void toEnd() {
        String str = "";
        for (int i = pos; i < arr.size(); i++) 
                    str+="\033[C";
                    
        setChanged();        
        pos = arr.size();
        notifyObservers(new ChangeWarn(Key.END, str));

    }

    public void ins() { //fa faltaaa????????
        super.setChanged();
        ins = !ins;
    }

    public void sup() {
        if (pos < arr.size() - 1) { //si tenim el cursor pel mig
            super.setChanged(); 
            arr.remove(pos);
            super.notifyObservers(new ChangeWarn(Key.SUP, getParteaEscribir(pos, arr.size()))); //le pasamos el array que debe sobresecribir

        } else if (pos == arr.size() - 1) {
            super.setChanged();
            arr.remove(pos);
            super.notifyObservers(new ChangeWarn(Key.SUPLAST));
        }
    }

    public void del() {
        if (pos != 0) { //no estem a l'inici
            if (pos == arr.size()){  //estem amb el cursor a la dreta de l'ultim caracter
                super.setChanged();
                super.notifyObservers(new ChangeWarn(Key.DELLAST));                           
            }

            else { // caracters pel mig
                super.setChanged();                
                super.notifyObservers(new ChangeWarn(Key.DEL, getParteaEscribir(pos, arr.size())));

            }
            arr.remove(pos - 1);
            pos--;
        }
    }

    public void write(char car) {

        super.setChanged();
        super.notifyObservers(new ChangeWarn(Key.WRITE, ins, getParteaEscribir(pos, arr.size()), car));

        if (pos < arr.size()) { // la posicio existeix (hem sobreescrit algun caracter)

            if (ins){ // la vull sobreescriure
                arr.set(pos, car);
            } 

            else {//NO sobreescrivim, per tant escrivim tot el que teniem a la dreta de pos
                arr.add(pos, car); //afegim el caracter a l'array (els que ja hi eren es mouen a la dreta)
            }

        } else{  // si la pos no existeix, afegeixo al final
            arr.add(pos, car);

        } // si la pos no existeix, afegeixo al final

        pos++; //avancem el cursor tant si hem escrit amb insert com si no

    }

    public String getLine(){
        String textLine = "";
        for (char s : arr) {
           textLine += s; //posem al String tot els caracters guardats a l'array
        }
        return textLine; //retornem el String

    }


    public String getParteaEscribir(int inicio, int fin){
        String str = "";
        for (int i = inicio; i < fin; i++) 
            str += arr.get(i);
        return str;
    }




    
}
