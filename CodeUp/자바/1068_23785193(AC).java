import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        int n = Integer.parseInt(s);
        if (n >= 90 && n <= 100) {
            System.out.println("A");
        }
        else if(n <= 89 && n >= 70) {
            System.out.println("B");
        }
        else if (n <= 69 && n >= 40){
            System.out.println("C");
        }
        else{
            System.out.println("D");
        }

    }
}

