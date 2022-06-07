import java.io.IOException;
import java.util.concurrent.ConcurrentHashMap;

public class Server implements Runnable {

  public static ConcurrentHashMap <String, MySocket> clientsMap = new ConcurrentHashMap<>();
  public MySocket mySocket;
  public static boolean userValid = false;
  public String nickName;
  
  public Server(String nickName, MySocket mySocket) {
    this.mySocket = mySocket;
    this.nickName = nickName;
  }

  public static void main(String[] args) {

    MyServerSocket server = null;
    MySocket clientSocket;
    String name;

    try {
      server = new MyServerSocket(5000);
    } catch (IOException e) {
      e.printStackTrace();
    }
   

    while (true) {
      clientSocket = server.accept();
      
      while (!userValid) {
        
        name = clientSocket.readLine();

        if (clientsMap.containsKey(name)) {
          clientSocket.printLine("existeix");

        } else {
          clientsMap.put(name, clientSocket);
          
          new Thread(new Server(name, clientSocket)).start();
          userValid = true;
          clientSocket.printLine("_valid_:"+name);
          clientSocket.printLine(getUsuaris());
          sendOthers("_actualitza_afegeix_:",name);
     
        }
      }
      userValid = false;

    }
  }

  @Override
  public void run() {
    String line;

    while ((line = clientsMap.get(nickName).readLine()) != null) {
      for (ConcurrentHashMap.Entry<String, MySocket> entry : clientsMap.entrySet()) {
        if (!entry.getKey().equals(nickName)) {
          entry.getValue().printLine(nickName + " : " + line);
        }
      }
    }
    clientsMap.get(nickName).close();
    clientsMap.remove(nickName);
    sendOthers("_actualitza_treu_:",nickName);  
  }

  public static void sendOthers(String Message, String name){
    for (ConcurrentHashMap.Entry<String, MySocket> entry : clientsMap.entrySet()) {
      if (!entry.getKey().equals(name)) {
        entry.getValue().printLine(Message + name);
      }
    }
  }

  public static String getUsuaris(){
    String usuaris ="";
    for (ConcurrentHashMap.Entry<String, MySocket> entry : clientsMap.entrySet()) {
      usuaris += entry.getKey() + ",";
    }
    System.out.println(usuaris);
    return usuaris;

   }
}