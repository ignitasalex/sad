package versio2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class EditableBufferedReader extends BufferedReader {
    
    InputStreamReader inputStreamReader;

    public EditableBufferedReader(InputStreamReader inputStreamReader) {

        super(inputStreamReader);
        this.inputStreamReader = inputStreamReader;

    }

    public static void setRaw() { // put terminal in raw mode

        try {
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty raw -echo </dev/tty" });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void unsetRaw() { // restore terminal to cooked mode
        try {
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty echo cooked </dev/tty" });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * RIGTH: Esc [ C --> Esc(27) [(91) 
     * LEFT: Esc [ D
     * HOME: Esc O H, Esc [1
     * INS: Esc [ 2 ~
     * SUP: Esc [ 3 ~ 
     * END: Esc O F, Esc [4
     * DEL: 127 
     */

    @Override
    public int read() throws IOException { // llegeix el següent caracter o la següent tecla de cursor
        
        int c, ch;
        if ((c = super.read()) != 27)
            return c;
        // c == ESC

        switch (c = super.read()) {
        case 'O':
            switch (c = super.read()) {
            case 'H':
                return Key.HOME;
            case 'F':
                return Key.END;
            default:
                return c;
            }

        case '[':
            switch (c = super.read()) {
            case 'H':
                return Key.HOME;
            case 'F':
                return Key.END;
            case 'C':
                return Key.RIGHT;
            case 'D':
                return Key.LEFT;
            case '1': 
                return Key.HOME;
            case '2':
                if ((ch = super.read()) != '~')
                    return ch;
                return Key.INS;
            case '3':
                if ((ch = super.read()) != '~')
                    return ch;
                return Key.SUP;
            case '4':
                return Key.END;                
            default:
                return c;
            }
        default:
            return c;

        }

    }

    @Override
    public String readLine() throws IOException {

        EditableBufferedReader.setRaw();
        int c; 
        Line line = new Line();

        while ((c = read()) != '\r') { //fins a retorno de carro. ASCII --> 13

            switch (c) {

            case Key.RIGHT:
                line.moveRight();
                break;
            case Key.LEFT:
                line.moveLeft();
                break;
            case Key.HOME:
                line.toHome();
                break;
            case Key.END:
                line.toEnd();
                break;
            case Key.INS:
                line.ins();
                break;
            case Key.SUP:
                line.sup();
                break;
            case Key.DEL:
                line.del();
                break;
            default:
                line.write((char) c);
                break;

            }
            
        }

        EditableBufferedReader.unsetRaw();
        return line.getLine();

    }



}    
