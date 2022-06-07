import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.awt.event.ActionListener;

public class JListDemoGeneric extends JPanel implements ActionListener {
    
    // define a JList and a DefaultListModel
    JList<String> list;
    DefaultListModel<String> listModel;

    //Add and Remove
    JButton remove, add;
    JTextField entry;

    public JListDemoGeneric() {
        super(new BorderLayout());

        // create initial listModel
        listModel = new DefaultListModel<>();
        listModel.addElement("Maria");
        listModel.addElement("Anna");
        listModel.addElement("Laura");
        listModel.addElement("Martina");
        listModel.addElement("Pau");
        listModel.addElement("Berta");
        
        //Create the list and put it in a scroll pane.
        list = new JList<>(listModel);
        JScrollPane listScrollPane = new JScrollPane(list);
        add(listScrollPane, BorderLayout.CENTER);

        //Add and Remove
        add = new JButton("Add");
        remove = new JButton("Remove");
        entry = new JTextField(10);

        JPanel addRemove = new JPanel(); 
        addRemove.setLayout(new BoxLayout(addRemove, BoxLayout.LINE_AXIS));

        addRemove.add(entry);
        addRemove.add(add);
        addRemove.add(remove);

        add(addRemove, BorderLayout.PAGE_END);

        entry.addActionListener(this);
        add.addActionListener(this);
        remove.addActionListener(this);

    }

    public void actionPerformed(ActionEvent event) {
        Object source = event.getSource();
        String text = entry.getText();

        if(source == remove) {
            for(int i=0; i<listModel.size(); i++) {
                if(listModel.get(i).contains(text)) {
                    listModel.remove(i);
                    break;
                }
            }
        } else {
            int i=0;
            for(i=0; i<listModel.size(); i++) {
                if(listModel.get(i).equals(text)) {
                    break;
                }
            }
            if(i == listModel.size()) {
                listModel.addElement(text);
            }
        }
    }

    private static void createAndShowGUI() {
        //Set the look and feel.
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {}

        //Make sure we have nice window decorations.
        JFrame.setDefaultLookAndFeelDecorated(true);
        
        //Create and set up the window.
        JFrame frame = new JFrame("List Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);        

        //Create and set up the content pane.
        JListDemoGeneric list = new JListDemoGeneric();
        frame.getContentPane().add(list);
      
        //Display the window.
        frame.setSize(new Dimension(400, 400));
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
}