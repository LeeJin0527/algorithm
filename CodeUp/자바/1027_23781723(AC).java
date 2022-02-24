import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws  IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        String st[] = s.split("\\.");
        System.out.printf("%02d-%02d-%04d",Integer.parseInt(st[2]),Integer.parseInt(st[1]) ,Integer.parseInt(st[0]));

     }
}

