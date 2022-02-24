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
        int result = 0;
       for (int i = 0; i <= n; i++){
           if ( i % 2 == 0){
               result += i;
           }

       }
        System.out.println(result);
    }
}

