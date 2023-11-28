package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MySwing07_1 extends JFrame {

   // 전화기 (버튼을 누르면 숫자가 입력이 되고 CALL버튼을 누르면 검색(java Swing alert)해서)
   // Calling 뜨고 입력한 번호가 뜨게 만들어라
   
   private JPanel contentPane;
   private JTextField tf;
   private JButton btn1;
   private JButton btn2;
   private JButton btn3;
   private JButton btn4;
   private JButton btn5;
   private JButton btn6;
   private JButton btn7;
   private JButton btn8;
   private JButton btn9;
   private JButton btn0;
   private JButton btn_call;

   /**
    * Launch the application.
    */
   public static void main(String[] args) {
      EventQueue.invokeLater(new Runnable() {
         public void run() {
            try {
               MySwing07 frame = new MySwing07();
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
   public MySwing07_1() {
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setBounds(100, 100, 246, 300);
      contentPane = new JPanel();
      contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

      setContentPane(contentPane);
      contentPane.setLayout(null);
      
      tf = new JTextField();
      tf.setHorizontalAlignment(SwingConstants.RIGHT);
      tf.setBounds(12, 10, 194, 21);
      contentPane.add(tf);
      tf.setColumns(10);
      
      btn1 = new JButton("1");
      
      btn1.setBounds(12, 53, 55, 23);
      contentPane.add(btn1);
      
      btn2 = new JButton("2");
      btn2.setBounds(84, 53, 55, 23);
      contentPane.add(btn2);
      
      btn3 = new JButton("3");
      btn3.setBounds(151, 53, 55, 23);
      contentPane.add(btn3);
      
      btn4 = new JButton("4");
      btn4.setBounds(12, 95, 55, 23);
      contentPane.add(btn4);
      
      btn5 = new JButton("5");
      btn5.setBounds(84, 95, 55, 23);
      contentPane.add(btn5);
      
      btn6 = new JButton("6");
      btn6.setBounds(151, 95, 55, 23);
      contentPane.add(btn6);
      
      btn7 = new JButton("7");
      btn7.setBounds(12, 140, 55, 23);
      contentPane.add(btn7);
      
      btn8 = new JButton("8");
      btn8.setBounds(84, 140, 55, 23);
      contentPane.add(btn8);
      
      btn9 = new JButton("9");
      btn9.setBounds(151, 140, 55, 23);
      contentPane.add(btn9);
      
      btn0 = new JButton("0");
      btn0.setBounds(12, 184, 55, 23);
      contentPane.add(btn0);
      
      btn_call = new JButton("CALL");
      btn_call.addMouseListener(new MouseAdapter() {
         @Override
         public void mouseClicked(MouseEvent e) {
            myCall();
         }
      });
      btn_call.setBounds(84, 184, 122, 23);
      contentPane.add(btn_call);
      
      btn1.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      
      btn2.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn3.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn4.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn5.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn6.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn7.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn8.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn9.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
      btn0.addMouseListener(new MouseAdapter() {
         public void mouseClicked(MouseEvent e) {
            myClick(e);
         }
      });
   }

   protected void myCall() {
      String str_tel = tf.getText();
      JOptionPane.showMessageDialog(this, "CALLING\n"+str_tel);
   }

   public void myClick(MouseEvent e) {
      String str_old = tf.getText();
      JButton imsi = (JButton) e.getSource();
      String str_new = imsi.getText();
      
      tf.setText(str_old+str_new);
      
   }
   
}