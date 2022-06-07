package ReentrantReadWriteLock;

import java.io.IOException;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Server implements Runnable {

  public static Map<String, MySocket> clientsMap = new HashMap();
  private static final ReentrantReadWriteLock rwl = new ReentrantReadWriteLock();
  private static final Lock r = rwl.readLock();
  private static final Lock w = rwl.writeLock();

  public MySocket mySocket;
  public static boolean validUser = false;
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

      while (!validUser) {
        clientSocket.printLine("Nom d'usuari: ");
        name = clientSocket.readLine();

        if (usedNickName(name)) {
          clientSocket.printLine(" " + name + " ja existeix, escull un altre nom d'usuari: ");

        } else {
          putClient(name, clientSocket);
          new Thread(new Server(name, clientSocket)).start();
          clientSocket.printLine("........ " + name + " t'has unit al xat ........");
          validUser = true;
        }
      }
      validUser = false;

    }
  }

  /*@Override
  public void run() {
    
    sendOthers(nick);
    closeClient(nick);
    removeClient(nick);
  }*/
  @Override
  public void run() {
    String line;
    while ((line = clientsMap.get(nick).readLine()) != null) {
        r.lock();
        try{
            for (HashMap.Entry<String, MySocket> entry : clientsMap.entrySet()) {

                if (!entry.getKey().equals(nick)) {
                    entry.getValue().printLine(nick + " : " + line);
                }
            }
        }finally{
            r.unlock();
        }    
    }
    System.out.println("........ "+ nick + " ha sortit del xat ........");

    r.lock();
    try {
      clientsMap.get(nick).close();
    } finally {
      r.unlock();
    }

    w.lock();
    try {
      clientsMap.remove(nick);
    } finally {
      w.unlock();
    }
    
  }

  public static boolean usedNickName(String name) {
    boolean used;
    r.lock();
    try {
      used = clientsMap.containsKey(name);
    } finally {
      r.unlock();
    }
    return used;
  }

  public static void putClient(String name, MySocket clientSocket) {
    w.lock();
    try {
      clientsMap.put(name, clientSocket);
    } finally {
      w.unlock();
    }
  }

}
