import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(bf.readLine());
        int result = (n == 1)? 0:1;
        System.out.println(result);
    }
}

