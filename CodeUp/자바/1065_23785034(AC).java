﻿import java.io.BufferedReader;
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
        int compare[] = new int[st.length];
        for(int i = 0; i < st.length; i++){
            compare[i] = Integer.parseInt(st[i]);
        }
       

       for (int i: compare) {
           if (i % 2 == 0){
               System.out.println(i);
           };
       }
    }
}

