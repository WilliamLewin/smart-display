#include <stdio.h>
#include <stdlib.h>
char test[30]="hello";
int main()
{
  readFromFile();
}

void readFromFile(){
  int i = 0;
  int l;
  char file_name[100] = "/home/pi/sender-python-c/testing/coordinates";
  FILE *fp = fopen(file_name, "r"); // read mode
  if (fp == NULL)
  {
     perror("Error while opening the file.\n");
     exit(EXIT_FAILURE);
  }
   while((l = fgetc(fp)) != EOF){
      test[i] = l;
      i++;
    }
  fclose(fp);
  printf("%s",test);
}
