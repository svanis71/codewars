#include <stdlib.h>
#include <stdio.h>

/* https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/c */

int *distinct(const int *values, size_t count, size_t *pResultCount);

int *distinct(const int *values, size_t count, size_t *pResultCount) {    
  int *distinct_list = (int *)malloc(sizeof(int) * count);
  size_t rescount = 0;
  for(int i = 0; i < count; i++) {
      int found=0;
      for(int j=0; j < rescount && !found; j++) {
        found=distinct_list[j]==values[i]?1:0;
      }
      if(!found) {
        distinct_list = (int*)realloc(distinct_list, (1+rescount)*sizeof(int));
        distinct_list[rescount]=values[i];
        rescount++;
      }
  }
  *pResultCount = rescount;
  return distinct_list;
}
