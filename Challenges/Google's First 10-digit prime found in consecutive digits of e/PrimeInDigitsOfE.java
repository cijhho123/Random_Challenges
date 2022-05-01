package src;

import java.io.IOException;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;


class GoogleBillboardChallenge {
    public static void main(String[] args) {
        
    	String eDigits = "";
		try {
			eDigits = Files.readString(Path.of("D:\\Users\\cijhho123456\\Desktop\\e.txt"), StandardCharsets.US_ASCII);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.exit(0);
		}
    	
		System.out.println(eDigits);
		
		int offset = 3;
		
		while(offset + 10 < eDigits.length()) {
			String currentNumber = eDigits.substring(offset, offset+10);  
			
			if(currentNumber.length() == 10	) 	//to take care of cases of leading 0s
				if(isPrime(currentNumber)) {
					System.out.println(currentNumber+".com");
					break;
				}
			
			
			offset++;
		}
    }

	private static boolean isPrime(String n) {
		BigInteger number = new BigInteger(n);
		
		if(number.isProbablePrime(4))
			return true;
		
		return false;
	}
	  
}
