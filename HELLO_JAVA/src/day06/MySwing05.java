package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl1;
	private JLabel lbl2;
	private JLabel lbl3;
	private JLabel lbl4;
	private JLabel lbl5;
	private JLabel lbl6;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(33, 64, 240, 23);
		contentPane.add(btn);
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(33, 29, 30, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(75, 29, 30, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(117, 29, 30, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(159, 29, 30, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(201, 29, 30, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(243, 29, 30, 15);
		contentPane.add(lbl6);
	}
	
	public void myClick() {
		
		int[] lotto = new int[45];
		for(int i = 0; i < lotto.length; i++) {
			lotto[i] = i + 1;
			System.out.println(lotto[i]);
		}
		
		int rnd = 0;
		int temp = 0;
		
		for(int i = 0; i < 1000; i++) {
			rnd = (int)(Math.random() * 45);
			temp = lotto[0];
			lotto[0] = lotto[rnd];
			lotto[rnd] = temp;
		}
		
		lbl1.setText(String.valueOf(lotto[0]));
		lbl2.setText(String.valueOf(lotto[1]));
		lbl3.setText(String.valueOf(lotto[2]));
		lbl4.setText(String.valueOf(lotto[3]));
		lbl5.setText(String.valueOf(lotto[4]));
		lbl6.setText(String.valueOf(lotto[5]));
		
	}

}
