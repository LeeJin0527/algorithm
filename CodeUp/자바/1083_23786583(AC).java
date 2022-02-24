import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        Integer  n = Integer.parseInt(bf.readLine());

       for ( int i = 1; i <=n; i++){
           if ( i % 3 == 0){
               System.out.printf("X"+" ");
           }
           else
                System.out.printf(i+" ");
       }

    }
}

