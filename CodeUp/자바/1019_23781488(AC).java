import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws  IOException{
     BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
     String a = bf.readLine();
     String s[] = a.split("\\.");
     int year = Integer.valueOf(s[0]);
     int month = Integer.valueOf(s[1]);
     int day = Integer.valueOf(s[2]);
        System.out.printf("%04d.%02d.%02d", year,month,day);
    }
}

