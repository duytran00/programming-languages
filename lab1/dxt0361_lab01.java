//Duy Tran
//1002190361
//openjdk 17.0.13
//Ubuntu

import java.io.File;

public class dxt0361_lab01 {

    public static long calculateDirectory(String folder) {
   
        //Create file object from folder to check if file or directory and its info
        File directory = new File(folder);
        long total = 0;

        File[] entries = directory.listFiles();

        if (entries != null) {

            //Per x in file array of listfiles
            for (File entry : entries) {
                
                if (entry.getName().equals(".") || entry.getName().equals("..")) {
                    continue;
                }

                String filePath = entry.getPath();

                //If file exists
                if (entry.exists()) {

                    if (entry.isDirectory()) {
                        total += calculateDirectory(filePath);
                    }
                    else {
                        //Get size of the file
                        total += entry.length();
                    }
                }
            }
        }

        return total;
    }

    public static void main(String[] args) {

        //String directory = args[0];
        long size = calculateDirectory(".");

        System.out.print(size);
    }

//$ javac dxt0361_lab01.java
//$ java dxt0361_lab01 .
//$ java dxt0361_lab01 testdir

}