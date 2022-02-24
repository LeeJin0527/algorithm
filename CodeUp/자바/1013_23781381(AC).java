import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws  IOException{
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer st = new StringTokenizer(bf.readLine());
       int n = Integer.parseInt(st.nextToken());
       int k = Integer.parseInt(st.nextToken());
        System.out.println(n+" " +k);


    }
}

