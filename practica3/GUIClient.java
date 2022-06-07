import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.plaf.ColorUIResource;
import java.awt.event.ActionListener;

public class GUIClient implements ActionListener {

    MySocket socket;

    JFrame initialPage, mainPage;
    JTextField nickField, text;
    JTextArea messages;
    JLabel textLabel;
    JButton join, send;
    String users = "";
    Boolean actualizedUsers = false;
    Color blauVerd,lavanda,blauClar;

    JList<String> list;
    static DefaultListModel<String> listModel;

    public GUIClient() {

        socket = new MySocket("localhost", 5000);

        initialPage = new JFrame("Xat Login");
        mainPage = new JFrame("Xat");

        listModel = new DefaultListModel<>();
        list = new JList<>(listModel);
        blauVerd = new ColorUIResource(0, 128, 128);
        lavanda = new ColorUIResource(230, 230, 250);
        blauClar = new ColorUIResource(51, 204, 204);
    }

    public void initialWindow() {

        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
        }

        JFrame.setDefaultLookAndFeelDecorated(true);
        initialPage.setBackground(blauVerd);
        initialPage.getRootPane().setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        initialPage.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel initialInf = new JPanel();
        
        JPanel initialMidle = new JPanel();
        JPanel initialSup = new JPanel();       
        initialInf.setBackground(blauVerd);
        initialSup.setBackground(blauVerd);
        initialMidle.setBackground(blauVerd);
        initialInf.setLayout(new BoxLayout(initialInf, BoxLayout.LINE_AXIS));

        JLabel label = new JLabel("LogIn");
        label.setFont(new Font("Arial", Font.BOLD, 40));
        label.setForeground(lavanda);
        label.setBackground(blauVerd);
        
        textLabel = new JLabel("Introdueix un nom d'usuari: ");
        textLabel.setBackground(lavanda);      

        nickField = new JTextField(30);
        nickField.setBackground(lavanda);
        join = new JButton("Unir-se");
        join.setBackground(lavanda);
        join.addActionListener(this);

        initialSup.add(label,BorderLayout.PAGE_START);
        initialInf.add(textLabel);
        initialInf.add(nickField);
        initialInf.add(Box.createHorizontalStrut(5));
        initialInf.add(join);

        initialPage.add(initialSup,BorderLayout.PAGE_START);
        initialPage.add(initialMidle);
        initialPage.add(initialInf,BorderLayout.PAGE_END);
    
        initialPage.pack();
        initialPage.setVisible(true);
    }

    public void mainWindow() {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
        }

        JFrame.setDefaultLookAndFeelDecorated(true);
        JFrame frame = new JFrame("Xat");
        frame.setBackground(lavanda);
        frame.setLayout(new BorderLayout(5, 5));
        frame.getRootPane().setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel titles = new JPanel();
        titles.setBackground(lavanda);

        JLabel xatLabel = new JLabel("X A T");
        xatLabel.setFont(new Font("Arial", Font.BOLD, 30));
        xatLabel.setForeground(new ColorUIResource(112, 128, 144));
        xatLabel.setBackground(lavanda);

        titles.add(xatLabel,BorderLayout.CENTER);

        JPanel output = new JPanel();
        output.setLayout(new BoxLayout(output, BoxLayout.LINE_AXIS));

        messages = new JTextArea(20, 30);
        messages.setEditable(false);
       
        messages.setBackground(blauClar);
        output.add(new JScrollPane(messages));

        JList<String> list = new JList<>(listModel);
        list.setBackground(blauVerd);
        list.setForeground(Color.WHITE);

        output.add(new JScrollPane(list));

        JPanel input = new JPanel();
        input.setLayout(new BoxLayout(input, BoxLayout.LINE_AXIS));
        text = new JTextField(25);
        send = new JButton("Enviar");
        send.setForeground(blauVerd);
        send.addActionListener(this);

        input.add(text);
        input.add(Box.createHorizontalStrut(5)); // espai de 5 Pixels
        input.add(send);

        frame.add(titles, BorderLayout.PAGE_START);
        frame.add(output, BorderLayout.CENTER);
        frame.add(input, BorderLayout.PAGE_END);
        
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent event) {
        Object source = event.getSource();
        String nickName = nickField.getText();
        String textMessage = "";

        if (source == join && nickName.length() > 0) {
            socket.printLine(nickName);
            String line = socket.readLine();
            if (line.contains("_valid_")) {
                initialPage.setVisible(false);
                listModel.addElement("....Usuaris Actius ....");
                showUsers(socket.readLine());
                mainWindow();
                chat();

            } else {
                textLabel.setForeground(Color.YELLOW);
                textLabel.setText("Nom d'usuari invalid, intrdueix una altre nom: ");

            }
        } else if (source == send) {
            textMessage = text.getText();
            socket.printLine(textMessage);

            if(textMessage.length()>0){
                messages.append("Jo: " + textMessage + "\n");
                text.setText("");
            }
        }
    }

    public void chat() {

        new Thread(() -> {
            String[] addRem;
            String outputLine;
            while ((outputLine = socket.readLine()) != null) {

                if (outputLine.contains("_actualitza_afegeix_:")) {
                    addRem = outputLine.split(":");
                    listModel.addElement(addRem[1]);
                    messages.append(addRem[1] + " s'ha unit a la conversa\n");

                } else if (outputLine.contains("_actualitza_treu_:")) {
                    addRem = outputLine.split(":");
                    listModel.removeElement(addRem[1]);
                    messages.append(addRem[1] + " ha marxat\n");

                } else {
                    messages.append(outputLine + "\n");
                }
            }
        }).start();
    }

    public static void showUsers(String users){

        String [] listUsers;
        listUsers = users.split(",");
        for(int i=0; i<listUsers.length;i++){
            listModel.addElement(listUsers[i]);
        }
    }

    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                GUIClient client = new GUIClient();
                client.initialWindow();
            }
        });
    }

}
