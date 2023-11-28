package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

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
	private String number = "";

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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 332, 350);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setBounds(29, 39, 256, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		
		btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn1.getText();
			}
		});
		btn1.setBounds(29, 83, 70, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn2.getText();
			}
		});
		btn2.setBounds(123, 83, 70, 23);
		contentPane.add(btn2);
		
		btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn3.getText();
			}
		});
		btn3.setBounds(215, 83, 70, 23);
		contentPane.add(btn3);
		
		btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn4.getText();
			}
		});
		btn4.setBounds(29, 135, 70, 23);
		contentPane.add(btn4);
		
		btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn5.getText();
			}
		});
		btn5.setBounds(123, 135, 70, 23);
		contentPane.add(btn5);
		
		btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn6.getText();
			}
		});
		btn6.setBounds(215, 135, 70, 23);
		contentPane.add(btn6);
		
		btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn7.getText();
			}
		});
		btn7.setBounds(29, 190, 70, 23);
		contentPane.add(btn7);
		
		btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn8.getText();
			}
		});
		btn8.setBounds(123, 190, 70, 23);
		contentPane.add(btn8);
		
		btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn9.getText();
			}
		});
		btn9.setBounds(215, 190, 70, 23);
		contentPane.add(btn9);
		
		btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				tf.setText(number);
				number += btn0.getText();
			}
		});
		btn0.setBounds(29, 239, 70, 23);
		contentPane.add(btn0);
		
		btn_call = new JButton("CALL");
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myCall();
			}
		});
		btn_call.setBounds(123, 239, 162, 23);
		contentPane.add(btn_call);
	}

	public void myCall() {
		JOptionPane.showMessageDialog(null, tf.getText() + " 번호로 전화중");
		reset();
	}

	public void reset() {
		tf.setText("");
		number = "";
	}
	
}
