import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y= Integer.parseInt(st.nextToken());
        int result =  (x != y)? 1 : 0;
        System.out.println(result);
    }
}

