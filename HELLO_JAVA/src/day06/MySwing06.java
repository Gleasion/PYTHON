package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 333, 551);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		ta = new JTextArea();
		ta.setText("별 결과");
		ta.setBounds(55, 172, 193, 292);
		contentPane.add(ta);
		
		JLabel lbl1_first = new JLabel("첫별수 :");
		lbl1_first.setBounds(55, 39, 57, 15);
		contentPane.add(lbl1_first);
		
		JLabel lbl1_last = new JLabel("끝별수 :");
		lbl1_last.setBounds(55, 84, 57, 15);
		contentPane.add(lbl1_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(132, 36, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(132, 81, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별 출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(55, 131, 193, 23);
		contentPane.add(btn);
	}

	public String drawStar(int cnt) {
        String ret ="";
         
         for (int i = 0; i < cnt; i++) {
             ret += "*";
         }
         ret += "\n";
         return ret;
     }

	public void myClick() {
         String a = tf_first.getText();
         String b = tf_last.getText();

         int aa = Integer.parseInt(a);
         int bb = Integer.parseInt(b);

        String str = "";

         for (int i = aa; i <= bb; i++) {
             str += drawStar(i);
         }

         ta.setText(str);
     }
	
}
