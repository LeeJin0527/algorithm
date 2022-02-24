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
       char st = s.charAt(0);
//        System.out.println(s);
       int num = (int)st;

       for (int i = 97; i <= num; i++){
           System.out.printf((char)i+" ");
       }

    }
}

