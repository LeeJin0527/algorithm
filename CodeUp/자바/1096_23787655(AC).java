import java.io.*;
import java.nio.Buffer;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        int[][] pan = new int[19][19];
        for ( int i = 0; i < n; i++){
            String s[] = bf.readLine().split(" ");
            pan[Integer.parseInt(s[0])-1][Integer.parseInt(s[1])-1] = 1;
        }
        for (int i =0; i < 19; i++){
            for (int j = 0; j < 19; j++) {
                System.out.print(pan[i][j]+" ");
            }
            System.out.println();
        }




    }
}

