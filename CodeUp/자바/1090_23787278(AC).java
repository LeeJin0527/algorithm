import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s[] = bf.readLine().split(" ");

        long result = Long.parseLong(s[0]);
        for (int i = 0 ; i < Long.parseLong(s[2])-1; i ++) {
            result *= Long.parseLong(s[1]);

        }
        System.out.println(result);
    }
}

