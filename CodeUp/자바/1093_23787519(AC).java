import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        String s[] = bf.readLine().split(" ");
        int numArr[] = new int [24];
        for(int i = 0; i <s.length; i++){
            numArr[Integer.parseInt(s[i])] += 1;
        }

        for(int i = 1; i < numArr.length; i++){
            System.out.print(numArr[i] +" ");
        }

    }
}

