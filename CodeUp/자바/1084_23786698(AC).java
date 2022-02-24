import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String s[] = bf.readLine().split(" ");
        BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
        int cnt = 0;
       for ( int i = 0; i < Integer.parseInt(s[0]); i++){
          for ( int j = 0 ; j < Integer.parseInt(s[1]); j++ ){
              String str ="";
              for ( int k = 0; k < Integer.parseInt(s[2]); k++){
                  str += i +" "+j+" "+k+"\n";
                  cnt += 1;
              }
              br.write(str);
              br.flush();
          }
       }
        System.out.println(cnt);

    }
}

