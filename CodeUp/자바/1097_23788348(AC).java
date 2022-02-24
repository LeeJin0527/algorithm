import java.io.*;
import java.nio.file.Path;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
        int[][]  pan= new int[19][19];
        for (int i =0; i < 19; i++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < 19; j++) {
                pan[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int n = Integer.parseInt(bf.readLine());
        for (int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            for(int j = 0; j <19; j++){
                if (pan[x-1][j] == 0)
                    pan[x-1][j] = 1;
                else
                    pan[x-1][j] = 0;

            }
            for(int j = 0; j <19; j++){
                if (pan[j][y-1] == 0)
                    pan[j][y-1] = 1;
                else
                    pan[j][y-1] = 0;

            }
        }

        for(int i = 0; i <19; i++){
            for (int j = 0; j <19; j++){
                br.write(pan[i][j]+" ");
            }
            br.write("\n");
        }
        br.flush();
        br.close();
        bf.close();

    }

}

