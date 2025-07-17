//Duy Tran
//1002190361
//gcc 13.3.0
//Ubuntu

#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <stdlib.h>

long long calculateDirectory(const char* folder) {
    //Open folder
    DIR *directory = opendir(folder);
    long long total = 0;

    //Read entries
    struct dirent *entry;
    while ((entry = readdir(directory)) != NULL) {

        //Skip entries name . ..
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        //Create path of entry
        char filePath[4096];
        snprintf(filePath, sizeof(filePath), "%s/%s", folder, entry->d_name);

        //See if entry info vaild
        struct stat fileInfo;
        if (stat(filePath, &fileInfo) == 0) {
            
            //If current entry == directory, recurse to open
            if (S_ISDIR(fileInfo.st_mode)) {
                total += calculateDirectory(filePath);
            } 
            //Else, add file size
            else {
                total += fileInfo.st_size;
            }
        }
    }


    closedir(directory);
    return total;
}

int main(int argc, char *argv[]) {
    //Get directory name
    //current .
    //const char *directory = argv[1];
    long long size = calculateDirectory(".");

    printf("%llu", size);
    return 0;

    //$ gcc dxt0361_lab01.c -o calcsz
    //$ ./calcsz .
    //$ ./calcsz testdir
}
