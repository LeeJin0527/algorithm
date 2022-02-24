import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
       int n = Integer.parseInt(bf.readLine());
       int cnt = 1;
       int result = 0;
       while(result < n){
           result += cnt;
           cnt += 1;
       }
        System.out.println(cnt-1);

    }
}

