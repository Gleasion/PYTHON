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

public class MySwing09_1 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	String com = "234";

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
	public MySwing09_1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 334, 400);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("스트라이크");
		lbl.setBounds(41, 28, 96, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(173, 25, 78, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(41, 64, 210, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(41, 97, 210, 235);
		contentPane.add(ta);
		ranC();
	}

	
	
	public int getS(String mine,String com) {
		int ret = 0;
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		if(m1.equals(c1)) ret++;
		if(m2.equals(c2)) ret++;
		if(m3.equals(c3)) ret++;
		
		return ret;
	}
	
	public int getB(String mine,String com) {
		int ret = 0;
		String m1 = mine.substring(0,1);
		String m2 = mine.substring(1,2);
		String m3 = mine.substring(2,3);
		
		String c1 = com.substring(0,1);
		String c2 = com.substring(1,2);
		String c3 = com.substring(2,3);
		
		if(m1.equals(c2)||m1.equals(c3)) ret++;
		if(m2.equals(c1)||m2.equals(c3)) ret++;
		if(m3.equals(c1)||m3.equals(c2)) ret++;
		
		return ret;
	}
	public void ranC() {
		int[] arr = {1,2,3,4,5 ,6,7,8,9};
		for(int i=0;i<100;i++) {
			int rnd = (int) (Math.random()*9);
			int a = arr[0];
			arr[0]=arr[rnd];
			arr[rnd]=a;
		}
		com = arr[0]+""+arr[1]+""+arr[2];
		
		System.out.println("com:"+com);
		
	}
	
	public void myclick(){
		String mine = tf.getText();
		int s = getS(mine,com);
		int b = getB(mine,com);
		String str_new = mine+"-----"+s+"S"+b+"B\n";
		String str_old = ta.getText();
		
		ta.setText(str_old+str_new);
		tf.setText("");
		
		if(s==3) {
			JOptionPane.showMessageDialog(this, "축하합니다.\n"+mine);
		}

	}
	
	
}















