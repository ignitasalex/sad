package test;

import java.io.IOException;

public class test2 {
    public static void main(String[] args) {
        byte[] buffer = new byte[30];
        byte[] a = new byte[1];
        int i=0;
        try {
            System.in.read(a);
            while(a[0]!=10){
                buffer[i]=a[0];
                i++;
                System.out.println(a[0]);
                System.in.read(a);
            }
            
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }

    }
}
