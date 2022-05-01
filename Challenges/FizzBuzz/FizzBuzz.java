package src;

import java.util.HashMap;

class FizzBuzz {
    public static void main(String[] args) {
        
    	/*	My approach:
    	 * 		Store each pair of number and word in an hashmap.
    	 *  		For each key check if the current number i is divisible by that key, if so add the value to the output string.
    	 * 		Check if the output string is empty, if it is print i. otherwise print the output string. 
    	 * 
    	 * 		This way adding new rules will be as easy as adding new keys to the hashmap.
    	 */
    	
    	
		//------------------------------The classic problem------------------------------
    	
    	HashMap<Integer, String> words = new HashMap<Integer, String>();

		words.put(3, "Fizz");
		words.put(5, "Buzz");
		
		
		System.out.println("Here's a classic game of FizzBuzz! \n");
		
		for(int i = 1; i <= 100; i++) {
			String output = "";
			
			for (Integer key : words.keySet()) {
				  if(i % key == 0)
					  output += words.get(key);
				}
			
			if(output == "")
				System.out.println(i);
			else
				System.out.println(output);
			
			
		}
		
		//------------------------------extended version------------------------------	
		
		words.put(7, "Fuzz");
		words.put(11, "Bizz");
		words.put(13, "Biff");
		
		System.out.println("Here's an extended game of FizzBuzz! \n");
		
		for(int i = 1; i <= 100; i++) {
			String output = "";
			
			for (Integer key : words.keySet()) {
				  if(i % key == 0)
					  output += words.get(key);
				}
			
			if(output == "")
				System.out.println(i);
			else
				System.out.println(output);
			
			
		}
		
        
    }
}
