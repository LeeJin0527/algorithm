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
       int num = Integer.parseInt(s);
       for (int i = num-1; i >= 0; i--){

           System.out.println(i);
       }

    }
}
