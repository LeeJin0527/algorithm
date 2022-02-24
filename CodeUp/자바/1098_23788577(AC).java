import java.io.*;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(bf.readLine());
        int[][] pan = new int[x][y];
        for(int i = 0; i < n; i++){
            StringTokenizer sk = new StringTokenizer(bf.readLine());

            int l = Integer.parseInt(sk.nextToken());
            int d = Integer.parseInt(sk.nextToken());
            int a = Integer.parseInt(sk.nextToken());
            int b = Integer.parseInt(sk.nextToken());
            if (d == 0){ //가로
                for(int u = 0; u < l; u++){
                    pan[a-1][b-1+u] = 1;
                }


            }
            else{ //세로
                for(int u = 0; u < l; u++){
                    pan[a-1+u][b-1] = 1;
                }

            }


        }



        for(int i =0; i < x; i++){
            for(int j = 0; j < y ; j++){
                br.write(pan[i][j]+" ");
            }
            br.write("\n");

        }
        br.flush();
        br.close();
        bf.close();

    }

}

