#include <iostream>
#include <thread>
#include <atomic>
#include <vector>
#include <chrono>
using namespace std;

// both not interested initially

atomic<bool> interested[2] = {false, false};
atomic<int> favoured(0); // turn 

void process(int boy) {
    int girl = 1 - boy; // boy and girl, boy is the other process if it's girl's perspective and vice versa
    while (true) {
	interested[boy].store(true); // interest in entering cs

	favoured.store(girl); // politely asking other person (girl) to enter CS even though I(boy) want to enter it
	// wait until girl is not interested or it's not their turn
	while (interested[girl].load() && favoured.load() == girl); // then don't allow boy to enter CS
        // else boy can enter CS

	cout << "Process " << boy << " is in CS" << endl;
	this_thread::sleep_for(chrono::milliseconds(100)); // simulate work
	interested[boy].store(false); // exit CS
	// Remainder Section
	cout << "Process " << boy << " is in the remainder section" << endl;
	this_thread::sleep_for(chrono::milliseconds(100));
    }
}

int main() {
    thread t1(process, 0);
    thread t2(process, 1);
    t1.join();
    t2.join();
    return 0;
}
