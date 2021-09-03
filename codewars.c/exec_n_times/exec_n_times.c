#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>

static int counter;

void thread() {
  fputs(".", stdout);
  sleep(1 /* second */);
  counter += 1;
}

void execute (void *(*action)(void*), int nTimes) {
  pthread_t *worker_threads = (pthread_t *)calloc(nTimes, sizeof(pthread_t));
  for(int i = 0; i < nTimes; i++) {
    pthread_create(&worker_threads[i], NULL, action, NULL);
  }
  for(int i = 0; i < nTimes; i++) {
    pthread_join ( worker_threads [ i ], NULL );
  }
}

int main(int argc, char **argv) {
  execute(&thread, 20);
  printf("counter = %d", counter);
}