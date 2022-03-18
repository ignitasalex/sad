package test;

import java.io.IOException;
import java.util.Arrays;

public class EditableBufferedReader1copy2 {
    private static int pos = 0;
    private static int arrSizeVar = 10;
    private static byte[] pantalla = new byte[10];

    public static void main(String[] args) {

        // raw mode
        String[] cmd = { "/bin/sh", "-c", "stty -echo raw </dev/tty" };
        try {
            Runtime.getRuntime().exec(cmd);
        } catch (IOException e) {
            e.printStackTrace();
        }

        int b;
        while (true) {

            try {
                byte[] a = new byte[4];
                System.in.read(a);
                if (a[0] == '\033' && a[2] != 0) {
                    // System.out.println("A1 "+a[1]+" a2 "+a[2]);
                    if (a[2] == 'C')
                        right();
                    else if (a[2] == 'D')
                        left();
                    else if(a[3]=='~')
                        suprimir();

                } else if (a[0] == 27 && a[1] == 0) {
                    // System.out.println("COMANDOS A1 "+a[1]+" a2 "+a[2]);
                    b = System.in.read();
                    // System.out.println("COMANDOS b "+b);
                    if (b == 'O') {
                        b = System.in.read();
                        // System.out.println("COMANDOS b2 "+b);
                        if (b == 'H') {
                            home();
                            break;
                        } else if (b == 'Q')
                            end();
                        break;
                    }
                } else if (a[0] == 127 && a[1] == 0)
                    delete();

                else {
                    // System.out.println("otros A1 "+a[1]+" a2 "+a[2]);
                    String str = new String(a, java.nio.charset.StandardCharsets.UTF_8);
                    System.out.print(str);

                    pantalla[pos] = a[0];
                    pos++;
                    if (pos >= arrSizeVar) {
                        // byte[] pantallaAux = Arrays.copyOf(pantalla, pos+10);
                        pantalla = Arrays.copyOf(pantalla, pos + 10);
                        arrSizeVar = pos + 10;
                    }

                }

                // System.out.println(a[0]+" A1 "+a[1]+" a2 "+a[2]);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }

    }

    public static void right() {
        // System.out.println("r");
        if (pos == arrSizeVar)
            return;

        if (pantalla[pos] == 0)
            return;

        pos++;
        System.out.print("\033[C");
    }

    public static void left() {
        // System.out.println("l");
        if (pos == 0)
            return;
        pos--;
        System.out.print("\033[D");
    }

    public static void home() {
        System.out.println("home");

    }

    public static void insert() {
    }

    public static void suprimir() {
        if (pos == arrSizeVar)
            return;

        if (pantalla[pos] == 0)
            return;
       
        right();
        delete();
        
    }

    public static void end() {
        // cooked mode
        String[] fin = { "/bin/sh", "-c", "stty sane </dev/tty" };
        try {
            Runtime.getRuntime().exec(fin);
        } catch (IOException e) {
            e.printStackTrace();
        }
        // System.out.println();
    }

    public static void delete() {
        // left();
        int counter = 0;
        if (pos == 0)
            return;
        left();
        // es posa a 0 la pos que borrem, internament segueix funcionant tenint en
        // compte que esta buit
        System.out.print("\033[K");
        for (int i = pos; i < pantalla.length - 2; i++)
            pantalla[i] = pantalla[i + 1];
        pantalla[pantalla.length - 1] = 0;
        byte[] pantallaAux = Arrays.copyOfRange(pantalla, pos, pantalla.length - 1);
        String str = new String(pantallaAux, java.nio.charset.StandardCharsets.UTF_8);
        System.out.print(str);
        System.arraycopy(pantallaAux, 0, pantalla, pos, pantallaAux.length);
        /*
         * Comprovar string original ok
         * System.out.println();
         * String a = new String(pantalla, java.nio.charset.StandardCharsets.UTF_8);
         * System.out.println(a);
         */

        for (int i = 0; i < pantallaAux.length - 1; i++)
            if (pantallaAux[i] != 0)
                counter++;
        pos += counter;
        for (int i = 0; i < counter; i++)
            left();

    }

}


