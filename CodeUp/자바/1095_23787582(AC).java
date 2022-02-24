import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        String s[] = bf.readLine().split(" ");
        int Min = 987654321;
        for(int i = 0; i <s.length; i++){
            Min = Math.min(Min, Integer.parseInt(s[i]));
        }
        System.out.println(Min);



    }
}

