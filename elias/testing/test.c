#import <stdlib.h>
#import <stdio.h>
#import <string.h>

int main(){
  char m[256];
  FILE *f = fopen("file.txt", "w");
  if (f == NULL)
  {
      printf("Error opening file!\n");
      exit(1);
  }

  const char *text = "Write this to the file";
  for(int i = 0; i < strlen(text); i++){
    m[i] = text[i];
  }
  printf("%s", m);
  fprintf(f, "%s", m);
  fclose(f);
}
