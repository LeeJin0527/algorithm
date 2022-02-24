import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        String s[] = bf.readLine().split(" ");

        for(int i = s.length-1; i>=0; i--){
            System.out.printf(s[i]+" ");

        }



    }
}

