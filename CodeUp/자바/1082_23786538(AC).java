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
        int n = Integer.parseInt(s, 16);
       for ( int i = 1; i <16; i++){
           System.out.printf("%X*%X=%X\n", n, i, n*i);
       }

    }
}

