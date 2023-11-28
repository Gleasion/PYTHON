package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing02 extends JFrame {

   private JPanel contentPane;
   private JTextField tf;

   /**
    * Launch the application.
    */
   public static void main(String[] args) {
      EventQueue.invokeLater(new Runnable() {
         public void run() {
            try {
               MySwing02 frame = new MySwing02();
               frame.setVisible(true);
            } catch (Exception e) {
               e.printStackTrace();
            }
         }
      });
   }

   /**
    * Create the frame.
    */
   public MySwing02() {
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setBounds(100, 100, 450, 300);
      contentPane = new JPanel();
      contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

      setContentPane(contentPane);
      contentPane.setLayout(null);
      
      tf = new JTextField();
      tf.setBounds(85, 48, 96, 21);
      tf.setText("555");
      contentPane.add(tf);
      tf.setColumns(10);
      
      JButton btn = new JButton("increase");
      btn.addMouseListener(new MouseAdapter() {
         @Override
         public void mouseClicked(MouseEvent e) {
            myclick();
            
         }
      });
      btn.setBounds(247, 47, 77, 23);
      btn.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent e) {
         }
      });
      contentPane.add(btn);
   }

   protected void myclick() {
      String a = tf.getText();
      int aa = Integer.parseInt(a);
      aa++;
      tf.setText(aa + "");
   }

}