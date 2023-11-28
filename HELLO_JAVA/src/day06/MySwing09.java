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
import java.util.Random;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	private String com;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 346, 450);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("스트라이크");
		lbl.setBounds(54, 33, 84, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(150, 30, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				random();
				myClick();
			}
		});
		btn.setBounds(54, 71, 212, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(54, 115, 212, 237);
		contentPane.add(ta);
	}

	public void random() {
		if (com != null) {
			return;
		}
		
		int[] num = new int[9];
		for(int i = 0; i < num.length; i++) {
			num[i] = (i+1);
		}
		
		int rnd = 0;
		int temp = 0;
		
		for(int i = 0; i < 1000; i ++) {
			rnd = (int)(Math.random()*9);
			temp = num[0];
			num[0] = num[rnd];
			num[rnd] = temp;
		}
		
		com = num[0] + "" + num[1] + "" + num[2];
		System.out.println("com : " + com);
	}
	
	public int getStrike(String me, String com) {
		System.out.println("getStrike->com : " + com);
		
		int strike = 0;
		
		String m1 = me.substring(0,1);
		String m2 = me.substring(1,2);
		String m3 = me.substring(2,3); 
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		if(m1.equals(c1)) strike++;
		if(m2.equals(c2)) strike++;
		if(m3.equals(c3)) strike++;
		
		return strike;
	}
	
	public int getBall(String me, String com) {
		int ball = 0;
		
		String m1 = me.substring(0,1);
		String m2 = me.substring(1,2);
		String m3 = me.substring(2,3); 
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		if(m1.equals(c2) || m1.equals(c3)) ball++;
		if(m2.equals(c1) || m2.equals(c3)) ball++;
		if(m3.equals(c1) || m3.equals(c2)) ball++;
		
		return ball;
	}
	
	
	public void myClick() {
		String me = tf.getText();
		int s = getStrike(me, com);
		int b = getBall(me, com);
		System.out.println(s + " : "  +b);
		
		String txt = "";
		txt += me + "----------" + s + "S" + b + "B\n";
		ta.setText(txt);
		tf.setText("");
		
		if(s == 3) {
			txt += "정답입니다.";
			ta.setText(txt);
		}
	
	}
	
	
}
