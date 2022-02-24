import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String st[] = bf.readLine().split(" ");
        double result = 1;
        for(String s: st){
            result*= Double.parseDouble(s);
        }
        Double answer = result/8/1024/1024;
        System.out.printf("%.2f\t",answer);
        System.out.println("MB");

    }
}

