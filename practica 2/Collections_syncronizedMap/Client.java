package Collections_syncronizedMap;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Client {

  public static final int PORT = 5000;

  public static void main(String[] args) throws IOException {
    MySocket mySocket = new MySocket("localhost", PORT);

    new Thread(() -> { //Thread para leer de teclado y enviar hacia servidor
     
        String inputLine;
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
          try {
            while ((inputLine = in.readLine()) != null) {
              mySocket.printLine(inputLine);
          }
          mySocket.close(); 
        }catch(IOException e) {
              e.printStackTrace();
        }
    
    }).start(); 
  
    new Thread(() -> {  //Thread para leer del servidor y printar por pantalla

        String outputLine;
        while ((outputLine = mySocket.readLine()) != null) {  
          System.out.println(outputLine);
      	}

    }).start();

  }
}

