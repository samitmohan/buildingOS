#include <iostream>
#include <pthread.h>
#include <semaphore.h>
#include <random>
#include <unistd.h>

using namespace std;

#define BUFFER_SIZE 10

int buffer[BUFFER_SIZE];
int idx = 0;

sem_t full, empty; // two semaphores
pthread_mutex_t mutex;

void *produce(void *arg) {
    while (true) {
        sleep(1); // Simulate time taken to produce an item
        sem_wait(&empty); // Wait for an empty slot in the buffer
        pthread_mutex_lock(&mutex); // Lock the mutex for exclusive access

        // Critical section
        int item = rand() % 100; // Produce a random item
        buffer[idx++] = item; // Store it in the buffer
        cout << "Produced: " << item << endl; // Output the produced item

        pthread_mutex_unlock(&mutex); // Unlock the mutex
        sem_post(&full); // Signal that an item has been produced
    }
}

void *consume(void *arg) {
    while (true) {
        sleep(1); // Simulate time taken to consume an item
        sem_wait(&full); // Wait for an available item in the buffer
        pthread_mutex_lock(&mutex); // Lock the mutex for exclusive access

        // Critical section
        int item = buffer[--idx]; // Retrieve the last produced item
        cout << "Consumed: " << item << endl; // Output the consumed item

        pthread_mutex_unlock(&mutex); // Unlock the mutex
        sem_post(&empty); // Signal that an item has been consumed
    }
}

int main() {
    pthread_t producer, consumer;

    // Initialize semaphores and mutex
    sem_init(&empty, 0, BUFFER_SIZE); // Set empty semaphore to BUFFER_SIZE
    sem_init(&full, 0, 0); // Set full semaphore to 0 (no items)
    pthread_mutex_init(&mutex, NULL); // Initialize the mutex

    // Create producer and consumer threads
    pthread_create(&producer, NULL, produce, NULL);
    pthread_create(&consumer, NULL, consume, NULL);

    // Wait for threads to finish (in this case they run indefinitely)
    pthread_join(producer, NULL);
    pthread_join(consumer, NULL);

    return 0;
}

