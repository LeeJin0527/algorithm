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

       for (int i = 0; i <= n; i++){
           System.out.println(i);
       }

    }
}

