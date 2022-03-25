package test;

import java.io.IOException;

public class TestBarra {
    public static void main(String[] args) {
        String[] cmd = { "/bin/sh", "-c", "stty -echo raw </dev/tty" };
        // Run a shell command
        try {
            Runtime.getRuntime().exec(cmd);
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        while (true) {

            byte[] a = new byte[3];
            try {
                System.in.read(a);
                if (a[0] == 27 && a[1] == 91 && a[2] == 'C') {
                    System.out.print("\u275A");
                    // System.out.print("\u25AE");

                }
                if (a[0] == 27 && a[1] == 91 && a[2] == 'D') {
                    System.out.print("\033[D");
                    System.out.print(" ");
                    System.out.print("\033[D");

                }
                if (a[0] == 'q' || a[0] == 'Q') {
                    break;

                }
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }

        // arreglar terminal
        String[] fin = { "/bin/sh", "-c", "stty sane </dev/tty" };
        try {
            Runtime.getRuntime().exec(fin);
            System.out.println();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
}
