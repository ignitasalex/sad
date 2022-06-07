package ReentrantReadWriteLock;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Client {

  public static final int PORT = 5000;

  public static void main(String[] args) throws IOException {
    MySocket mySocket = new MySocket("localhost", PORT);

    new Thread(() -> {
     
        String input;

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

    
    new Thread(() -> {

        String output;

        while ((outputLine = mySocket.readLine()) != null) {  
          System.out.println(outputLine);
      	}

    }).start();

  }
}
