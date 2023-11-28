package day04;

import java.util.ArrayList;

public class Musk {

	ArrayList<String> companies = new ArrayList<String>();
	
	public void tell(String c_name) {
		companies.add(c_name);
	}
	
	public void show() {
		String str = "";
		for(int i = 0; i < companies.size(); i++) {
			System.out.println(companies.get(i));
		}
	}
	
}
