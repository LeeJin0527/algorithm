import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws  IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        Float x = Float.parseFloat(st.nextToken());
        Float y = Float.parseFloat(st.nextToken());
        Float z = Float.parseFloat(st.nextToken());
        System.out.println((int)(x+y+z));

        System.out.printf("%.1f",(x+y+z)/3);

     }
}

