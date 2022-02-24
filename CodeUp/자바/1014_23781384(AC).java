import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws  IOException{
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(bf.readLine());
      String a = st.nextToken();
      String b = st.nextToken();
      System.out.println(b + " " + a);


    }
}

