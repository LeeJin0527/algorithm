import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

       String st[] = bf.readLine().split(" ");
       for (String s: st){
           if (s.equals("0"))
               break;
           System.out.println(s);
       }

    }
}

