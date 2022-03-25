package versio2;

import java.util.ArrayList;

public class Line {

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
            pos++;
            System.out.print("\033[C");
        }
    }

    public void moveLeft() {
        if (pos > 0) {
            pos--;
            System.out.print("\033[D");
        }
    }

    public void toHome() {
        pos = 0;
        System.out.print("\033[G"); // o System.out.print("\r");
    }

    public void toEnd() {
        for (int i = pos; i < arr.size(); i++) {
            System.out.print("\033[C");
        }
        pos = arr.size();
    }

    public void ins() {
        ins = !ins;
    }

    public void sup() {
        if (pos < arr.size() - 1) { //si tenim el cursor pel mig

            for (int i = pos + 1; i < arr.size(); i++) {
                System.out.print(arr.get(i));  //sobreescrivim tots els caracters de l'array
            }
            System.out.print(" "); //tapem ultim caracter
            
            for (int i = pos ; i < arr.size(); i++) {
                System.out.print("\033[D");  //tornem el cursor a lloc
            }
            arr.remove(pos);

        } else if (pos == arr.size() - 1) {
            arr.remove(pos);
            System.out.print(" ");
            System.out.print("\033[D"); //escriure espai i tirar enrere enrere el cursor un
        }

    }

    public void del() {
        if (pos != 0) { //no estem a l'inici
            if (pos == arr.size()){  //estem amb el cursor a la dreta de l'ultim caracter
                System.out.print("\033[D"); //movem el cursor esquerra
                System.out.print(" ");  //sobresescrivim espai en blanc
                System.out.print("\033[D"); //tornem el cursor on era
            }

            else { // caracters pel mig

                System.out.print("\033[D");//tirem el cursor un enrere
                for (int i = pos; i < arr.size(); i++) {
                    System.out.print(arr.get(i));
                }
                
                System.out.print(" "); // tapem ultim caracter

                for (int i = 0; i < arr.size()-pos +1; i++) {
                    System.out.print("\033[D"); //tornem cursor a lloc
                }

            }
            arr.remove(pos - 1);
            pos--;
        }
    }

    public void write(char car) {

        System.out.print(car); //printem el caracter pel terminal on tenim el cursor (sobreescrivim)

        if (pos < arr.size()) { // la posicio existeix (hem sobreescrit algun caracter)

            if (ins) // la vull sobreescriure
                arr.set(pos, car);

            else {//NO sobreescrivim, per tant escrivim tot el que teniem a la dreta de pos

                for (int i = pos; i < arr.size(); i++)
                    System.out.print(arr.get(i)); //printem pel terminal

                for (int i = pos; i < arr.size(); i++)
                    System.out.print("\033[D"); //tornem el cursor a lloc
                    
                /*no funciona
                int cont= arr.size()- pos;
                System.out.print("\033["+ (char) (arr.size()-pos) +"D");
                no funciona
                */

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

}