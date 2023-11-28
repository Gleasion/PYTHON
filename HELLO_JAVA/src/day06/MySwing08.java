package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	private int rnd = (int) (Math.random() * 99);
	private String txt = "";
	private int cnt = 1;

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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 296, 370);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞출수 :");
		lbl.setBounds(45, 35, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(123, 32, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
			
		});
		btn.setBounds(45, 60, 194, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(45, 93, 194, 205);
		contentPane.add(ta);
	}
	
	private void restartGame() {
		rnd = (int) (Math.random() * 99);
		cnt = 1;
		ta.setText("");
		txt = "";
		tf.setText("");
	}
	
	
	public void myClick() {
		int num = Integer.parseInt(tf.getText());
		System.out.println(rnd);
		if (num > rnd) {
			txt += "DOWN입니다.\n";
			ta.setText(txt);
			cnt++;
		}else if(num < rnd) {
			txt += "UP입니다.\n";
			ta.setText(txt);
			cnt++;
		}else if(num == rnd) {
			txt += ("com:" + rnd);
			txt += "맞췄습니다.";
			ta.setText(txt);
			JOptionPane.showMessageDialog(this, "정답입니다. \n 다시시작");
			restartGame();
		}
		
		if(cnt > 10) {
			txt += ("com:" + rnd);
			txt += "GAME OVER입니다.\n";
			ta.setText(txt);
			JOptionPane.showMessageDialog(this, "GAME OVER \n 다시시작");
			restartGame();
		}
	}
		
}
