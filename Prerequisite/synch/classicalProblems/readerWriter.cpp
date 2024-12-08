#include <iostream>
#include <pthread.h>
#include <semaphore.h>
#include <random>
#include <unistd.h>

using namespace std;

// can be as many readers together but only one writer at a time

sem_t wrtr; // control access for writers (only one writer at a time)
sem_t mutex; // when updating read_count
int read_count = 0; // how many readers are currently reading

// Simulating reader process
//
// Make readcount (increment and decrement) atomic by wait(mutex) and signal(mutex)
void *reader() {
    while (true) {
        // making readcount atomic
        sem_wait(&mutex);
        read_count++;
        // if this is the first reader, waits wrt to prevent writing
        if (read_count == 1) sem_wait(&wrtr);
        sem_post(&mutex);

        // CS
        cout << "Reader " << pthread_self() << " is reading." << endl;
        sleep(1);
        // CS Over

        sem_wait(&mutex); // lock to update readcount
        read_count--; // decrement number of readers
        // last reader : means now writers can write
        if (read_count == 0) {
            sem_post(&wrtr); // Signal writers that they can write
        }
        sem_post(&mutex);
        sleep(1);
    }
}

void *writer() {
    while (true) {
        // entry
        sem_wait(&wrt); // wait until no readers are reading
        cout << "Writer " << pthread_self() << " is writing." << endl;
        sleep(1); 

        sem_post(&wrt); 
        sleep(1);
    }
}

int main() {
    pthread_t readers[5], writers[2];

    sem_init(&wrt, 0, 1);
    sem_init(&mutex, 0, 1);

    for (int i = 0; i < 5; i++) {
        pthread_create(&readers[i], NULL, reader, NULL);
    }

    for (int i = 0; i < 2; i++) {
        pthread_create(&writers[i], NULL, writer, NULL);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(readers[i], NULL);
    }

    for (int i = 0; i < 2; i++) {
        pthread_join(writers[i], NULL);
    }

    sem_destroy(&wrt);
    sem_destroy(&mutex);

    return 0;
}
