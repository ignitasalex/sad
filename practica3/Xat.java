import java.awt.*;
import javax.swing.*;

public class Xat {
    private static void createAndShowGUI() {
        //Set the look and feel.
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {}
        
        //Make sure we have nice window decorations.
        JFrame.setDefaultLookAndFeelDecorated(true);

        // Create and set up the window.
        JFrame frame = new JFrame("Xat");
        frame.setLayout(new BorderLayout(5, 5));
        frame.getRootPane().setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create an output JPanel and add a JTextArea(20, 30) inside a JScrollPane
        JPanel output = new JPanel();
        output.setLayout(new BoxLayout(output, BoxLayout.PAGE_AXIS));
        JTextArea messages = new JTextArea(20, 30);
        messages.setEditable(false);
        output.add(new JScrollPane(messages));

        // Create an input JPanel and add a JTextField(25) and a JButton
        JPanel input = new JPanel();
        input.setLayout(new BoxLayout(input, BoxLayout.LINE_AXIS));
        JTextField text = new JTextField(25);
        JButton button = new JButton("Send");
        input.add(text);
        input.add(Box.createHorizontalStrut(5)); // espai de 5 Pixels
        input.add(button);
        
        // add panels to main frame
        frame.add(output, BorderLayout.CENTER);
        frame.add(input, BorderLayout.PAGE_END);
        
        //Display the window centered.
        //frame.setSize(new Dimension(400, 500));
        frame.pack();
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