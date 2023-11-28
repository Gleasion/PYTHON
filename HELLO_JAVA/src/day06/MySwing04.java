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

public class MySwing04 extends JFrame {
	
	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 372, 521);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(67, 33, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(165, 30, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		
		btn.setBounds(67, 58, 214, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(67, 91, 214, 357);
		contentPane.add(ta);
	}
	
	public void myclick() {
		int dan = Integer.parseInt(tf.getText());
		String result = "";
		
		String txt = "";
		
		for(int i = 1; i < 9; i++) {
			txt += (dan + " * " + i + " = " + dan*i + "\n");
		}
		ta.setText(txt);
	}
}
