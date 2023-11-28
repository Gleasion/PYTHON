package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08_1 extends JFrame {

   // 임의의 전역변수 하나 만들어서 0 ~ 99 사이의 랜덤한 수를 실행시켜
   // 그걸 맞추는 up&down 게임을 만드는데 입력하고나면 텍스트 지워주자

   private JPanel contentPane;
   private JTextField tf;
   int com;
   JTextArea ta;

   /**
    * Launch the application.
    */
   public static void main(String[] args) {
      EventQueue.invokeLater(new Runnable() {
         public void run() {
            try {
               MySwing08 frame = new MySwing08();
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
   public MySwing08_1() {
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setBounds(100, 100, 299, 482);
      contentPane = new JPanel();
      contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

      setContentPane(contentPane);
      contentPane.setLayout(null);

      JLabel lbl = new JLabel("맞추는 수");
      lbl.setBounds(40, 43, 57, 15);
      contentPane.add(lbl);

      tf = new JTextField();
      tf.setBounds(131, 40, 116, 21);
      contentPane.add(tf);
      tf.setColumns(10);

      JButton btn = new JButton("맞춰보기");
      btn.addMouseListener(new MouseAdapter() {
         @Override
         public void mouseClicked(MouseEvent e) {
            myClick();
         }
      });
      btn.setBounds(40, 91, 207, 23);
      contentPane.add(btn);

      ta = new JTextArea();
      ta.setBounds(40, 143, 207, 263);
      contentPane.add(ta);
      
      com = (int)(Math.random()*99)+1;
      System.out.println("com : " + com);
      
   }

   protected void myClick() {
      String mine = tf.getText();
      int m = Integer.parseInt(mine);
      String txt = "";
      if(com>m) {
         txt = mine + "-----------UP\n";
      } else if(com<m) {
         txt = mine + "---------DOWN\n";
      } else {
         txt = mine + "------CORRECT\n";
      }
      
      String str_old = ta.getText();
      ta.setText(str_old + txt);
      tf.setText("");
   }

}