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
        if ( n < 0){
            System.out.println("minus");
            if (n % 2 == 0){
                System.out.println("even");
            }
            else{
                System.out.println("odd");
            }
        }
        else{
            System.out.println("plus");
            if (n % 2 == 0){
                System.out.println("even");
            }
            else{
                System.out.println("odd");
            }

        }

    }
}

