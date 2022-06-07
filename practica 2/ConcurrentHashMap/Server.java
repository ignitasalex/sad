package ConcurrentHashMap;

import java.io.IOException;
import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

public class Server implements Runnable {

  public static ConcurrentHashMap <String, MySocket> clientsMap = new ConcurrentHashMap<>();

  public MySocket mySocket;
  public static boolean validUser = false;  //boolean per si nom d'usuari introduit es valid
  public String nick;

  public Server(String nickName, MySocket mySocket) {
    this.mySocket = mySocket;
    this.nick = nickName;
  }

  public static void main(String[] args) {
    MyServerSocket server = null;

    try {
      server = new MyServerSocket(5000);
    } catch (IOException e) {
      e.printStackTrace();
    }

    MySocket clientSocket;
    String name;

    while (true) {
      clientSocket = server.accept();

      while (!validUser) {  //fins que no tinguem un nom d'usuari valid
        clientSocket.printLine("Nom d'usuari: ");
        name = clientSocket.readLine();

        if (clientsMap.containsKey(name)) { //comprovem que no existeixi el nom dins del diccionari
          clientSocket.printLine(" " + name + " ja existeix, escull un altre nom d'usuari: ");

        } else {

          clientsMap.put(name, clientSocket); // afegim el nou socket al diccionari
          new Thread(new Server(name, clientSocket)).start();   // nou thread del fill del servidor que aten al client nou
          validUser = true;
          clientSocket.printLine("........ " + name + " t'has unit al xat ........");
        }
      }
      validUser = false;

    }
  }

  @Override
  public void run() {
    
    System.out.println("........ "+ nick + " s'ha unit al xat ........");

    sendOthers(nick);

    clientsMap.get(nick).close(); //tanquem el socket 

    clientsMap.remove(nick);  //borrem el socket del diccionari

    System.out.println("........ "+ nick + " ha sortit del xat ........");
    
  }

  public static void sendOthers(String nickName) {

    String line;
    while ((line = clientsMap.get(nickName).readLine()) != null) { 
 
      for (HashMap.Entry<String, MySocket> entry : clientsMap.entrySet()) { //per tots els usuaris del xat

        if (!entry.getKey().equals(nickName)) { 
          entry.getValue().printLine(nickName + " : " + line);
        }
        
      }
    }
  }


}
