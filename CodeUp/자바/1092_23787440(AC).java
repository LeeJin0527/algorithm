import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s[] = bf.readLine().split(" ");

        int day = 1;
        while (day % Integer.parseInt(s[0]) != 0 || day % Integer.parseInt(s[1]) != 0 || day % Integer.parseInt(s[2]) != 0 ){
            day += 1;
        }
        System.out.println(day);
    }
}

