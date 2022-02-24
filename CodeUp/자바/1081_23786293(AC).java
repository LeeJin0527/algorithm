import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
       String s[] = bf.readLine().split(" ");
       int x = Integer.parseInt(s[0]);
       int y = Integer.parseInt(s[1]);
       for ( int i = 1; i <= x; i++){
           for (int j = 1; j <= y; j++){
               System.out.println(i+" "+j);
           }
       }

    }
}

