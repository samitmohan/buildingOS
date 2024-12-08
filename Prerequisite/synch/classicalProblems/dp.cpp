// computer scientists dislike philosophers -galvin pg 272
#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono>

class DP {
public:
    mutex forks[5]; // number of semaphores = number of forks
    void eat(int ph) {
        int left = ph;
        int right = (ph + 1) % 5;
        // lock both forks for eating
        lock(forks[left], forks[right]);
        lock_guard<mutex> leftLock(forks[left], adopt_lock);
        lock_guard<mutex> rightLock(forks[right], adopt_lock);

        cout << "Philosopher " << ph << " is eating" << endl;
        sleep(1);
    }
};

void philosopher(int id, DP &dining) {
    while (1) {
        dininig.eat(id);
        cout << "Philosopher " << id << " is thinking" << endl;
        sleep(1);
    }
}

int main() {
    DP dininig;
    vector<thread> ph;
    for (int i = 0; i < 5; i++) {
        ph.emplace_back(ph, i, ref(dining));
    }
    for (auto *p : ph) {
        p.join();
    }
    return 0;
}
