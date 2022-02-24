import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s = bf.readLine();
        String st[] = s.split(" ");
        
        for ( int i = 0; i < st.length; i++){
            if (Integer.parseInt(st[i]) == 0)
                break;
            System.out.println(st[i]);
        }


    }
}

