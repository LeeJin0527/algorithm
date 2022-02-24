import java.io.*;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        int dx[] = {1, 0};
        int dy[] = {0, 1};
       BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
       BufferedWriter br = new BufferedWriter(new OutputStreamWriter(System.out));
       int[][] pan = new int[10][10];
       for(int i = 0; i < 10; i++){
           StringTokenizer st = new StringTokenizer(bf.readLine());
           for(int j = 0; j <10; j++){
               pan[i][j] = Integer.parseInt(st.nextToken());
           }
       }
        int start_x = 1;
        int start_y = 1;
        while(true){
            if (pan[start_x][start_y] == 2){
                pan[start_x][start_y] = 9;
                break;
            }
            pan[start_x][start_y] = 9;
            if (pan[start_x][start_y+1] == 0 || pan[start_x][start_y+1] == 2){
                start_y++;
                continue;
            }
            else if(pan[start_x][start_y+1] == 1){
                if(pan[start_x+1][start_y] == 0 ||pan[start_x+1][start_y] == 2 ){
                    start_x++;
                    continue;
                }
                else if(pan[start_x+1][start_y]==1){
                    break;
                }
            }
        }

        for(int i = 0; i < 10; i++){
            for(int j = 0; j <10; j++){
                br.write(pan[i][j]+" ");
            }
            br.write("\n");
        }
       br.flush();
       br.close();
       bf.close();


    }

}

