// Binary Semaphore
int Semaphore::P(){
    Lock();
    while (value <= 0){   // not if
        pthread_cond_wait(&c, &m);
    }
    // value is now > 0, guaranteed by while loop
    value--;
    // value is now >= 0
    Unlock();
}

int Semaphore::V(){
    Lock();
    int prior_value = value++;
    Unlock();

    // E.g. if prior_value is 50, should we signal? Why?

    if (prior_value == 0) // was not signaled previously, now is.
        pthread_cond_signal(&c);
}
o
