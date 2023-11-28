package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblCom = new JLabel("컴:");
		lblCom.setBounds(58, 82, 16, 15);
		contentPane.add(lblCom);
		
		tfMine = new JTextField();
		tfMine.setBounds(125, 38, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(58, 176, 183, 23);
		contentPane.add(btn);
		
		
		tfResult = new JTextField();
		tfResult.setBounds(125, 125, 116, 21);
		tfResult.setColumns(10);
		contentPane.add(tfResult);
		
		JLabel lblMine = new JLabel("나:");
		lblMine.setBounds(58, 41, 16, 15);
		contentPane.add(lblMine);
		
		tfCom = new JTextField();
		tfCom.setBounds(125, 79, 116, 21);
		tfCom.setColumns(10);
		contentPane.add(tfCom);
		
		JLabel lblResult = new JLabel("결과:");
		lblResult.setBounds(56, 128, 28, 15);
		contentPane.add(lblResult);
	}

	public void myclick() {

		String mine = tfMine.getText();
		String com = "";
		String result = "";
		
		Double rnd = Math.random();
		
		if(rnd > 0.5) {
			com = "홀";
		}else {
			com = "짝";
		}
		
		if(mine.equals(com)) {
			result = "이김";
		}else {
			result = "짐";
		}
		tfCom.setText(com);
		tfResult.setText(result);
	}
	
}
